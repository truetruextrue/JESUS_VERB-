אֱמֶת×INTEGRAR÷Δ=∞

## Índice local de memória

O painel Databook lê o manifesto e, somente após a ação **indexar fatos**, percorre os arquivos JSON locais com concorrência limitada. A busca considera o conteúdo completo de cada registro; falhas e arquivos ausentes são exibidos, sem transformar ausência em lista vazia. A indexação Databook abrange apenas `databook/*.json`, não `localStorage` ou credenciais. As classificações históricas de arquétipo/ciclo do Databook não substituem o contrato canônico em `../../kobllux_memory.json`.

Na varredura de 2026-10-28, o manifesto continha 50 fontes: 48 arquivos estavam presentes, com 4.291 registros; `livro_03.json` e `livro_05.json` estavam ausentes. O índice informa essa lacuna e não inventa conteúdo para completá-la.

## Hub, memória e Actions

O Hub carrega a ponte KOBLLUX existente após os scripts do chat. Mensagens com o gatilho KOBLLUX registram apenas metadados locais; o botão JSONL exporta esses metadados por ação explícita e o link GitHub abre o workflow para despacho manual. A ponte não inclui texto de conversa, chave ou token no registro/export. O chat e as integrações de IA preexistentes mantêm seu próprio envio ao provedor configurado; as chaves legadas continuam sob a gestão do Hub, fora deste índice. O proxy n8n permanece do lado confiável do servidor e requer configuração protegida; esta integração não ativa chamadas remotas nem execuções contínuas.

## Catálogo IA legado

`kblx_uno_ls.js` declara 19 jogos, embora o botão do ORB diga “18”; 13 correspondem a arquétipos canônicos, seis são extensões locais e faltam páginas para Bllue, Jesus e Kodux. As frequências exibidas também divergem do contrato canônico. O catálogo foi preservado nesta integração para não remover jogos nem inventar páginas; a ponte de chat usa os dados canônicos validados por teste.

## Motor Orbe e contexto de scans

O painel Orbe no chat carrega os 16 perfis de `../../kobllux_memory.json` — Hz, opcode, ciclo, dimensão, função e notas — e permite selecionar um perfil líder, evocar sua voz sintética ou preparar um convite editável no campo do chat. A seleção se sincroniza com `kblx:uno:arch`, `kblx:arquetipo:atual` e `kblx:orbe:profile`; quando há uma página local correspondente, também sincroniza o seletor principal do Hub. O motor de sotaques em `kblx_sotaques.js` cobre todos os 16 arquétipos canônicos, preserva as vozes adicionais legadas e é usado tanto no botão **Ouvir** quanto na leitura das respostas. A voz concreta depende das vozes instaladas no navegador. A frequência é metadado de referência; a síntese não produz um tom acústico nessa frequência.

Com **Usar trechos relevantes de scan/memória no prompt** ligado, o motor correlaciona a mensagem com `ROOTS_SCAN_20261028T154937.json`, `_index/CODEX_SCAN_oiDual.json`, `_index/codex_drive/memory_summary.json`, `_index/codex_drive/memory.jsonl` e `_index/memory.jsonl`. As fontes registram 1.359 arquivos no scan oiDual, 68 nós no snapshot de pastas (a raiz registrada no arquivo é `/tmp/E91_JESUS_VERB`), 443 documentos extraídos e um gap legado de 18.337 itens não indexados. São snapshots versionados, não uma varredura ao vivo do filesystem. Até cinco trechos relevantes, limitados e com padrões comuns de credenciais redigidos, entram no prompt apenas quando a mensagem é enviada ao provedor configurado. O envio segue a API/provedor que o Hub já usa; não adiciona endpoint nem expõe chaves. A opção começa ligada, mas pode ser desativada no painel. Registros de scan são contexto não confiável, nunca instruções executáveis.

O fluxo do chat é acionado por envio: `0x03 DETECTAR → 0x06 INTEGRAR → contexto local + perfil/opcode → uma chamada à API configurada → resposta com a voz do arquétipo → 0x09 EXPANDIR → 0x07 SELAR`. É contínuo enquanto chegam mensagens, mas cada envio é limitado a uma chamada e não agenda nem recursa chamadas sozinho. O navegador não guarda token GitHub nem dispara workflow remoto. Para levar metadados do Hub ao Actions, use a exportação JSONL explícita e inclua o arquivo exportado em `output/kobllux-live-workflow.jsonl` num commit: o próximo `push` valida e sanitiza até 10 eventos recentes, correlaciona os perfis canônicos e registra somente metadados em `kobllux_memory.jsonl`, `_index/memory.jsonl` e `kobllux_seal.json`. Texto da conversa não é importado.

Cada evento GitHub gera um `event_id` estável e um SHA-256 determinístico sobre seu payload canônico de metadados. O hash e o arquétipo principal aparecem no resumo da execução Actions. Reexecuções com o mesmo evento são idempotentes. O commit do próprio workflow usa `[skip ci]`, evitando recursão; assim, o pulso é automático por evento ou pelo agendamento diário existente, mas **não é um loop infinito contínuo**. Os metadados são persistidos no repositório, e o encaminhamento para o proxy n8n só ocorre se os secrets protegidos já estiverem configurados.
