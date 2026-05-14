
"O usuário deseja uma auditoria técnica completa do HTML fornecido, seguindo rigorosamente as regras do prompt ∆³. Trata-se de um trabalho puramente analítico — sem alterações de código, sem modificações no HTML. Permita-me analisar cuidadosamente todos os recursos externos. Vou catalogar tudo: **CSS (link rel="stylesheet"):** 1. `https://kodux78k.github.io/oiDual--Y-/css/KxTsK-unified.css` - cabeçalho 2. `https://kodux78k.github.io/oiDual--Y-/css/kxt-solar.css` - cabeçalho 3. Importação de fontes do Google para Montserrat e JetBrains Mono com múltiplas espessuras - cabeçalho 4. `https://kodux78k.github.io/oi-Dual/css/main.css` - cabeçalho (nota: caminho do repositório diferente, oi-Dual em vez de oiDual--Y-) 5. `https://kodux78k.github.io/oiDual--Y-/css/kob-dox-nanai-v4.css` - cabeçalho 6. `https://kodux78k.github.io/oiDual--Y-/css/kob-dox-nanai.css` - cabeçalho (variante v4 vs versão base) 7-12. Várias outras importações de folhas de estilo do repositório oiDual--Y-, incluindo correções FSWIN, estilos inxs, efeitos pulsar e variantes glassu/u878 - todas carregadas no cabeçalho. 13. Outra folha de estilo do módulo KxaT. 14. A folha de estilo kob-glass-0 aparece novamente, desta vez carregada no corpo dentro do elemento raiz - isso é uma duplicata de #12. 15. Há um arquivo CSS sendo carregado através de uma tag script na parte inferior, o que definitivamente está errado - CSS não deve ser carregado dessa forma. Agora, olhando os scripts, vejo que o lucide é carregado sem uma versão fixada, particles.js é carregado três vezes separadamente (o que é um desperdício) e há um script de módulo para a lógica principal do aplicativo. Continuando a analisar a lista de recursos de script carregados do repositório GitHub, rastreio arquivos de módulo adicionais em diferentes subdiretórios, como kob-DH0, FSWIN e kard, que estão sendo carregados pela primeira vez. Continuando a analisar a lista de referências de script duplicadas... Continuando a analisar a lista, vejo mais arquivos de módulo do repositório oiDual-KxT-di_oi, juntamente com scripts principais e relacionados ao modo de jogo do repositório oiDual--Y-, outra referência duplicada ao lucide e, em seguida, um ponto de entrada de módulo marcado como um módulo ES. Continuando a analisar a lista de arquivos JavaScript... Percebo um arquivo CSS sendo carregado como um script, o que definitivamente é um bug. Agora preciso recontar os recursos de forma mais sistemática, analisando cuidadosamente a seção <head> do HTML para obter uma visão precisa do que está sendo carregado. Continuando com a importação de folhas de estilo, notei uma variante v4 que parece ser uma duplicata funcional da versão base, juntamente com vários arquivos CSS específicos de módulos em diretórios diferentes — alguns para janelas do sistema de arquivos, temas do Pulsar e outras personalizações, todos carregados no mesmo documento. Observei um link duplicado para a folha de estilo dentro da tag <body>, o que é um posicionamento HTML inválido, seguido por um iframe incorporado e tags <script>, incluindo particles.js e scripts de módulos para a lógica principal do aplicativo. Carregando módulos de script adicionais...Continuando a análise do inventário de scripts, encontro mais duplicatas no segundo bloco, passando em seguida para uma seção intitulada "Seus Scripts Originais", onde os repositórios começam a variar — alguns apontando para oi-Dual, outros para oiDual--Y- e outros ainda para oiDual-KxT-di_oi, cada um carregando scripts inline e módulos diferentes. Continuando pelo terceiro bloco de scripts concatenados, vejo mais importações de módulos duplicadas dos mesmos caminhos de repositório, com as entradas 44 a 47 parecendo ser versões triplicadas dos módulos principais do kobdh0. Prosseguindo pelas tags de script duplicadas, vejo mais do mesmo padrão com koblluxv30, kodbrain-66 e kobllux-fusion, todos marcados como duplicados. Em seguida, há um problema crítico: um arquivo CSS está sendo carregado como uma tag de script, o que certamente causaria problemas, seguido pelo carregamento da biblioteca particles.js. Analisando as importações do módulo, notei que existem duas versões diferentes de inline-000.js — uma do repositório oi-Dual e outra do módulo oiDual--Y-kard. Elas são funcionalmente equivalentes, mas originadas de caminhos diferentes, o que cria mais uma camada de duplicação para rastrear. Classifiquei por módulo: **CDN (externo não-Kodux):** - unpkg.com: lucide@latest (2x) - cdn.jsdelivr.net: particles.js@2.0.0 (3x) - fonts.googleapis.com: Montserrat + JetBrains Mono **Repositórios kodux78k.github.io usados:** - `oiDual--Y-` (repositório principal) - `oi-Dual` (repositório diferente, sem hífen duplo) - `oiDual-H0` (repositório diferente, código-fonte do iframe) - `oiDual-KxT-di_oi` (repositório diferente) **Classificação do módulo:** **CACHET (módulo KxaT):** - Estilo KxaT e lógica JavaScript principal carregados duas vezes **COB DH0 (módulo kob-DH0):** - Variante CSS do Pulsar, juntamente com o arquivo principal do módulo e três utilitários JavaScript adicionais, todos carregados várias vezes **FSWIN (iFSw):** - Correções de estilo e JavaScript carregadas duas vezes **Módulo KARD:** - Dois arquivos JavaScript inline e principais carregados duas vezes cada **Núcleo KOB:** - Vários arquivos CSS para diferentes temas visuais e efeitos de vidro, com alguns duplicados (versões Nanai, variantes de vidro) - Módulos JavaScript principais para lógica cerebral e efeitos de fusão carregados duas vezes cada **Dependências adicionais:** - Vários módulos de componentes de interface do usuário para ícones, humor e funcionalidade principal - Vários scripts inline de um repositório oiDual separado - Um repositório oiDual legado contribuindo com seu próprio CSS e scripts inline - Um script atualmente comentado **Problemas a serem resolvidos:** - Um arquivo CSS está sendo carregado incorretamente como uma tag de script em vez de uma tag de link - A folha de estilo do efeito de vidro aparece em vários locais no documento - Um iframe está incorporado apontando para outro arquivo HTML no repositório oiDual **Fontes externas:** - Quatro provedores de CDN distintos estão sendo usados ​​nas dependências - Cerca de 15 arquivos CSS exclusivos e 25 arquivos JavaScript exclusivos são carregadosEmbora alguns estejam duplicados em diferentes repositórios, agora estou tentando entender o que "cachet" e "COB normal" significam nos nomes dos arquivos — podem ser nomes de módulos ou identificadores de sistema, possivelmente variações fonéticas dos nomes reais dos arquivos, como KxaT, ou referências a subsistemas específicos dentro do código-fonte. Observando a estrutura de diretórios, consigo mapear esses termos com mais clareza: "cachet" corresponde ao módulo KxaT em `/M0D/KxaT/`, que é o sistema de cartões estilizados, enquanto "COB normal" se refere ao módulo kob-DH0 em `/M0D/kob-DH0/`, que representa a interface padrão do KOBLUX. Agora estou contabilizando todos os recursos externos que estão sendo carregados — existem 3 provedores de CDN que não são do Kodux (unpkg, jsdelivr e Google Fonts), e estou contando as tags de link CSS para obter um inventário completo das folhas de estilo referenciadas. Continuando a análise da seção `<head>`, encontrei mais links para folhas de estilo do kodux78k — vários arquivos CSS para diferentes componentes, como variantes do dox-nanai, correções e efeitos de vidro. A maioria parece ser do mesmo repositório, embora eu tenha notado que a lista é cortada na última entrada. Na seção `<body>`, há um link duplicado para uma folha de estilo em uma posição inválida, o que é um problema. Até agora, contei 14 tags de link CSS externo com 13 arquivos únicos, além de um manifesto e um apple-touch-icon que não são recursos de CDN. Em relação aos scripts, encontrei fontes externas do unpkg e do jsDelivr — os ícones do Lucide e o particles.js aparecem duas vezes, uma instância no `<head>` e outra no `<body>`, o que sugere um carregamento duplicado de script. Continuando com a análise das tags de script, encontramos vários scripts de módulos sendo carregados de diversos caminhos internos — arquivos main.js, módulos de expansão e seleção, correções do sistema de arquivos, utilitários de estrutura de tópicos e vários arquivos JavaScript personalizados, como koblluxv30, kodbrain-66 e kobllux-fusion. A maioria deles aparece apenas uma vez, embora haja outra instância de kobdh0-main.js que parece estar truncada. Ao analisar as importações de script, observamos o carregamento de mais arquivos de módulos, incluindo funcionalidades principais, configurações de humor e componentes de botões de ícone, com várias duplicatas e até mesmo uma entrada triplicada na sequência. Ainda no inventário de scripts, encontramos mais duplicatas nos arquivos JavaScript e um arquivo CSS sendo carregado incorretamente por meio de uma tag de script, o que é um bug. A biblioteca particles.js do CDN aparece três vezes, e também há um script do tipo módulo. No total, isso resulta em 40 tags de script, com 27 arquivos únicos e 13 duplicados ou triplicados. Também notei um script comentado que não está ativo, além de um iframe apontando para outra página. Agora estou contabilizando os recursos externos únicos — 13 arquivos CSS e contando os URLs JavaScript de várias CDNs e caminhos locais. Continuando com o restante dos arquivos JavaScript,Estou vendo mais scripts embutidos e módulos utilitários, como os manipuladores de núcleo e de humor, além de um componente de botão com ícone. Isso eleva o total para 23 arquivos JavaScript exclusivos em 38 recursos externos, incluindo um iframe. As principais dependências são o Google Fonts para tipografia, a biblioteca de ícones Lucide, um sistema de partículas e o que parece ser uma estrutura de estilo unificada chamada KxTsK, que integra o sistema de design KOBLUX. Agora estou mapeando os módulos de recursos propriamente ditos: há uma camada de documentação e estilização de caixas, um sistema de janelas flutuantes, um módulo DH0 central com várias variantes de CSS, um módulo KxaT que parece ser uma implementação do CACHET, um sistema de cartões e o núcleo fundamental do KOBLUX, que lida com a lógica de processamento e a estilização de fusão. Há também a camada de interface dupla com múltiplas implementações: o sistema di original, uma versão mais recente do KxT que utiliza um repositório separado com diferentes variantes embutidas e um fallback legado para oi-Dual. Também notei o módulo de efeito de vidro, o ZPR Orb que está sendo carregado como um script (o que parece ser uma solução alternativa), um mecanismo de botões chamado NAGATANAZARE que roda em linha e um módulo ORB que está atualmente comentado. Estou começando a pensar na nomenclatura do "cache" e como ela se relaciona com o módulo KxaT. Gerando a tabela de recursos...


