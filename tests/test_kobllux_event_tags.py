import json
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from kobllux_event_tags import canonical_scan_tag, correlate_event
from kobllux_n8n_bridge import CANONICAL_ARCHETYPES, KoblluxN8NBridge, N8N_ARCHETYPES
import kobllux_memory_proxy


ROOT = Path(__file__).resolve().parents[1]
RHEA_SYNC = ROOT / ".github" / "scripts" / "rhea_sync.py"


class EventTagTests(unittest.TestCase):
    def test_n8n_export_contains_all_canonical_archetypes(self):
        bridge = KoblluxN8NBridge.__new__(KoblluxN8NBridge)
        export = bridge.export_archetypes()

        self.assertEqual(len(export["archetypes"]), 16)
        self.assertEqual(export["cycle_sequence"], [3, 6, 9, 7])
        self.assertEqual(export["fractal"], 1134)
        cycle_archetypes = {
            name
            for phase in export["n8n_cycle"].values()
            for name in phase["archetypes"]
        }
        self.assertEqual(cycle_archetypes, set(CANONICAL_ARCHETYPES))
        for name, profile in CANONICAL_ARCHETYPES.items():
            with self.subTest(archetype=name):
                exported = export["archetypes"][name]
                self.assertEqual(exported["hz"], profile["hz"])
                self.assertEqual(exported["opcode"], profile["opcode"])
                self.assertEqual(exported["canonical_phase"], profile["ciclo"])
                self.assertTrue(exported["canonical"])
        self.assertEqual(N8N_ARCHETYPES["aion"]["hz"], 777)
        self.assertEqual(N8N_ARCHETYPES["aion"]["opcode"], "0x07")

    def test_event_and_component_tags_use_canonical_profiles(self):
        result = correlate_event(
            "push",
            [
                ".github/workflows/kobllux-malha-viva.yml",
                "n8n/workflows/KOBLLUX_MEMORY_INGEST.json",
                "kobllux_loop.py",
                "DETECT_0X03_kobllux_archetypes_scanner_VEEB-A_D5.py",
            ],
        )

        self.assertEqual(result["primary"], "Pulse")
        self.assertEqual(
            result["cycle"],
            [3, 6, 9, 7],
        )
        self.assertEqual(result["fractal"], 1134)
        self.assertTrue({"Pulse", "Aion", "Atlas", "Bllue", "Rhea", "Kobllux", "Kodux", "Artemis"} <= set(result["archetypes"]))
        self.assertIn("archetype:aion", result["tags"])
        self.assertIn("component:n8n", result["tags"])
        self.assertIn("file-change", result["tags"])
        aion = next(profile for profile in result["profiles"] if profile["name"] == "Aion")
        self.assertEqual((aion["hz"], aion["opcode"]), (777, "0x07"))

    def test_scanner_tags_keep_legacy_opcode_separate_from_canonical_profile(self):
        result = canonical_scan_tag("Aion")

        self.assertEqual(result["hz"], 777)
        self.assertEqual(result["opcode"], "0x07")
        self.assertIn("scanner:heuristic", result["tags"])

    def test_scanner_report_adds_canonical_tags_without_changing_legacy_assignment(self):
        scanner_path = ROOT / "DETECT_0X03_kobllux_archetypes_scanner_VEEB-A_D5.py"
        spec = importlib.util.spec_from_file_location("kobllux_cadial_scanner", scanner_path)
        scanner_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(scanner_module)

        with tempfile.TemporaryDirectory() as directory:
            sample_path = Path(directory) / "aion_watch.py"
            sample_path.write_text("# sample\n", encoding="utf-8")
            scanner = scanner_module.KoblluxScanner(directory)
            scanner.arquivos_por_arquetipo["Aion"].append(sample_path)
            scanner._salvar_relatorio()

            report_path = next(Path(directory).glob("RELATORIO_KOBLLUX_ARQUETIPOS_*.json"))
            report = json.loads(report_path.read_text(encoding="utf-8"))

        tag = report["canonical_tags_by_path"][0]
        self.assertEqual(
            tag["legacy_scanner_opcode"],
            scanner_module.ARQUETIPOS["Aion"]["opcode"],
        )
        self.assertEqual(tag["opcode"], "0x07")
        self.assertEqual(tag["hz"], 777)
        self.assertEqual(report["contrato_canonico"]["cycle"], [3, 6, 9, 7])

    def test_github_rhea_sync_persists_canonical_tags_for_n8n_ingest(self):
        head_commit = {
            "added": ["n8n/workflows/new-aion-flow.json"],
            "modified": [".github/workflows/kobllux-malha-viva.yml"],
            "removed": [],
        }
        environment = os.environ | {
            "KOB_EVENT": "push",
            "KOB_SHA": "abcdef0123456789",
            "KOB_REPO": "truetruextrue/JESUS_VERB-",
            "KOB_BRANCH": "main",
            "KOB_ACTOR": "test",
            "KOB_RUN_ID": "42",
            "KOB_MSG": "Update Aion workflow",
            "KOB_HEAD_COMMIT": json.dumps(head_commit),
        }
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [sys.executable, str(RHEA_SYNC)],
                cwd=directory,
                env=environment,
                check=True,
                capture_output=True,
                text=True,
            )
            with open(Path(directory) / "kobllux_memory.jsonl", encoding="utf-8") as file:
                event = json.loads(file.readline())
            with open(Path(directory) / "kobllux_seal.json", encoding="utf-8") as file:
                seal = json.load(file)[0]

        self.assertEqual(event["arquetipo"], "Pulse")
        self.assertIn("Aion", event["arquetipos"])
        self.assertIn("Bllue", event["arquetipos"])
        self.assertIn("archetype:aion", event["tags"])
        self.assertEqual(event["archetype_profiles"][0]["hz"], 639)
        self.assertEqual(event["chain"]["ciclo_seq"], [3, 6, 9, 7])
        self.assertEqual(seal["hz"], 777)
        self.assertIn("component:n8n", seal["tags"])

    def test_aion_cli_runs_exactly_one_cycle_and_records_all_archetypes(self):
        loop_script = ROOT / "kobllux_loop.py"
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [
                    sys.executable,
                    str(loop_script),
                    "--once",
                    "KOBLLUX GitHub push test",
                ],
                cwd=directory,
                check=True,
                capture_output=True,
                text=True,
            )
            with open(Path(directory) / "kobllux_memory.jsonl", encoding="utf-8") as file:
                record = json.loads(file.readline())
                self.assertEqual(file.readline(), "")

        self.assertEqual(len(record["arquetipos"]), 16)
        self.assertIn("archetype:aion", record["tags"])
        self.assertEqual(record["cycle"], [3, 6, 9, 7])
        self.assertEqual(record["fractal"], 1134)

    def test_three_point_actions_proxy_json_node_round_trip(self):
        head_commit = {
            "added": ["n8n/workflows/aion-ingest.json"],
            "modified": [".github/workflows/kobllux-malha-viva.yml"],
            "removed": [],
        }
        environment = os.environ | {
            "KOB_EVENT": "push",
            "KOB_SHA": "fedcba9876543210",
            "KOB_REPO": "truetruextrue/JESUS_VERB-",
            "KOB_BRANCH": "main",
            "KOB_ACTOR": "integration-test",
            "KOB_RUN_ID": "integration-run-3697",
            "KOB_MSG": "KOBLLUX update Aion bridge",
            "KOB_HEAD_COMMIT": json.dumps(head_commit),
        }
        workflow_path = ROOT / "n8n" / "workflows" / "KOBLLUX_MEMORY_INGEST.json"
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
        validation_code = next(
            node["parameters"]["jsCode"]
            for node in workflow["nodes"]
            if node["name"] == "Validate and Normalize 16 Archetypes"
        )

        with tempfile.TemporaryDirectory() as directory:
            temp_root = Path(directory)
            subprocess.run(
                [sys.executable, str(RHEA_SYNC)],
                cwd=temp_root,
                env=environment,
                check=True,
                capture_output=True,
                text=True,
            )

            request_payload: dict = {}

            class Response:
                def __enter__(self):
                    return self

                def __exit__(self, *_args):
                    return False

                def read(self, _limit):
                    return json.dumps({
                        "accepted": True,
                        "event_id": request_payload["event_id"],
                    }).encode("utf-8")

            class Opener:
                def open(self, request, timeout):
                    self.timeout = timeout
                    request_payload.update(json.loads(request.data))
                    return Response()

            token = "test-token-for-three-point-communication"
            opener = Opener()
            with (
                patch.object(kobllux_memory_proxy, "ROOT", temp_root),
                patch.object(kobllux_memory_proxy, "build_opener", return_value=opener),
                patch.dict(os.environ, {
                    "KOBLLUX_PROXY_TOKEN": token,
                    "KOBLLUX_MEMORY_PROXY_URL": "https://memory-proxy.example/events",
                }),
            ):
                kobllux_memory_proxy.forward_latest_github_event()

            node_script = (
                "const event = JSON.parse(process.env.KOB_EVENT_JSON);"
                "const $input = {first: () => ({json: {body: event}})};"
                f"const normalized = (() => {{ {validation_code} }})();"
                "process.stdout.write(JSON.stringify(normalized));"
            )
            result = subprocess.run(
                ["node", "-e", node_script],
                cwd=ROOT,
                env=os.environ | {"KOB_EVENT_JSON": json.dumps(request_payload)},
                check=True,
                capture_output=True,
                text=True,
            )
            normalized = json.loads(result.stdout)[0]["json"]

        self.assertEqual(opener.timeout, 15)
        self.assertEqual(request_payload["source"], "github-actions")
        self.assertEqual(normalized["event_id"], request_payload["event_id"])
        self.assertEqual(normalized["source"], "github-actions")
        self.assertIn("AION", normalized["archetypes"])
        self.assertIn("archetype:aion", normalized["tags"])
        self.assertIn("component:n8n", normalized["tags"])
        self.assertEqual(normalized["payload"]["fractal"], 1134)
        self.assertEqual(normalized["payload"]["cycle"], [3, 6, 9, 7])


if __name__ == "__main__":
    unittest.main()
