// Inicializador do Organismo
document.addEventListener('DOMContentLoaded', () => {
    console.log('🌀 Iniciando organismo SÜMBÜS...');
    
    // Verificar sistemas
    const systems = ['circulatory', 'nervous', 'endocrine', 'motor'];
    const statusEl = document.getElementById('system-status');
    
    systems.forEach(sys => {
        const div = document.createElement('div');
        div.className = 'system-status-item';
        div.innerHTML = `🔧 ${sys}: <span class="status">verificando...</span>`;
        statusEl.appendChild(div);
    });
    
    // Simular inicialização
    setTimeout(() => {
        document.body.setAttribute('data-organism-state', 'active');
        console.log('✅ Organismo ativo na frequência 3Hz');
    }, 3000);
});
