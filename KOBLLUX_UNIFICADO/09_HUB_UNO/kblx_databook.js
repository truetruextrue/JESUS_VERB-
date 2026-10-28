/* ⟦ KBLX·UNO · DATABOOK 78K · VERDADE × INTEGRAR ÷ Δ = ∞ aplicado aos dados ⟧
   35 livros · ressonância arquetípica · ciclo 369 · fase 12 · consulta à IA viva */
(function(){
'use strict';
var MAN=null, cache={};
function g(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function s(k,v){try{localStorage.setItem(k,v);}catch(e){}}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function LSset(k,v){s(k,v); if(window.KBLX_UNO_LS&&KBLX_UNO_LS.canon&&KBLX_UNO_LS.sync)setTimeout(KBLX_UNO_LS.sync,80);}
function loadManifest(){return fetch('databook/manifest.json').then(function(r){return r.json();}).catch(function(){return null;});}
function loadBook(slug){if(cache[slug])return Promise.resolve(cache[slug]);
 return fetch('databook/'+slug+'.json').then(function(r){return r.json();}).then(function(d){cache[slug]=d;return d;}).catch(function(){return[];});}
function consultarIA(meta, trecho){
 var prompt='KOBLLUX, consulte o livro "'+meta.titulo+'" (arquétipo '+meta.arquetipo+', fase '+meta.fase12+', ciclo 369-'+meta.ciclo369+'). Trecho: '+trecho+' — sintetize com VERDADE×INTEGRAR÷Δ=∞.';
 try{s('kblx:uno:context',JSON.stringify({livro:meta.slug,titulo:meta.titulo,arquetipo:meta.arquetipo,ts:Date.now()}));}catch(e){}
 if(typeof feedPush==='function')feedPush('user','📕 '+prompt.slice(0,220)+'…');
 var un=(g('kblx:uno:user')||g('infodose:userName')||'').trim();
 var sk=(g('kblx:uno:sk')||g('dual.keys.openrouter')||'').trim();
 var mdl=g('kblx:uno:model')||'openrouter/auto';
 if(typeof handleUserMessage==='function'&&sk){handleUserMessage(prompt,un,sk,mdl);}
 else if(typeof toast==='function')toast('📕 contexto armado · configure a chave no Brain','warn');
}
function render(container){
 if(!MAN){container.innerHTML='<div class="mut">databook offline</div>';return;}
 var stats={}; MAN.forEach(function(m){stats[m.arquetipo]=(stats[m.arquetipo]||0)+1;});
 var html='<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px">'
  +'<input id="kblx_lib_q" placeholder="buscar nos 35 livros…" style="flex:1;min-width:140px;background:#0f1426;border:1px solid #f0c06044;border-radius:10px;padding:8px 10px;color:#f5f7ff;font:12px monospace;outline:none">'
  +'<button class="btn fx-trans fx-press ring" id="kblx_lib_all" style="font-size:10px">∞ tudo</button></div>'
  +'<div class="mut" style="font-size:10px;margin-bottom:8px">'+MAN.length+' livros · '
  +Object.keys(stats).map(function(a){return a+'×'+stats[a];}).join(' · ')+'</div>'
  +'<div id="kblx_lib_list" style="display:grid;gap:6px;max-height:44vh;overflow-y:auto"></div>';
 container.innerHTML=html;
 var list=container.querySelector('#kblx_lib_list');
 function draw(q){
  q=(q||'').toLowerCase();
  list.innerHTML='';
  MAN.filter(function(m){return !q||((m.titulo+' '+m.arquetipo+' '+m.fase12+' '+m.resumo).toLowerCase().indexOf(q)>=0);})
   .forEach(function(m){
    var row=document.createElement('div');
    row.style.cssText='background:rgba(0,0,0,.25);border:1px solid '+m.cor+'33;border-left:3px solid '+m.cor+';border-radius:10px;padding:8px 10px;cursor:pointer';
    row.innerHTML='<div style="display:flex;justify-content:space-between;gap:6px;flex-wrap:wrap;align-items:center">'
     +'<b style="color:'+m.cor+';font-size:12px">'+m.simbolo+' '+esc(m.titulo)+'</b>'
     +'<span style="font:9px monospace;color:#8a8a95">'+m.arquetipo+' · fase '+m.fase12+' · 369-'+m.ciclo369+' · '+m.falas+' falas</span></div>'
     +'<div class="mut" style="font-size:10px;margin-top:3px">'+esc(m.resumo)+'…</div>';
    row.onclick=function(){
     loadBook(m.slug).then(function(d){
      var txt=d.slice(0,10).map(function(x){return x.autor+': '+x.fala;}).join('\n').slice(0,1200);
      var det=document.createElement('div');
      det.style.cssText='margin-top:6px;padding:8px;background:#07070a;border-radius:8px;font:10px/1.5 monospace;color:#c9d1d9;white-space:pre-wrap;max-height:180px;overflow:auto';
      det.textContent=txt+'…';
      var bar=document.createElement('div'); bar.style.cssText='display:flex;gap:6px;margin-top:6px;flex-wrap:wrap';
      var bIA=document.createElement('button'); bIA.className='btn fx-trans fx-press ring'; bIA.style.fontSize='10px'; bIA.textContent='⚡ consultar IA';
      bIA.onclick=function(e){e.stopPropagation();consultarIA(m,txt.slice(0,600));};
      var bCp=document.createElement('button'); bCp.className='btn fx-trans fx-press ring'; bCp.style.fontSize='10px'; bCp.textContent='📋 copiar';
      bCp.onclick=function(e){e.stopPropagation();navigator.clipboard.writeText(txt);};
      var bMem=document.createElement('button'); bMem.className='btn fx-trans fx-press ring'; bMem.style.fontSize='10px'; bMem.textContent='◉ memorizar';
      bMem.onclick=function(e){e.stopPropagation();LSset('kblx:uno:lib:lastRead',JSON.stringify(m));if(typeof toast==='function')toast('◉ '+m.titulo+' memorizado','ok');};
      bar.appendChild(bIA);bar.appendChild(bCp);bar.appendChild(bMem);
      var old=row.querySelector('.kblx_det'); if(old)old.remove();
      var wrapd=document.createElement('div'); wrapd.className='kblx_det'; wrapd.appendChild(det); wrapd.appendChild(bar);
      row.appendChild(wrapd);
     });
    };
    list.appendChild(row);
   });
 }
 draw('');
 container.querySelector('#kblx_lib_q').addEventListener('input',function(e){draw(e.target.value);});
 container.querySelector('#kblx_lib_all').onclick=function(){draw('');container.querySelector('#kblx_lib_q').value='';};
}
function mount(){
 var host=document.getElementById('kblx_library');
 if(!host)return;
 loadManifest().then(function(m){
  MAN=m;
  if(m){try{LSset('kblx:uno:lib:index',JSON.stringify({livros:m.length,ts:Date.now(),formula:'VERDADE×INTEGRAR÷Δ=∞'}));}catch(e){}}
  render(host);
 });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(mount,700);});
else setTimeout(mount,700);
window.KBLX_BOOK={reload:mount,manifest:function(){return MAN;}};
console.log('[DATABOOK 78K] VERDADE×INTEGRAR÷Δ=∞ · dados vivos integrados');
})();
