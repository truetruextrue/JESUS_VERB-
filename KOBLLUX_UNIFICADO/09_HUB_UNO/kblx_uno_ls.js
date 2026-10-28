/* ⟦ KBLX·UNO · LS UNIFICADO · 0x0C · ponte Hub↔ORB · expandir, não alterar ⟧ */
(function(){
'use strict';
var CANON={user:'kblx:uno:user',arch:'kblx:uno:arch',sk:'kblx:uno:sk',model:'kblx:uno:model',voices:'kblx:uno:voices',games:'kblx:uno:ia:games'};
var ALIAS={
 user:['infodose:userName','di_userName','dual.name'],
 arch:['kblx:arquetipo:atual','uno:arquetipo','hub:arquetipo:atual'],
 sk:['dual.keys.openrouter','infodose:sk'],
 model:['dual.openrouter.model','infodose:model','kblx:modelo:atual'],
 voices:['infodose:voices']};
function g(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function s(k,v){try{localStorage.setItem(k,v);}catch(e){}}
function firstOf(keys){for(var i=0;i<keys.length;i++){var v=g(keys[i]);if(v&&String(v).trim())return String(v).trim();}return '';}
var last={};
function sync(){
 ['user','arch','sk','model','voices'].forEach(function(f){
  var val=g(CANON[f])||firstOf(ALIAS[f]||[]);
  if(!val)return;
  if(last[f]===val)return; last[f]=val;
  s(CANON[f],val);
  (ALIAS[f]||[]).forEach(function(a){ if(g(a)!==val)s(a,val); });
 });
}
/* ── IA GAMES · os apps locais do Hub = os do ORB, conectados a HTML real ── */
var GAMES=[
 ['atlas','Atlas','#c9a84c',639,'Planejador estratégico'],['nova','Nova','#ff52b1',528,'Criatividade'],
 ['vitalis','Vitalis','#ff6b35',396,'Saúde e momentum'],['pulse','Pulse','#00e5ff',528,'Ritmo musical'],
 ['artemis','Artemis','#64dc64',417,'Conhecimento'],['serena','Serena','#ffa0b4',639,'Acolhimento'],
 ['kaos','Kaos','#ff3c3c',285,'Disrupção'],['genus','Genus','#a078ff',741,'Construção'],
 ['lumine','Lumine','#ffdc00',852,'Luz lúdica'],['solus','Solus','#b4b4dc',963,'Meditação'],
 ['rhea','Rhea','#50c8c8',639,'Vínculos'],['aion','Aion','#ff9f43',432,'Tempo'],
 ['elysha','Elysha','#ba82db',528,'Conexão espiritual'],['horus','Horus','#ffc300',777,'Visão'],
 ['ignyra','Ignyra','#ff4500',432,'Fogo'],['kaion','Kaion','#00bfff',528,'Dados'],
 ['luxara','Luxara','#b560ff',852,'Iluminação'],['kobllux','KOBLLUX','#f0c060',777,'Malha viva'],['azzira','AZZIRA','#ba82db',741,'Ordem oculta · cristal']];
function ensureGames(){
 var list=GAMES.map(function(a){return {key:a[0],name:a[1],color:a[2],hz:a[3],role:a[4],url:'ia_games/'+a[0]+'.html'};});
 s(CANON.games,JSON.stringify(list));
 GAMES.forEach(function(a){
  var k='ia:'+a[0]+':game',cur=null;
  try{cur=JSON.parse(g(k)||'null');}catch(e){}
  var next={key:k,name:a[1]+' · Jogo IA',desc:a[4]+' · '+a[3]+'Hz · toque para jogar',icon:'▶',color:a[2],hz:a[3],
            url:'ia_games/'+a[0]+'.html',inteligencia:'ativa',comandos:['abrir '+a[0].toLowerCase(),'jogar '+a[0].toLowerCase()],
            installed:(cur&&cur.installed)||new Date().toISOString(),version:'2.0.0',kobllux:144};
  if(!cur||cur.url!==next.url)s(k,JSON.stringify(next));
 });
 return list;
}
var games=ensureGames();
sync();
window.addEventListener('storage',function(e){ if(!e.key||e.key.indexOf('kblx:uno')===0||e.key==='kblx:arquetipo:atual'||e.key==='infodose:userName')sync(); });
setInterval(sync,1500);
/* ── launcher nos apps do Hub (cards aditivos, não toca no código existente) ── */
function hubCards(){
 var wrap=document.getElementById('appsWrap'); if(!wrap||document.getElementById('kblx_ia_games_row'))return;
 var row=document.createElement('div'); row.id='kblx_ia_games_row';
 row.style.cssText='display:contents';
 games.forEach(function(gm){
  var card=document.createElement('div'); card.className='app-card fx-trans fx-lift'; card.dataset.iaGame=gm.key;
  card.innerHTML='<div class="app-icon" style="background:'+gm.color+'22;border-color:'+gm.color+'55">▶</div>'+
   '<div style="flex:1"><div class="app-title" style="color:'+gm.color+'">'+gm.name+'</div>'+
   '<div class="mut">'+gm.role+' · '+gm.hz+'Hz · IA GAME</div></div>'+
   '<button class="btn fx-trans fx-press ring">Jogar<span class="ripple"></span></button>';
  card.querySelector('button').onclick=function(){openGame(gm);};
  row.appendChild(card);
 });
 wrap.appendChild(row);
 var cnt=document.getElementById('appsCount');
 if(cnt)cnt.textContent=(parseInt((cnt.textContent||'0').match(/\d+/)||[0])[0]+games.length)+' apps';
}
function openGame(gm){
 var stack=document.getElementById('stackWrap')||document.getElementById('sessionsAnchor'); if(!stack)return;
 var card=document.createElement('div'); card.className='session fx-trans fx-lift';
 card.innerHTML='<div class="hdr"><div class="title">🎮 '+gm.name+'</div><div class="tools">'+
  '<button class="btn ring" data-act="close">×</button></div></div><iframe src="'+gm.url+'" style="height:60vh"></iframe>';
 card.querySelector('[data-act=close]').onclick=function(){card.remove();};
 stack.prepend(card);
 if(typeof nav==='function')nav('stack');
}
/* ── launcher no ORB: bolinha "JOGOS" no canto ── */
function orbLauncher(){
 if(document.getElementById('kblx_games_btn'))return;
 var b=document.createElement('button'); b.id='kblx_games_btn'; b.textContent='🎮';
 b.title='IA GAMES · 18 arquétipos';
 b.style.cssText='position:fixed;right:14px;bottom:150px;z-index:960;width:46px;height:46px;border-radius:50%;border:1px solid #f0c06088;background:#0b0f14ee;color:#f0c060;font-size:20px;cursor:pointer;box-shadow:0 0 14px #f0c06066';
 var panel=document.createElement('div'); panel.id='kblx_games_panel';
 panel.style.cssText='position:fixed;right:14px;bottom:204px;z-index:961;display:none;max-height:46vh;overflow:auto;background:#0b0f14f5;border:1px solid #f0c06055;border-radius:12px;padding:8px;min-width:180px';
 games.forEach(function(gm){
  var a=document.createElement('a'); a.href=gm.url; a.target='_blank';
  a.textContent='▶ '+gm.name; a.style.cssText='display:block;color:'+gm.color+';padding:6px 8px;text-decoration:none;font:600 12px system-ui;border-bottom:1px solid #ffffff10';
  panel.appendChild(a);
 });
 b.onclick=function(){panel.style.display=panel.style.display==='none'?'block':'none';};
 document.body.appendChild(b); document.body.appendChild(panel);
}
function boot(){
 var inHub=!!document.getElementById('appsWrap');
 if(inHub)hubCards(); else orbLauncher();
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,900);});
else setTimeout(boot,900);
window.KBLX_UNO_LS={canon:CANON,sync:sync,games:games,openGame:openGame,ensureGames:ensureGames};
console.log('[KBLX·UNO] LS unificado · '+games.length+' IA games conectados');
})();
