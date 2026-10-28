/* ⟦ KBLX·UNO · DATABOOK · índice local de fatos e consulta à IA ⟧ */
(function(){
'use strict';
var MAN=null, cache={}, factIndex=null, indexPromise=null, indexSummary=null;
function g(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function s(k,v){try{localStorage.setItem(k,v);}catch(e){}}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function LSset(k,v){s(k,v); if(window.KBLX_UNO_LS&&KBLX_UNO_LS.canon&&KBLX_UNO_LS.sync)setTimeout(KBLX_UNO_LS.sync,80);}
function fetchJson(path){
 return fetch(path).then(function(r){
  if(!r.ok)throw new Error(path+' retornou HTTP '+r.status);
  return r.json();
 });
}
function loadManifest(){
 return fetchJson('databook/manifest.json').then(function(m){
  if(!Array.isArray(m))throw new TypeError('O manifesto do databook precisa ser uma lista.');
  return m;
 });
}
function loadBook(slug){if(cache[slug])return Promise.resolve(cache[slug]);
 return fetchJson('databook/'+slug+'.json').then(function(d){
  if(!Array.isArray(d))throw new TypeError('databook/'+slug+'.json precisa conter uma lista de fatos.');
  cache[slug]=d;return d;
 });}
function summarizeFact(fact){
 if(typeof fact==='string')return fact;
 try{return JSON.stringify(fact);}catch(error){return String(fact);}
}
function indexFacts(onProgress){
 if(indexSummary)return Promise.resolve(indexSummary);
 if(indexPromise)return indexPromise;
 if(!MAN)return Promise.reject(new Error('O manifesto do databook ainda não foi carregado.'));
 var results=new Array(MAN.length), cursor=0, completed=0;
 function worker(){
  var i=cursor++;
  if(i>=MAN.length)return Promise.resolve();
  var meta=MAN[i];
  return loadBook(meta.slug).then(function(rows){
   results[i]={meta:meta,rows:rows};
  },function(error){
   results[i]={meta:meta,error:error};
  }).then(function(){
   completed++;
   if(onProgress)onProgress({completed:completed,total:MAN.length});
   return worker();
  });
 }
 var workers=new Array(Math.min(4,MAN.length)).fill(0).map(function(){return worker();});
 indexPromise=Promise.all(workers).then(function(){
  var missing=[], indexedSources=0;
  factIndex=[];
  results.forEach(function(result){
   if(result.error){
    missing.push({slug:result.meta.slug,file:result.meta.slug+'.json',error:result.error.message});
    return;
   }
   indexedSources++;
   result.rows.forEach(function(fact){
    factIndex.push({meta:result.meta,fact:fact,searchText:summarizeFact(fact).toLowerCase()});
   });
  });
  indexSummary={sourcesExpected:MAN.length,sourcesIndexed:indexedSources,factsIndexed:factIndex.length,missing:missing};
  return indexSummary;
 }).catch(function(error){
  indexPromise=null;
  throw error;
 });
 return indexPromise;
}
function searchFacts(query){
 var q=String(query||'').trim().toLowerCase();
 if(!q||!factIndex)return[];
 return factIndex.filter(function(entry){return entry.searchText.indexOf(q)>=0;});
}
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
 if(!MAN){container.innerHTML='<div class="mut">Databook indisponível. Verifique a rede local e o manifesto.</div>';return;}
 var stats={}; MAN.forEach(function(m){stats[m.arquetipo]=(stats[m.arquetipo]||0)+1;});
 var html='<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px">'
  +'<input id="kblx_lib_q" placeholder="buscar títulos e fatos indexados…" style="flex:1;min-width:140px;background:#0f1426;border:1px solid #f0c06044;border-radius:10px;padding:8px 10px;color:#f5f7ff;font:12px monospace;outline:none">'
  +'<button class="btn fx-trans fx-press ring" id="kblx_lib_all" style="font-size:10px">∞ limpar</button>'
  +'<button class="btn fx-trans fx-press ring" id="kblx_lib_index" style="font-size:10px">◉ indexar fatos</button></div>'
  +'<div class="mut" style="font-size:10px;margin-bottom:8px">'+MAN.length+' fontes · '
  +Object.keys(stats).map(function(a){return a+'×'+stats[a];}).join(' · ')
  +' · classificações históricas; contrato canônico inalterado</div>'
  +'<div id="kblx_lib_index_status" class="mut" role="status" aria-live="polite" style="font-size:10px;margin-bottom:8px">Indexação sob demanda; consulta apenas os JSONs locais do databook.</div>'
  +'<div id="kblx_lib_facts" style="display:grid;gap:6px;max-height:30vh;overflow-y:auto"></div>'
  +'<div id="kblx_lib_list" style="display:grid;gap:6px;max-height:44vh;overflow-y:auto"></div>';
 container.innerHTML=html;
 var list=container.querySelector('#kblx_lib_list');
 var facts=container.querySelector('#kblx_lib_facts');
 var status=container.querySelector('#kblx_lib_index_status');
 var indexButton=container.querySelector('#kblx_lib_index');
 var queryInput=container.querySelector('#kblx_lib_q');
 function drawFacts(q){
  facts.innerHTML='';
  if(!factIndex||!q)return;
  var matches=searchFacts(q);
  var count=document.createElement('div');
  count.className='mut';
  count.textContent=matches.length+' fatos encontrados'+(matches.length>25?' · exibindo os primeiros 25':'');
  facts.appendChild(count);
  matches.slice(0,25).forEach(function(entry){
   var row=document.createElement('div');
   row.style.cssText='background:rgba(0,0,0,.25);border:1px solid #f0c06033;border-left:3px solid #f0c060;border-radius:10px;padding:8px 10px';
   var title=document.createElement('b');
   title.textContent=entry.meta.titulo+' · '+entry.meta.arquetipo+' · '+entry.meta.slug;
   var body=document.createElement('div');
   body.className='mut';
   var fact=entry.fact;
   body.textContent=fact&&typeof fact==='object'
    ?String(fact.autor||'')+(fact.autor?': ':'')+String(fact.fala===undefined?summarizeFact(fact):fact.fala)
    :String(fact);
   row.appendChild(title);row.appendChild(body);facts.appendChild(row);
  });
 }
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
     }).catch(function(error){
      console.error('KBLX Databook: falha ao abrir '+m.slug+'.',error);
      var detail=document.createElement('div');
      detail.className='mut';detail.textContent='Falha ao carregar '+m.slug+': '+error.message;
      row.appendChild(detail);
     });
    };
    list.appendChild(row);
   });
  drawFacts(q);
 }
 draw('');
 queryInput.addEventListener('input',function(e){draw(e.target.value);});
 container.querySelector('#kblx_lib_all').onclick=function(){draw('');queryInput.value='';};
 indexButton.onclick=function(){
  indexButton.disabled=true;indexButton.textContent='indexando…';
  status.textContent='Indexando 0/'+MAN.length+' fontes locais…';
  indexFacts(function(progress){status.textContent='Indexando '+progress.completed+'/'+progress.total+' fontes locais…';})
   .then(function(summary){
    indexButton.disabled=true;indexButton.textContent='✓ fatos indexados';
    status.textContent=summary.sourcesIndexed+'/'+summary.sourcesExpected+' fontes indexadas · '+summary.factsIndexed+' fatos'
     +(summary.missing.length?' · ausentes: '+summary.missing.map(function(item){return item.file;}).join(', '):' · cobertura completa');
    drawFacts(queryInput.value);
   }).catch(function(error){
    indexButton.disabled=false;indexButton.textContent='◉ tentar indexar novamente';
    status.textContent='Falha ao indexar o databook: '+error.message;
    console.error('KBLX Databook: falha na indexação completa.',error);
   });
 };
}
function mount(){
 var host=document.getElementById('kblx_library');
 if(!host)return Promise.resolve(null);
 return loadManifest().then(function(m){
  MAN=m;
  if(m){try{LSset('kblx:uno:lib:index',JSON.stringify({livros:m.length,ts:Date.now(),formula:'VERDADE×INTEGRAR÷Δ=∞'}));}catch(e){}}
  render(host);
  return m;
 }).catch(function(error){
  host.textContent='Falha ao carregar o índice de memória: '+error.message;
  console.error('KBLX Databook: falha ao carregar o manifesto.',error);
  return null;
 });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(mount,700);});
else setTimeout(mount,700);
window.KBLX_BOOK={reload:mount,manifest:function(){return MAN;},indexFacts:indexFacts,searchFacts:searchFacts};
console.log('[DATABOOK 78K] VERDADE×INTEGRAR÷Δ=∞ · dados vivos integrados');
})();