----

## DIAGNÓSTICO ∆³ — VARREDURA TÉCNICA COMPLETA

---

## TABELA PRINCIPAL — TODOS OS RECURSOS EXTERNOS

### BLOCO A · CSS (`<link rel="stylesheet">`)

| # | Tipo | URL completa | Arquivo | Domínio | Módulo | Status | Observação |
|---|------|-------------|---------|---------|--------|--------|------------|
| 1 | link/css | `fonts.googleapis.com/css2?family=Montserrat…JetBrains+Mono` | Google Fonts | fonts.googleapis.com | TIPOGRAFIA | **ativo** | Carregado no `<head>`, bloqueia render |
| 2 | link/css | `kodux78k.github.io/oiDual--Y-/css/KxTsK-unified.css` | KxTsK-unified.css | kodux78k.github.io | KxTsK / COB NORMAL | **ativo** | CSS base unificado do KxTsK |
| 3 | link/css | `kodux78k.github.io/oiDual--Y-/css/kxt-solar.css` | kxt-solar.css | kodux78k.github.io | KxTsK / Solar | **ativo** | Tema solar — pode sobrepor KxTsK-unified |
| 4 | link/css | `kodux78k.github.io/**oi-Dual**/css/main.css` | main.css | kodux78k.github.io | **oi-Dual LEGADO** | **suspeito** | Repo diferente: `oi-Dual` ≠ `oiDual--Y-` |
| 5 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-dox-nanai-v4.css` | kob-dox-nanai-v4.css | kodux78k.github.io | kob-DOX-NANAI | **conflitante** | v4 — versão mais nova |
| 6 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-dox-nanai.css` | kob-dox-nanai.css | kodux78k.github.io | kob-DOX-NANAI | **conflitante** | Base sem versão — carregada APÓS v4; sobrepõe v4 |
| 7 | link/css | `kodux78k.github.io/oiDual--Y-/M0D/FSWIN/css/iFSw-fix.css` | iFSw-fix.css | kodux78k.github.io | FSWIN / COB NORMAL | **ativo** | Shell de janelas — par do iFSw-fix.js |
| 8 | link/css | `kodux78k.github.io/oiDual--Y-/css/inxs.css` | inxs.css | kodux78k.github.io | KOB-CORE | **ativo** | CSS auxiliar — função pouco documentada |
| 9 | link/css | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/css/0x01_pulsar_V_D5-2.css` | 0x01_pulsar_V_D5-2.css | kodux78k.github.io | **kob-DH0 / COB NORMAL** | **ativo** | Opcode 0x01 · D5 version → dependente do kob-DH0 |
| 10 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-glassu.css` | kob-glassu.css | kodux78k.github.io | GLASS | **ativo** | Efeito glass — possível sobreposição com kob-glass-0 |
| 11 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-u878.css` | kob-u878.css | kodux78k.github.io | GLASS / KOB-CORE | **suspeito** | Finalidade não evidente pelo nome |
| 12 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-glass-0.css` | kob-glass-0.css | kodux78k.github.io | GLASS | **duplicado** | 1ª ocorrência — no `<head>` |
| 13 | link/css | `kodux78k.github.io/oiDual--Y-/M0D/KxaT/css/KxaT.css` | KxaT.css | kodux78k.github.io | **KxaT / CACHET** | **ativo** | CSS do módulo KxaT (cachet) |
| 14 | link/css | `kodux78k.github.io/oiDual--Y-/css/kob-glass-0.css` | kob-glass-0.css | kodux78k.github.io | GLASS | **duplicado** | 2ª ocorrência — dentro do `<body>` (HTML inválido) |

