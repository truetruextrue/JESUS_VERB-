'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const hubRoot = path.join(
  __dirname,
  '..',
  'inbox',
  'KΦꓷ8DΦꓘ',
  'KOBLLUX_∆³_Design_System',
  'KOBLLUX_HUB_UNO_BlueCup_ZPR_Portal Nexus',
  'ui_kits',
  'hub-uno'
);
const bridgePath = path.join(hubRoot, 'js', '19-kobllux-live-bridge.js');
const bridgeSource = fs.readFileSync(bridgePath, 'utf8');

function createHub() {
  const values = new Map();
  const elements = new Map();
  let lastDownload = null;
  const localStorage = {
    getItem(key) { return values.has(key) ? values.get(key) : null; },
    setItem(key, value) { values.set(key, String(value)); },
    removeItem(key) { values.delete(key); }
  };
  const inputBar = {
    children: [],
    appendChild(child) {
      this.children.push(child);
      if (child.id) elements.set(child.id, child);
    }
  };
  const document = {
    getElementById(id) { return id === 'chatInputBar' ? inputBar : elements.get(id) || null; },
    createElement(tag) {
      return {
        tagName: tag,
        style: {},
        listeners: {},
        setAttribute(name, value) { this[name] = value; },
        addEventListener(name, callback) { this.listeners[name] = callback; },
        click() {
          if (tag === 'a') lastDownload = this;
          else if (this.listeners.click) this.listeners.click();
        }
      };
    }
  };
  const window = {
    localStorage,
    crypto: { randomUUID: () => 'event-id-1' },
    koblluxSystemLog() { return 'base system prompt'; },
    handleUserMessage: async function (text) {
      return { text, systemPrompt: window.koblluxSystemLog() };
    }
  };
  const context = {
    window,
    document,
    console,
    Date,
    JSON,
    Math,
    String,
    TypeError,
    Blob,
    URL: { createObjectURL: () => 'blob:local', revokeObjectURL() {} }
  };
  vm.runInNewContext(bridgeSource, context, { filename: bridgePath });
  return { window, values, elements, getLastDownload: () => lastDownload };
}

test('bridge archetypes match the Python canonical memory and phase contract', () => {
  const memory = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'kobllux_memory.json'), 'utf8'));
  const { window } = createHub();
  const expected = Object.entries(memory.arquetipos).map(([name, data]) => ({
    name,
    hz: data.hz,
    opcode: data.opcode
  }));
  const actual = window.KOBLLUX_LIVE_BRIDGE.archetypes.map(({ name, hz, opcode }) => ({
    name,
    hz,
    opcode
  }));

  assert.equal(JSON.stringify(actual), JSON.stringify(expected));
  assert.equal(
    JSON.stringify(window.KOBLLUX_LIVE_BRIDGE.phases.map(({ step }) => step)),
    JSON.stringify([3, 6, 9, 7])
  );
  assert.equal(window.KOBLLUX_LIVE_BRIDGE.namespaces.length, 16);
});

test('only KOBLLUX messages add context and persist metadata without message or credentials', async () => {
  const { window, values, elements, getLastDownload } = createHub();
  const normal = await window.handleUserMessage('mensagem comum');

  assert.equal(normal.text, 'mensagem comum');
  assert.equal(normal.systemPrompt, 'base system prompt');
  assert.equal(values.has('kobllux.live.workflow.v1'), false);

  const prompted = await window.handleUserMessage('KOBLLUX, integrar o fluxo');
  const events = JSON.parse(values.get('kobllux.live.workflow.v1'));
  const eqEvents = JSON.parse(values.get('kobllux.eq.log'));

  assert.equal(prompted.text, 'KOBLLUX, integrar o fluxo');
  assert.match(prompted.systemPrompt, /KOBLLUX LIVE BRIDGE/);
  assert.match(prompted.systemPrompt, /uma fala curta de cada arquétipo, sem omissões/);
  assert.match(prompted.systemPrompt, /3 \/ 0x03 DETECTAR → 6 \/ 0x06 INTEGRAR → 9 \/ 0x09 EXPANDIR → 7 \/ 0x07 SELAR/);
  assert.match(prompted.systemPrompt, /Kobllux \(1134 Hz, 0x0F\)/);
  assert.equal(events.length, 1);
  assert.equal(events[0].message_chars, 'KOBLLUX, integrar o fluxo'.length);
  assert.equal(Object.hasOwn(events[0], 'message'), false);
  assert.equal(JSON.stringify(events).includes('dual.keys'), false);
  assert.equal(events[0].secrets_stored, false);
  assert.equal(eqEvents[0].eventId, 'event-id-1');
  assert.match(window.KOBLLUX_LIVE_BRIDGE.exportJsonl(), /"type":"kobllux-chat-trigger"/);
  assert.equal(getLastDownload(), null);
  assert.match(elements.get('koblluxLiveActions').href, /actions\/workflows\/kobllux-malha-viva\.yml$/);
  elements.get('koblluxLiveExport').click();
  assert.equal(getLastDownload().download, 'kobllux-live-workflow.jsonl');
  assert.equal(window.koblluxSystemLog(), 'base system prompt');
});
