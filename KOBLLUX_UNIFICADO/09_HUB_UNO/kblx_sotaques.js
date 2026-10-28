/* ⟦ KBLX·UNO · SOTAQUES ARQUETÍPICOS · 9 sotaques · 18 vozes · expandir ⟧ */
(function(){
'use strict';
if(window.KBLX_VOZ)return;
var NORM=function(s){return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();};
var MAP={
 atlas:{v:'Hans',s:'alemão',g:'m'},vitalis:{v:'Klaus',s:'alemão',g:'m'},genus:{v:'Friedrich',s:'alemão',g:'m'},
 kaion:{v:'Markus',s:'alemão',g:'m'},pulse:{v:'Carlos',s:'espanhol',g:'m'},solus:{v:'José',s:'espanhol',g:'m'},
 artemis:{v:'Pierre',s:'francês',g:'m'},azzira:{v:'Amélie',s:'francês',g:'f'},aion:{v:'William',s:'inglês',g:'m'},kaos:{v:'João',s:'lusitano',g:'m'},
 horus:{v:'João',s:'lusitano',g:'m'},ignyra:{v:'Giulia',s:'italiano',g:'f'},nova:{v:'Luciana',s:'nativo',g:'f'},
 serena:{v:'Luciana',s:'nativo',g:'f'},lumine:{v:'Luciana',s:'nativo',g:'f'},rhea:{v:'Luciana',s:'nativo',g:'f'},
 luxara:{v:'Luciana',s:'nativo',g:'f'},elysha:{v:'Luciana',s:'nativo',g:'f'},kobllux:{v:'Luciana',s:'nativo',g:'f'}};
function findVoice(arch){
 var p=MAP[NORM(arch)]||MAP.kobllux, vs=speechSynthesis.getVoices(); if(!vs.length)return null;
 var L=function(x){return NORM(x.lang).startsWith('pt');};
 var ex=vs.filter(function(v){return NORM(v.name)===NORM(p.v)&&L(v);})[0];
 var par=vs.filter(function(v){return NORM(v.name).indexOf(NORM(p.v))>=0&&L(v);})[0];
 var any=vs.filter(L)[0];
 return ex||par||any||vs[0];
}
function falar(arch,texto){
 try{
  var t=texto||('Olá, eu sou '+arch);
  var u=new SpeechSynthesisUtterance(t); var v=findVoice(arch);
  if(v){u.voice=v;u.lang=v.lang;}
  speechSynthesis.cancel(); speechSynthesis.speak(u);
  return v?v.name:null;
 }catch(e){return null;}
}
function mapa(){return Object.keys(MAP).map(function(k){return {arch:k,voz:MAP[k].v,sotaque:MAP[k].s,genero:MAP[k].g};});}
window.KBLX_VOZ={falar:falar,findVoice:findVoice,mapa:mapa,MAP:MAP};
/* ORB: fala o arquétipo com sotaque ao mudar (aditivo) */
if(!document.getElementById('appsWrap')){
 var lastArch=null;
 setInterval(function(){
  try{var a=localStorage.getItem('kblx:arquetipo:atual')||localStorage.getItem('kblx:uno:arch');
   if(a&&a!==lastArch){lastArch=a;falar(a);}}catch(e){}
 },2000);
}
console.log('[KBLX·UNO] 9 sotaques · 18 vozes arquetípicas ativos');
})();