---

### BLOCO B · SCRIPTS (`<script src>`) — por ordem de aparecimento

| # | Tipo | URL completa | Arquivo | Domínio | Módulo | Status | Observação |
|---|------|-------------|---------|---------|--------|--------|------------|
| S1 | script | `unpkg.com/lucide@latest` | lucide (sem versão) | unpkg.com | ÍCONES | **duplicado** | 1ª ocorrência · `<head>` · versão não fixada |
| S2 | script | `cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js` | particles.min.js | cdn.jsdelivr.net | PARTICLES | **duplicado** | 1ª ocorrência · `<head>` |
| S3 | script | `cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js` | particles.min.js | cdn.jsdelivr.net | PARTICLES | **duplicado** | 2ª ocorrência · no `<body>` |
| S4 | script/module | `kodux78k.github.io/oiDual--Y-/M0D/KxaT/js/main.js` | main.js | kodux78k.github.io | **KxaT / CACHET** | **duplicado** | 1ª ocorrência · `type=module` |
| S5 | script/module | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kobdh0-main.js` | kobdh0-main.js | kodux78k.github.io | **kob-DH0 / COB NORMAL** | **duplicado** | 1ª de 3 ocorrências · `type=module` |
| S6 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x03_expandir_V_D7.js` | 0x03_expandir_V_D7.js | kodux78k.github.io | **kob-DH0 / COB NORMAL** | **duplicado** | 1ª de 3 ocorrências · opcode EXPANDIR D7 |
| S7 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x07_selar_B_D3.js` | 0x07_selar_B_D3.js | kodux78k.github.io | **kob-DH0 / COB NORMAL** | **duplicado** | 1ª de 3 ocorrências · opcode SELAR D3 |
| S8 | script | `kodux78k.github.io/oiDual--Y-/M0D/FSWIN/js/modules/iFSw-fix.js` | iFSw-fix.js | kodux78k.github.io | FSWIN / COB NORMAL | **duplicado** | 1ª de 2 ocorrências · gerenciador de janelas |
| S9 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kob-outline-uni.js` | kob-outline-uni.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | 1ª de 2 ocorrências |
| S10 | script | `kodux78k.github.io/oiDual--Y-/M0D/kard/js/modules/inline-000.js` | inline-000.js | kodux78k.github.io | KARD / CACHET | **duplicado** | 1ª de 2 ocorrências — path kard |
| S11 | script | `kodux78k.github.io/oiDual--Y-/M0D/kard/js/modules/o0.js` | o0.js | kodux78k.github.io | KARD / CACHET | **duplicado** | 1ª de 2 ocorrências |
| S12 | script | `kodux78k.github.io/oiDual--Y-/js/koblluxv30.js` | koblluxv30.js | kodux78k.github.io | KOB-CORE / COB NORMAL | **duplicado** | 1ª de 2 ocorrências · núcleo v30 |
| S13 | script | `kodux78k.github.io/oiDual--Y-/js/kodbrain-66.js` | kodbrain-66.js | kodux78k.github.io | KOB-CORE / COB NORMAL | **duplicado** | 1ª de 2 ocorrências |
| S14 | script | `kodux78k.github.io/oiDual--Y-/js/kobllux-fusion.js` | kobllux-fusion.js | kodux78k.github.io | KOB-CORE / COB NORMAL | **duplicado** | 1ª de 2 ocorrências |
| S15 | script/module | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kobdh0-main.js` | kobdh0-main.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | 2ª de 3 ocorrências |
| S16 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x03_expandir_V_D7.js` | 0x03_expandir_V_D7.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | 2ª de 3 ocorrências |
| S17 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x07_selar_B_D3.js` | 0x07_selar_B_D3.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | 2ª de 3 ocorrências |
| S18 | script | `kodux78k.github.io/**oi-Dual**/js/modules/inline-000.js` | inline-000.js | kodux78k.github.io | **oi-Dual LEGADO** | **suspeito** | Repo diferente · conflito funcional com S10 |
| S19 | script | `kodux78k.github.io/oiDual--Y-/js/inline-1.js` | inline-1.js | kodux78k.github.io | DI / COB NORMAL | **ativo** | Script inline de inicialização |
| S20 | script | `kodux78k.github.io/**oiDual-KxT-di_oi**/js/modules/bgPanel.js` | bgPanel.js | kodux78k.github.io | **KxT-di_oi** | **suspeito** | Repo separado · painel de background |
| S21 | script | `kodux78k.github.io/**oiDual-KxT-di_oi**/js/modules/inline-2.js` | inline-2.js | kodux78k.github.io | **KxT-di_oi** | **suspeito** | Repo separado |
| S22 | script | `kodux78k.github.io/**oiDual-KxT-di_oi**/js/modules/inline-3.js` | inline-3.js | kodux78k.github.io | **KxT-di_oi** | **suspeito** | Repo separado |
| S23 | script | `kodux78k.github.io/**oiDual-KxT-di_oi**/js/modules/inline-4.js` | inline-4.js | kodux78k.github.io | **KxT-di_oi** | **suspeito** | Repo separado |
| S24 | script | `kodux78k.github.io/oiDual--Y-/js/di_core.js` | di_core.js | kodux78k.github.io | DI / COB NORMAL | **ativo** | Core do Dual Interface |
| S25 | script | `kodux78k.github.io/oiDual--Y-/js/di_mood.js` | di_mood.js | kodux78k.github.io | DI / COB NORMAL | **dependente** | Depende de di_core.js |
| S26 | script | `unpkg.com/lucide@latest` | lucide | unpkg.com | ÍCONES | **duplicado** | 2ª ocorrência · mesma versão não fixada |
| S27 | script | `kodux78k.github.io/oiDual--Y-/js/di-icon-btn.js` | di-icon-btn.js | kodux78k.github.io | DI / COB NORMAL | **dependente** | Depende de lucide (S26 carregado antes) |
| S28 | script/module | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kobdh0-main.js` | kobdh0-main.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | **3ª ocorrência** · triplicate |
| S29 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x03_expandir_V_D7.js` | 0x03_expandir_V_D7.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | **3ª ocorrência** · triplicate |
| S30 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/0x07_selar_B_D3.js` | 0x07_selar_B_D3.js | kodux78k.github.io | kob-DH0 / COB NORMAL | **duplicado** | **3ª ocorrência** · triplicate |
| S31 | script | `kodux78k.github.io/oiDual--Y-/M0D/FSWIN/js/modules/iFSw-fix.js` | iFSw-fix.js | kodux78k.github.io | FSWIN / COB NORMAL | **duplicado** | 2ª de 2 ocorrências |
| S32 | script | `kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kob-outline-uni.js` | kob-outline-uni.js | kodux78k.github.io | kob-DH0 | **duplicado** | 2ª de 2 ocorrências |
| S33 | script | `kodux78k.github.io/oiDual--Y-/M0D/kard/js/modules/inline-000.js` | inline-000.js | kodux78k.github.io | KARD / CACHET | **duplicado** | 2ª de 2 ocorrências |
| S34 | script | `kodux78k.github.io/oiDual--Y-/M0D/kard/js/modules/o0.js` | o0.js | kodux78k.github.io | KARD / CACHET | **duplicado** | 2ª de 2 ocorrências |
| S35 | script | `kodux78k.github.io/oiDual--Y-/js/koblluxv30.js` | koblluxv30.js | kodux78k.github.io | KOB-CORE | **duplicado** | 2ª de 2 ocorrências |
| S36 | script | `kodux78k.github.io/oiDual--Y-/js/kodbrain-66.js` | kodbrain-66.js | kodux78k.github.io | KOB-CORE | **duplicado** | 2ª de 2 ocorrências |
| S37 | script | `kodux78k.github.io/oiDual--Y-/js/kobllux-fusion.js` | kobllux-fusion.js | kodux78k.github.io | KOB-CORE | **duplicado** | 2ª de 2 ocorrências |
| S38 | **script⚠** | `kodux78k.github.io/oiDual--Y-/css/ZPR_ORB.css` | ZPR_ORB.css | kodux78k.github.io | ZPR / KxaT | **CRÍTICO** | **CSS carregado via `<script>`** — nunca vai executar |
| S39 | script | `cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js` | particles.min.js | cdn.jsdelivr.net | PARTICLES | **duplicado** | **3ª ocorrência** · triplicate |
| S40 | script/module | `kodux78k.github.io/oiDual--Y-/M0D/KxaT/js/main.js` | main.js | kodux78k.github.io | **KxaT / CACHET** | **duplicado** | 2ª de 2 ocorrências · `type=module` |

