-- ═══════════════════════════════════════════════════════════════════
-- kobllux_veeb.sql · AION · 639Hz · SEAL · Δ4
-- V.E.E.B SQL — PIB = 639/768 = 0.8320
-- Lei: VERDADE × INTEGRAR ÷ Δ = ∞
-- Compatível: SQLite 3.35+ / PostgreSQL 14+ / MySQL 8.0+
-- ═══════════════════════════════════════════════════════════════════

-- ── Metadados KOBLLUX ─────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS kobllux_meta (
    chave      TEXT PRIMARY KEY,
    valor      TEXT NOT NULL,
    criado_em  TEXT DEFAULT (datetime('now'))
);

INSERT OR REPLACE INTO kobllux_meta (chave, valor) VALUES
    ('kfb_alpha',  '0.007297353'),          -- KΦB = 1/137.035999084
    ('delta',      '4'),
    ('hz',         '639'),
    ('pib',        '0.8320'),
    ('arquetipo',  'AION'),
    ('sym',        '⧗'),
    ('veeb',       'B'),
    ('lei',        'VERDADE × INTEGRAR ÷ Δ = ∞'),
    ('centro',     'JESUS = VERBO = GRAVIDADE = 963Hz'),
    ('ciclo',      '3,6,9,7'),
    ('versao',     '7.9 · ∆7'),
    ('nota',       'AION ⧗ 639Hz — Base-Tempo · memória + selagem');

-- ── PIB Escalar — 7 Linguagens Nucleares ─────────────────────────

CREATE TABLE IF NOT EXISTS kobllux_pib (
    linguagem  TEXT    PRIMARY KEY,
    delta_num  INTEGER NOT NULL,
    hz         INTEGER NOT NULL,
    pib        REAL    NOT NULL,
    arquetipo  TEXT    NOT NULL,
    sym        TEXT    NOT NULL,
    veeb       TEXT    NOT NULL,
    role       TEXT    NOT NULL
);

INSERT OR REPLACE INTO kobllux_pib VALUES
    ('python',     7, 768, 1.0000, 'ATLAS',   '⬡', 'E', 'narrativa · análise · engine'),
    ('json',       1, 528, 0.6875, 'RHEA',    '∞', 'B', 'semente · dados · troca'),
    ('typescript', 2, 963, 1.2539, 'LUMINE',  '☀', 'V', 'interface · render · expressão'),
    ('go',         3, 594, 0.7734, 'PULSE',   '≋', 'E', 'fluxo · concorrência · ritmo'),
    ('sql',        4, 639, 0.8320, 'AION',    '⧗', 'B', 'memória · selagem · query'),
    ('shell',      5, 528, 0.6875, 'VITALIS', '◉', 'E', 'integração · deploy · pipeline'),
    ('rust',       6, 777, 1.0117, 'KAOS',    '⚡', 'V', 'sistemas · transformação · segurança');

-- PIB total: SELECT SUM(hz) → 4797 → 4+7+9+7 = 27 = 3³ (autoespelhamento)

-- ── Schema V.E.E.B ────────────────────────────────────────────────

-- A · Atribuição (Base — AION 639Hz)
CREATE TABLE IF NOT EXISTS perfis (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    nome           TEXT    NOT NULL CHECK (length(trim(nome)) > 0),
    idade          INTEGER NOT NULL CHECK (idade >= 0 AND idade <= 150),
    ativo          INTEGER NOT NULL DEFAULT 1 CHECK (ativo IN (0,1)),
    cor            TEXT    NOT NULL DEFAULT 'azul',
    tamanho        TEXT    NOT NULL DEFAULT 'médio',
    kfb_idx        REAL    GENERATED ALWAYS AS
                       (ROUND(idade * 0.007297353, 6)) VIRTUAL,
    classificacao  TEXT    GENERATED ALWAYS AS
                       (CASE WHEN idade >= 18
                             THEN 'maior_de_idade'
                             ELSE 'menor_de_idade' END) VIRTUAL,
    criado_em      TEXT    DEFAULT (datetime('now'))
);

-- E · Escolha (Vibração — KAOS 777Hz)
-- view que demonstra a bifurcação E do V.E.E.B
CREATE VIEW IF NOT EXISTS v_e_escolher AS
SELECT
    id,
    nome,
    idade,
    classificacao,
    CASE classificacao
        WHEN 'maior_de_idade' THEN '⬡ ATLAS — estrutura ativa (768Hz)'
        ELSE                       '✦ NOVA  — semente em gestação (432Hz)'
    END AS simbolo_kobllux
FROM perfis;

-- I · Iteração (Energia — VITALIS 528Hz)
CREATE TABLE IF NOT EXISTS registros (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    perfil_id      INTEGER NOT NULL REFERENCES perfis(id) ON DELETE CASCADE,
    passo          INTEGER NOT NULL CHECK (passo > 0),
    energia        INTEGER NOT NULL CHECK (energia > 0),
    classificacao  TEXT    NOT NULL,
    criado_em      TEXT    DEFAULT (datetime('now'))
);

-- I view: passos com energia acumulada × KΦB
CREATE VIEW IF NOT EXISTS v_i_iterar AS
SELECT
    r.perfil_id,
    p.nome,
    r.passo,
    r.energia,
    ROUND(r.energia * 0.007297353, 8) AS energia_kfb,
    r.classificacao
