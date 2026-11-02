(()=>{'use strict';
const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('.main-nav');
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
// Reset the mobile menu after browser history restores a cached page.
window.addEventListener('pageshow',()=>{nav?.classList.remove('open');menu?.setAttribute('aria-expanded','false')});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');menu?.setAttribute('aria-expanded','false');menu?.focus()}});
const pages=[...document.querySelectorAll('[data-route]')];
function route(){if(!pages.length)return;const fragment=location.hash.slice(1);if(fragment==='top'||fragment==='content'){const target=document.getElementById(fragment);target?.setAttribute('tabindex','-1');target?.focus();target?.scrollIntoView();return}let id=fragment.split('/')[0]||document.body.dataset.startRoute||'home';if(!pages.some(p=>p.dataset.route===id))id='home';pages.forEach(p=>p.hidden=p.dataset.route!==id);document.querySelectorAll('[data-nav]').forEach(a=>{if(a.dataset.nav===id)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});nav?.classList.remove('open');menu?.setAttribute('aria-expanded','false');const active=pages.find(p=>p.dataset.route===id);document.title=active.querySelector('h1').textContent+' · Alek’s Birdhouse Project';window.scrollTo(0,0);active.setAttribute('tabindex','-1');active.focus({preventScroll:true});const anchor=fragment.split('/')[1];if(anchor)document.getElementById(anchor)?.scrollIntoView()}
window.addEventListener('hashchange',route);route();
function updateExpand(){const steps=[...document.querySelectorAll('.step')];const b=document.querySelector('[data-expand]');if(b)b.textContent=steps.every(s=>s.open)?'Close all steps':'Open all steps'}
document.querySelector('[data-expand]')?.addEventListener('click',()=>{const steps=[...document.querySelectorAll('.step')];const open=steps.some(s=>!s.open);steps.forEach(s=>s.open=open);updateExpand()});document.querySelectorAll('.step').forEach(s=>s.addEventListener('toggle',updateExpand));
})();