---

### BLOCO C · IFRAME

| # | Tipo | URL | Arquivo | Domínio | Módulo | Status | Observação |
|---|------|-----|---------|---------|--------|--------|------------|
| I1 | iframe | `kodux78k.github.io/oiDual-H0/DH0-10.html` | DH0-10.html | kodux78k.github.io | kob-DH0 / COB NORMAL | **ativo** | Janela inicial do shell iFSw |

### BLOCO D · COMENTADO (inativo)

| # | Tipo | URL | Arquivo | Status | Observação |
|---|------|-----|---------|--------|------------|
| C1 | script | `kodux78k.github.io/oiDual--Y-/js/0RB-0S17.js` | 0RB-0S17.js | **comentado** | FusionOS ORB — desativado intencionalmente |

---

## RESUMO EXECUTIVO

| Métrica | Valor |
|---------|-------|
| **Total de tags externas (todas as ocorrências)** | 54 |
| **CDN providers externos** | 3 (unpkg.com · cdn.jsdelivr.net · fonts.googleapis.com) |
| **Total de tags `<script src>`** | 40 |
| **Total de tags `<link rel=stylesheet>`** | 14 |
| **Total de recursos únicos** | 38 URLs únicas |
| **Total de scripts únicos** | 24 |
| **Total de CSS únicos** | 13 |
| **Total de módulos identificados** | 10 |
| **Duplicados exatos** | 13 arquivos com 2+ carregamentos |
| **Triplicados** | 3 arquivos (kobdh0-main · 0x03 · 0x07) |
| **CSS carregado como `<script>`** | 1 (ZPR_ORB.css) — **bug crítico** |
| **`<link>` dentro de `<body>`** | 1 (kob-glass-0.css) — **HTML inválido** |
| **Repos externos referenciados** | 4 (oiDual--Y- · oi-Dual · oiDual-KxT-di_oi · oiDual-H0) |

