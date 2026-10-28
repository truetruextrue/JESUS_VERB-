/* bluevoice-1milhaum.js · BLLUE·VOICE 1MILHAUM · AKaTeX -> SSML -> Voz · frequencias verdadeiras */
(function(){
'use strict';
var HZ={atlas:432,nova:528,vitalis:396,pulse:528,artemis:417,serena:639,kaos:285,genus:741,lumine:852,
 solus:963,rhea:639,aion:432,kodux:528,bllue:528,jesus:777,kobllux:777,elysha:528,horus:777,ignyra:432,
 kaion:528,luxara:852,azzira:741};
var TONES={gold:{rate:1.2,pitch:1.2},madeira:{rate:.8,pitch:.9},blue:{rate:1.0,pitch:1.0}};
var VERBOS={nova:'Conte a historia como quem ilumina.',elysha:'Fale entre o dito e o nao-dito.',
 kaion:'Clareza e codigo.',artemis:'Vai direto.',pulse:'Bata junto.',lumine:'Nasca enquanto fala.',
 kaos:'Quebre.',serena:'Respira comigo.',genus:'Dar forma e amar.',rhea:'Segura o chao.',
 solus:'Menos e tudo.',aion:'Nada comeca — tudo continua.'};

function norm(s){return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();}
function parseAKaTeX(ritual){
 var out={archetype:null,attrs:{tone:'blue',fx:null},text:''};
 if(!ritual||typeof ritual!=='string')return out;
 var am=ritual.match(/text\/([A-Za-z0-9_]+)/)||ritual.match(/^([A-Za-z0-9_]+)\b/);
 if(am)out.archetype=am[1];
 var tm=ritual.match(/\/tone\/([a-zA-Z0-9_]+)/); if(tm)out.attrs.tone=tm[1];
 var attr=ritual.match(/attr\/\{([^}]+)\}/);
 if(attr)attr[1].split(',').forEach(function(kv){var p=kv.split(':');if(p[0]&&p[1])out.attrs[p[0].trim()]=p[1].trim();});
 if(ritual.indexOf('fx:369')>=0||ritual.indexOf('/fx/369')>=0)out.attrs.fx='369';
 var tx=ritual.match(/\/text\/([\s\S]+)$/);
 if(tx)out.text=tx[1].trim();
 var q=ritual.match(/"(.*?)"/); if(!out.text&&q)out.text=q[1];
 if(out.archetype)out.archetype=out.archetype.charAt(0).toUpperCase()+out.archetype.slice(1).toLowerCase();
 return out;}
function esc(x){return String(x||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function akatexToSSML(ritual){
 var p=parseAKaTeX(ritual);
 var tone=TONES[p.attrs.tone]||TONES.blue;
 var fx=p.attrs.fx==='369';
 var hz=HZ[norm(p.archetype)]||528;
 var brk=fx?'<break time="369ms"/> ':'';
 return {ssml:'<speak version="1.0" xml:lang="pt-BR"><voice name="'+norm(p.archetype)+'">'
  +'<prosody rate="'+Math.round(tone.rate*100)+'%" pitch="'+(fx?'+10%':'+0%')+'">'
  +brk+esc(p.text)+brk+'</prosody></voice></speak>',
  parsed:p,hz:hz,tone:p.attrs.tone,fx:fx};}
function playSonar(){try{if(typeof window==='undefined'||!window.AudioContext)return;
 var c=new (window.AudioContext||window.webkitAudioContext)(),o=c.createOscillator(),g=c.createGain();
 o.type='square';o.frequency.value=440;g.gain.value=.02;o.connect(g);g.connect(c.destination);o.start();
 setTimeout(function(){o.frequency.value=220;g.gain.value=.01;},80);
 setTimeout(function(){o.stop();c.close();},280);}catch(e){}}
/* voz persistente com as frequencias verdadeiras */
var q=[],sp=false,voice=null;
function pick(){var vs=speechSynthesis.getVoices().filter(function(v){return /^pt/i.test(v.lang);});return vs[0]||null;}
if(typeof window!=='undefined'&&'speechSynthesis' in window){
 speechSynthesis.onvoiceschanged=function(){voice=pick();};voice=pick();
 setInterval(function(){if(sp&&speechSynthesis.paused){try{speechSynthesis.resume();}catch(e){}}},300);
 document.addEventListener('visibilitychange',function(){if(document.hidden&&sp&&speechSynthesis.paused){try{speechSynthesis.resume();}catch(e){}}});}
function chunks(t){var p=String(t).replace(/\s+/g,' ').split(/([.!?;:])\s*/),o=[],c='';
 for(var i=0;i<p.length;i++){if((c+p[i]).length<180)c+=p[i];else{if(c)o.push(c);c=p[i];}}if(c)o.push(c);return o.filter(Boolean);}
function pump(){if(!q.length){sp=false;return;}sp=true;
 var job=q.shift(),u=new SpeechSynthesisUtterance(job.text);
 if(voice)u.voice=voice;
 var tone=TONES[job.tone]||TONES.blue, hz=job.hz||528;
 u.rate=Math.max(.6,Math.min(1.35, tone.rate*(528/hz)*0.92+0.08));
 u.pitch=Math.max(.5,Math.min(1.6, tone.pitch*(hz/528)));
 u.onend=function(){setTimeout(pump,job.fx?369:60);};
 u.onerror=function(){setTimeout(pump,60);};
 speechSynthesis.speak(u);}
function speakRitual(ritual,opts){
 if(typeof window==='undefined'||!('speechSynthesis' in window))return null;
 opts=opts||{};
 var pr=akatexToSSML(ritual);
 var texto=pr.parsed.text||VERBOS[norm(pr.parsed.archetype)]||'A voz vem.';
 if(opts.replace){q=[];sp=false;try{speechSynthesis.cancel();}catch(e){}}
 playSonar();
 q.push({text:texto,tone:pr.tone,hz:pr.hz,fx:pr.fx});
 if(!sp)pump();
 return {arquetipo:pr.parsed.archetype,hz:pr.hz,tone:pr.tone,fx:pr.fx,texto:texto};}
function invokeBlueVoice(raw,opts){
 var sig=String(raw||''),p=parseAKaTeX(sig);
 return {signature:sig,archetype:p.archetype||'default',result:speakRitual(sig,opts),ssml:akatexToSSML(sig).ssml};}
window.KBLX_BLUEVOICE={invoke:invokeBlueVoice,speak:speakRitual,parse:parseAKaTeX,toSSML:akatexToSSML,
 sonar:playSonar,HZ:HZ,VERBOS:VERBOS,
 evoca:function(arch,opts){ /* evocação curta: text/ARCH/.../frase verdadeira */
  var a=norm(arch);var frase=(opts&&opts.texto)||VERBOS[a]||('Eu sou '+arch+'.');
  return speakRitual('text/'+arch+'/attr/{tone:'+((a==='kaos'||a==='rhea'||a==='genus')?'madeira':(a==='lumine'||a==='nova'||a==='aion')?'gold':'blue')+', fx:369}/div/text/'+frase,opts);}};
/* ponte: KBLX_VOICE passa a entender rituais text/... */
if(window.KBLX_VOICE){var _s=window.KBLX_VOICE.speak;
 window.KBLX_VOICE.speak=function(text,opts){ if(typeof text==='string'&&/^text\//i.test(text.trim())){
   var r=window.KBLX_BLUEVOICE.speak(text,{replace:opts&&opts.replace}); if(r)return; } return _s(text,opts); };
 console.log('[BLLUE·VOICE] KBLX_VOICE conectado ao motor AKaTeX');}
console.log('[BLLUE·VOICE 1MILHAUM] '+Object.keys(HZ).length+' frequencias verdadeiras · tones gold/madeira/blue · fx:369');
})();
