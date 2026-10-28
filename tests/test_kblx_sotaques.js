'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const hubRoot = path.join(__dirname, '..', 'KOBLLUX_UNIFICADO', '09_HUB_UNO');
const voiceSource = fs.readFileSync(path.join(hubRoot, 'kblx_sotaques.js'), 'utf8');
const memory = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'kobllux_memory.json'), 'utf8'));

function createVoiceEngine(savedVoices) {
  const spoken = [];
  const voices = [
    { name: 'Hans', lang: 'pt-BR' },
    { name: 'Luciana', lang: 'pt-BR' },
    { name: 'Carlos', lang: 'pt-BR' },
    { name: 'Custom Voice', lang: 'pt-BR' },
    { name: 'Default', lang: 'en-US' }
  ];
  const speechSynthesis = {
    getVoices() { return voices; },
    cancel() {},
    speak(utterance) { spoken.push(utterance); }
  };
  function SpeechSynthesisUtterance(text) {
    this.text = text;
  }
  const window = {
    speechSynthesis,
    SpeechSynthesisUtterance,
    localStorage: { getItem(key) { return key === 'infodose:voices' ? savedVoices || '{}' : null; } },
    KBLX_ORBE: {
      profiles() {
        return Object.entries(memory.arquetipos).map(([name, attributes]) => ({
          name,
          hz: attributes.hz,
          opcode: attributes.opcode
        }));
      }
    }
  };
  const document = { getElementById(id) { return id === 'appsWrap' ? {} : null; } };
  vm.runInNewContext(voiceSource, { window, document, console, String }, {
    filename: path.join(hubRoot, 'kblx_sotaques.js')
  });
  return { window, spoken };
}

test('voice map covers every canonical archetype and retains extensions', () => {
  const { window } = createVoiceEngine();
  const canonicalNames = Object.keys(memory.arquetipos).map((name) => name.toLowerCase());
  const mappedNames = Object.keys(window.KBLX_VOZ.MAP);

  canonicalNames.forEach((name) => assert.ok(mappedNames.includes(name), `missing voice mapping for ${name}`));
  assert.ok(mappedNames.includes('elysha'));
  assert.ok(mappedNames.includes('horus'));
});

test('speaking uses the archetype accent mapping and exposes canonical Hz/opcode metadata', () => {
  const { window, spoken } = createVoiceEngine();
  const voice = window.KBLX_VOZ.falar('Atlas', 'Resposta do Atlas');

  assert.equal(voice, 'Hans');
  assert.equal(spoken.length, 1);
  assert.equal(spoken[0].text, 'Resposta do Atlas');
  assert.equal(spoken[0].voice.name, 'Hans');
  assert.deepEqual(
    JSON.parse(JSON.stringify(window.KBLX_VOZ.last())),
    { archetype: 'Atlas', hz: 594, opcode: '0x00', voice: 'Hans', accent: 'alemão' }
  );
});

test('a saved per-archetype voice preference takes precedence over the default mapping', () => {
  const { window, spoken } = createVoiceEngine(JSON.stringify({ Atlas: 'Custom Voice' }));

  assert.equal(window.KBLX_VOZ.falar('Atlas', 'Voz personalizada'), 'Custom Voice');
  assert.equal(spoken[0].voice.name, 'Custom Voice');
});