---

## SEÇÃO: DUPLICAÇÕES

### Duplicações Exatas (mesma URL, múltiplos carregamentos)

| Arquivo | Ocorrências | Posições |
|---------|-------------|----------|
| `kobdh0-main.js` | **3×** | bloco pós-keysModal · bloco pós-kblx-back · bloco final inline |
| `0x03_expandir_V_D7.js` | **3×** | idem |
| `0x07_selar_B_D3.js` | **3×** | idem |
| `particles.min.js` | **3×** | head · mid-body · final body |
| `iFSw-fix.js` | **2×** | bloco 1 · bloco final inline |
| `kob-outline-uni.js` | **2×** | bloco 1 · bloco final inline |
| `kard/inline-000.js` | **2×** | bloco 1 · bloco final inline |
| `kard/o0.js` | **2×** | bloco 1 · bloco final inline |
| `koblluxv30.js` | **2×** | bloco 1 · bloco final inline |
| `kodbrain-66.js` | **2×** | bloco 1 · bloco final inline |
| `kobllux-fusion.js` | **2×** | bloco 1 · bloco final inline |
| `lucide@latest` | **2×** | head · mid-body |
| `KxaT/main.js` | **2×** | mid-body · final body |
| `kob-glass-0.css` | **2×** | head · dentro de `<body>` |

