import { projects, skills } from './projects.js';

const $ = (selector) => document.querySelector(selector);
const params = new URLSearchParams(location.search);
const initialSelection = params.has('compare') ? params.get('compare').split(',').filter(id => projects.some(p => p.id === id)) : projects.map(p => p.id);
let selected = new Set(initialSelection);
let activeSkill = skills.includes(params.get('skill')) ? params.get('skill') : 'All work';
let view = params.get('view') === 'compare' ? 'compare' : 'projects';
let query = (params.get('q') || '').slice(0,200);
let activeProject = null;
const dialog = $('#case-dialog');

function saveState() {
  const state = new URLSearchParams();
  if (view === 'compare') state.set('view',view);
  if (activeSkill !== 'All work') state.set('skill',activeSkill);
  if (query) state.set('q',query);
  if (selected.size !== projects.length) state.set('compare',[...selected].join(','));
  if (activeProject) state.set('project',activeProject.id);
  const q = state.toString();
  history.replaceState(null,'',location.pathname + (q ? '?' + q : '') + location.hash);
}

function art(id) {
  const grid = '<defs><pattern id="grid-'+id+'" width="15" height="15" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".5" fill="#98b091" opacity=".5"/></pattern></defs><rect width="400" height="170" fill="url(#grid-'+id+')"/>';
  let drawing = '';
  if (id === 'notes') drawing = '<g fill="#f7fbf0" stroke="#73956c" stroke-width="1"><rect x="149" y="44" width="111" height="98" rx="4" transform="rotate(9 205 94)"/><rect x="136" y="39" width="111" height="98" rx="4" transform="rotate(-7 191 88)"/><rect x="141" y="36" width="112" height="99" rx="4"/></g><path d="M159 58h24M159 71h73M159 83h58M159 95h65M159 118h39" stroke="#90aa7f" stroke-width="3"/><path d="M209 51h26v13h-26z" fill="#cee1bd"/><g fill="#3d663f" font-family="monospace" font-size="10"><text x="61" y="88">{ patterns }</text><text x="285" y="117">/ docs</text></g><path d="M100 108h24M269 75h31" stroke="#799a69" stroke-dasharray="3 3"/>';
  if (id === 'governance') drawing = '<g stroke="#8da381" stroke-width="1.3" fill="none"><path d="M78 88h59M257 88h63M200 44V30M200 130v20"/><circle cx="74" cy="88" r="7"/><circle cx="325" cy="88" r="7"/><circle cx="200" cy="27" r="3"/><circle cx="200" cy="151" r="3"/></g><rect x="145" y="39" width="108" height="99" rx="7" fill="#eaf2e0" stroke="#819d72"/><path d="M199 57l26 10v21c0 18-26 30-26 30s-26-12-26-30V67z" fill="#c7dfb3" stroke="#42693a" stroke-width="1.5"/><path d="m186 86 9 9 17-19" stroke="#3a6837" stroke-width="3" fill="none"/><g font-family="monospace" font-size="8" fill="#56764a"><text x="51" y="113">RUN</text><text x="305" y="113">CHECK</text></g>';
  if (id === 'engine') drawing = '<g fill="none" stroke="#8ba980" stroke-width="1.3"><path d="M93 91h58M248 91h49"/><path d="m142 87 7 4-7 4m146-8 7 4-7 4"/></g><g fill="#eef5e6" stroke="#819c73"><rect x="41" y="65" width="57" height="53" rx="4"/><rect x="157" y="51" width="87" height="78" rx="6"/><rect x="303" y="64" width="59" height="55" rx="4"/></g><g fill="#d1e5bc" stroke="#6d905b"><ellipse cx="200" cy="78" rx="22" ry="8"/><path d="M178 78v24c0 11 44 11 44 0V78"/><path d="M178 89c0 11 44 11 44 0" fill="none"/></g><path d="M54 80h30M54 90h22M54 100h27" stroke="#8ba579" stroke-width="2"/><g fill="#648b50" font-family="monospace"><text x="315" y="98" font-size="19">&gt;_</text><text x="176" y="147" font-size="7">RETRIEVE</text></g>';
  return '<svg viewBox="0 0 400 170" aria-hidden="true">'+grid+drawing+'</svg>';
}

function tags(items) { return items.map(t => `<span class="tag">${t}</span>`).join(''); }
function matches(p) {
  const skillMatch = activeSkill === 'All work' || (p.evidence[activeSkill] && p.evidence[activeSkill][0] !== 'none');
  const haystack = [p.name,p.kind,p.summary,p.problem,p.solution,...p.technologies,...p.tags,p.strengths,...Object.values(p.evidence).map(v=>v[2])].join(' ').toLowerCase();
  return skillMatch && query.trim().toLowerCase().split(/\s+/).every(term => haystack.includes(term));
}

