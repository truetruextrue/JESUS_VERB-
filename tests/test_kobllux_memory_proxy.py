import json
import os
import tempfile
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from unittest.mock import patch
import uuid

import kobllux_memory_proxy
from kobllux_memory_proxy import build_handler, validate_event


ORIGIN = "https://truetruextrue.github.io"
TOKEN = "test-proxy-token-with-more-than-32-characters"


def valid_event():
    return {
        "event_id": str(uuid.uuid4()),
        "ts": "2026-08-24T12:00:00+00:00",
        "source": "sumbus-fusion/hypervision",
        "archetypes": ["KODUX", "RHEA"],
        "tags": ["hypervision", "369"],
        "payload": {"user": "hello", "assistant": "world"},
    }


class ProxyHandlerTests(unittest.TestCase):
    def setUp(self):
        self.forward = patch("kobllux_memory_proxy.forward_to_n8n", return_value=(201, b"{}"))
        self.forward_mock = self.forward.start()
        self.server = ThreadingHTTPServer(
            ("127.0.0.1", 0),
            build_handler({ORIGIN}, TOKEN),
        )
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()
        self.url = f"http://127.0.0.1:{self.server.server_port}/events"

    def tearDown(self):
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()
        self.forward.stop()

    def post(self, event, token=TOKEN, origin=ORIGIN):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Origin": origin,
        }
        request = Request(self.url, json.dumps(event).encode(), headers, method="POST")
        try:
            return urlopen(request)
        except HTTPError as exc:
            return exc

    def test_valid_event_is_forwarded_and_cors_allowed(self):
        event = valid_event()
        response = self.post(event)
        self.assertEqual(response.status, 201)
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], ORIGIN)
        self.assertEqual(json.loads(response.read()), {
            "accepted": True,
            "event_id": event["event_id"],
        })

    def test_invalid_archetype_is_rejected_before_forwarding(self):
        event = valid_event()
        event["archetypes"] = ["NOT_CANONICAL"]
        response = self.post(event)
        self.assertEqual(response.status, 400)
        self.forward_mock.assert_not_called()

    def test_invalid_token_is_rejected(self):
        response = self.post(valid_event(), token="wrong-token")
        self.assertEqual(response.status, 401)
        self.forward_mock.assert_not_called()

    def test_disallowed_origin_is_rejected(self):
        response = self.post(valid_event(), origin="https://attacker.example")
        self.assertEqual(response.status, 403)
        self.forward_mock.assert_not_called()

    def test_validation_requires_timezone_aware_timestamp(self):
        event = valid_event()
        event["ts"] = "2026-08-24T12:00:00"
        with self.assertRaisesRegex(ValueError, "timezone"):
            validate_event(event)


class GitHubForwardingTests(unittest.TestCase):
    def test_latest_rhea_event_is_forwarded_with_stable_identity(self):
        source = {
            "ts": "2026-08-24T12:00:00+00:00",
            "z": "abcdef0123456789",
            "arquetipo": "Pulse",
            "evento": "push",
            "repo": "truetruextrue/JESUS_VERB-",
            "branch": "main",
            "actor": "maintainer",
            "commit_msg": "Update file library",
            "pr_title": "",
            "pr_num": "",
            "run_id": "123456",
            "arquivos": {
                "added": ["systems/editor/atlas.html"],
                "modified": [],
                "removed": [],
            },
            "chain": {"fractal": 1134},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = kobllux_memory_proxy.Path(directory)
            (root / "kobllux_memory.jsonl").write_text(json.dumps(source) + "\n")
            response = unittest.mock.MagicMock()
            response.read.return_value = json.dumps({
                "accepted": True,
                "event_id": str(uuid.uuid5(
                    uuid.NAMESPACE_URL,
                    f"github:{source['run_id']}:{source['z']}",
                )),
            }).encode()
            opener = unittest.mock.MagicMock()
            opener.open.return_value.__enter__.return_value = response
            with (
                patch.object(kobllux_memory_proxy, "ROOT", root),
                patch.object(kobllux_memory_proxy, "build_opener", return_value=opener),
                patch.dict(os.environ, {
                    "KOBLLUX_PROXY_TOKEN": TOKEN,
                    "KOBLLUX_MEMORY_PROXY_URL": "https://proxy.example/events",
                }),
            ):
                kobllux_memory_proxy.forward_latest_github_event()

            request = opener.open.call_args.args[0]
            event = json.loads(request.data)
            self.assertEqual(event["source"], "github-actions")
            self.assertIn("PULSE", event["archetypes"])
            self.assertIn("ATLAS", event["archetypes"])
            self.assertEqual(event["payload"]["repository"], source["repo"])
            self.assertEqual(event["payload"]["changed_files"], source["arquivos"])
            self.assertIn("file-change", event["tags"])
            self.assertEqual(request.full_url, "https://proxy.example/events")


if __name__ == "__main__":
    unittest.main()
