/* ⟦ KOBLLUX ESPELHO PACK v24 · conecta o que ja existe · sem botoes novos · VERDADE x INTEGRAR / D = INF ⟧ */
(function(){
'use strict';
function g(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function s(k,v){try{localStorage.setItem(k,v);}catch(e){}}

/* ═══ 1 · VOZ PERSISTENTE (guardiao · sem UI · so funciona) ═══ */
var KBLX_VOICE=(function(){
 var queue=[],speaking=false,voice=null;
 function pick(){var vs=speechSynthesis.getVoices().filter(function(v){return /^pt/i.test(v.lang);});return vs.filter(function(v){return /BR/i.test(v.lang);})[0]||vs[0]||null;}
 if('speechSynthesis' in window){
  speechSynthesis.onvoiceschanged=function(){voice=pick();};voice=pick();
  setInterval(function(){if(speaking&&speechSynthesis.paused){try{speechSynthesis.resume();}catch(e){}}},300);
  document.addEventListener('visibilitychange',function(){if(document.hidden&&speaking&&speechSynthesis.paused){try{speechSynthesis.resume();}catch(e){}}});
 }
 function chunks(text){var parts=String(text).replace(/\s+/g,' ').split(/([.!?;:…])\s*/),out=[],cur='';
  for(var i=0;i<parts.length;i++){if((cur+parts[i]).length<180)cur+=parts[i];else{if(cur)out.push(cur);cur=parts[i];}}
  if(cur)out.push(cur);return out.filter(Boolean);}
 function pump(){if(!queue.length){speaking=false;return;}speaking=true;
  var u=new SpeechSynthesisUtterance(queue.shift());
  if(voice)u.voice=voice;u.rate=1;u.pitch=.95;
  u.onend=function(){setTimeout(pump,60);};u.onerror=function(){setTimeout(pump,60);};
  speechSynthesis.speak(u);}
 function speak(text,opts){if(!('speechSynthesis' in window))return;opts=opts||{};
  if(opts.replace)stop();
  if(opts.arch&&window.KBLX_VOZ&&KBLX_VOZ.findVoice){var v=KBLX_VOZ.findVoice(opts.arch);if(v)voice=v;}
  queue.push.apply(queue,chunks(text));if(!speaking)pump();}
 function stop(){queue=[];speaking=false;try{speechSynthesis.cancel();}catch(e){}}
 window.KBLX_VOICE={speak:speak,stop:stop,pause:function(){try{speechSynthesis.pause();}catch(e){}},resume:function(){try{speechSynthesis.resume();speaking=true;if(queue.length&&!speechSynthesis.pending)pump();}catch(e){}},isActive:function(){return speaking||queue.length>0;}};
 return window.KBLX_VOICE;
})();

/* ═══ 2 · MODULOS (estojo · historias · abre via Apps/Stack que ja existem) ═══ */
var KBLX_MODULES=(function(){
 var ARCHS=(typeof ARCHETYPES!=='undefined')?ARCHETYPES:[];
 var EXTRA=[
  {file:'pulse.html',name:'Pulse · Som',desc:'Musica e emocao',icon:'~',frequencia:'432Hz',opcode:'0x01',comandos:['pulse','musica','som']},
  {file:'serena.html',name:'Serena · Cuidado',desc:'Acolhimento emocional',icon:'o',frequencia:'639Hz',opcode:'0x0A',comandos:['serena','acolhimento']},
  {file:'solus.html',name:'Solus · Zen',desc:'Sabedoria e meditacao',icon:'*',frequencia:'741Hz',opcode:'0x0B',comandos:['solus','meditacao']},
  {file:'vitalis.html',name:'Vitalis · Corpo',desc:'Saude e rotina',icon:'v',frequencia:'528Hz',opcode:'0x09',comandos:['vitalis','saude']},
  {file:'artemis.html',name:'Artemis · Saber',desc:'Conhecimento',icon:'>',frequencia:'528Hz',opcode:'0x05',comandos:['artemis','conhecimento']},
  {file:'kobllux.html',name:'KOBLLUX · Nucleo',desc:'Codigo do Verbo',icon:'K',frequencia:'369Hz',opcode:'0x00',comandos:['kobllux','nucleo']},
  {file:'bllue.html',name:'BLLUE · Espirito',desc:'Ponte sensivel',icon:'B',frequencia:'528Hz',opcode:'0x08',comandos:['bllue','espirito']}];
 var ALL=ARCHS.concat(EXTRA.filter(function(e){return !ARCHS.some(function(a){return a.file===e.file;});}));
 var HISTORIA='HISTORICO DO CAMPO. Equacao-mae: EMET x INTEGRAR / D = INF. 13 opcodes, 10 dimensoes. O campo pulsa em 3x6x9x7 = 1134. Cada arquetipo guarda uma frequencia viva do verbo.';
 function story(a){return a.name+'. Essencia: '+a.desc+'. Frequencia: '+a.frequencia+', opcode: '+a.opcode+'. '+HISTORIA+' O pulso e um so, mas a forma e multipla.';}
 function pulseModule(a){
  return '<!DOCTYPE html><html><head><meta charset="utf-8"><style>body{margin:0;height:100vh;display:grid;place-items:center;background:radial-gradient(circle,#1a1a2e,#050507);color:#fff;font-family:monospace}canvas{display:block}</style></head><body><canvas id="c"></canvas><script>'
  +'var f=parseInt("'+a.frequencia+'",10),op="'+a.opcode+'";var c=document.getElementById("c"),x=c.getContext("2d");'
  +'function rs(){c.width=innerWidth;c.height=innerHeight}rs();addEventListener("resize",rs);var t=0;'
  +'(function loop(){t+=f/60000;x.fillStyle="rgba(5,5,7,.12)";x.fillRect(0,0,c.width,c.height);'
  +'var R=60+40*Math.sin(t*6.28),cx=c.width/2,cy=c.height/2;x.strokeStyle="hsl("+(200+40*Math.sin(t))+",90%,60%)";x.lineWidth=2;'
  +'x.beginPath();x.arc(cx,cy,R,0,6.29);x.stroke();'
  +'for(var i=0;i<3;i++){var a2=i/3*6.28+t;x.beginPath();x.arc(cx+Math.cos(a2)*R,cy+Math.sin(a2)*R,6,0,6.29);x.fillStyle="#ffd700";x.fill();}'
  +'x.fillStyle="rgba(255,255,255,.85)";x.font="14px monospace";x.textAlign="center";x.fillText(op+" · "+f+"Hz",cx,cy+R+30);requestAnimationFrame(loop)})();'
  +'</'+'script></body></html>';}
 function open(a){
  var done=function(html){
   var url=URL.createObjectURL(new Blob([html],{type:'text/html'}));
   var app={key:'ia:'+a.file.replace('.html','')+':game',title:a.name,desc:a.desc,url:url,icon:a.icon||'K'};
   try{s(app.key,JSON.stringify({key:app.key,file:a.file,name:a.name,icon:a.icon,desc:a.desc,url:url,installed:new Date().toISOString(),version:'24.0'}));}catch(e){}
   if(typeof window.openApp==='function')window.openApp(app);else window.open(url,'_blank');
   KBLX_VOICE.speak(story(a),{arch:a.file.replace('.html','')});
  };
  fetch('archetypes/'+a.file).then(function(r){return r.ok?r.text():null;})
   .then(function(h){if(h)return done(h);
    return fetch('ia_games/'+a.file).then(function(r2){return r2.ok?r2.text():null;}).then(function(h2){done(h2||pulseModule(a));});})
   .catch(function(){done(pulseModule(a));});
 }
 window.KBLX_MODULES={ALL:ALL,story:story,open:open};
 return window.KBLX_MODULES;
})();

/* ═══ 3 · CAMADA HIBRIDA · CONFIG dentro do BRAIN · usa #sk e #model que ja existem ═══ */
var KBLX_HYBRID=(function(){
 var RKEY='kblx:uno:hybrid.routes';
 var TAGS=[['empatia','Empatia · historias e relacionamentos'],['logica','Logica · codigo e dados'],['geral','Geral · todo o resto']];
 function routes(){try{var r=JSON.parse(g(RKEY)||'null');if(r)return r;}catch(e){}
  return {empatia:'__mayara__',logica:'__padrao__',geral:'__padrao__'};}
 function persist(rt){s(RKEY,JSON.stringify(rt));}
 /* modelos disponiveis = opcoes do #model do Brain (inclui os adicionados via customModel) */
 function modelOptions(){
  var sel=document.getElementById('model'),out=[];
  if(sel)for(var i=0;i<sel.options.length;i++)out.push({v:sel.options[i].value,t:sel.options[i].textContent});
  return out;}
 function classify(t){t=t.toLowerCase();
  if(/historia|relacionamento|amor|sentimento|emocional|narrar|conta|sinto|medo|saudade|coracao/.test(t))return 'empatia';
  if(/codigo|script|dados|logica|funcao|erro|python|javascript|bug|sistema/.test(t))return 'logica';
  return 'geral';}
 function resolveModel(route){
  if(route==='__mayara__')return {name:'Mayara',model:'openrouter/auto'};
  if(route==='__padrao__'){var sel=document.getElementById('model');return {name:'Padrao',model:sel?sel.value:'openrouter/auto'};}
  return {name:route,model:route};}
 function brainKey(){var skEl=document.getElementById('sk');return ((skEl&&skEl.value.trim())||g('dual.keys.openrouter')||g('kblx:uno:sk')||'').trim();}
 function callOne(m,sys,user){
  var key=brainKey();
  if(!key)return Promise.reject(new Error('sem chave no Brain'));
  if(key.indexOf('sk-ant')===0)
   return fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01'},body:JSON.stringify({model:m.model.indexOf('/')>=0?'claude-sonnet-4-20250514':m.model,max_tokens:1600,system:sys,messages:[{role:'user',content:user}]})})
    .then(function(r){if(!r.ok)throw new Error('ANT '+r.status);return r.json();}).then(function(d){return d.content.map(function(b){return b.text||'';}).join('');});
  return fetch('https://openrouter.ai/api/v1/chat/completions',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+key},body:JSON.stringify({model:m.model,messages:[{role:'system',content:sys},{role:'user',content:user}]})})
   .then(function(r){if(!r.ok)throw new Error('OR '+r.status);return r.json();}).then(function(d){return d.choices[0].message.content;});
 }
 function ask(user,sys){
  sys=sys||'Voce e KOBLLUX, o Codigo do Verbo. Responda em pt-BR com verdade, clareza e luz. Equacao: VERDADE x INTEGRAR / D = INF.';
  var tag=classify(user),rt=routes(),order=[rt[tag],rt.geral,'__padrao__'],seen={},i=0;
  function next(){
   if(i>=order.length)return Promise.reject(new Error('falha em todos os modelos ('+tag+')'));
   var route=order[i++];if(seen[route])return next();seen[route]=1;
   var m=resolveModel(route);
   return callOne(m,sys,user).then(function(text){return {text:text,model:m.name,tag:tag,route:route};},function(e){return next();});
  }
  return next();
 }
 /* Card de config DENTRO do v-brain, apos o card da API (usa #sk/#model existentes) */
 function mountCard(){
  var skEl=document.getElementById('sk');if(!skEl)return false;
  var apiCard=skEl.closest('.card')||skEl.parentNode;
  if(document.getElementById('kblx_hybrid_card'))return true;
  var card=document.createElement('div');card.className='card fx-trans fx-lift';card.id='kblx_hybrid_card';card.style.display='block';
  card.setAttribute('data-frequency','777');card.setAttribute('data-opcode','0x07');card.setAttribute('data-geometry','<>');
  card.innerHTML='<div style="font-weight:800;letter-spacing:.06em">CAMADA HIBRIDA · roteamento por intencao</div>'
   +'<div class="mut" style="font-size:11px;margin:4px 0 8px">usa a chave e os modelos ja configurados acima · Mayara = rota empatia do espelho</div>'
   +'<div id="kblx_hybrid_rows" style="display:grid;gap:6px"></div>'
   +'<div class="mut" style="font-size:11px;margin-top:8px" id="kblx_hybrid_st"></div>';
  apiCard.parentNode.insertBefore(card,apiCard.nextSibling);
  drawRows();
  return true;
 }
 function drawRows(){
  var host=document.getElementById('kblx_hybrid_rows');if(!host)return;
  var rt=routes(),opts=modelOptions();
  host.innerHTML=TAGS.map(function(t){
   var optsHtml='<option value="__padrao__">(padrao do Brain)</option><option value="__mayara__">Mayara · espelho empatia</option>'
    +opts.map(function(o){return '<option value="'+o.v.replace(/"/g,'&quot;')+'"'+(rt[t[0]]===o.v?' selected':'')+'>'+o.t+'</option>';}).join('');
   return '<label style="display:flex;gap:8px;align-items:center;font-size:12px"><span style="min-width:220px;color:#8a8a95">'+t[1]+'</span>'
    +'<select data-route="'+t[0]+'" style="flex:1;background:#0f1426;border:1px solid rgba(255,255,255,.12);border-radius:8px;color:#f5f7ff;padding:6px;font:11px monospace">'+optsHtml+'</select></label>';
  }).join('');
  host.querySelectorAll('select[data-route]').forEach(function(sel){
   sel.value=rt[sel.dataset.route]||'__padrao__';
   sel.onchange=function(){var r=routes();r[sel.dataset.route]=sel.value;persist(r);status();};
  });
  status();
 }
 function status(){
  var st=document.getElementById('kblx_hybrid_st');if(!st)return;
  var rt=routes(),k=brainKey();
  st.textContent='rotas: empatia→'+JSON.stringify(rt.empatia)+' · logica→'+JSON.stringify(rt.logica)+' · geral→'+JSON.stringify(rt.geral)
   +' · chave: '+(k?(k.slice(0,10)+'…'):'AUSENTE (salve a chave acima)');
 }
 /* conecta: refaz linhas quando o usuario adiciona modelo via botao existente addModel */
 function hookBrain(){
  var addBtn=document.getElementById('addModel');
  if(addBtn&&!addBtn.__hyb){addBtn.__hyb=1;addBtn.addEventListener('click',function(){setTimeout(drawRows,300);});}
  var sk=document.getElementById('sk');if(sk&&!sk.__hyb){sk.__hyb=1;sk.addEventListener('input',status);}
  var sv=document.getElementById('saveSK');if(sv&&!sv.__hyb){sv.__hyb=1;sv.addEventListener('click',function(){setTimeout(status,200);});}
 }
 function patch(){
  if(window.__kblxHybridPatched)return;window.__kblxHybridPatched=true;
  var orig=window.handleUserMessage;
  if(typeof orig==='function'){
   window.handleUserMessage=async function(text,userName,sk,model){
    if(brainKey()){
     try{var r=await ask(text);
      if(r.text){
       if(typeof feedPush==='function')feedPush('ai',r.model+': '+r.text);
       if(typeof showArchMessage==='function')showArchMessage(r.text,'ok');
       try{var sel=document.getElementById('arch-select');var arch=sel?(sel.value||'').replace(/\.html$/i,''):'kobllux';KBLX_VOICE.speak(r.text,{arch:arch});}catch(e){}
       return;
      }}catch(e){}
    }
    return orig.apply(this,arguments);
   };
  }
  if(typeof window.callClaude==='function'){var oc=window.callClaude;window.callClaude=async function(sys,user){try{var r=await ask(user,sys);return r.text;}catch(e){return oc(sys,user);}};}
  window.KBLX_HYBRID_ASK=ask;
 }
 window.KBLX_HYBRID={ask:ask,classify:classify,mountCard:mountCard,drawRows:drawRows,status:status,patch:patch,routes:routes};
 return window.KBLX_HYBRID;
})();

/* ═══ 4 · CORRECOES DE ROBUSTEZ (fala / modelo / 401) ═══ */
(function(){
 /* 4a · reconhecimento de fala: no max 2 erros por janela de 8s, depois silencia */
 var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
 if(SR){
  var SR2=function(){var r=new SR();var count=0,last=0;
   r.onerror=function(e){var now=Date.now();if(now-last>8000)count=0;last=now;count++;
    if(count<=2){if(typeof dualLog==='function')dualLog('voz: erro de reconhecimento ('+(e.error||'?')+')');}
    else if(count===3&&typeof dualLog==='function')dualLog('voz: reconhecimento pausado apos 3 tentativas · toque no microfone para reativar');};
   return r;};
  SR2.prototype=SR.prototype;
  if(window.SpeechRecognition)window.SpeechRecognition=SR2;else window.webkitSpeechRecognition=SR2;
 }
 /* 4b · sanitiza modelo + aviso claro de 401 (uma vez por minuto) */
 if(typeof window.sendAIMessage==='function'&&!window.sendAIMessage.__san){
  var orig=window.sendAIMessage;
  var lastWarn=0;
  var wrapped=async function(content,sk,model,systemPrompt,layer){
   var clean=String(model||'').replace(/["'`“”‘’]/g,'').trim()||'openrouter/auto';
   try{ return await orig(content,sk,clean,systemPrompt,layer); }
   catch(e){
    var msg=String(e&&e.message||'');
    if(/401/.test(msg)){var now=Date.now();if(now-lastWarn>60000){lastWarn=now;
     if(typeof toast==='function')toast('chave da API invalida (401) — atualize no Brain','err');
     if(typeof dualLog==='function')dualLog('API 401: verifique a chave salva no Brain');}}
    throw e;
   }};
  wrapped.__san=1;window.sendAIMessage=wrapped;
 }
})();

/* ═══ 5 · COMANDOS DE VOZ/TEXTO (falar/rodar/selar/parar/abrir) — sem UI nova ═══ */
(function(){
 function cmd(text){var t=String(text).toLowerCase().trim(),m;
  if(m=t.match(/(?:falar|fale|diga|narra(?:r)?)\s+(\w+)(?:\s*:\s*([\s\S]+))?/))return {verb:'falar',arch:m[1],payload:m[2]||''};
  if(m=t.match(/(?:fechar|close)\s*(\w+)?/))return {verb:'fechar',arch:m[1]||''};
  if(m=t.match(/(?:rodar|girar|wheel|proximo|next)/))return {verb:'rodar'};
  if(m=t.match(/(?:selar|bau|selo)/))return {verb:'selar'};
  if(m=t.match(/(?:parar|silencio|quieto)/))return {verb:'parar'};
  if(m=t.match(/(?:continuar|resume)/))return {verb:'continuar'};
  if(m=t.match(/(?:abrir|jogar|iniciar|open)\s+(\w+)/))return {verb:'abrir',arch:m[1]};
  return null;}
 function findArch(name){var n=name.toLowerCase();
  return KBLX_MODULES.ALL.filter(function(a){return a.comandos.some(function(c){return c.toLowerCase().indexOf(n)===0;})||a.name.toLowerCase().indexOf(n)>=0;})[0];}
 window.KBLX_CMD=function(text){
  var c=cmd(text);if(!c)return false;
  var a=c.arch?findArch(c.arch):null;
  if(c.verb==='falar'){var sp=c.payload||(a?KBLX_MODULES.story(a):text.replace(/^falar\s*/i,''));KBLX_VOICE.speak(sp,{arch:a?a.file.replace('.html',''):null});return true;}
  if(c.verb==='abrir'&&a){KBLX_MODULES.open(a);return true;}
  if(c.verb==='rodar'){var nx=KBLX_MODULES.ALL[Math.floor(Math.random()*KBLX_MODULES.ALL.length)];KBLX_MODULES.open(nx);return true;}
  if(c.verb==='selar'){KBLX_VOICE.speak('Selo ativado. VERDADE x INTEGRAR / D = INF. 3x6x9x7 = 1134. AMEM.');return true;}
  if(c.verb==='fechar'){var s2=document.querySelector('.session');if(s2){s2.remove();if(typeof updateDock==='function')updateDock();}return true;}
  if(c.verb==='parar'){KBLX_VOICE.stop();return true;}
  if(c.verb==='continuar'){KBLX_VOICE.resume();return true;}
  return false;};
 /* intercepta Enter somente nos campos de CHAT (nao nos campos do Brain) */
 document.addEventListener('keydown',function(e){
  if(e.key!=='Enter')return;
  var el=e.target;if(!el.matches||!el.matches('input,textarea'))return;
  if(el.id!=='chatInputTA'&&el.id!=='chatInput'&&el.id!=='homeInput'&&el.name!=='msg')return;
  var v=(el.value||'').trim();
  if(/^(falar|fale|narra|fechar|rodar|selar|parar|continuar)\b/i.test(v)&&window.KBLX_CMD(v)){el.value='';e.preventDefault();}
 },true);
})();

/* ═══ BOOT ═══ */
function boot(){
 KBLX_HYBRID.mountCard();
 KBLX_HYBRID.patch();
 /* reconstrói as linhas do híbrido quando entrar no Brain (modelos podem ter sido adicionados) */
 document.addEventListener('click',function(e){
  var b=e.target.closest&&e.target.closest('[data-nav]');
  if(b&&b.dataset.nav==='brain')setTimeout(function(){KBLX_HYBRID.mountCard();KBLX_HYBRID.drawRows();},250);
 },true);
 if(typeof dualLog==='function')dualLog('ESPELHO v24: hibrido no Brain · voz persistente · reconhecimento estabilizado');
 console.log('[ESPELHO v24] conecta o que ja existe · VERDADE x INTEGRAR / D = INF');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,500);});
else setTimeout(boot,500);
})();