function renderFilters() {
  $('#filters').innerHTML = ['All work',...skills].map(s => {
    const count = s === 'All work' ? 3 : projects.filter(p=>p.evidence[s][0] !== 'none').length;
    return `<button class="filter" data-filter="${s}" aria-pressed="${activeSkill===s}">${s}<small>${String(count).padStart(2,'0')}</small></button>`;
  }).join('');
}

function card(p) {
  return `<article class="project-card" data-card="${p.id}" aria-labelledby="title-${p.id}">
    <div class="card-art"><span class="card-art-label">${p.kind}</span><span class="card-number">${p.number}</span>${art(p.id)}</div>
    <div class="card-body"><div class="card-kicker">${p.number} / ${p.id==='notes'?'KNOWLEDGE':p.id==='governance'?'CONTROL':'APPLICATION'}<span class="card-state">${p.cardState}</span></div>
    <h3 id="title-${p.id}">${p.name}</h3><p class="card-description">${p.summary}</p><div class="tags">${tags(p.tags)}</div><div class="card-stack">${p.stack}</div>
    <div class="card-bottom"><button class="case-button" data-project="${p.id}" aria-label="Read ${p.name} case study">Read case study <span>↗</span></button><label class="compare-check"><input type="checkbox" data-select="${p.id}" ${selected.has(p.id)?'checked':''} aria-label="Include ${p.name} in comparison">Compare</label></div></div></article>`;
}

function renderComparison(filtered) {
  const displayed = filtered.filter(p=>selected.has(p.id));
  const hiddenCount = selected.size-displayed.length;
  const hint = displayed.length > 1 ? 'Compare the evidence behind each strength.' : displayed.length === 1 ? 'One project shown. Add another or clear filters to compare.' : 'Choose projects from the cards, or restore all three.';
  let html = `<div class="compare-toolbar"><p>${hint}${hiddenCount ? ` ${hiddenCount} selected ${hiddenCount===1?'project is':'projects are'} hidden by filters.` : ''}</p><button class="text-button" id="compare-all">Restore all projects</button></div>`;
  if (displayed.length) {
    const row = (label,fn) => `<tr><th scope="row">${label}</th>${displayed.map(p=>`<td>${fn(p)}</td>`).join('')}</tr>`;
    html += `<div class="comparison-scroll" role="region" aria-label="Project comparison table; scroll horizontally on small screens" tabindex="0"><table class="comparison-table"><caption class="sr-only">Comparison of selected AI projects by evidence, technology, and current state</caption><thead><tr><th scope="col">PROJECT / EVIDENCE</th>${displayed.map(p=>`<th scope="col"><small>${p.number} / ${p.kind}</small>${p.name}<button class="remove-project" data-remove="${p.id}" aria-label="Remove ${p.name} from comparison">Remove ×</button></th>`).join('')}</tr></thead><tbody>`;
    html += row('Problem addressed',p=>p.problem);
    for(const s of skills) html += row(s,p=>{const [type,label,detail]=p.evidence[s];return `<span class="evidence-type"><i class="evidence-dot ${type}"></i>${label}</span>${detail}`;});
    html += row('Technologies',p=>tags(p.technologies));
    html += row('Current state',p=>`<strong>${p.state}</strong><br>${p.current}`);
    html += row('Scope & trade-offs',p=>p.tradeoff);
    html += row('Explore further',p=>`<button class="case-button" data-project="${p.id}">Case study ↗</button><div class="evidence-links"><a href="${p.repo}" target="_blank" rel="noopener noreferrer">Repository ↗</a></div>`);
    html += '</tbody></table></div><div class="compare-legend"><span><i class="evidence-dot"></i> Implemented in repository</span><span><i class="evidence-dot documented"></i> Documentation / tests</span><span><i class="evidence-dot none"></i> Not a core focus</span><em>Evidence categories, not skill ratings.</em></div>';
  }
  $('#comparison').innerHTML = html;
  return displayed.length;
}

