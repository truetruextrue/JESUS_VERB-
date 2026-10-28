'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const hubRoot = path.join(__dirname, '..', 'KOBLLUX_UNIFICADO', '09_HUB_UNO');
const scriptPath = path.join(hubRoot, 'kblx_databook.js');
const scriptSource = fs.readFileSync(scriptPath, 'utf8');

function node() {
  return {
    children: [],
    listeners: {},
    style: {},
    addEventListener(name, callback) { this.listeners[name] = callback; },
    appendChild(child) { this.children.push(child); },
    setAttribute(name, value) { this[name] = value; },
    querySelector() { return null; }
  };
}

function createDatabook() {
  const storage = new Map();
  const host = node();
  const elements = new Map([
    ['#kblx_lib_list', node()],
    ['#kblx_lib_facts', node()],
    ['#kblx_lib_index_status', node()],
    ['#kblx_lib_index', node()],
    ['#kblx_lib_q', node()],
    ['#kblx_lib_all', node()]
  ]);
  host.querySelector = (selector) => elements.get(selector);
  const document = {
    readyState: 'loading',
    addEventListener() {},
    getElementById(id) { return id === 'kblx_library' ? host : null; },
    createElement() { return node(); }
  };
  const localStorage = {
    getItem(key) { return storage.has(key) ? storage.get(key) : null; },
    setItem(key, value) { storage.set(key, String(value)); }
  };
  const fetch = async (relativePath) => {
    const file = path.join(hubRoot, relativePath);
    if (!fs.existsSync(file)) return { ok: false, status: 404 };
    return {
      ok: true,
      status: 200,
      json: async () => JSON.parse(fs.readFileSync(file, 'utf8'))
    };
  };
  const window = {};
  const context = {
    window,
    document,
    localStorage,
    fetch,
    console,
    Date,
    JSON,
    Math,
    String,
    TypeError,
    Error,
    Promise,
    Array,
    setTimeout() {}
  };
  vm.runInNewContext(scriptSource, context, { filename: scriptPath });
  return { window, host, elements };
}

test('Databook indexes every present source and reports missing memory files', async () => {
  const { window } = createDatabook();
  await window.KBLX_BOOK.reload();

  const summary = await window.KBLX_BOOK.indexFacts();

  assert.equal(summary.sourcesExpected, 50);
  assert.equal(summary.sourcesIndexed, 48);
  assert.equal(summary.factsIndexed, 4291);
  assert.deepEqual(
    Array.from(summary.missing, (item) => item.file).sort(),
    ['livro_03.json', 'livro_05.json']
  );
  assert.ok(window.KBLX_BOOK.searchFacts('interdimensionalidade').length > 0);
});
