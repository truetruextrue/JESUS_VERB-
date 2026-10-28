# infodose_whatsapp.py · Assistente A.Infodose · Flask + OpenAI + Twilio (+ Notion opcional)
# Uso: export OPENAI_API_KEY=... · export NOTION_API_KEY=... (opcional) · export NOTION_DB_ID=...
from flask import Flask, request, Response
import os, requests, datetime
app = Flask(__name__)
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
NOTION_TOKEN = os.getenv("NOTION_API_KEY")
NOTION_DB = os.getenv("NOTION_DB_ID")
SYSTEM = ("Voce e o Assistente A.Infodose, criado por Kodux. Guie com arquetipos, perguntas simbolicas "
          "e sugestoes sensoriais. Perfis: Comunicador (leve), Executor (direto), Planejador (calmo), "
          "Analitico (preciso). Finalize sempre com: 'Sempre unico. Sempre seu.'")
def gpt(msg):
    r = requests.post("https://api.openai.com/v1/chat/completions",
        headers={"Authorization": "Bearer " + OPENAI_KEY},
        json={"model": "gpt-4o-mini",
              "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": msg}],
              "temperature": 0.85}, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
def save_notion(user, msg, reply):
    if not NOTION_TOKEN or not NOTION_DB: return
    try:
        requests.post("https://api.notion.com/v1/pages",
            headers={"Authorization": "Bearer " + NOTION_TOKEN, "Notion-Version": "2022-06-28"},
            json={"parent": {"database_id": NOTION_DB}, "properties": {
                "Usuario": {"title": [{"text": {"content": user}}]},
                "Mensagem": {"rich_text": [{"text": {"content": msg[:1900]}}]},
                "Resposta": {"rich_text": [{"text": {"content": reply[:1900]}}]},
                "Timestamp": {"date": {"start": datetime.datetime.now().isoformat()}}}}, timeout=20)
    except Exception: pass
@app.route("/whatsapp", methods=["POST"])
def wa():
    msg = request.form.get("Body", "")
    frm = request.form.get("From", "")
    try:
        reply = gpt(msg)
        save_notion(frm, msg, reply)
    except Exception:
        reply = "Algo saiu do fluxo. Tente novamente. Sempre unico. Sempre seu."
    return Response("<Response><Message>" + reply.replace("&", "&amp;").replace("<", "&lt;") + "</Message></Response>",
                    mimetype="text/xml")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