function render() {
  renderFilters();
  const filtered = projects.filter(matches);
  $('#project-grid').innerHTML = filtered.map(card).join('');
  const comparedCount = renderComparison(filtered);
  $('#project-grid').hidden = view !== 'projects';
  $('#comparison').hidden = view !== 'compare';
  $('#empty-state').hidden = filtered.length > 0 || view === 'compare';
  $('.filter-row').hidden = false;
  const count = view === 'compare' ? comparedCount : filtered.length;
  $('#result-status').textContent = `${String(count).padStart(2,'0')} / 03 projects ${view==='compare'?'in comparison':'shown'}${activeSkill==='All work'?'':' · '+activeSkill}${query ? ' · Search active' : ''}`;
  $('#clear-filters').hidden = activeSkill === 'All work' && !query;
  $('#compare-count').textContent = selected.size;
  document.querySelectorAll('.view-switch button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.view===view));
  saveState();
}

function openProject(id) {
  const p = projects.find(p=>p.id===id);
  if(!p)return;
  activeProject = p;
  const next = projects[(projects.indexOf(p)+1)%projects.length];
  $('#case-index').textContent = `CASE STUDY ${p.number} / 03`;
  $('#case-content').innerHTML = `<article class="case-main"><div class="case-header"><div><div class="eyebrow">${p.kind}</div><h2 id="case-title">${p.name}</h2><p>${p.summary}</p></div><a class="button primary" href="${p.repo}" target="_blank" rel="noopener noreferrer">View repository <span>↗</span></a></div>
    <div class="case-tags">${tags(p.technologies)}</div><div class="case-facts"><div><h3>THE PROBLEM</h3><p>${p.problem}</p></div><div><h3>THE APPROACH</h3><p>${p.solution}</p></div></div>
    <div class="architecture"><div class="architecture-heading"><h3>${p.architectureLabel}</h3><span>SELECT A COMPONENT TO EXPLORE ↓</span></div><div class="arch-nodes" role="group" aria-label="Architecture components">${p.nodes.map((n,i)=>`<button class="arch-node" data-node="${i}" aria-pressed="${i===0}" aria-controls="arch-detail"><small>${String(i+1).padStart(2,'0')}</small>${n[0]}</button>`).join('')}</div><div class="arch-detail" id="arch-detail" aria-live="polite"><strong>${p.nodes[0][0]}.</strong> ${p.nodes[0][1]}</div><p>${p.architectureNote}</p></div>
    <div class="case-lower"><div><h3 class="case-subheading">CURRENT STATE</h3><p class="state-summary">${p.current}</p><ul>${p.implemented.map(s=>`<li>${s}</li>`).join('')}</ul><p class="scope-note">${p.tradeoff}</p></div><div><h3 class="case-subheading">WHAT THIS DEMONSTRATES</h3><p class="state-summary">${p.strengths}</p><h3 class="case-subheading" style="margin-top:23px">GO TO THE SOURCE</h3><p class="state-summary">Explore the implementation and design decisions in the repository.</p><div class="evidence-links">${p.links.map(([label,path])=>`<a href="${p.repo+path}" target="_blank" rel="noopener noreferrer">${label} ↗</a>`).join('')}</div></div></div>
    <div class="case-source"><span>Source reviewed: 25 Sep 2026 · Repository tests not rerun for this case study.</span><button class="case-next" data-project="${next.id}">Next: ${next.short} →</button></div></article>`;
  if(!dialog.open) { dialog.showModal(); document.body.classList.add('ai-case-open'); }
  dialog.scrollTop=0;
  $('.close-dialog').focus({preventScroll:true});
  saveState();
}

function resetFilters() { activeSkill='All work';query='';$('#project-search').value='';render(); }

document.addEventListener('click',e=>{
  const project = e.target.closest('[data-project]');
  if(project) return openProject(project.dataset.project);
  const filter = e.target.closest('[data-filter]');
  if(filter) { activeSkill=filter.dataset.filter;render(); document.querySelector(`[data-filter="${activeSkill}"]`).focus({preventScroll:true});return; }
  const switcher = e.target.closest('[data-view]');
  if(switcher) { view=switcher.dataset.view;render();if(switcher.classList.contains('nav-compare'))$('#explorer').scrollIntoView();return; }
  const remove = e.target.closest('[data-remove]');
  if(remove) { selected.delete(remove.dataset.remove);render();$('#compare-all').focus({preventScroll:true});return; }
  const node = e.target.closest('[data-node]');
  if(node && activeProject) {
    document.querySelectorAll('[data-node]').forEach(n=>n.setAttribute('aria-pressed',n===node));
    const info=activeProject.nodes[Number(node.dataset.node)];
    $('#arch-detail').innerHTML=`<strong>${info[0]}.</strong> ${info[1]}`;
  }
  if(e.target.closest('#compare-all')) { selected=new Set(projects.map(p=>p.id));resetFilters(); }
});
document.addEventListener('change',e=>{
  if(e.target.matches('[data-select]')) {const id=e.target.dataset.select; e.target.checked?selected.add(id):selected.delete(id);render();document.querySelector(`[data-select="${id}"]`)?.focus({preventScroll:true});}
});
$('#project-search').value=query;
$('#project-search').addEventListener('input',e=>{query=e.target.value.slice(0,200);render();});
$('#clear-filters').addEventListener('click',()=>{resetFilters();$('#project-search').focus({preventScroll:true});});
$('#reset-empty').addEventListener('click',()=>{resetFilters();$('#project-search').focus({preventScroll:true});});
$('.close-dialog').addEventListener('click',()=>dialog.close());
dialog.addEventListener('keydown',e=>{
  if(e.key!=='Tab')return;
  const focusable=[...dialog.querySelectorAll('button:not(:disabled),a[href],input:not(:disabled),[tabindex="0"]')].filter(el=>el.getClientRects().length);
  const first=focusable[0],last=focusable[focusable.length-1];
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
  else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
});
dialog.addEventListener('close',()=>{activeProject=null;document.body.classList.remove('ai-case-open');saveState();});
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
render();
if(params.has('project'))openProject(params.get('project'));
