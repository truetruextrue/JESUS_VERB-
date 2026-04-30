// 0x02 · SymbolBar + Archetypes + Internal Frame
(function(){
  const ARCHETYPES=[{name:'kobllux',p:'#C9A84C',s:'#8B4513',a:'#F0C060',f:432},{name:'nova',p:'#00e5ff',s:'#0099cc',a:'#80f4ff',f:528},{name:'trinity',p:'#D4AF37',s:'#9a7a10',a:'#f0d060',f:639}];
  function applyArchetype(idx){
    const a=ARCHETYPES[(idx+ARCHETYPES.length)%ARCHETYPES.length];
    document.documentElement.style.setProperty('--kob-voice-primary',a.p);
    document.getElementById('hudStatus').textContent=a.name.toUpperCase();
    localStorage.setItem('kob_arch',a.name);
  }
  document.addEventListener('DOMContentLoaded',()=>{
    const wheel=document.getElementById('archWheel');
    ARCHETYPES.forEach((a,i)=>{const b=document.createElement('button');b.className='arch-chip';b.textContent=`${a.name} · ${a.f}Hz`;b.onclick=()=>applyArchetype(i);wheel.appendChild(b);});
    document.getElementById('btn-arch')?.addEventListener('click',()=>document.getElementById('arch-overlay').classList.toggle('open'));
    const saved=localStorage.getItem('kob_arch');
    const i=ARCHETYPES.findIndex(x=>x.name===saved); applyArchetype(i>=0?i:0);
  });
})();