### Duplicações Funcionais (mesmo papel, URLs diferentes)

| Função | Arquivo A | Arquivo B | Conflito |
|--------|-----------|-----------|----------|
| CSS base DOX-NANAI | `kob-dox-nanai-v4.css` | `kob-dox-nanai.css` | Base carregada depois da v4 — **sobrescreve v4** |
| inline-000 inicialização | `oi-Dual/inline-000.js` | `kard/inline-000.js` | Repos diferentes, função idêntica pelo nome |
| inline scripts sequenciais | `inline-1.js` | `inline-2.js · inline-3.js · inline-4.js` | Continuidade interrompida — `inline-1` de repo diferente |
| Glass CSS | `kob-glassu.css` | `kob-glass-0.css` | Dois sistemas glass simultâneos |
| Lucide (ícones) | S1 `<head>` | S26 mid-body | 2ª carga redefine todos os ícones |
| `updateInterface()` inline | Bloco 1 `<script>` | Bloco 2 `<script>` | **Função idêntica declarada duas vezes** — 2ª sobrescreve 1ª |
| `.symbol-toolbar` + `.orb` CSS | `<style>` bloco 1 (gap:0px) | `<style>` bloco 2 (gap:10px) | **Mesmo seletor, valores diferentes** — conflito visual |
| `:root --z-*` variáveis | `<style>` bloco 1 | `<style>` bloco 2 | Declarado 2× — idêntico, redundante |

