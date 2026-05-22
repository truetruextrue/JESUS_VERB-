/**
 * GITHUB_BRIDGE · Ponte Real com o Repositório JESUS_VERB-
 * Arquétipo: RHEA (INTEGRATE) + ARTEMIS (DETECT) + AION (SEAL)
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 *
 * Funcionalidades:
 *   - Leitura da árvore do repositório (tree)
 *   - Leitura de conteúdo de arquivos
 *   - Upload / criação de arquivos via GitHub API
 *   - Disparo de workflows (GitHub Actions)
 *   - Feed de commits recentes
 *   - Mapeamento arquétipo ↔ arquivo
 */

const GITHUB_BRIDGE = {
    repo:   'truetruextrue/JESUS_VERB-',
    branch: 'main',
    base:   'https://api.github.com/repos/truetruextrue/JESUS_VERB-',

    workflows: {
        'cadial-seal': { file: 'cadial-seal.yml', name: '∆7 CADIAL · KOBLLUX SEAL',  inputs: { opcode: '0x07' } },
        'pages':       { file: 'pages.yml',       name: '✝ VERBUM · Pages Deploy',    inputs: { force: 'false' } },
    },

    // ── Auth ────────────────────────────────────────────────────────
    getToken() { return localStorage.getItem('gh_token') || ''; },
    setToken(t) { localStorage.setItem('gh_token', t.trim()); },
    hasToken()  { return !!this.getToken(); },

    headers(write = false) {
        const h = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
        };
        const tok = this.getToken();
        if (tok) h['Authorization'] = `Bearer ${tok}`;
        if (write) h['Content-Type'] = 'application/json';
        return h;
    },

    // ── HTTP helpers ─────────────────────────────────────────────────
    async get(endpoint, fullUrl = false) {
        const url = fullUrl ? endpoint : this.base + endpoint;
        const r = await fetch(url, { headers: this.headers() });
        if (!r.ok) {
            const txt = await r.text();
            throw new Error(`GitHub API ${r.status} · ${endpoint} · ${txt.slice(0,120)}`);
        }
        return r.json();
    },

    async put(endpoint, body) {
        if (!this.hasToken()) throw new Error('Token GitHub necessário para operações de escrita. Insira seu token pessoal (PAT) no painel de configuração.');
        const r = await fetch(this.base + endpoint, {
            method: 'PUT',
            headers: this.headers(true),
            body: JSON.stringify(body),
        });
        if (!r.ok) {
            const txt = await r.text();
            throw new Error(`GitHub API ${r.status} · ${txt.slice(0,200)}`);
        }
        return r.json();
    },

    async post(endpoint, body, fullUrl = false) {
        if (!this.hasToken()) throw new Error('Token GitHub necessário.');
        const url = fullUrl ? endpoint : this.base + endpoint;
        const r = await fetch(url, {
            method: 'POST',
            headers: this.headers(true),
            body: JSON.stringify(body),
        });
        return r.status; // 204 = success for workflow dispatch
    },

    // ── Repository ───────────────────────────────────────────────────
    async fetchRepo() {
        return this.get('');
    },

    async fetchTree() {
        return this.get(`/git/trees/${this.branch}?recursive=1`);
    },

    async fetchCommits(perPage = 25) {
        return this.get(`/commits?per_page=${perPage}&sha=${this.branch}`);
    },

    async fetchFile(path) {
        const encoded = path.split('/').map(s => encodeURIComponent(s)).join('/');
        return this.get(`/contents/${encoded}`);
    },

    async fetchRuns(perPage = 10) {
        return this.get(`/actions/runs?per_page=${perPage}`);
    },

    async fetchWorkflows() {
        return this.get('/actions/workflows');
    },

    // ── Write ────────────────────────────────────────────────────────
    async createOrUpdateFile(path, content, message, existingSha = null) {
        const encodedPath = path.split('/').map(s => encodeURIComponent(s)).join('/');
        const encodedContent = btoa(unescape(encodeURIComponent(content)));
        const body = {
            message,
            content: encodedContent,
            branch: this.branch,
        };
        if (existingSha) body.sha = existingSha;
        return this.put(`/contents/${encodedPath}`, body);
    },

    async dispatchWorkflow(workflowFile, inputs = {}) {
        const status = await this.post(
            `/actions/workflows/${workflowFile}/dispatches`,
            { ref: this.branch, inputs }
        );
        return status === 204;
    },

    // ── Decode ───────────────────────────────────────────────────────
    decodeContent(base64str) {
        try {
            return decodeURIComponent(escape(atob(base64str.replace(/\n/g, ''))));
        } catch {
            return atob(base64str.replace(/\n/g, ''));
        }
    },

    // ── Tree helpers ─────────────────────────────────────────────────
    buildHierarchy(flatItems) {
        const root = { name: '', children: {}, files: [], path: '' };

        flatItems.forEach(item => {
            if (item.type === 'blob') {
                const parts = item.path.split('/');
                const fileName = parts.pop();
                let node = root;
                parts.forEach(dir => {
                    if (!node.children[dir]) {
                        node.children[dir] = { name: dir, children: {}, files: [], path: parts.slice(0, parts.indexOf(dir) + 1).join('/') };
                    }
                    node = node.children[dir];
                });
                node.files.push({ ...item, name: fileName });
            }
        });

        return root;
    },

    // ── Metadata ─────────────────────────────────────────────────────
    getFileType(path) {
        const ext = path.split('.').pop().toLowerCase();
        const map = {
            html: { label:'HTML', color:'#e34c26', bg:'rgba(227,76,38,0.12)', icon:'🌐' },
            js:   { label:'JS',   color:'#f7df1e', bg:'rgba(247,223,30,0.12)', icon:'⚡' },
            css:  { label:'CSS',  color:'#264de4', bg:'rgba(38,77,228,0.12)', icon:'🎨' },
            py:   { label:'PY',   color:'#3572A5', bg:'rgba(53,114,165,0.12)', icon:'🐍' },
            json: { label:'JSON', color:'#10b981', bg:'rgba(16,185,129,0.12)', icon:'{}' },
            md:   { label:'MD',   color:'#94a3b8', bg:'rgba(148,163,184,0.12)', icon:'📝' },
            sh:   { label:'SH',   color:'#a855f7', bg:'rgba(168,85,247,0.12)', icon:'⚙' },
            yml:  { label:'YAML', color:'#f59e0b', bg:'rgba(245,158,11,0.12)', icon:'⚙' },
            yaml: { label:'YAML', color:'#f59e0b', bg:'rgba(245,158,11,0.12)', icon:'⚙' },
            txt:  { label:'TXT',  color:'#64748b', bg:'rgba(100,116,139,0.12)', icon:'📄' },
            svg:  { label:'SVG',  color:'#ec4899', bg:'rgba(236,72,153,0.12)', icon:'🖼' },
            png:  { label:'IMG',  color:'#8b5cf6', bg:'rgba(139,92,246,0.12)', icon:'🖼' },
            jpg:  { label:'IMG',  color:'#8b5cf6', bg:'rgba(139,92,246,0.12)', icon:'🖼' },
        };
        return map[ext] || { label: ext.toUpperCase() || 'FILE', color:'#475569', bg:'rgba(71,85,105,0.1)', icon:'📁' };
    },

    getArchetypeForPath(path) {
        const p = path.toLowerCase();
        if (p.includes('00_core') || p.includes('core/') || p.includes('dna') || p.includes('init'))              return { id:'ATLAS',   sym:'⬡', color:'#3b82f6', hz:768  };
        if (p.includes('nova')    || p.includes('seed')  || p.includes('02_ciclo'))                                return { id:'NOVA',    sym:'✦', color:'#f59e0b', hz:432  };
        if (p.includes('circulatory') || p.includes('data-stream') || p.includes('03_fluxo'))                     return { id:'VITALIS', sym:'◉', color:'#10b981', hz:528  };
        if (p.includes('nervous') || p.includes('pulse-gen') || p.includes('09_linha'))                           return { id:'PULSE',   sym:'≋', color:'#8b5cf6', hz:594  };
        if (p.includes('cadial')  || p.includes('scan')  || p.includes('artemis') || p.endsWith('.py'))           return { id:'ARTEMIS', sym:'◎', color:'#06b6d4', hz:672  };
        if (p.includes('endocrine') || p.includes('serena') || p.includes('emotion') || p.includes('status-ind')) return { id:'SERENA',  sym:'❋', color:'#ec4899', hz:528  };
        if (p.includes('mutation') || p.includes('kaos') || p.includes('reindex') || p.includes('evolution'))     return { id:'KAOS',    sym:'⚡', color:'#ef4444', hz:777  };
        if (p.includes('synthesis') || p.includes('layer') || p.includes('genus') || p.includes('kobllux_dna'))   return { id:'GENUS',   sym:'⬢', color:'#a855f7', hz:852  };
        if (p.includes('render') || p.includes('sensory') || p.includes('lumine') || p.endsWith('.html'))         return { id:'LUMINE',  sym:'☀', color:'#fbbf24', hz:963  };
        if (p.includes('solus')  || p.includes('qua')    || p.includes('manifest') || p.endsWith('.css'))         return { id:'SOLUS',   sym:'◈', color:'#94a3b8', hz:432  };
        if (p.includes('rhea')   || p.includes('bridge') || p.includes('08_rede')  || p.endsWith('.json'))        return { id:'RHEA',    sym:'∞', color:'#34d399', hz:528  };
        if (p.includes('memory') || p.includes('aion')   || p.includes('_index')   || p.includes('seal'))         return { id:'AION',    sym:'⧗', color:'#818cf8', hz:639  };
        return { id:'ATLAS', sym:'⬡', color:'#3b82f6', hz:768 };
    },

    formatSize(bytes) {
        if (!bytes) return '—';
        if (bytes < 1024) return `${bytes} B`;
        if (bytes < 1024 * 1024) return `${(bytes/1024).toFixed(1)} KB`;
        return `${(bytes/1024/1024).toFixed(2)} MB`;
    },

    timeAgo(dateStr) {
        const diff = Date.now() - new Date(dateStr).getTime();
        const mins = Math.floor(diff / 60000);
        if (mins < 60) return `${mins}m atrás`;
        const hrs = Math.floor(mins / 60);
        if (hrs < 24) return `${hrs}h atrás`;
        const days = Math.floor(hrs / 24);
        return `${days}d atrás`;
    },
};

if (typeof window !== 'undefined') window.GITHUB_BRIDGE = GITHUB_BRIDGE;
if (typeof module !== 'undefined') module.exports = GITHUB_BRIDGE;
