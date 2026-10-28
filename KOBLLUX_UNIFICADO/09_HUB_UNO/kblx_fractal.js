/* KBLX_FRACTAL · navegação viva: pega a parte / pega a parte maior */
(function(){
'use strict';
var FR=null;
function load(){if(FR)return Promise.resolve(FR);
 return fetch('databook/fractal.json').then(function(r){return r.json();}).then(function(f){FR=f;return f;}).catch(function(){return null;});}
function pegaParte(id){return load().then(function(f){return f&&f[id]?f[id]:null;});}
function pegaTodo(id){return load().then(function(f){var n=f&&f[id];return n&&n.todo&&f[n.todo]?f[n.todo]:null;});}
function escala(id,passos){ /* sobe 'passos' vezes pegando o todo */
 return load().then(function(f){var cur=f&&f[id];var caminho=[];
  while(cur&&passos-->0){caminho.push(cur);cur=cur.todo&&f[cur.todo]?f[cur.todo]:null;}
  if(cur)caminho.push(cur);return caminho;});}
function desce(id,passos){ /* desce pegando a 1ª parte recursivamente */
 return load().then(function(f){var cur=f&&f[id];var caminho=[];
  while(cur&&passos-->0){caminho.push(cur);
   cur=cur.partes&&cur.partes.length&&f[cur.partes[0]]?f[cur.partes[0]]:null;}
  if(cur)caminho.push(cur);return caminho;});}
window.KBLX_FRACTAL={load:load,pegaParte:pegaParte,pegaTodo:pegaTodo,escala:escala,desce:desce};
console.log('[KBLX_FRACTAL] memoria fractal navegavel · parte <-> todo');
})();