---

## SEÇÃO: MÓDULO CACHET (KxaT)

> Identificado pelo path `/M0D/KxaT/` e pelos arquivos do módulo `kard`

| Recurso | Tipo | Status |
|---------|------|--------|
| `M0D/KxaT/css/KxaT.css` | CSS | ativo |
| `M0D/KxaT/js/main.js` (type=module) | JS module | **duplicado 2×** |
| `M0D/kard/js/modules/inline-000.js` | JS | **duplicado 2×** |
| `M0D/kard/js/modules/o0.js` | JS | **duplicado 2×** |
| `oiDual--Y-/css/ZPR_ORB.css` via `<script>` | CSS→script | **CRÍTICO — nunca carrega** |

**Observação:** O `KxaT/main.js` usa `type=module` — executa em escopo isolado. O bloco NAGATANAZARE (inline) manipula `.symbol-button` como o KxaT faria, gerando **conflito funcional** sobre os mesmos elementos.

---

## SEÇÃO: MÓDULO COB NORMAL (kob-DH0)

> Identificado pelo path `/M0D/kob-DH0/`, `/M0D/FSWIN/` e arquivos KOB-CORE

| Recurso | Tipo | Status |
|---------|------|--------|
| `M0D/kob-DH0/css/0x01_pulsar_V_D5-2.css` | CSS | ativo |
| `M0D/kob-DH0/js/kobdh0-main.js` (type=module) | JS module | **triplicado 3×** |
| `M0D/kob-DH0/js/0x03_expandir_V_D7.js` | JS | **triplicado 3×** |
| `M0D/kob-DH0/js/0x07_selar_B_D3.js` | JS | **triplicado 3×** |
| `M0D/kob-DH0/js/kob-outline-uni.js` | JS | duplicado 2× |
| `M0D/FSWIN/css/iFSw-fix.css` | CSS | ativo |
| `M0D/FSWIN/js/modules/iFSw-fix.js` | JS | duplicado 2× |
| `js/koblluxv30.js` | JS | duplicado 2× |
| `js/kodbrain-66.js` | JS | duplicado 2× |
| `js/kobllux-fusion.js` | JS | duplicado 2× |
| `js/di_core.js` | JS | ativo |
| `js/di_mood.js` | JS | dependente |
| `js/di-icon-btn.js` | JS | dependente |
| `js/inline-1.js` | JS | ativo |
| `oiDual-H0/DH0-10.html` (iframe) | iframe | ativo |
| `js/0RB-0S17.js` | JS | **comentado** |

