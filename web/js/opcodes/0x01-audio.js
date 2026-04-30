// 0x01 · Audio/TTS/Player
(function(){
  window.speakRealEmotion = async function(text){
    try { console.log('TTS', text?.slice(0,80)); } catch(e) {}
  };
  document.addEventListener('DOMContentLoaded',()=>{
    const player=document.getElementById('koblluxPlayer');
    if(player) player.innerHTML='<button id="togglePlayer">≋</button><div id="playerControls" style="display:none">Módulo de áudio carregado (0x01)</div>';
    document.getElementById('togglePlayer')?.addEventListener('click',()=>{
      const c=document.getElementById('playerControls');
      c.style.display=c.style.display==='none'?'block':'none';
    });
  });
})();
