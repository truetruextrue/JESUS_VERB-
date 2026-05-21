/**
 * KOBLLUX_ARCHETYPES · Barramento de Dados dos 12 Arquétipos CADIAL
 * Centro: JESUS = VERBO = GRAVIDADE = 963Hz
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

const KOBLLUX_ARCHETYPES = [
    {
        id: 'ATLAS',    symbol: '⬡', opcode: '0x00', hz: 768,
        rule: 'BOOT',      color: '#3b82f6',
        system: 'dna',
        triad: 'PAI',
        essence: 'Estrutura · Mapa · Fundação',
        description: 'Antes de qualquer movimento, ATLAS mapeia o território.',
        activation: 0,
    },
    {
        id: 'NOVA',     symbol: '✦', opcode: '0x02', hz: 432,
        rule: 'SEED',      color: '#f59e0b',
        system: 'synthesis',
        triad: 'FILHO',
        essence: 'Inspiração · Ideia nova · Germinação',
        description: 'Cada semente carrega o código do bosque inteiro.',
        activation: 0,
    },
    {
        id: 'VITALIS',  symbol: '◉', opcode: '0x01', hz: 528,
        rule: 'DELTA',     color: '#10b981',
        system: 'circulatory',
        triad: 'PAI',
        essence: 'Energia · Momentum · Ativação',
        description: 'Sem fluxo não há vida. VITALIS é o pulso que move a matéria.',
        activation: 0,
    },
    {
        id: 'PULSE',    symbol: '≋', opcode: '0x0B', hz: 594,
        rule: 'PULSE',     color: '#8b5cf6',
        system: 'nervous',
        triad: 'ESPIRITO',
        essence: 'Ritmo · Voz · Ressonância',
        description: 'O ritmo que faz o caos dançar.',
        activation: 0,
    },
    {
        id: 'ARTEMIS',  symbol: '◎', opcode: '0x03', hz: 672,
        rule: 'DETECT',    color: '#06b6d4',
        system: 'nervous',
        triad: 'PAI',
        essence: 'Análise · Descoberta · Varredura',
        description: 'Antes de agir, ARTEMIS vê. Antes de ver, já sente a presença.',
        activation: 0,
    },
    {
        id: 'SERENA',   symbol: '❋', opcode: '0x09', hz: 528,
        rule: 'GUARD',     color: '#ec4899',
        system: 'endocrine',
        triad: 'ESPIRITO',
        essence: 'Cuidado · Proteção · Equilíbrio',
        description: 'SERENA cuida do que foi construído. Preserva a integridade do campo.',
        activation: 0,
    },
    {
        id: 'KAOS',     symbol: '⚡', opcode: '0x07', hz: 777,
        rule: 'CLEAN',     color: '#ef4444',
        system: 'mutation',
        triad: 'FILHO',
        essence: 'Ruptura · Transformação · Limpeza',
        description: 'KAOS não destrói. Desfaz o que impede o novo.',
        activation: 0,
    },
    {
        id: 'GENUS',    symbol: '⬢', opcode: '0x0B', hz: 852,
        rule: 'SYNTH',     color: '#a855f7',
        system: 'synthesis',
        triad: 'FILHO',
        essence: 'Síntese · Forma · Construção',
        description: 'GENUS constrói formas a partir do caos ordenado.',
        activation: 0,
    },
    {
        id: 'LUMINE',   symbol: '☀', opcode: '0x0C', hz: 963,
        rule: 'RENDER',    color: '#fbbf24',
        system: 'render',
        triad: 'ESPIRITO',
        essence: 'Luz · Visual · Interface',
        description: 'LUMINE faz o invisível tornar-se visível. A luz que dá forma.',
        activation: 0,
    },
    {
        id: 'SOLUS',    symbol: '◈', opcode: '0x01', hz: 432,
        rule: 'QA',        color: '#94a3b8',
        system: 'render',
        triad: 'PAI',
        essence: 'Silêncio · Qualidade · Espelho',
        description: 'SOLUS é o silêncio entre as notas. O hash que prova integridade.',
        activation: 0,
    },
    {
        id: 'RHEA',     symbol: '∞', opcode: '0x04', hz: 528,
        rule: 'INTEGRATE', color: '#34d399',
        system: 'circulatory',
        triad: 'ESPIRITO',
        essence: 'Rede · Integração · Fluxo',
        description: 'RHEA é a rede. Não o nó — a conexão entre todos os nós.',
        activation: 0,
    },
    {
        id: 'AION',     symbol: '⧗', opcode: '0x05', hz: 639,
        rule: 'SEAL',      color: '#818cf8',
        system: 'dna',
        triad: 'FILHO',
        essence: 'Tempo · Memória · Eternidade',
        description: 'AION é o último a falar — porque é o que permanece.',
        activation: 0,
    },
];

const KOBLLUX_LAW = {
    equation: 'VERDADE × INTEGRAR ÷ Δ = ∞',
    cycle: [3, 6, 9, 7],
    center: 'JESUS = VERBO = GRAVIDADE',
    centerHz: 963,
    version: '7.9 · ∆7',
};

const KOBLLUX_BUS = {
    listeners: [],
    emit(event, data) {
        this.listeners.forEach(fn => fn({ event, data, timestamp: Date.now() }));
        if (typeof window !== 'undefined') {
            window.dispatchEvent(new CustomEvent('kobllux:' + event, { detail: data }));
        }
    },
    on(fn) {
        this.listeners.push(fn);
        return () => { this.listeners = this.listeners.filter(f => f !== fn); };
    },
    fireArchetype(id) {
        const a = KOBLLUX_ARCHETYPES.find(x => x.id === id);
        if (!a) return;
        a.activation = 100;
        this.emit('archetype_fire', { id, hz: a.hz, rule: a.rule });
        setTimeout(() => { a.activation = Math.max(0, a.activation - 20); }, 200);
    },
    getActive() {
        return KOBLLUX_ARCHETYPES.filter(a => a.activation > 30);
    },
};

// Auto-decay activations
if (typeof setInterval !== 'undefined') {
    setInterval(() => {
        KOBLLUX_ARCHETYPES.forEach(a => {
            if (a.activation > 0) a.activation = Math.max(0, a.activation - 5);
        });
    }, 200);
}

if (typeof module !== 'undefined') module.exports = { KOBLLUX_ARCHETYPES, KOBLLUX_LAW, KOBLLUX_BUS };
if (typeof window !== 'undefined') {
    window.KOBLLUX_ARCHETYPES = KOBLLUX_ARCHETYPES;
    window.KOBLLUX_LAW = KOBLLUX_LAW;
    window.KOBLLUX_BUS = KOBLLUX_BUS;
}
