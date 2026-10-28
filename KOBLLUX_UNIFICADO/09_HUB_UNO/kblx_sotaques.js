/* ⟦ KBLX·UNO · SOTAQUES ARQUETÍPICOS · perfis canônicos + vozes locais ⟧ */
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
 kodux:{v:'Luciana',s:'nativo',g:'f'},bllue:{v:'Luciana',s:'nativo',g:'f'},jesus:{v:'Luciana',s:'nativo',g:'f'},
 luxara:{v:'Luciana',s:'nativo',g:'f'},elysha:{v:'Luciana',s:'nativo',g:'f'},kobllux:{v:'Luciana',s:'nativo',g:'f'}};
function findVoice(arch){
 var p=MAP[NORM(arch)]||MAP.kobllux;
 var synth=window.speechSynthesis;
 if(!synth)return null;
 var vs=synth.getVoices(); if(!vs.length)return null;
 var L=function(x){return NORM(x.lang).startsWith('pt');};
 var savedName='';
 try{
  var saved=JSON.parse(window.localStorage.getItem('infodose:voices')||'{}');
  Object.keys(saved||{}).some(function(name){
   if(NORM(name)===NORM(arch)&&typeof saved[name]==='string'){savedName=saved[name];return true;}
   return false;
  });
 }catch(e){
  if(window.console&&typeof window.console.error==='function')window.console.error('KBLX Voz: não foi possível ler a preferência de voz salva.',e);
 }
 var custom=savedName&&vs.filter(function(v){return v.name===savedName;})[0];
 var ex=vs.filter(function(v){return NORM(v.name)===NORM(p.v)&&L(v);})[0];
 var par=vs.filter(function(v){return NORM(v.name).indexOf(NORM(p.v))>=0&&L(v);})[0];
 var any=vs.filter(L)[0];
 return custom||ex||par||any||vs[0];
}
function canonicalProfile(arch){
 if(!window.KBLX_ORBE||typeof window.KBLX_ORBE.profiles!=='function')return null;
 return window.KBLX_ORBE.profiles().filter(function(profile){
  return NORM(profile.name)===NORM(arch);
 })[0]||null;
}
var last=null;
function falar(arch,texto){
 try{
  var synth=window.speechSynthesis;
  if(!synth||typeof window.SpeechSynthesisUtterance!=='function')return null;
  var t=texto||('Olá, eu sou '+arch);
  var u=new window.SpeechSynthesisUtterance(t); var v=findVoice(arch);
  if(v){u.voice=v;u.lang=v.lang;}
  var profile=canonicalProfile(arch);
  last={
   archetype:profile?profile.name:String(arch||'Kobllux'),
   hz:profile?profile.hz:null,
   opcode:profile?profile.opcode:null,
   voice:v?v.name:null,
   accent:(MAP[NORM(arch)]||MAP.kobllux).s
  };
  synth.cancel(); synth.speak(u);
  return v?v.name:'voz padrão do navegador';
 }catch(e){
  if(window.console&&typeof window.console.error==='function')window.console.error('KBLX Voz: não foi possível sintetizar a fala.',e);
  return null;
 }
}
function mapa(){return Object.keys(MAP).map(function(k){return {arch:k,voz:MAP[k].v,sotaque:MAP[k].s,genero:MAP[k].g};});}
window.KBLX_VOZ={falar:falar,findVoice:findVoice,mapa:mapa,MAP:MAP,last:function(){return last;}};
/* ORB: fala o arquétipo com sotaque ao mudar (aditivo) */
if(!document.getElementById('appsWrap')){
 var lastArch=null;
 setInterval(function(){
  try{var a=localStorage.getItem('kblx:arquetipo:atual')||localStorage.getItem('kblx:uno:arch');
   if(a&&a!==lastArch){lastArch=a;falar(a);}}catch(e){}
 },2000);
}
console.log('[KBLX·UNO] Mapeamento de sotaques ligado aos perfis canônicos; vozes dependem do navegador.');
})();
