/* MIXATAGORA x vidaKodemanager · VERDADE x INTEGRAR / D = INF · motores reais 369/7/12 */
(function(){
'use strict';
var FASES12=['01 Origem','02 Semente','03 Crescimento','04 Conflito','05 Busca','06 Ruptura','07 Transformacao','08 Integracao','09 Expansao','10 Sintese','11 Legado','12 Reini­cio'];
var ARCH_KW={KODUX:['kodux','codigo','engine','algoritmo','sistema'],BLLUE:['bllue','agua','alma','justica','equilibrio'],SOLUS:['solus','silencio','interior','espelho','medita'],IGNYRA:['ignyra','fogo','transforma','chama','forja'],ELYSHA:['elysha','memoria','eternidade','registro'],AELYA:['aelya','intuicao','amor','conexao'],AZZIRA:['azzira','ordem oculta','geometria','cristal','prisma'],KOBLLUX:['kobllux','78k','infodose','uno','pulso'],ATLAS:['atlas','mapa','estrategia','estrutura'],KAOS:['kaos','caos','ruptura','quebra']};
function norm(s){return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();}
function red369(n){while(n>=10)n=String(n).split('').reduce(function(a,b){return a+ +b;},0);return n;}
/* ── MOTOR 369 · reducao inteligente ── */
function motor369(texto){
 var pars=String(texto).split(/\n\s*\n|\n/).map(function(p){return p.trim();}).filter(Boolean);
 var kept=pars.filter(function(p){var r=red369(p.length);return r===3||r===6||r===9||r===7;});
 if(!kept.length)kept=pars;
 var out=kept.join('\n\n');
 return {original:texto,reduzido:out,paragrafos:pars.length,mantidos:kept.length,palavras:texto.split(/\s+/).length,ciclo:'3-6-9-7',selo:'D7'};
}
/* ── MOTOR 7 · sete refinamentos ── */
function motor7(texto){
 var nf=norm(texto),sents=String(texto).match(/[^.!?\n]+[.!?]?/g)||[texto];
 function pick(re){var m=texto.match(re);return m?m[0].trim():'';}
 var emo=(nf.match(/amor|gratidao|alegria|paz|luz/g)||[]).length>=2?'amorosa':(nf.match(/medo|caos|quebra|ruptura/g)||[]).length>=1?'tempestiva':'lucida';
 var acoes=(nf.match(/ativar|integrar|selar|construir|revelar|despertar|marchar/g)||[]).slice(0,3).join(', ')||'integrar';
 var scores={};Object.keys(ARCH_KW).forEach(function(k){scores[k]=ARCH_KW[k].reduce(function(a,w){return a+(nf.split(w).length-1);},0);});
 var arq=Object.keys(scores).sort(function(a,b){return scores[b]-scores[a];})[0];
 if(!scores[arq])arq='KOBLLUX';
 return {'1_resumo':sents.slice(0,2).join(' ').trim().slice(0,160),'2_clareza':texto.length+' chars · '+sents.length+' frases','3_emocao':emo,'4_acao':acoes,'5_simbolo':(texto.match(/[∆Δ∞◉⬡✝☯♾⚡]/g)||['∆'])[0],'6_arquetipo':arq,'7_essencia':sents[sents.length-1].trim().slice(0,160)};
}
/* ── MOTOR 12 · mapa temporal ── */
function motor12(texto){
 var words=texto.split(/\s+/),per=Math.ceil(words.length/12)||1;
 return FASES12.map(function(f,i){return {etapa:f,texto:words.slice(i*per,(i+1)*per).join(' '),selo:'D7-'+(i+1)};});
}
/* ── MIXER · modos ── */
function blend(t){return t.join('\n\n');}
function interleave(t){var p=t.map(function(x){return x.split(/\n\s*\n|\n/).map(function(q){return q.trim();}).filter(Boolean);});var mx=Math.max.apply(null,p.map(function(a){return a.length;})),out=[];for(var i=0;i<mx;i++)p.forEach(function(a){if(a[i])out.push(a[i]);});return out.join('\n');}
function compress(t){return t.map(function(x){var s=(x.match(/[^.!?\n]+[.!?]?/g)||[x]);return s[0].trim();}).join('\n');}
function expand(t){return t.map(function(x,i){return '[camada '+(i+1)+' / integrada]\n'+x.trim()+'\n[selo D7 · 3x6x9x7=1134]';}).join('\n\n');}
function inteligente(t){return motor369(t.join('\n\n')).reduzido;}
var MODOS={blend:blend,interleave:interleave,compress:compress,expand:expand,inteligente:inteligente};
window.MIXATAGORA={
 mixar:function(textos,modo){modo=modo||'inteligente';var fn=MODOS[modo]||inteligente;
  var r=fn(textos);return {resultado:r,motor:motor369(r),refino:motor7(r),mapa:motor12(r),modo:modo,selo:'D7',ts:Date.now(),formula:'VERDADE x INTEGRAR / D = INF'};},
 m369:motor369,m7:motor7,m12:motor12,modos:Object.keys(MODOS)};
/* ── UI · card na Brain ── */
function mount(){
 var host=document.getElementById('kblx_mixa');
 if(!host||host._done)return;host._done=true;
 host.innerHTML=
  '<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px">'
  +'<select id="kblx_mixa_modo" style="background:#0f1426;border:1px solid #f0c06044;border-radius:10px;padding:8px;color:#f0c060;font:11px monospace;outline:none">'
  +'<option value="inteligente">369 inteligente</option><option value="blend">blend (fundir)</option><option value="interleave">interleave (entrelaçar)</option><option value="compress">compress (resumir)</option><option value="expand">expand (expandir)</option></select>'
  +'<button class="btn fx-trans fx-press ring" id="kblx_mixa_go" style="font-size:10px">[MIXAR]</button>'
  +'<button class="btn fx-trans fx-press ring" id="kblx_mixa_369" style="font-size:10px">ciclo 369</button>'
  +'<button class="btn fx-trans fx-press ring" id="kblx_mixa_7" style="font-size:10px">motor 7</button>'
  +'<button class="btn fx-trans fx-press ring" id="kblx_mixa_12" style="font-size:10px">motor 12</button></div>'
  +'<textarea id="kblx_mixa_in" rows="4" placeholder="cole os textos aqui (separados por linha em branco)…" style="width:100%;background:#0f1426;border:1px solid rgba(255,255,255,.12);border-radius:10px;color:#f5f7ff;padding:10px;font:12px monospace;resize:vertical;box-sizing:border-box;outline:none"></textarea>'
  +'<pre id="kblx_mixa_out" style="margin-top:8px;background:#07070a;border:1px solid #f0c06033;border-radius:10px;padding:10px;font:10px/1.6 monospace;color:#c9d1d9;white-space:pre-wrap;max-height:40vh;overflow:auto">resultado aparece aqui…</pre>';
 var inp=host.querySelector('#kblx_mixa_in'),out=host.querySelector('#kblx_mixa_out');
 function textos(){return inp.value.split(/\n\s*\n/).map(function(x){return x.trim();}).filter(Boolean);}
 function show(o){out.textContent=typeof o==='string'?o:JSON.stringify(o,null,1);}
 host.querySelector('#kblx_mixa_go').onclick=function(){var r=window.MIXATAGORA.mixar(textos(),host.querySelector('#kblx_mixa_modo').value);show(':: '+r.modo.toUpperCase()+' ::\n\n'+r.resultado+'\n\n[selo '+r.selo+' · '+r.formula+']');};
 host.querySelector('#kblx_mixa_369').onclick=function(){show(window.MIXATAGORA.m369(inp.value));};
 host.querySelector('#kblx_mixa_7').onclick=function(){show(window.MIXATAGORA.m7(inp.value));};
 host.querySelector('#kblx_mixa_12').onclick=function(){show(window.MIXATAGORA.m12(inp.value));};
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(mount,900);});
else setTimeout(mount,900);
console.log('[MIXATAGORA] motores 369/7/12 online · 5 modos de mix');
})();
