// 0x00 · Core Chat + Theme + Boot
window.applyThemeSelector = function(val){
  const body=document.body;
  body.classList.remove('light','medium','vibe','dark','cyberpunk','anime');
  if(val!=='dark') body.classList.add(val);
  localStorage.setItem('infodoseTheme',val);
};
(function(){
  const savedTheme=localStorage.getItem('infodoseTheme')||'dark';
  window.applyThemeSelector(savedTheme);
  document.addEventListener('DOMContentLoaded',()=>{
    if(typeof particlesJS!=='undefined') particlesJS('particles-js',{particles:{number:{value:40},size:{value:2.4},move:{enable:true,speed:1.5}},retina_detect:true});
    const boot=document.getElementById('bootText'); if(boot) boot.textContent=boot.dataset.text||'';
    document.getElementById('themeToggle')?.addEventListener('click',()=>{
      const o=['dark','light','medium','vibe'];
      const c=localStorage.getItem('infodoseTheme')||'dark';
      const n=o[(o.indexOf(c)+1)%o.length];
      window.applyThemeSelector(n);
    });
  });
})();
