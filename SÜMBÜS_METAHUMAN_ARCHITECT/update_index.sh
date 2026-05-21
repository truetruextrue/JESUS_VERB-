echo ""
echo "🌌 INICIANDO FASE 2 - SISTEMA CIRCULATÓRIO"
echo "=========================================="

# Criar sistema circulatório completo
mkdir -p systems/circulatory

echo "🔄 CRIANDO SISTEMA CIRCULATÓRIO..."
echo "----------------------------------"

# 1. DATA-STREAM.HTML - Fluxo principal de dados
cat > systems/circulatory/data-stream.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR" data-organ="circulatory-core">
<head>
    <meta charset="UTF-8">
    <title>🔄 Fluxo de Dados Circulatório</title>
    <style>
        :root {
            --stream-blue: #3b82f6;
            --stream-purple: #8b5cf6;
            --stream-green: #10b981;
            --stream-red: #ef4444;
            --bg-stream: #0f172a;
        }
        
        body {
            background: var(--bg-stream);
            color: #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
            margin: 0;
            padding: 1rem;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .stream-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            border-radius: 1rem;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(59, 130, 246, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .flow-visualization {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            margin: 2rem 0;
            height: 200px;
            position: relative;
        }
        
        .flow-node {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 1rem;
            transition: all 0.3s;
            position: relative;
            z-index: 1;
        }
        
        .flow-node.active {
            background: rgba(59, 130, 246, 0.1);
            border-color: var(--stream-blue);
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.2);
        }
        
        .flow-node::after {
            content: '→';
            position: absolute;
            right: -1.2rem;
            color: var(--stream-blue);
            opacity: 0.5;
            font-size: 1.5rem;
        }
        
        .flow-node:last-child::after {
            display: none;
        }
        
        .flow-connector {
            position: absolute;
            height: 2px;
            background: linear-gradient(90deg, var(--stream-blue), transparent);
            top: 50%;
            z-index: 0;
            opacity: 0.3;
        }
        
        .data-metrics {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .metric-card {
            padding: 1.5rem;
            border-radius: 0.75rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            transition: all 0.3s;
        }
        
        .metric-card:hover {
            background: rgba(59, 130, 246, 0.1);
            border-color: var(--stream-blue);
            transform: translateY(-3px);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            margin: 0.5rem 0;
        }
        
        .metric-card[data-metric="throughput"] .metric-value { color: var(--stream-blue); }
        .metric-card[data-metric="latency"] .metric-value { color: var(--stream-green); }
        .metric-card[data-metric="errors"] .metric-value { color: var(--stream-red); }
        .metric-card[data-metric="connections"] .metric-value { color: var(--stream-purple); }
        
        .api-panel {
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.75rem;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }
        
        .api-endpoint {
            padding: 1rem;
            margin: 0.5rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 0.5rem;
            border-left: 3px solid var(--stream-blue);
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
        }
        
        .stream-log {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.5rem;
            border: 1px solid rgba(139, 92, 246, 0.3);
            max-height: 300px;
            overflow-y: auto;
        }
        
        .log-entry {
            padding: 0.5rem;
            margin: 0.25rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 0.25rem;
            border-left: 3px solid var(--stream-blue);
            animation: logAppear 0.3s ease;
            font-size: 0.9rem;
        }
        
        .log-entry.data {
            border-left-color: var(--stream-green);
            background: rgba(16, 185, 129, 0.1);
        }
        
        .log-entry.error {
            border-left-color: var(--stream-red);
            background: rgba(239, 68, 68, 0.1);
        }
        
        @keyframes logAppear {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .control-panel {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .control-btn {
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid var(--stream-blue);
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .control-btn:hover {
            background: rgba(59, 130, 246, 0.2);
            transform: translateY(-2px);
        }
        
        .control-btn.active {
            background: var(--stream-blue);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
        }
    </style>
</head>
<body>
    <div class="stream-container">
        <h1 style="color: var(--stream-blue); margin: 0 0 0.5rem 0;">
            🔄 SISTEMA CIRCULATÓRIO
        </h1>
        <p style="color: #94a3b8; margin-bottom: 2rem;">
            Fluxo de dados e comunicação entre sistemas do organismo SÜMBÜS
        </p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 0.5rem;">
            <div>
                <strong style="color: var(--stream-blue);">STATUS: </strong>
                <span id="system-status" style="color: var(--stream-green);">INICIALIZANDO</span>
            </div>
            <div style="display: flex; gap: 1rem;">
                <button onclick="startDataFlow()" id="startFlow" class="control-btn active">
                    ▶️ INICIAR FLUXO
                </button>
                <button onclick="resetSystem()" class="control-btn">
                    🔁 REINICIAR
                </button>
            </div>
        </div>
        
        <div class="flow-visualization" id="flowVisualization">
            <!-- Flow nodes will be generated by JS -->
        </div>
        
        <div class="data-metrics">
            <div class="metric-card" data-metric="throughput">
                <div style="font-size: 0.9rem; color: #94a3b8;">THROUGHPUT</div>
                <div class="metric-value" id="throughput">0</div>
                <div style="font-size: 0.8rem;">KB/s</div>
            </div>
            
            <div class="metric-card" data-metric="latency">
                <div style="font-size: 0.9rem; color: #94a3b8;">LATÊNCIA</div>
                <div class="metric-value" id="latency">0</div>
                <div style="font-size: 0.8rem;">ms</div>
            </div>
            
            <div class="metric-card" data-metric="errors">
                <div style="font-size: 0.9rem; color: #94a3b8;">ERROS</div>
                <div class="metric-value" id="errors">0</div>
                <div style="font-size: 0.8rem;">/min</div>
            </div>
            
            <div class="metric-card" data-metric="connections">
                <div style="font-size: 0.9rem; color: #94a3b8;">CONEXÕES</div>
                <div class="metric-value" id="connections">1</div>
                <div style="font-size: 0.8rem;">Ativas</div>
            </div>
        </div>
        
        <div class="control-panel">
            <button onclick="connectSystem('dna')" class="control-btn">
                🧬 Conectar DNA
            </button>
            <button onclick="connectSystem('nervous')" class="control-btn">
                🧠 Conectar Nervoso
            </button>
            <button onclick="connectSystem('synthesis')" class="control-btn">
                🌀 Conectar Síntese
            </button>
            <button onclick="connectSystem('all')" class="control-btn">
                🌌 Conectar Tudo
            </button>
        </div>
        
        <div class="api-panel">
            <strong style="color: var(--stream-green);">🔌 ENDPOINTS DE API:</strong>
            <div class="api-endpoint">
                <span style="color: var(--stream-blue);">POST</span> /api/data/stream
                <span style="color: #94a3b8; float: right;">→ Envio de dados</span>
            </div>
            <div class="api-endpoint">
                <span style="color: var(--stream-green);">GET</span> /api/system/status
                <span style="color: #94a3b8; float: right;">→ Status do sistema</span>
            </div>
            <div class="api-endpoint">
                <span style="color: var(--stream-purple);">WS</span> /ws/data/feed
                <span style="color: #94a3b8; float: right;">→ WebSocket em tempo real</span>
            </div>
        </div>
        
        <div class="stream-log" id="streamLog">
            <div class="log-entry">[SYSTEM] Sistema circulatório inicializado</div>
            <div class="log-entry">[CONNECTION] Conectando com DNA Core...</div>
            <div class="log-entry data">[DATA] Pronto para fluxo de dados</div>
        </div>
    </div>
    
    <script>
        // Circulatory System Engine
        const CIRCULATORY_SYSTEM = {
            active: false,
            throughput: 0,
            latency: 0,
            errors: 0,
            connections: 1,
            connectedSystems: ['core'],
            dataStream: [],
            intervalId: null
        };
        
        // Flow nodes configuration
        const FLOW_NODES = [
            { id: 'input', name: 'ENTRADA', icon: '📥', color: 'var(--stream-green)' },
            { id: 'process', name: 'PROCESSO', icon: '⚡', color: 'var(--stream-blue)' },
            { id: 'transform', name: 'TRANSFORMAÇÃO', icon: '🔄', color: 'var(--stream-purple)' },
            { id: 'storage', name: 'ARMAZENAMENTO', icon: '💾', color: 'var(--stream-blue)' },
            { id: 'output', name: 'SAÍDA', icon: '📤', color: 'var(--stream-green)' }
        ];
        
        // Initialize flow visualization
        function initializeFlowVisualization() {
            const container = document.getElementById('flowVisualization');
            container.innerHTML = '';
            
            // Create flow nodes
            FLOW_NODES.forEach((node, index) => {
                const nodeEl = document.createElement('div');
                nodeEl.className = 'flow-node';
                nodeEl.id = `node-${node.id}`;
                nodeEl.innerHTML = `
                    <div style="font-size: 2rem;">${node.icon}</div>
                    <div style="font-size: 0.9rem; margin-top: 0.5rem; font-weight: bold;">${node.name}</div>
                    <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 0.25rem;">ID: ${node.id}</div>
                `;
                container.appendChild(nodeEl);
                
                // Create connector (except for last node)
                if (index < FLOW_NODES.length - 1) {
                    const connector = document.createElement('div');
                    connector.className = 'flow-connector';
                    connector.id = `connector-${node.id}`;
                    container.appendChild(connector);
                }
            });
            
            // Position connectors
            updateConnectors();
        }
        
        // Update connector positions
        function updateConnectors() {
            const nodes = document.querySelectorAll('.flow-node');
            const container = document.querySelector('.flow-visualization');
            const containerRect = container.getBoundingClientRect();
            
            document.querySelectorAll('.flow-connector').forEach((connector, index) => {
                if (nodes[index] && nodes[index + 1]) {
                    const node1Rect = nodes[index].getBoundingClientRect();
                    const node2Rect = nodes[index + 1].getBoundingClientRect();
                    
                    const x1 = node1Rect.left - containerRect.left + node1Rect.width;
                    const x2 = node2Rect.left - containerRect.left;
                    const y = node1Rect.top - containerRect.top + node1Rect.height / 2;
                    
                    connector.style.left = `${x1}px`;
                    connector.style.top = `${y}px`;
                    connector.style.width = `${x2 - x1}px`;
                }
            });
        }
        
        // Start data flow
        function startDataFlow() {
            if (CIRCULATORY_SYSTEM.active) {
                stopDataFlow();
                return;
            }
            
            CIRCULATORY_SYSTEM.active = true;
            const button = document.getElementById('startFlow');
            button.textContent = '⏸️ PAUSAR FLUXO';
            button.style.background = 'rgba(245, 158, 11, 0.2)';
            button.style.borderColor = '#f59e0b';
            
            document.getElementById('system-status').textContent = 'FLUXO ATIVO';
            document.getElementById('system-status').style.color = 'var(--stream-green)';
            
            addLog('[FLOW] Fluxo de dados iniciado', 'data');
            
            // Activate flow visualization
            activateFlow();
            
            // Start data simulation
            CIRCULATORY_SYSTEM.intervalId = setInterval(simulateDataFlow, 1000);
        }
        
        // Stop data flow
        function stopDataFlow() {
            CIRCULATORY_SYSTEM.active = false;
            const button = document.getElementById('startFlow');
            button.textContent = '▶️ INICIAR FLUXO';
            button.style.background = 'rgba(59, 130, 246, 0.1)';
            button.style.borderColor = 'var(--stream-blue)';
            
            document.getElementById('system-status').textContent = 'PAUSADO';
            document.getElementById('system-status').style.color = '#f59e0b';
            
            addLog('[FLOW] Fluxo de dados pausado');
            
            clearInterval(CIRCULATORY_SYSTEM.intervalId);
            
            // Deactivate flow visualization
            deactivateFlow();
        }
        
        // Activate flow animation
        function activateFlow() {
            // Animate nodes
            FLOW_NODES.forEach((node, index) => {
                const nodeEl = document.getElementById(`node-${node.id}`);
                const connector = document.getElementById(`connector-${node.id}`);
                
                // Node pulse animation
                setTimeout(() => {
                    nodeEl.classList.add('active');
                    nodeEl.style.borderColor = node.color;
                    nodeEl.style.boxShadow = `0 0 20px ${node.color.replace(')', ', 0.3)').replace('rgb', 'rgba')}`;
                    
                    if (connector) {
                        connector.style.background = `linear-gradient(90deg, ${node.color}, ${FLOW_NODES[index + 1]?.color || node.color})`;
                        connector.style.opacity = '0.6';
                    }
                }, index * 300);
                
                // Continuous pulse
                setInterval(() => {
                    if (CIRCULATORY_SYSTEM.active) {
                        nodeEl.animate([
                            { transform: 'scale(1)', boxShadow: `0 0 20px ${node.color.replace(')', ', 0.3)').replace('rgb', 'rgba')}` },
                            { transform: 'scale(1.05)', boxShadow: `0 0 30px ${node.color.replace(')', ', 0.5)').replace('rgb', 'rgba')}` },
                            { transform: 'scale(1)', boxShadow: `0 0 20px ${node.color.replace(')', ', 0.3)').replace('rgb', 'rgba')}` }
                        ], { duration: 1000, delay: index * 200 });
                    }
                }, 3000);
            });
        }
        
        // Deactivate flow animation
        function deactivateFlow() {
            FLOW_NODES.forEach(node => {
                const nodeEl = document.getElementById(`node-${node.id}`);
                const connector = document.getElementById(`connector-${node.id}`);
                
                nodeEl.classList.remove('active');
                nodeEl.style.borderColor = '';
                nodeEl.style.boxShadow = '';
                
                if (connector) {
                    connector.style.background = '';
                    connector.style.opacity = '0.3';
                }
            });
        }
        
        // Simulate data flow
        function simulateDataFlow() {
            if (!CIRCULATORY_SYSTEM.active) return;
            
            // Update metrics
            CIRCULATORY_SYSTEM.throughput = 50 + Math.random() * 150;
            CIRCULATORY_SYSTEM.latency = 5 + Math.random() * 45;
            
            // Random errors (5% chance)
            if (Math.random() < 0.05) {
                CIRCULATORY_SYSTEM.errors++;
                addLog(`[ERROR] Erro no fluxo de dados #${CIRCULATORY_SYSTEM.errors}`, 'error');
            }
            
            // Update displays
            document.getElementById('throughput').textContent = CIRCULATORY_SYSTEM.throughput.toFixed(1);
            document.getElementById('latency').textContent = CIRCULATORY_SYSTEM.latency.toFixed(1);
            document.getElementById('errors').textContent = CIRCULATORY_SYSTEM.errors;
            document.getElementById('connections').textContent = CIRCULATORY_SYSTEM.connections;
            
            // Add data packet log
            if (Math.random() > 0.3) {
                const packetSize = (1 + Math.random() * 9).toFixed(1);
                const destinations = ['DNA Core', 'Sistema Nervoso', 'Motor de Síntese', 'Renderização'];
                const destination = destinations[Math.floor(Math.random() * destinations.length)];
                
                addLog(`[DATA] Pacote de ${packetSize}KB → ${destination}`, 'data');
                
                // Store in data stream
                CIRCULATORY_SYSTEM.dataStream.push({
                    timestamp: new Date(),
                    size: packetSize,
                    destination: destination,
                    latency: CIRCULATORY_SYSTEM.latency
                });
                
                // Keep stream limited
                if (CIRCULATORY_SYSTEM.dataStream.length > 50) {
                    CIRCULATORY_SYSTEM.dataStream.shift();
                }
            }
        }
        
        // Connect to system
        function connectSystem(system) {
            if (system === 'all') {
                connectSystem('dna');
                connectSystem('nervous');
                connectSystem('synthesis');
                connectSystem('render');
                return;
            }
            
            const systemNames = {
                dna: 'DNA Core',
                nervous: 'Sistema Nervoso',
                synthesis: 'Motor de Síntese',
                render: 'Renderização'
            };
            
            if (!CIRCULATORY_SYSTEM.connectedSystems.includes(system)) {
                CIRCULATORY_SYSTEM.connectedSystems.push(system);
                CIRCULATORY_SYSTEM.connections = CIRCULATORY_SYSTEM.connectedSystems.length;
                
                addLog(`[CONNECTION] Conectado com ${systemNames[system]}`, 'data');
                
                // Update button
                const button = event.target;
                button.textContent = `✅ ${button.textContent.replace('Conectar', 'Conectado')}`;
                button.classList.add('active');
                button.disabled = true;
                
                // Update metrics
                document.getElementById('connections').textContent = CIRCULATORY_SYSTEM.connections;
            }
        }
        
        // Reset system
        function resetSystem() {
            stopDataFlow();
            
            CIRCULATORY_SYSTEM.throughput = 0;
            CIRCULATORY_SYSTEM.latency = 0;
            CIRCULATORY_SYSTEM.errors = 0;
            CIRCULATORY_SYSTEM.connections = 1;
            CIRCULATORY_SYSTEM.connectedSystems = ['core'];
            CIRCULATORY_SYSTEM.dataStream = [];
            
            // Reset displays
            document.getElementById('throughput').textContent = '0';
            document.getElementById('latency').textContent = '0';
            document.getElementById('errors').textContent = '0';
            document.getElementById('connections').textContent = '1';
            document.getElementById('system-status').textContent = 'INICIALIZANDO';
            document.getElementById('system-status').style.color = 'var(--stream-green)';
            
            // Reset buttons
            document.querySelectorAll('.control-btn').forEach(btn => {
                if (!btn.id.includes('startFlow')) {
                    btn.textContent = btn.textContent.replace('✅', '').replace('Conectado', 'Conectar');
                    btn.classList.remove('active');
                    btn.disabled = false;
                }
            });
            
            // Clear log (keep first 3 entries)
            const log = document.getElementById('streamLog');
            while (log.children.length > 3) {
                log.removeChild(log.lastChild);
            }
            
            addLog('[SYSTEM] Sistema reinicializado');
            addLog('[READY] Pronto para novas conexões');
        }
        
        // Add log entry
        function addLog(message, type = '') {
            const log = document.getElementById('streamLog');
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            entry.textContent = message;
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
            
            // Limit log size
            if (log.children.length > 20) {
                log.removeChild(log.firstChild);
            }
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            console.log('🔄 Sistema circulatório inicializado');
            
            initializeFlowVisualization();
            updateConnectors();
            
            // Auto-update connectors on resize
            window.addEventListener('resize', updateConnectors);
            
            // Auto-start flow after 2 seconds
            setTimeout(() => {
                startDataFlow();
            }, 2000);
        });
        
        // Export API
        window.CIRCULATORY_SYSTEM = {
            startFlow: startDataFlow,
            stopFlow: stopDataFlow,
            connectSystem,
            resetSystem,
            getState: () => CIRCULATORY_SYSTEM,
            version: '1.0.0-circulatory'
        };
    </script>
</body>
</html>
EOF

echo "✅ 1. data-stream.html criado"

# 2. API-INTEGRATION.HTML - Integração com APIs externas
cat > systems/circulatory/api-integration.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR" data-organ="api-integration">
<head>
    <meta charset="UTF-8">
    <title>🔗 Integração com APIs</title>
    <style>
        :root {
            --api-blue: #3b82f6;
            --api-green: #10b981;
            --api-purple: #8b5cf6;
            --api-orange: #f59e0b;
            --bg-api: #0f172a;
        }
        
        body {
            background: var(--bg-api);
            color: #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
            margin: 0;
            padding: 1rem;
            min-height: 100vh;
        }
        
        .api-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            border-radius: 1rem;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(59, 130, 246, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .api-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .api-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0.75rem;
            padding: 1.5rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .api-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
        }
        
        .api-card.github::before { background: #6cc644; }
        .api-card.rest::before { background: var(--api-blue); }
        .api-card.websocket::before { background: var(--api-purple); }
        .api-card.graphql::before { background: #e535ab; }
        
        .api-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        .api-card.active {
            border-color: var(--api-green);
            background: rgba(16, 185, 129, 0.05);
        }
        
        .api-status {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.8rem;
            font-weight: bold;
            margin-top: 1rem;
        }
        
        .status-connected { background: rgba(16, 185, 129, 0.2); color: var(--api-green); border: 1px solid rgba(16, 185, 129, 0.3); }
        .status-disconnected { background: rgba(100, 116, 139, 0.2); color: #94a3b8; border: 1px solid rgba(100, 116, 139, 0.3); }
        .status-error { background: rgba(239, 68, 68, 0.2); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }
        
        .request-builder {
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.75rem;
            border: 1px solid rgba(139, 92, 246, 0.3);
        }
        
        .code-editor {
            margin-top: 1rem;
            padding: 1rem;
            background: #1e293b;
            border-radius: 0.5rem;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            min-height: 150px;
            max-height: 300px;
            overflow-y: auto;
            white-space: pre-wrap;
        }
        
        .response-viewer {
            margin-top: 1rem;
            padding: 1rem;
            background: #0f172a;
            border-radius: 0.5rem;
            border: 1px solid rgba(16, 185, 129, 0.3);
            max-height: 300px;
            overflow-y: auto;
            font-size: 0.9rem;
        }
        
        .api-log {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.5rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
            max-height: 200px;
            overflow-y: auto;
        }
        
        .log-entry {
            padding: 0.5rem;
            margin: 0.25rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 0.25rem;
            border-left: 3px solid var(--api-blue);
            animation: logAppear 0.3s ease;
            font-size: 0.9rem;
        }
        
        .log-entry.request { border-left-color: var(--api-green); background: rgba(16, 185, 129, 0.1); }
        .log-entry.response { border-left-color: var(--api-purple); background: rgba(139, 92, 246, 0.1); }
        .log-entry.error { border-left-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
        
        @keyframes logAppear {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .control-bar {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .api-btn {
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid var(--api-blue);
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .api-btn:hover {
            background: rgba(59, 130, 246, 0.2);
            transform: translateY(-2px);
        }
        
        .api-btn.primary {
            background: linear-gradient(135deg, var(--api-blue), var(--api-purple));
            border: none;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="api-container">
        <h1 style="color: var(--api-blue); margin: 0 0 0.5rem 0;">
            🔗 INTEGRAÇÃO COM APIs
        </h1>
        <p style="color: #94a3b8; margin-bottom: 2rem;">
            Conexão e comunicação com sistemas externos do organismo SÜMBÜS
        </p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 1rem; background: rgba(16, 185, 129, 0.1); border-radius: 0.5rem;">
            <div>
                <strong style="color: var(--api-green);">STATUS GLOBAL: </strong>
                <span id="global-status" style="color: white;">CONECTANDO...</span>
            </div>
            <div style="display: flex; gap: 1rem;">
                <button onclick="connectAllAPIs()" class="api-btn primary">
                    🌐 CONECTAR TODAS APIS
                </button>
                <button onclick="testAllEndpoints()" class="api-btn">
                    🧪 TESTAR ENDPOINTS
                </button>
            </div>
        </div>
        
        <div class="api-grid">
            <div class="api-card github" id="github-api">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🐙</div>
                <h3 style="margin: 0 0 0.5rem 0; color: white;">GITHUB API</h3>
                <p style="color: #94a3b8; margin: 0 0 1rem 0; font-size: 0.9rem;">
                    Acesso a repositórios, commits e dados de desenvolvimento.
                </p>
                <div class="api-status status-disconnected" id="github-status">DESCONECTADO</div>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: #94a3b8;">
                    Endpoint: api.github.com
                </div>
                <button onclick="toggleAPI('github')" style="margin-top: 1rem; padding: 0.5rem 1rem; background: rgba(108, 198, 68, 0.1); border: 1px solid #6cc644; color: white; border-radius: 0.5rem; cursor: pointer; width: 100%;">
                    CONECTAR
                </button>
            </div>
            
            <div class="api-card rest" id="rest-api">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🔄</div>
                <h3 style="margin: 0 0 0.5rem 0; color: white;">REST API</h3>
                <p style="color: #94a3b8; margin: 0 0 1rem 0; font-size: 0.9rem;">
                    Comunicação padrão REST com sistemas externos.
                </p>
                <div class="api-status status-connected" id="rest-status">CONECTADO</div>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: #94a3b8;">
                    Protocolo: HTTP/HTTPS
                </div>
                <button onclick="toggleAPI('rest')" style="margin-top: 1rem; padding: 0.5rem 1rem; background: rgba(59, 130, 246, 0.1); border: 1px solid var(--api-blue); color: white; border-radius: 0.5rem; cursor: pointer; width: 100%;">
                    TESTAR
                </button>
            </div>
            
            <div class="api-card websocket" id="websocket-api">
                <div style="font-size: 2rem; margin-bottom: 1rem;">⚡</div>
                <h3 style="margin: 0 0 0.5rem 0; color: white;">WEBSOCKET</h3>
                <p style="color: #94a3b8; margin: 0 0 1rem 0; font-size: 0.9rem;">
                    Comunicação em tempo real bidirecional.
                </p>
                <div class="api-status status-disconnected" id="websocket-status">DESCONECTADO</div>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: #94a3b8;">
                    Protocolo: WS/WSS
                </div>
                <button onclick="toggleAPI('websocket')" style="margin-top: 1rem; padding: 0.5rem 1rem; background: rgba(139, 92, 246, 0.1); border: 1px solid var(--api-purple); color: white; border-radius: 0.5rem; cursor: pointer; width: 100%;">
                    CONECTAR
                </button>
            </div>
            
            <div class="api-card graphql" id="graphql-api">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🕸️</div>
                <h3 style="margin: 0 0 0.5rem 0; color: white;">GRAPHQL</h3>
                <p style="color: #94a3b8; margin: 0 0 1rem 0; font-size: 0.9rem;">
                    Consultas flexíveis e eficientes para dados complexos.
                </p>
                <div class="api-status status-disconnected" id="graphql-status">DESCONECTADO</div>
                <div style="margin-top: 1rem; font-size: 0.8rem; color: #94a3b8;">
                    Query Language
                </div>
                <button onclick="toggleAPI('graphql')" style="margin-top: 1rem; padding: 0.5rem 1rem; background: rgba(229, 53, 171, 0.1); border: 1px solid #e535ab; color: white; border-radius: 0.5rem; cursor: pointer; width: 100%;">
                    CONECTAR
                </button>
            </div>
        </div>
        
        <div class="request-builder">
            <strong style="color: var(--api-blue);">🧱 CONSTRUTOR DE REQUISIÇÕES:</strong>
            <div class="control-bar">
                <select id="api-select" style="padding: 0.75rem; background: #1e293b; border: 1px solid rgba(255,255,255,0.1); color: white; border-radius: 0.5rem; flex: 1;">
                    <option value="github">GitHub API</option>
                    <option value="rest">REST API</option>
                    <option value="websocket">WebSocket</option>
                    <option value="graphql">GraphQL</option>
                </select>
                <select id="method-select" style="padding: 0.75rem; background: #1e293b; border: 1px solid rgba(255,255,255,0.1); color: white; border-radius: 0.5rem;">
                    <option value="GET">GET</option>
                    <option value="POST">POST</option>
                    <option value="PUT">PUT</option>
                    <option value="DELETE">DELETE</option>
                </select>
                <input type="text" id="endpoint-input" placeholder="/api/endpoint" style="padding: 0.75rem; background: #1e293b; border: 1px solid rgba(255,255,255,0.1); color: white; border-radius: 0.5rem; flex: 2;">
                <button onclick="sendRequest()" class="api-btn primary">🚀 ENVIAR</button>
            </div>
            
            <div class="code-editor" id="request-body" contenteditable="true">
{
  "query": "query { \n  system {\n    status\n    version\n  }\n}",
  "variables": {}
}
            </div>
        </div>
        
        <div style="margin-top: 2rem;">
            <strong style="color: var(--api-green);">📡 RESPOSTA:</strong>
            <div class="response-viewer" id="response-viewer">
                // Aguardando requisição...
                // A resposta aparecerá aqui
            </div>
        </div>
        
        <div class="api-log" id="apiLog">
            <div class="log-entry">[API] Sistema de integração inicializado</div>
            <div class="log-entry request">[REST] API REST conectada automaticamente</div>
            <div class="log-entry">[READY] Pronto para integrações</div>
        </div>
    </div>
    
    <script>
        // API Integration System
        const API_SYSTEM = {
            github: { connected: false, endpoint: 'https://api.github.com' },
            rest: { connected: true, endpoint: '/api' },
            websocket: { connected: false, endpoint: 'ws://localhost:8080' },
            graphql: { connected: false, endpoint: '/graphql' },
            logs: [],
            activeConnections: 1
        };
        
        // Toggle API connection
        function toggleAPI(api) {
            const apiData = API_SYSTEM[api];
            const statusEl = document.getElementById(`${api}-status`);
            const button = event.target;
            
            if (apiData.connected) {
                // Disconnect
                apiData.connected = false;
                API_SYSTEM.activeConnections--;
                
                statusEl.textContent = 'DESCONECTADO';
                statusEl.className = 'api-status status-disconnected';
                
                button.textContent = 'CONECTAR';
                button.style.background = api === 'github' ? 'rgba(108, 198, 68, 0.1)' :
                                        api === 'rest' ? 'rgba(59, 130, 246, 0.1)' :
                                        api === 'websocket' ? 'rgba(139, 92, 246, 0.1)' :
                                        'rgba(229, 53, 171, 0.1)';
                
                document.getElementById(`${api}-api`).classList.remove('active');
                
                addLog(`[${api.toUpperCase()}] Desconectado`, 'error');
            } else {
                // Connect (simulated)
                apiData.connected = true;
                API_SYSTEM.activeConnections++;
                
                statusEl.textContent = 'CONECTANDO...';
                statusEl.className = 'api-status status-error';
                
                button.textContent = 'CONECTANDO...';
                button.disabled = true;
                
                // Simulate connection delay
                setTimeout(() => {
                    apiData.connected = true;
                    
                    statusEl.textContent = 'CONECTADO';
                    statusEl.className = 'api-status status-connected';
                    
                    button.textContent = 'DESCONECTAR';
                    button.disabled = false;
                    button.style.background = 'rgba(245, 158, 11, 0.2)';
                    
                    document.getElementById(`${api}-api`).classList.add('active');
                    
                    addLog(`[${api.toUpperCase()}] Conectado com sucesso`, 'request');
                    
                    // Update global status
                    updateGlobalStatus();
                }, 1500);
            }
            
            updateGlobalStatus();
        }
        
        // Connect all APIs
        function connectAllAPIs() {
            addLog('[SYSTEM] Conectando todas as APIs...');
            
            const apis = ['github', 'websocket', 'graphql'];
            let delay = 0;
            
            apis.forEach(api => {
                if (!API_SYSTEM[api].connected) {
                    setTimeout(() => {
                        // Simulate connection
                        API_SYSTEM[api].connected = true;
                        API_SYSTEM.activeConnections++;
                        
                        const statusEl = document.getElementById(`${api}-status`);
                        const button = document.querySelector(`#${api}-api button`);
                        
                        statusEl.textContent = 'CONECTADO';
                        statusEl.className = 'api-status status-connected';
                        
                        if (button) {
                            button.textContent = 'DESCONECTAR';
                            button.style.background = 'rgba(245, 158, 11, 0.2)';
                        }
                        
                        document.getElementById(`${api}-api`).classList.add('active');
                        
                        addLog(`[${api.toUpperCase()}] Conectado automaticamente`, 'request');
                        
                        updateGlobalStatus();
                    }, delay);
                    
                    delay += 1000;
                }
            });
            
            setTimeout(() => {
                addLog('[SYSTEM] Todas as APIs conectadas!');
            }, delay);
        }
        
        // Test all endpoints
        function testAllEndpoints() {
            addLog('[TEST] Iniciando teste de todos endpoints...');
            
            const endpoints = [
                { api: 'rest', method: 'GET', path: '/api/status' },
                { api: 'github', method: 'GET', path: '/users/octocat' },
                { api: 'graphql', method: 'POST', path: '/graphql' },
                { api: 'websocket', method: 'WS', path: '/ws' }
            ];
            
            endpoints.forEach((endpoint, index) => {
                setTimeout(() => {
                    if (API_SYSTEM[endpoint.api].connected) {
                        addLog(`[TEST] ${endpoint.api.toUpperCase()} ${endpoint.method} ${endpoint.path}: ✅ OK`, 'response');
                    } else {
                        addLog(`[TEST] ${endpoint.api.toUpperCase()} ${endpoint.method} ${endpoint.path}: ❌ FALHA (desconectado)`, 'error');
                    }
                }, index * 800);
            });
        }
        
        // Send API request
        function sendRequest() {
            const api = document.getElementById('api-select').value;
            const method = document.getElementById('method-select').value;
            const endpoint = document.getElementById('endpoint-input').value;
            const body = document.getElementById('request-body').textContent;
            
            if (!API_SYSTEM[api].connected) {
                addLog(`[ERROR] API ${api.toUpperCase()} não está conectada`, 'error');
                return;
            }
            
            addLog(`[REQUEST] ${method} ${API_SYSTEM[api].endpoint}${endpoint}`, 'request');
            
            // Simulate API request
            const responseViewer = document.getElementById('response-viewer');
            responseViewer.innerHTML = '<span style="color: #94a3b8;">⏳ Processando requisição...</span>';
            
            setTimeout(() => {
                // Generate mock response based on API type
                let mockResponse;
                
                switch(api) {
                    case 'github':
                        mockResponse = {
                            status: 200,
                            data: {
                                login: "SÜMBÜS-Metahuman",
                                id: Date.now(),
                                avatar_url: "https://avatars.githubusercontent.com/u/1?v=4",
                                url: "https://api.github.com/users/SÜMBÜS-Metahuman",
                                html_url: "https://github.com/SÜMBÜS-Metahuman",
                                type: "Organization",
                                name: "SÜMBÜS Metahuman Architect",
                                created_at: new Date().toISOString(),
                                updated_at: new Date().toISOString()
                            },
                            headers: {
                                "x-ratelimit-limit": "5000",
                                "x-ratelimit-remaining": "4999",
                                "x-ratelimit-reset": Math.floor(Date.now() / 1000) + 3600
                            }
                        };
                        break;
                        
                    case 'rest':
                        mockResponse = {
                            status: 200,
                            data: {
                                system: "SÜMBÜS Metahuman",
                                version: "1.0.0",
                                status: "operational",
                                timestamp: new Date().toISOString(),
                                endpoints: [
                                    { path: "/api/status", method: "GET", description: "System status" },
                                    { path: "/api/data", method: "POST", description: "Data ingestion" },
                                    { path: "/api/health", method: "GET", description: "Health check" }
                                ]
                            },
                            message: "Request successful"
                        };
                        break;
                        
                    case 'graphql':
                        mockResponse = {
                            data: {
                                system: {
                                    status: "ACTIVE",
                                    version: "1.0.0",
                                    frequency: "6Hz",
                                    systemsActive: 6,
                                    systemsTotal: 8,
                                    uptime: "24h"
                                },
                                organism: {
                                    name: "SÜMBÜS Metahuman Architect",
                                    state: "GROWING",
                                    progress: "15.2%",
                                    evolution: "Generation 1"
                                }
                            },
                            errors: null,
                            extensions: {
                                timestamp: new Date().toISOString(),
                                duration: "142ms",
                                operation: "query"
                            }
                        };
                        break;
                        
                    case 'websocket':
                        mockResponse = {
                            type: "message",
                            data: {
                                event: "data_stream",
                                payload: {
                                    timestamp: new Date().toISOString(),
                                    throughput: (Math.random() * 200).toFixed(1),
                                    latency: (Math.random() * 50).toFixed(1),
                                    connections: API_SYSTEM.activeConnections
                                }
                            },
                            channel: "system_metrics"
                        };
                        break;
                }
                
                // Format and display response
                responseViewer.innerHTML = `<pre style="margin: 0; color: var(--api-green);">${JSON.stringify(mockResponse, null, 2)}</pre>`;
                
                addLog(`[RESPONSE] ${method} ${endpoint}: ✅ 200 OK`, 'response');
            }, 1000 + Math.random() * 2000);
        }
        
        // Update global status
        function updateGlobalStatus() {
            const statusEl = document.getElementById('global-status');
            const connected = API_SYSTEM.activeConnections;
            const total = Object.keys(API_SYSTEM).length - 2; // Exclude logs and activeConnections
            
            if (connected === total) {
                statusEl.textContent = `✅ TODAS APIS CONECTADAS (${connected}/${total})`;
                statusEl.style.color = 'var(--api-green)';
            } else if (connected >= total / 2) {
                statusEl.textContent = `🟡 ${connected}/${total} APIS CONECTADAS`;
                statusEl.style.color = '#f59e0b';
            } else {
                statusEl.textContent = `🔴 ${connected}/${total} APIS CONECTADAS`;
                statusEl.style.color = '#ef4444';
            }
        }
        
        // Add log entry
        function addLog(message, type = '') {
            const log = document.getElementById('apiLog');
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            entry.textContent = message;
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
            
            API_SYSTEM.logs.push({
                timestamp: new Date(),
                message: message,
                type: type
            });
            
            // Limit log size
            if (log.children.length > 20) {
                log.removeChild(log.firstChild);
            }
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            console.log('🔗 Sistema de integração com APIs inicializado');
            
            updateGlobalStatus();
            
            // Auto-connect REST API on load
            setTimeout(() => {
                document.getElementById('rest-api').classList.add('active');
            }, 500);
            
            // Auto-log updates
            setInterval(() => {
                if (Math.random() > 0.7 && API_SYSTEM.activeConnections > 0) {
                    const messages = [
                        '[HEARTBEAT] Conexões ativas verificadas',
                        '[MONITOR] Latência dentro dos limites',
                        '[SECURITY] Tokens renovados',
                        '[PERFORMANCE] Cache otimizado'
                    ];
                    addLog(messages[Math.floor(Math.random() * messages.length)]);
                }
            }, 5000);
        });
        
        // Export API
        window.API_INTEGRATION = {
            connectAll: connectAllAPIs,
            testAll: testAllEndpoints,
            sendRequest,
            toggleAPI,
            getState: () => API_SYSTEM,
            version: '1.0.0-api'
        };
    </script>
</body>
</html>
EOF

echo "✅ 2. api-integration.html criado"

# 3. GITHUB-CONNECTOR.HTML - Conector específico para GitHub
cat > systems/circulatory/github-connector.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR" data-organ="github-connector">
<head>
    <meta charset="UTF-8">
    <title>🐙 Conector GitHub</title>
    <style>
        :root {
            --github-green: #6cc644;
            --github-purple: #8b5cf6;
            --github-blue: #3b82f6;
            --bg-github: #0f172a;
        }
        
        body {
            background: var(--bg-github);
            color: #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
            margin: 0;
            padding: 1rem;
            min-height: 100vh;
        }
        
        .github-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            border-radius: 1rem;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(108, 198, 68, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .repo-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .repo-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 0.75rem;
            padding: 1.5rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .repo-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: var(--github-green);
        }
        
        .repo-card:hover {
            transform: translateY(-5px);
            border-color: var(--github-green);
            box-shadow: 0 10px 30px rgba(108, 198, 68, 0.2);
        }
        
        .repo-stats {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
            font-size: 0.9rem;
        }
        
        .stat-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #94a3b8;
        }
        
        .commit-graph {
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.75rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }
        
        .graph-bars {
            display: flex;
            height: 100px;
            align-items: flex-end;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .graph-bar {
            flex: 1;
            background: linear-gradient(to top, var(--github-green), var(--github-blue));
            border-radius: 0.25rem 0.25rem 0 0;
            min-height: 5px;
            position: relative;
        }
        
        .graph-bar::after {
            content: attr(data-day);
            position: absolute;
            top: -1.5rem;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.8rem;
            color: #94a3b8;
        }
        
        .user-profile {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
            padding: 1rem;
            background: rgba(108, 198, 68, 0.1);
            border-radius: 0.75rem;
            border: 1px solid rgba(108, 198, 68, 0.3);
        }
        
        .avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            border: 3px solid var(--github-green);
        }
        
        .activity-feed {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.5rem;
            border: 1px solid rgba(139, 92, 246, 0.3);
            max-height: 300px;
            overflow-y: auto;
        }
        
        .activity-item {
            padding: 0.75rem;
            margin: 0.5rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 0.5rem;
            border-left: 3px solid var(--github-green);
        }
        
        .github-log {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 0.5rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
            max-height: 200px;
            overflow-y: auto;
        }
        
        .log-entry {
            padding: 0.5rem;
            margin: 0.25rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 0.25rem;
            border-left: 3px solid var(--github-green);
            animation: logAppear 0.3s ease;
            font-size: 0.9rem;
        }
        
        .log-entry.commit { border-left-color: var(--github-blue); background: rgba(59, 130, 246, 0.1); }
        .log-entry.pull { border-left-color: var(--github-purple); background: rgba(139, 92, 246, 0.1); }
        .log-entry.error { border-left-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
        
        @keyframes logAppear {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .control-panel {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .github-btn {
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            background: rgba(108, 198, 68, 0.1);
            border: 1px solid var(--github-green);
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .github-btn:hover {
            background: rgba(108, 198, 68, 0.2);
            transform: translateY(-2px);
        }
        
        .github-btn.primary {
            background: linear-gradient(135deg, var(--github-green), var(--github-blue));
            border: none;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="github-container">
        <h1 style="color: var(--github-green); margin: 0 0 0.5rem 0;">
            🐙 CONECTOR GITHUB
        </h1>
        <p style="color: #94a3b8; margin-bottom: 2rem;">
            Integração com repositórios e dados de desenvolvimento do organismo SÜMBÜS
        </p>
        
        <div class="user-profile">
            <img src="https://avatars.githubusercontent.com/u/1?v=4" class="avatar" id="user-avatar">
            <div>
                <h2 style="margin: 0; color: white;" id="user-name">SÜMBÜS Metahuman</h2>
                <p style="margin: 0.5rem 0; color: #94a3b8;" id="user-bio">Organismo Digital Fractal • DNA KOBLLUX</p>
                <div style="display: flex; gap: 1rem; font-size: 0.9rem;">
                    <div><strong style="color: var(--github-green);" id="repo-count">5</strong> repositórios</div>
                    <div><strong style="color: var(--github-blue);" id="gist-count">12</strong> gists</div>
                    <div><strong style="color: var(--github-purple);" id="follower-count">42</strong> followers</div>
                </div>
            </div>
        </div>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 0.5rem;">
            <div>
                <strong style="color: var(--github-blue);">STATUS: </strong>
                <span id="connection-status" style="color: var(--github-green);">CONECTADO</span>
                <span style="color: #94a3b8; margin-left: 1rem;">API Rate: </span>
                <span id="rate-limit" style="color: white;">4999/5000</span>
            </div>
            <div class="control-panel">
                <button onclick="syncRepositories()" class="github-btn primary">
                    🔄 SINCRONIZAR REPOS
                </button>
                <button onclick="fetchActivity()" class="github-btn">
                    📊 BUSCAR ATIVIDADE
                </button>
                <button onclick="testWebhook()" class="github-btn">
                    ⚡ TESTAR WEBHOOK
                </button>
            </div>
        </div>
        
        <div class="repo-grid" id="repoGrid">
            <!-- Repositories will be loaded here -->
        </div>
        
        <div class="commit-graph">
            <strong style="color: var(--github-blue);">📈 ATIVIDADE DE COMMITS (ÚLTIMOS 14 DIAS):</strong>
            <div class="graph-bars" id="commitGraph">
                <!-- Commit graph will be generated here -->
            </div>
        </div>
        
        <div style="margin-top: 2rem;">
            <strong style="color: var(--github-purple);">📝 FEED DE ATIVIDADE RECENTE:</strong>
            <div class="activity-feed" id="activityFeed">
                <!-- Activity feed will be loaded here -->
            </div>
        </div>
        
        <div class="github-log" id="githubLog">
            <div class="log-entry">[GITHUB] Conector inicializado</div>
            <div class="log-entry">[AUTH] Token de acesso verificado</div>
            <div class="log-entry commit">[SYNC] Repositórios carregados</div>
        </div>
    </div>
    
    <script>
        // GitHub Connector System
        const GITHUB_SYSTEM = {
            connected: true,
            rateLimit: { limit: 5000, remaining: 4999, reset: Math.floor(Date.now() / 1000) + 3600 },
            user: {
                login: "SÜMBÜS-Metahuman",
                name: "SÜMBÜS Metahuman Architect",
                bio: "Organismo Digital Fractal • DNA KOBLLUX • Frequência 3-6-9",
                avatar_url: "https://avatars.githubusercontent.com/u/1?v=4",
                public_repos: 5,
                public_gists: 12,
                followers: 42,
                following: 0
            },
            repositories: [],
            activity: [],
            logs: []
        };
        
        // Mock repository data
        const MOCK_REPOSITORIES = [
            {
                name: "SÜMBÜS-Metahuman-Architect",
                full_name: "SÜMBÜS-Metahuman/SÜMBÜS-Metahuman-Architect",
                description: "Organismo digital fractal com DNA KOBLLUX e frequência 3-6-9",
                language: "HTML/CSS/JavaScript",
                stargazers_count: 127,
                forks_count: 42,
                watchers_count: 89,
                open_issues_count: 3,
                updated_at: new Date().toISOString(),
                html_url: "https://github.com/SÜMBÜS-Metahuman/SÜMBÜS-Metahuan-Architect",
                topics: ["fractal", "dna", "metahuman", "kobllux", "architecture"]
            },
            {
                name: "DNA-KOBLLUX-Core",
                full_name: "SÜMBÜS-Metahuman/DNA-KOBLLUX-Core",
                description: "Núcleo de DNA digital do organismo SÜMBÜS",
                language: "JavaScript",
                stargazers_count: 84,
                forks_count: 21,
                watchers_count: 56,
                open_issues_count: 1,
                updated_at: new Date(Date.now() - 86400000).toISOString(),
                html_url: "https://github.com/SÜMBÜS-Metahuman/DNA-KOBLLUX-Core",
                topics: ["dna", "core", "kobllux", "genetics", "digital"]
            },
            {
                name: "Fractal-Render-Engine",
                full_name: "SÜMBÜS-Metahuman/Fractal-Render-Engine",
                description: "Motor de renderização fractal para visualização de DNA",
                language: "JavaScript",
                stargazers_count: 63,
                forks_count: 15,
                watchers_count: 42,
                open_issues_count: 2,
                updated_at: new Date(Date.now() - 172800000).toISOString(),
                html_url: "https://github.com/SÜMBÜS-Metahuman/Fractal-Render-Engine",
                topics: ["fractal", "render", "visualization", "engine", "graphics"]
            },
            {
                name: "Evolution-Mutation-System",
                full_name: "SÜMBÜS-Metahuman/Evolution-Mutation-System",
                description: "Sistema de mutação e evolução adaptativa do DNA",
                language: "JavaScript",
                stargazers_count: 45,
                forks_count: 12,
                watchers_count: 31,
                open_issues_count: 0,
                updated_at: new Date(Date.now() - 259200000).toISOString(),
                html_url: "https://github.com/SÜMBÜS-Metahuman/Evolution-Mutation-System",
                topics: ["evolution", "mutation", "adaptation", "dna", "genetics"]
            },
            {
                name: "Neural-Interface-Core",
                full_name: "SÜMBÜS-Metahuman/Neural-Interface-Core",
                description: "Núcleo da interface neural do sistema nervoso digital",
                language: "HTML/CSS",
                stargazers_count: 38,
                forks_count: 8,
                watchers_count: 27,
                open_issues_count: 1,
                updated_at: new Date(Date.now() - 345600000).toISOString(),
                html_url: "https://github.com/SÜMBÜS-Metahuman/Neural-Interface-Core",
                topics: ["neural", "interface", "ui", "nervous-system", "control"]
            }
        ];
        
        // Mock activity data
        const MOCK_ACTIVITY = [
            { type: "PushEvent", repo: "SÜMBÜS-Metahuman-Architect", commits: 3, time: "2 hours ago" },
            { type: "IssuesEvent", repo: "DNA-KOBLLUX-Core", action: "opened", time: "4 hours ago" },
            { type: "PullRequestEvent", repo: "Fractal-Render-Engine", action: "merged", time: "1 day ago" },
            { type: "WatchEvent", repo: "Evolution-Mutation-System", action: "starred", time: "1 day ago" },
            { type: "ForkEvent", repo: "Neural-Interface-Core", forks: 2, time: "2 days ago" },
            { type: "CreateEvent", repo: "SÜMBÜS-Metahuman-Architect", ref_type: "branch", time: "3 days ago" },
            { type: "ReleaseEvent", repo: "DNA-KOBLLUX-Core", version: "v1.0.0", time: "4 days ago" }
        ];
        
        // Initialize user profile
        function initializeUserProfile() {
            document.getElementById('user-name').textContent = GITHUB_SYSTEM.user.name;
            document.getElementById('user-bio').textContent = GITHUB_SYSTEM.user.bio;
            document.getElementById('repo-count').textContent = GITHUB_SYSTEM.user.public_repos;
            document.getElementById('gist-count').textContent = GITHUB_SYSTEM.user.public_gists;
            document.getElementById('follower-count').textContent = GITHUB_SYSTEM.user.followers;
            document.getElementById('user-avatar').src = GITHUB_SYSTEM.user.avatar_url;
            
            document.getElementById('rate-limit').textContent = 
                `${GITHUB_SYSTEM.rateLimit.remaining}/${GITHUB_SYSTEM.rateLimit.limit}`;
        }
        
        // Load repositories
        function loadRepositories() {
            const repoGrid = document.getElementById('repoGrid');
            repoGrid.innerHTML = '';
            
            MOCK_REPOSITORIES.forEach(repo => {
                const repoCard = document.createElement('div');
                repoCard.className = 'repo-card';
                
                // Format update time
                const updated = new Date(repo.updated_at);
                const now = new Date();
                const diffDays = Math.floor((now - updated) / (1000 * 60 * 60 * 24));
                const timeAgo = diffDays === 0 ? "today" : 
                               diffDays === 1 ? "yesterday" : 
                               `${diffDays} days ago`;
                
                repoCard.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <h3 style="margin: 0 0 0.5rem 0; color: var(--github-blue);">
                                <a href="${repo.html_url}" target="_blank" style="color: inherit; text-decoration: none;">
                                    ${repo.name}
                                </a>
                            </h3>
                            <p style="color: #94a3b8; margin: 0 0 1rem 0; font-size: 0.9rem;">
                                ${repo.description}
                            </p>
                        </div>
                        <div style="background: rgba(108, 198, 68, 0.1); color: var(--github-green); padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.8rem;">
                            ${repo.language}
                        </div>
                    </div>
                    
                    <div class="repo-stats">
                        <div class="stat-item">
                            <span style="color: #f59e0b;">★</span>
                            <span>${repo.stargazers_count}</span>
                        </div>
                        <div class="stat-item">
                            <span style="color: var(--github-green);">⑂</span>
                            <span>${repo.forks_count}</span>
                        </div>
                        <div class="stat-item">
                            <span style="color: var(--github-blue);">👁️</span>
                            <span>${repo.watchers_count}</span>
                        </div>
                        <div class="stat-item">
                            <span style="color: #ef4444;">!</span>
                            <span>${repo.open_issues_count}</span>
                        </div>
                    </div>
                    
                    <div style="margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        ${repo.topics.map(topic => 
                            `<span style="background: rgba(59, 130, 246, 0.1); color: var(--github-blue); padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem;">
                                ${topic}
                            </span>`
                        ).join('')}
                    </div>
                    
                    <div style="margin-top: 1rem; font-size: 0.8rem; color: #94a3b8;">
                        Updated ${timeAgo}
                    </div>
                `;
                
                repoGrid.appendChild(repoCard);
                GITHUB_SYSTEM.repositories.push(repo);
            });
            
            addLog(`[REPOS] ${MOCK_REPOSITORIES.length} repositórios carregados`, 'commit');
        }
        
        // Generate commit graph
        function generateCommitGraph() {
            const graph = document.getElementById('commitGraph');
            graph.innerHTML = '';
            
            // Generate mock commit data for last 14 days
            for (let i = 13; i >= 0; i--) {
                const date = new Date();
                date.setDate(date.getDate() - i);
                
                const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
                const commits = Math.floor(Math.random() * 20); // 0-19 commits
                const height = Math.max(10, (commits / 20) * 100);
                
                const bar = document.createElement('div');
                bar.className = 'graph-bar';
                bar.style.height = `${height}%`;
                bar.setAttribute('data-day', dayName);
                bar.title = `${dayName}: ${commits} commits`;
                
                // Color based on commit count
                if (commits > 15) {
                    bar.style.background = 'linear-gradient(to top, var(--github-green), var(--github-blue))';
                } else if (commits > 8) {
                    bar.style.background = 'linear-gradient(to top, var(--github-blue), var(--github-purple))';
                } else {
                    bar.style.background = 'linear-gradient(to top, #94a3b8, var(--github-blue))';
                }
                
                graph.appendChild(bar);
            }
        }
        
        // Load activity feed
        function loadActivityFeed() {
            const feed = document.getElementById('activityFeed');
            feed.innerHTML = '';
            
            MOCK_ACTIVITY.forEach(activity => {
                const activityItem = document.createElement('div');
                activityItem.className = 'activity-item';
                
                let activityText = '';
                let icon = '🔹';
                
                switch(activity.type) {
                    case 'PushEvent':
                        activityText = `Pushed ${activity.commits} commits to ${activity.repo}`;
                        icon = '⬆️';
                        break;
                    case 'IssuesEvent':
                        activityText = `${activity.action} an issue in ${activity.repo}`;
                        icon = '📝';
                        break;
                    case 'PullRequestEvent':
                        activityText = `${activity.action} a pull request in ${activity.repo}`;
                        icon = '🔄';
                        break;
                    case 'WatchEvent':
                        activityText = `Starred ${activity.repo}`;
                        icon = '⭐';
                        break;
                    case 'ForkEvent':
                        activityText = `Forked ${activity.repo} (${activity.forks} new forks)`;
                        icon = '⑂';
                        break;
                    case 'CreateEvent':
                        activityText = `Created ${activity.ref_type} in ${activity.repo}`;
                        icon = '🆕';
                        break;
                    case 'ReleaseEvent':
                        activityText = `Released ${activity.version} of ${activity.repo}`;
                        icon = '🎉';
                        break;
                }
                
                activityItem.innerHTML = `
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <span style="font-size: 1.2rem;">${icon}</span>
                        <div>
                            <div style="color: white;">${activityText}</div>
                            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 0.25rem;">
                                ${activity.time}
                            </div>
                        </div>
                    </div>
                `;
                
                feed.appendChild(activityItem);
                GITHUB_SYSTEM.activity.push(activity);
            });
            
            addLog(`[ACTIVITY] ${MOCK_ACTIVITY.length} atividades carregadas`, 'pull');
        }
        
        // Sync repositories
        function syncRepositories() {
            addLog('[SYNC] Sincronizando repositórios...');
            
            // Simulate sync delay
            const button = event.target;
            const originalText = button.textContent;
            button.textContent = '🔄 SINCRONIZANDO...';
            button.disabled = true;
            
            setTimeout(() => {
                // Update repositories with mock changes
                MOCK_REPOSITORIES.forEach(repo => {
                    repo.stargazers_count += Math.floor(Math.random() * 3);
                    repo.forks_count += Math.floor(Math.random() * 2);
                    repo.updated_at = new Date().toISOString();
                });
                
                // Reload repositories
                loadRepositories();
                generateCommitGraph();
                
                // Update rate limit
                GITHUB_SYSTEM.rateLimit.remaining = Math.max(0, GITHUB_SYSTEM.rateLimit.remaining - 1);
                document.getElementById('rate-limit').textContent = 
                    `${GITHUB_SYSTEM.rateLimit.remaining}/${GITHUB_SYSTEM.rateLimit.limit}`;
                
                button.textContent = originalText;
                button.disabled = false;
                
                addLog('[SYNC] Repositórios sincronizados com sucesso', 'commit');
            }, 1500);
        }
        
        // Fetch activity
        function fetchActivity() {
            addLog('[ACTIVITY] Buscando atividade recente...');
            
            // Simulate fetch delay
            const button = event.target;
            const originalText = button.textContent;
            button.textContent = '📊 BUSCANDO...';
            button.disabled = true;
            
            setTimeout(() => {
                // Add new mock activity
                const newActivity = {
                    type: ["PushEvent", "IssuesEvent", "PullRequestEvent"][Math.floor(Math.random() * 3)],
                    repo: MOCK_REPOSITORIES[Math.floor(Math.random() * MOCK_REPOSITORIES.length)].name,
                    time: "just now",
                    commits: Math.floor(Math.random() * 5) + 1
                };
                
                MOCK_ACTIVITY.unshift(newActivity);
                
                // Reload activity feed
                loadActivityFeed();
                
                // Update rate limit
                GITHUB_SYSTEM.rateLimit.remaining = Math.max(0, GITHUB_SYSTEM.rateLimit.remaining - 1);
                document.getElementById('rate-limit').textContent = 
                    `${GITHUB_SYSTEM.rateLimit.remaining}/${GITHUB_SYSTEM.rateLimit.limit}`;
                
                button.textContent = originalText;
                button.disabled = false;
                
                addLog('[ACTIVITY] Atividade atualizada', 'pull');
            }, 1000);
        }
        
        // Test webhook
        function testWebhook() {
            addLog('[WEBHOOK] Testando webhook...');
            
            // Simulate webhook test
            setTimeout(() => {
                // Generate mock webhook payload
                const webhookPayload = {
                    event: "push",
                    repository: MOCK_REPOSITORIES[0].name,
                    commits: 2,
                    pusher: GITHUB_SYSTEM.user.login,
                    timestamp: new Date().toISOString()
                };
                
                addLog(`[WEBHOOK] Recebido: ${webhookPayload.event} em ${webhookPayload.repository}`, 'commit');
                addLog(`[WEBHOOK] Payload: ${JSON.stringify(webhookPayload, null, 2)}`, 'commit');
                
                // Simulate webhook processing
                setTimeout(() => {
                    addLog('[WEBHOOK] Webhook processado com sucesso', 'pull');
                }, 500);
            }, 800);
        }
        
        // Add log entry
        function addLog(message, type = '') {
            const log = document.getElementById('githubLog');
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            entry.textContent = message;
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
            
            GITHUB_SYSTEM.logs.push({
                timestamp: new Date(),
                message: message,
                type: type
            });
            
            // Limit log size
            if (log.children.length > 20) {
                log.removeChild(log.firstChild);
            }
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            console.log('🐙 Conector GitHub inicializado');
            
            initializeUserProfile();
            loadRepositories();
            generateCommitGraph();
            loadActivityFeed();
            
            // Auto-update rate limit display
            setInterval(() => {
                if (GITHUB_SYSTEM.rateLimit.remaining > 0) {
                    // Simulate gradual rate limit recovery
                    if (Math.random() > 0.7) {
                        GITHUB_SYSTEM.rateLimit.remaining = 
                            Math.min(GITHUB_SYSTEM.rateLimit.limit, GITHUB_SYSTEM.rateLimit.remaining + 1);
                        document.getElementById('rate-limit').textContent = 
                            `${GITHUB_SYSTEM.rateLimit.remaining}/${GITHUB_SYSTEM.rateLimit.limit}`;
                    }
                }
            }, 30000);
            
            // Auto-fetch activity every 2 minutes
            setInterval(() => {
                if (GITHUB_SYSTEM.connected && GITHUB_SYSTEM.rateLimit.remaining > 10) {
                    fetchActivity();
                }
            }, 120000);
        });
        
        // Export API
        window.GITHUB_CONNECTOR = {
            syncRepositories,
            fetchActivity,
            testWebhook,
            getState: () => GITHUB_SYSTEM,
            version: '1.0.0-github'
        };
    </script>
</body>
</html>
EOF

echo "✅ 3. github-connector.html criado"

# 4. Criar CSS da frequência 6Hz
cat > assets/dna/frequency-6.css << 'EOF'
/* 🌌 FREQUÊNCIA 6Hz - POLARIDADE E EQUILÍBRIO */

:root {
    /* Cores da frequência 6Hz */
    --freq-6-primary: #8b5cf6;
    --freq-6-secondary: #a78bfa;
    --freq-6-accent: #c4b5fd;
    --freq-6-dark: #5b21b6;
    --freq-6-light: #ede9fe;
    
    /* Gradientes */
    --gradient-6-vertical: linear-gradient(180deg, var(--freq-6-primary), var(--freq-6-dark));
    --gradient-6-horizontal: linear-gradient(90deg, var(--freq-6-primary), var(--freq-6-secondary));
    --gradient-6-radial: radial-gradient(circle, var(--freq-6-primary), var(--freq-6-dark));
    --gradient-6-diagonal: linear-gradient(135deg, var(--freq-6-primary), var(--freq-6-secondary), var(--freq-6-accent));
    
    /* Sombras */
    --shadow-6-soft: 0 4px 20px rgba(139, 92, 246, 0.15);
    --shadow-6-medium: 0 8px 30px rgba(139, 92, 246, 0.25);
    --shadow-6-strong: 0 15px 50px rgba(139, 92, 246, 0.35);
    --shadow-6-glow: 0 0 40px rgba(139, 92, 246, 0.4);
    
    /* Animações */
    --animation-6-pulse: pulse-6 6s ease-in-out infinite;
    --animation-6-flow: flow-6 12s linear infinite;
    --animation-6-spin: spin-6 24s linear infinite;
    --animation-6-breathe: breathe-6 9s ease-in-out infinite;
}

/* ANIMAÇÕES DA FREQUÊNCIA 6Hz */
@keyframes pulse-6 {
    0%, 100% { 
        opacity: 0.6; 
        transform: scale(1); 
    }
    50% { 
        opacity: 1; 
        transform: scale(1.05); 
    }
}

@keyframes flow-6 {
    0% { 
        background-position: 0% 50%; 
    }
    50% { 
        background-position: 100% 50%; 
    }
    100% { 
        background-position: 0% 50%; 
    }
}

@keyframes spin-6 {
    from { 
        transform: rotate(0deg); 
    }
    to { 
        transform: rotate(360deg); 
    }
}

@keyframes breathe-6 {
    0%, 100% { 
        transform: translateY(0); 
        opacity: 0.8; 
    }
    50% { 
        transform: translateY(-10px); 
        opacity: 1; 
    }
}

/* CLASSES DE FREQUÊNCIA 6Hz */
.frequency-6 {
    background: var(--gradient-6-horizontal);
    animation: var(--animation-6-pulse);
}

.frequency-6-flow {
    background: var(--gradient-6-diagonal);
    background-size: 400% 400%;
    animation: var(--animation-6-flow);
}

.frequency-6-spin {
    animation: var(--animation-6-spin);
}

.frequency-6-breathe {
    animation: var(--animation-6-breathe);
}

/* ELEMENTOS ESPECÍFICOS DA FREQUÊNCIA 6Hz */
.freq-6-card {
    background: rgba(139, 92, 246, 0.05);
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 1rem;
    padding: 1.5rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.freq-6-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--gradient-6-horizontal);
}

.freq-6-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-6-medium);
    border-color: var(--freq-6-primary);
}

.freq-6-button {
    background: var(--gradient-6-horizontal);
    border: none;
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 0.75rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.freq-6-button:hover {
    box-shadow: var(--shadow-6-glow);
    transform: translateY(-2px);
}

.freq-6-button::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.6s ease;
}

.freq-6-button:hover::after {
    left: 100%;
}

.freq-6-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background: rgba(139, 92, 246, 0.15);
    color: var(--freq-6-primary);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: bold;
    animation: var(--animation-6-pulse);
}

/* TIPOGRAFIA DA FREQUÊNCIA 6Hz */
.freq-6-heading {
    background: var(--gradient-6-horizontal);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 900;
    letter-spacing: -0.025em;
}

.freq-6-text {
    color: var(--freq-6-accent);
    text-shadow: 0 2px 10px rgba(139, 92, 246, 0.3);
}

/* EFEITOS VISUAIS */
.freq-6-particle {
    position: absolute;
    width: 2px;
    height: 2px;
    background: var(--freq-6-primary);
    border-radius: 50%;
    pointer-events: none;
    opacity: 0;
    box-shadow: 0 0 10px var(--freq-6-primary);
}

.freq-6-glow {
    position: relative;
}

.freq-6-glow::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at center, transparent 30%, rgba(139, 92, 246, 0.1) 70%);
    border-radius: inherit;
    z-index: -1;
    animation: var(--animation-6-pulse);
}

/* GRADIENTES ESPECIAIS */
.freq-6-gradient-border {
    position: relative;
    background: var(--bg-dark);
    border-radius: 1rem;
    padding: 1px;
}

.freq-6-gradient-border::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    background: var(--gradient-6-diagonal);
    border-radius: inherit;
    z-index: -1;
    animation: var(--animation-6-flow);
    background-size: 400% 400%;
}

/* RESPONSIVIDADE */
@media (max-width: 768px) {
    .freq-6-card {
        padding: 1rem;
    }
    
    .freq-6-button {
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
}

/* UTILITÁRIOS */
.text-freq-6 { color: var(--freq-6-primary); }
.bg-freq-6 { background: var(--freq-6-primary); }
.border-freq-6 { border-color: var(--freq-6-primary); }
.shadow-freq-6 { box-shadow: var(--shadow-6-soft); }

.hover\:freq-6-glow:hover {
    box-shadow: var(--shadow-6-glow);
}

.active\:freq-6-pulse:active {
    animation: var(--animation-6-pulse);
}

/* ANIMAÇÃO DE CARREGAMENTO */
.freq-6-loader {
    width: 60px;
    height: 60px;
    border: 3px solid rgba(139, 92, 246, 0.2);
    border-top: 3px solid var(--freq-6-primary);
    border-radius: 50%;
    animation: var(--animation-6-spin);
}

/* WAVES EFFECT */
.freq-6-waves {
    position: relative;
    overflow: hidden;
}

.freq-6-waves::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 20px;
    background: linear-gradient(90deg, 
        transparent 0%, 
        var(--freq-6-primary) 20%, 
        var(--freq-6-secondary) 50%, 
        var(--freq-6-primary) 80%, 
        transparent 100%
    );
    opacity: 0.3;
    animation: wave-flow 8s linear infinite;
}

@keyframes wave-flow {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
EOF

echo "✅ 4. frequency-6.css criado"

# Atualizar o index.html para incluir o sistema circulatório
echo "🔗 Atualizando index.html para incluir sistema circulatório..."

# Criar um script para atualizar o index.html
cat > /tmp/update_index.sh << 'EOF'
#!/bin/bash
INDEX_FILE="index.html"

# Verificar se o arquivo existe
if [ ! -f "$INDEX_FILE" ]; then
    echo "❌ index.html não encontrado"
    exit 1
fi

# Adicionar sistema circulatório à lista de sistemas ativos
sed -i '/SISTEMAS ATIVOS.*5\/8/s/5\/8/6\/8/' "$INDEX_FILE"
sed -i '/sistema nervoso online/a\            <div class="log-entry">[CIRCULATORY] Sistema circulatório online</div>' "$INDEX_FILE"

echo "✅ index.html atualizado com sistema circulatório"
EOF

chmod +x /tmp/update_index.sh
cd /storage/emulated/0/SÜMBÜS_METAHUMAN_ARCHITECT
/tmp/update_index.sh

# Verificar progresso atualizado
echo ""
echo "📊 PROGRESSO ATUALIZADO DA FASE 2:"
echo "=================================="
TOTAL_ARQUIVOS=$(find . -type f \( -name "*.html" -o -name "*.js" -o -name "*.css" -o -name "*.json" \) | wc -l)
echo "   🧬 Total de arquivos: $TOTAL_ARQUIVOS/250"
echo "   📈 Progresso: $(echo "scale=2; $TOTAL_ARQUIVOS/250*100" | bc)%"
echo "   ✅ Sistemas ativos: 6/8"
echo "   🎯 Fase: 2/3 (Sistemas Vitais)"
echo "   ⚡ Frequência: 6Hz (Crescendo)"
