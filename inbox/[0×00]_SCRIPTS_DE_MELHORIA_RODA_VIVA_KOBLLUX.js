//<script type="text/javascript">
// ═══════════════════════════════════════════════════════════════
// SCRIPTS DE MELHORIA - RODA VIVA KOBLLUX
// ═══════════════════════════════════════════════════════════════

function onPageLoaded() {
    // Aplicar animações em elementos específicos
    aplicarAnimacoes();
    
    // Formatando tabelas automaticamente
    formatarTabelas();
    
    // Destacar blocos de código
    destacarCodigo();
    
    // Scroll suave para âncoras
    scrollSuave();
    
    console.log("🌀 KOBLLUX: Sistema de visualização ativado");
    console.log("✧ VERDADE × INTEGRAR ÷ Δ = ∞");
}

function aplicarAnimacoes() {
    // Adicionar classe pulse em headings
    const headings = document.querySelectorAll('h1, h2, h3');
    headings.forEach((h, index) => {
        h.style.animationDelay = `${index * 0.1}s`;
    });
}

function formatarTabelas() {
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        // Adicionar classe para estilização
        table.classList.add('kobllux-table');
        
        // Adicionar números nas linhas
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach((row, index) => {
            row.setAttribute('data-line', index + 1);
        });
    });
}

function destacarCodigo() {
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        // Adicionar contador de linhas
        const lines = block.textContent.split('\n').length;
        block.setAttribute('data-lines', lines);        
        // Simular syntax highlighting básico
        aplicarHighlight(block);
    });
}

function aplicarHighlight(element) {
    let html = element.innerHTML;
    
    // Comentários
    html = html.replace(/(#.*$)/gm, '<span class="ansi-green">$1</span>');
    
    // Strings
    html = html.replace(/(".*?")/g, '<span class="ansi-yellow">$1</span>');
    
    // Números
    html = html.replace(/\b(\d+)\b/g, '<span class="ansi-magenta">$1</span>');
    
    // Keywords Python
    const keywords = ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'return', 'import', 'from'];
    keywords.forEach(kw => {
        const regex = new RegExp(`\\b(${kw})\\b`, 'g');
        html = html.replace(regex, '<span class="ansi-cyan ansi-bold">$1</span>');
    });
    
    element.innerHTML = html;
}

function scrollSuave() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Detectar tema do sistema
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add('dark-theme');
}

// Auto-scroll para o final em modo de leitura contínua
function autoScroll() {    const scrollInterval = setInterval(() => {
        if (document.body.scrollHeight > window.innerHeight) {
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        }
    }, 3000);
    
    // Parar após 30 segundos
    setTimeout(() => clearInterval(scrollInterval), 30000);
}

// Ativar se necessário
// autoScroll();

console.log("🧿 KOBLLUX v14 carregado · 3×6×9×7 = 1134");
