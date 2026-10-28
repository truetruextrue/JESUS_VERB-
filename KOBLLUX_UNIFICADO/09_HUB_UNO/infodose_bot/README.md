# INFODOSE BOT · Assistente A.Infodose (Twilio + OpenAI + Notion)
Modulo extraido do livro_25 do databook (Cópias de Milhões x Kodux Dual).

## Subir (Python)
    pip install flask openai requests
    export OPENAI_API_KEY="sua-chave"
    export NOTION_API_KEY="..."        # opcional
    export NOTION_DB_ID="..."          # opcional
    python infodose_whatsapp.py

## Subir (Node)
    npm i express openai
    OPENAI_API_KEY="sua-chave" node infodose_whatsapp.js

## Twilio
1. Twilio Console > Messaging > Try it out > WhatsApp — conecte o numero
2. Studio > importar flow > webhook: POST https://SEU_SERVIDOR/whatsapp
3. Sem Studio: Messaging > WhatsApp sender > "When a message comes in" = URL acima

## Notion (registro simbólico)
1. notion.so/my-integrations > nova integração > copie o token
2. Crie um database com: Usuario (title), Mensagem (text), Resposta (text), Timestamp (date)
3. Compartilhe o DB com a integração e copie o ID da URL

Assinatura obrigatória do assistente: "Sempre unico. Sempre seu."