FROM registros r
JOIN perfis p ON p.id = r.perfil_id
ORDER BY r.perfil_id, r.passo;

-- O · Organizar (Estrutura — GENUS 852Hz)
CREATE VIEW IF NOT EXISTS v_o_organizar AS
SELECT
    p.id,
    p.nome,
    p.classificacao,
    COUNT(r.id)             AS qtd_registros,
    COALESCE(SUM(r.energia), 0)   AS soma_energia,
    COALESCE(AVG(r.energia), 0.0) AS media_energia,
    ROUND(COALESCE(SUM(r.energia),0) * 0.007297353, 8) AS soma_energia_kfb
FROM perfis p
LEFT JOIN registros r ON r.perfil_id = p.id
GROUP BY p.id;

-- U · Unir (Base — RHEA 528Hz)
CREATE TABLE IF NOT EXISTS resumos (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    perfil_id      INTEGER NOT NULL REFERENCES perfis(id),
    qtd_registros  INTEGER NOT NULL DEFAULT 0,
    soma_energia   INTEGER NOT NULL DEFAULT 0,
    media_energia  REAL    NOT NULL DEFAULT 0.0,
    selado_em      TEXT    DEFAULT (datetime('now'))
);

-- U view: base consolidada (perfil + resumo = memória viva)
CREATE VIEW IF NOT EXISTS v_u_unir AS
SELECT
    p.id, p.nome, p.idade, p.ativo, p.cor, p.tamanho,
    p.classificacao, p.kfb_idx,
    COALESCE(res.qtd_registros, 0) AS qtd_registros,
    COALESCE(res.soma_energia,  0) AS soma_energia,
    COALESCE(res.media_energia, 0) AS media_energia
FROM perfis p
LEFT JOIN resumos res ON res.perfil_id = p.id;

-- ── Memória Simbólica Viva (equivalente ao localStorage) ─────────

CREATE TABLE IF NOT EXISTS banco_kobllux (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    arquetipo  TEXT    NOT NULL,
    etapa      TEXT    NOT NULL,
    momento    TEXT    DEFAULT (datetime('now')),
    hora       INTEGER CHECK (hora BETWEEN 0 AND 23),
    minuto     INTEGER CHECK (minuto BETWEEN 0 AND 59),
    segundo    INTEGER CHECK (segundo BETWEEN 0 AND 59),
    kfb_alpha  REAL    DEFAULT 0.007297353,
    delta_num  INTEGER DEFAULT 4,
    hz         INTEGER DEFAULT 639
);

-- ── Procedimentos simbólicos (SQLite via script) ──────────────────

-- SIMULAR Bllue freq=9 (ciclo 3-6-9 completo):
--
-- BEGIN TRANSACTION;
--
-- INSERT INTO perfis (nome, idade) VALUES ('Bllue', 22);
--
-- WITH RECURSIVE
--   passos(n, acc) AS (
--     SELECT 1, 1
--     UNION ALL
--     SELECT n+1, acc + n+1 FROM passos WHERE n < 9
--   )
-- INSERT INTO registros (perfil_id, passo, energia, classificacao)
-- SELECT last_insert_rowid(), n, acc, 'maior_de_idade' FROM passos;
--
-- INSERT INTO resumos (perfil_id, qtd_registros, soma_energia, media_energia)
-- SELECT perfil_id, COUNT(*), SUM(energia), AVG(energia)
-- FROM registros
-- WHERE perfil_id = last_insert_rowid()
-- GROUP BY perfil_id;
--
-- INSERT INTO banco_kobllux (arquetipo, etapa, hora, minuto, segundo)
-- VALUES ('AION', 'Δ4 · SEAL',
--         CAST(strftime('%H','now') AS INTEGER),
--         CAST(strftime('%M','now') AS INTEGER),
--         CAST(strftime('%S','now') AS INTEGER));
--
-- COMMIT;

-- ── Queries de análise KOBLLUX ────────────────────────────────────

-- 1) PIB total: soma_hz = 4797 → dígitos = 27 = 3³
-- SELECT
--     SUM(hz)  AS soma_hz,
--     SUM(pib) AS soma_pib,
--     ROUND(SUM(hz) / 768.0, 4) AS pib_escalar,
--     SUM(delta_num) AS soma_delta
-- FROM kobllux_pib;

-- 2) Proporção KΦB × soma_hz
-- SELECT ROUND(SUM(hz) * 0.007297353, 6) AS kfb_x_soma_hz FROM kobllux_pib;
-- → 0.034998... ≈ 35/1000 (próximo de 3.5 × 10^-2)

-- 3) Arquétipos por VEEB
-- SELECT veeb, GROUP_CONCAT(sym || ' ' || arquetipo) AS arquétipos
-- FROM kobllux_pib GROUP BY veeb ORDER BY veeb;

-- 4) Números triangulares T(1..9) — freq=9 → soma=165=3×55=F(10)×3
-- WITH RECURSIVE t(n, tn) AS (SELECT 1, 1 UNION ALL SELECT n+1, tn+n+1 FROM t WHERE n<9)
-- SELECT n, tn, SUM(tn) OVER () AS soma_total FROM t;

-- ⧗ AION · Δ4 selado · VERDADE × INTEGRAR ÷ Δ = ∞