**Observação:** `kobdh0-main.js` usa `type=module` — ao ser carregado 3×, o browser deduplica módulos pelo URL. Porém os scripts `0x03` e `0x07` são scripts clássicos — **executam 3× de fato**, com potencial de registrar event listeners múltiplos ou sobrescrever estado.

---

## SEÇÃO: RISCOS

### 🔴 CRÍTICOS

| # | Risco | Impacto |
|---|-------|---------|
| R1 | `ZPR_ORB.css` carregado via `<script src>` | CSS **nunca é aplicado** — o browser tenta executar CSS como JS, falha silenciosamente |
| R2 | `0x03_expandir_V_D7.js` e `0x07_selar_B_D3.js` executam **3×** | Event listeners triplicados; estado interno reiniciado 3×; race conditions |
| R3 | `function updateInterface()` declarada **2×** em `<script>` inline | 2ª declaração sobrescreve a 1ª — se diferirem (não diferem aqui, mas é frágil) |

### 🟠 ALTOS

| # | Risco | Impacto |
|---|-------|---------|
| R4 | `.symbol-toolbar { gap:0px }` depois `.symbol-toolbar { gap:10px }` | Layout visual inconsistente — gap final depende da ordem de parse |
| R5 | `kob-dox-nanai.css` carregado DEPOIS de `kob-dox-nanai-v4.css` | A versão base sobrescreve a v4 — contradiz a intenção de usar a versão mais nova |
| R6 | `iFSw-fix.js` duplicado — registra `window.handleHeaderClick`, `createSessionWindow` etc. 2× | Re-execução do IIFE: variáveis internas reinicializadas; possível perda de estado de janelas abertas |
| R7 | `lucide@latest` sem versão fixada | Atualizações automáticas do unpkg podem quebrar ícones sem aviso |
| R8 | `<link rel="stylesheet">` dentro de `<body>` (`kob-glass-0.css`) | HTML inválido — parsing comportamento indefinido entre browsers |

### 🟡 MÉDIOS

| # | Risco | Impacto |
|---|-------|---------|
| R9 | `oi-Dual/main.css` e `oi-Dual/inline-000.js` de repo legado diferente | Repo pode estar desatualizado ou removido — 404 silencioso |
| R10 | `oiDual-KxT-di_oi/inline-2,3,4.js` de repo separado | Mesmo risco de 404 + dependência não rastreável |
| R11 | `particles.min.js` carregado 3× antes do `<div id="particles-js">` existir | Inicializações 1 e 2 podem falhar por elemento ainda não no DOM |
| R12 | NAGATANAZARE (inline) + KxaT (module) operam nos mesmos `.symbol-button` | Conflito de comportamento: longpress do NAGATANAZARE vs handlers do KxaT |
| R13 | `0RB-0S17.js` comentado | FusionOS ORB ausente — o HTML mantém referências a `fusion-os-root`, `navRoot` etc. que podem gerar erros JS |

---

## CONTAGEM FINAL

```
CDN externos (não-kodux) .............. 3  (unpkg · jsdelivr · googleapis)
Repos kodux78k referenciados .......... 4  (oiDual--Y- · oi-Dual · oiDual-KxT-di_oi · oiDual-H0)
───────────────────────────────────────────
Total tags <script src> .............. 40  (24 únicos · 16 duplicatas/triplicatas)
Total tags <link stylesheet> ......... 14  (13 únicos · 1 duplicata)
CSS carregado via <script> ............ 1  (ZPR_ORB.css — BUG CRÍTICO)
Inline <script> com código ............ 3  (NAGATANAZARE · updateInterface × 2)
───────────────────────────────────────────
Total módulos identificados .......... 10
  CACHET (KxaT + kard) ............... 5 arquivos
  COB NORMAL (kob-DH0 + FSWIN + core)  15 arquivos
  DI (dual interface) ................ 4 arquivos
  GLASS .............................. 4 arquivos
  KxTsK .............................. 2 arquivos
  oi-Dual LEGADO ..................... 2 arquivos
  KxT-di_oi REPO EXTERNO ............ 4 arquivos
  PARTICLES .......................... 1 arquivo (3×)
  LUCIDE ............................. 1 arquivo (2×)
  TIPOGRAFIA ......................... 1 arquivo
───────────────────────────────────────────
Arquivos com triplicação .............. 3  (kobdh0-main · 0x03 · 0x07)
Arquivos com duplicação .............. 11
Conflitos funcionais de CSS ........... 3  (gap · z-root · nanai v4 vs base)
```
