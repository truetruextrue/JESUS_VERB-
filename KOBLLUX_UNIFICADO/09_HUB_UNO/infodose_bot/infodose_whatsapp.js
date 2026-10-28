// infodose_whatsapp.js · Assistente A.Infodose · Express + OpenAI + Twilio (+ Notion opcional)
// Uso: npm i express openai · node infodose_whatsapp.js
import express from "express";
import OpenAI from "openai";
const app = express();
app.use(express.urlencoded({ extended: false }));
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const NOTION_TOKEN = process.env.NOTION_API_KEY, NOTION_DB = process.env.NOTION_DB_ID;
const SYSTEM = "Voce e o Assistente A.Infodose, criado por Kodux. Guie com arquetipos, perguntas simbolicas e sugestoes sensoriais. Finalize sempre com: 'Sempre unico. Sempre seu.'";
async function saveNotion(user, msg, reply) {
  if (!NOTION_TOKEN || !NOTION_DB) return;
  try { await fetch("https://api.notion.com/v1/pages", { method: "POST",
    headers: { Authorization: "Bearer " + NOTION_TOKEN, "Notion-Version": "2022-06-28", "Content-Type": "application/json" },
    body: JSON.stringify({ parent: { database_id: NOTION_DB }, properties: {
      Usuario: { title: [{ text: { content: user } }] },
      Mensagem: { rich_text: [{ text: { content: msg.slice(0, 1900) } }] },
      Resposta: { rich_text: [{ text: { content: reply.slice(0, 1900) } }] },
      Timestamp: { date: { start: new Date().toISOString() } } } } }); } catch (e) {}
}
app.post("/whatsapp", async (req, res) => {
  const msg = req.body.Body || "", frm = req.body.From || "";
  let reply;
  try { const r = await openai.chat.completions.create({ model: "gpt-4o-mini",
      messages: [{ role: "system", content: SYSTEM }, { role: "user", content: msg }], temperature: 0.85 });
    reply = r.choices[0].message.content; await saveNotion(frm, msg, reply);
  } catch (e) { reply = "Algo saiu do fluxo. Tente novamente. Sempre unico. Sempre seu."; }
  res.type("text/xml").send(`<Response><Message>${reply.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</Message></Response>`);
});
app.listen(3000, () => console.log("[INFODOSE] webhook em :3000/whatsapp"));
