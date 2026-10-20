/* VMS keynote deck: one idea per scene. The AI co-presenter drives it through SITE.show_section(). */

const ICONS = {
  target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
  users: '<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16.5 14.2A5 5 0 0 1 21 19.5"/>',
  shield: '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
  layers: '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
  cpu: '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/>',
  flex: '<path d="M4 12h16M8 8l-4 4 4 4M16 8l4 4-4 4"/>',
  headset: '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/><path d="M19 20c0 1.5-2 2-5 2"/>',
  file: '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
  search: '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
  support: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="M5.6 5.6l3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"/>',
  calc: '<rect x="5" y="3" width="14" height="18" rx="2.5"/><path d="M8 7h8v3H8zM8 14h.01M12 14h.01M16 14h.01M8 17.5h.01M12 17.5h.01M16 17.5h.01"/>',
  building: '<path d="M4 21V6l8-3 8 3v15"/><path d="M9 9h2M13 9h2M9 13h2M13 13h2M10 21v-4h4v4"/>',
  spark: '<path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>',
  phone: '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
  chat: '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
  scan: '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3M8 12h8"/>',
  route: '<circle cx="6" cy="5" r="2"/><circle cx="18" cy="19" r="2"/><path d="M8 5h6a3.5 3.5 0 0 1 0 7h-4a3.5 3.5 0 0 0 0 7h6"/>',
  chart: '<path d="M5 20V10M12 20V4M19 20v-7"/>',
  mail: '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 8l9 6 9-6"/>',
  pin: '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
  x: '<path d="M6 6l12 12M18 6L6 18"/>',
  check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
};
const icon = (name) => `<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICONS[name]}</svg>`;
const arrow = '<span class="arrow" aria-hidden="true">→</span>';

// The pain, in the words business owners use, paired with how VMS removes it.
const PAINS = [
  ['Hiring, training and attrition keep resetting your team.', 'A trained team is already running, and attrition is our job.'],
  ['Quality varies, and nobody can see why.', 'Agreed KPIs, speech analytics and compliance monitoring.'],
  ['Demand swings leave you over- or under-staffed.', 'Flexible seating that scales up for peaks and down again.'],
  ['Dialers, CRM and workspace are costly to build.', 'Workspace, dialers and CRM integrations already in place.'],
  ['Leads and renewals slip through the cracks.', 'One partner from first lead to renewal.'],
];

const WHY = [
  ['target', 'Result oriented', 'Built around the outcome you need: sales, renewals, resolutions.'],
  ['users', 'People expertise', 'Deep experience with attrition and staffing trends keeps teams steady.'],
  ['shield', 'Quality you can measure', 'Service levels and KPIs agreed upfront, then tracked.'],
  ['layers', 'Comprehensive services', 'Front office, back office and infrastructure from one partner.'],
  ['cpu', 'Strong technology', 'VoIP/SIP infrastructure, intelligent dialers, CRM integrations.'],
  ['flex', 'Flexibility', 'Flexible seating that scales for peaks and long-term growth.'],
];

const SERVICES = [
  ['headset', 'Contact center operations', 'Inbound and outbound teams for care, sales, lead generation, upsell and renewals.'],
  ['file', 'Back-office services', 'Data processing, merchant onboarding and document verification.'],
  ['search', 'Research & lead generation', 'Targeted B2B outreach, surveys and market intelligence.'],
  ['support', 'Technical support', 'Multi-tier helpdesk and software troubleshooting.'],
  ['calc', 'Finance & accounting', 'Payables, receivables, reconciliation, payroll and collections.'],
  ['building', 'Commercial infrastructure', 'Equipped workspace and flexible seating, ready to launch.'],
];

const CAPABILITIES = [
  ['spark', 'Agent assist', 'Live call guidance, script suggestions and knowledge lookup.'],
  ['phone', 'Intelligent dialers', 'Predictive and progressive dialing with answering-machine detection.'],
  ['chat', 'Voice & chat automation', 'Voicebots and chatbots for qualification, surveys and inquiries.'],
  ['scan', 'Document intelligence', 'AI-OCR for KYC, merchant onboarding and loan applications.'],
  ['route', 'Workflow orchestration', 'Predictive ticket routing and automated SLA tracking.'],
  ['chart', 'Speech & workforce insights', 'Sentiment, compliance and adherence analytics, plus staffing forecasts.'],
];

const STEPS = [
  ['Discover', 'Your goals, volumes, processes and what success looks like.'],
  ['Design', 'Team, technology, scripts, KPIs and reporting shaped around you.'],
  ['Pilot', 'Prove quality and value on one process before you scale.'],
  ['Scale', 'Add seats, channels and services as the results come in.'],
];

const INDUSTRIES = [
  ['E-commerce & marketplaces', 'Merchant acquisition, sales enablement, customer support and retention.'],
  ['Fintech & business lending', 'Business-loan sales, credit processing and onboarding.'],
  ['SaaS, payroll & HR tech', 'Renewals, upsell and customer success.'],
  ['Logistics & supply chain', 'Fleet-solution sales, onboarding and lead generation.'],
  ['Education & immigration', 'Applicant funnels, counselling support and documentation.'],
  ['BFSI', 'Customer, sales and process support for financial-services operations.'],
];

const CLIENTS = [
  ['IndiaMART', 'Inbound & outbound sales'],
  ['Alibaba.com', 'Sales, service, upsell & renewals'],
  ['PagarBook', 'Sales, renewals & retention'],
  ['Indifi Technologies', 'MSME business-loan sales'],
  ['WheelsEye', 'Logistics & fleet sales'],
  ['Busy', ''],
  ['Livekeeping', ''],
  ['CREW HRMS', ''],
  ['TOI', ''],
];

const FAQS = [
  ['Why outsource instead of hiring in-house?', 'Trained teams, seats, dialers and supervision are already running, so there is no fixed cost or hiring cycle.'],
  ['How do we keep control of quality?', 'KPIs and service levels are agreed upfront, conversations are monitored, and you get regular reporting.'],
  ['What does it cost?', 'It depends on process, volume and channels. Flexible seating means you pay for the capacity you need.'],
  ['How quickly can we start?', 'Workspace and technology are already running. The exact plan follows a short discovery call.'],
  ['Is our customer data safe?', 'Security and compliance requirements are agreed and built into the process before launch.'],
  ['Will AI replace our people?', 'No. AI supports people: it makes human teams faster and more consistent.'],
];


// Words that tell the deck which item Irfan is describing. The match follows his live speech, so the
// right card lights up as he says it, with no extra work from the AI.
const SPOT_KEYS = {
  challenge: [
    ['attrition', 'hiring', 'training', 'turnover', 'resetting'],
    ['quality', 'kpi', 'analytics', 'compliance', 'monitor', 'nobody can see'],
    ['demand', 'peaks', 'seasonal', 'seating', 'over- or under', 'overstaffed', 'understaffed'],
    ['dialer', 'crm', 'workspace', 'costly', 'infrastructure'],
    ['renewal', 'leads', 'slip', 'cracks', 'journey', 'one partner'],
  ],
  'why-vms': [
    ['result', 'outcome'],
    ['people', 'expertise', 'attrition', 'staffing'],
    ['quality', 'kpi', 'service level', 'measure'],
    ['comprehensive', 'front office', 'back office', 'one partner', 'end-to-end', 'end to end'],
    ['technology', 'voip', 'sip', 'crm', 'dialer'],
    ['flexib', 'seating', 'scale', 'peak'],
  ],
  services: [
    ['contact center', 'contact centre', 'inbound', 'outbound', 'calling', 'upsell'],
    ['back office', 'back-office', 'onboarding', 'verification', 'data processing'],
    ['research', 'lead generation', 'survey', 'b2b', 'outreach'],
    ['technical support', 'helpdesk', 'troubleshoot'],
    ['finance', 'accounting', 'payroll', 'reconciliation', 'collections', 'payable'],
    ['infrastructure', 'workspace', 'seating', 'ready to launch'],
  ],
  capabilities: [
    ['agent assist', 'script', 'live guidance', 'knowledge lookup'],
    ['dialer', 'predictive', 'progressive', 'answering machine', 'voicemail'],
    ['voicebot', 'chatbot', 'voice and chat', 'voice & chat', 'qualification'],
    ['document', 'ocr', 'kyc', 'loan application'],
    ['workflow', 'ticket', 'routing', 'sla'],
    ['speech', 'sentiment', 'forecast', 'workforce', 'adherence'],
  ],
  approach: [
    ['discover', 'first call', 'your goals'],
    ['design', 'kpis', 'scripts', 'shaped'],
    ['pilot', 'prove', 'proof', 'before you scale'],
    ['scale', 'add seats', 'grow'],
  ],
  industries: [
    ['e-commerce', 'ecommerce', 'marketplace', 'merchant'],
    ['fintech', 'lending', 'loan', 'credit'],
    ['saas', 'payroll', 'hr tech', 'subscription'],
    ['logistics', 'supply chain', 'fleet'],
    ['education', 'immigration', 'abroad', 'counselling'],
    ['bfsi', 'banking', 'insurance', 'financial services'],
  ],
  faq: [
    ['outsourc', 'in-house', 'in house', 'hiring'],
    ['quality', 'control', 'kpi', 'reporting'],
    ['cost', 'price', 'pricing', 'expensive', 'budget', 'afford'],
    ['quickly', 'how fast', 'launch', 'timeline', 'get started'],
    ['data', 'security', 'secure', 'privacy', 'safe'],
    ['replace', 'jobs', 'ai '],
  ],
};

// shade: "hero" darkens the text side, "even" darkens the whole frame for card-heavy scenes.
const SCENES = [
  { id: 'home', label: 'Welcome', video: '41541', shade: 'hero' },
  { id: 'challenge', label: 'The problem', video: '308', shade: 'even' },
  { id: 'company', label: 'About', video: '23064', shade: 'hero' },
  { id: 'why-vms', label: 'Why VMS', video: '4547', shade: 'even' },
  { id: 'services', label: 'Services', video: '914', shade: 'even' },
  { id: 'capabilities', label: 'AI', video: '12748', shade: 'even' },
  { id: 'approach', label: 'Approach', video: '42664', shade: 'even' },
  { id: 'industries', label: 'Industries', video: '42648', shade: 'even' },
  { id: 'clients', label: 'Clients', video: '22987', shade: 'even' },
  { id: 'faq', label: 'FAQ', video: '21401', shade: 'even' },
  { id: 'contact', label: 'Contact', video: '41541', shade: 'hero' },
];

const head = (n, eyebrow, title) => `
  <header class="head rv">
    <p class="eyebrow"><b>${n}</b>${eyebrow}</p>
    <h2>${title}</h2>
  </header>`;

const tile = ([ico, title, text]) => `
  <article class="glass tile rv spot">
    <span class="tile-ico">${icon(ico)}</span>
    <h3>${title}</h3>
    <p>${text}</p>
  </article>`;

const BODY = {
  home: () => `
    <div class="hero-copy">
      <p class="eyebrow rv"><i class="live-dot"></i>AI-enabled contact center & BPO · New Delhi</p>
      <h1 class="rv">Better conversations.<br /><em>Smarter operations.</em></h1>
      <p class="lede rv">We run the customer conversations and business processes that grow your revenue, with trained people, proven process and AI built in.</p>
      <div class="actions rv">
        <button class="cta" type="button" data-start>Start presentation ${arrow}</button>
        <span class="hint">Meet Irfan, our AI co-presenter</span>
      </div>
    </div>
    <div class="glass stat-bar rv">
      <div><strong data-count="10" data-suffix="+">10+</strong><small>Years of experience</small></div>
      <div><strong data-count="6">6</strong><small>Core service lines</small></div>
      <div><strong data-count="6" data-suffix="+">6+</strong><small>Industries served</small></div>
      <div><strong class="word">End-to-end</strong><small>From first lead to renewal</small></div>
    </div>`,

  challenge: () => `
    <div class="challenge">
      <div class="challenge-copy">
        ${head('01', 'The real problem', 'Growth stalls when<br /><em>operations<br />can’t keep up.</em>')}
        <p class="lede rv">Founders and leaders end up running hiring, dialers and follow-ups, instead of the business.</p>
        <p class="result rv"><i></i>The result: your leaders stay focused on growth while VMS runs the conversations.</p>
      </div>
      <div class="pains">
        ${PAINS.map(([pain, fix], i) => `
          <div class="glass pain-row rv spot" style="--n:${i}">
            <div class="pain"><span class="mark mark-x">${icon('x')}</span><p>${pain}</p></div>
            <div class="fix"><span class="mark mark-ok">${icon('check')}</span><p>${fix}</p></div>
          </div>`).join('')}
      </div>
    </div>`,

  company: () => `
    ${head('02', 'Who we are', 'We turn complex operations<br /><em>into better experiences.</em>')}
    <p class="lede rv">Vintaqe Management Solutions partners with growing businesses to run the conversations and processes that keep customers coming back, bringing people, process and technology together around your outcome.</p>
    <div class="flow rv" aria-label="Customer lifecycle we cover">
      <div class="flow-line"></div>
      ${['Lead generation', 'Sales', 'Onboarding', 'Customer care', 'Upsell', 'Renewals'].map((s, i) => `
        <div class="flow-node" style="--n:${i}"><span>${i + 1}</span><b>${s}</b></div>`).join('')}
    </div>`,

  'why-vms': () => `
    ${head('03', 'Why VMS', 'Six reasons businesses<br /><em>choose us.</em>')}
    <div class="grid g3">${WHY.map(tile).join('')}</div>`,

  services: () => `
    ${head('04', 'What we do', 'One partner.<br /><em>Every operation covered.</em>')}
    <div class="grid g3">${SERVICES.map(tile).join('')}</div>`,

  capabilities: () => `
    ${head('05', 'Technology in action', 'AI that supports the work.<br /><em>People who make it matter.</em>')}
    <div class="grid g3">${CAPABILITIES.map(tile).join('')}</div>`,

  approach: () => `
    ${head('06', 'How we start', 'From first call to full scale,<br /><em>in four steps.</em>')}
    <ol class="steps">
      <div class="steps-line"><i></i></div>
      ${STEPS.map(([t, d], i) => `
        <li class="glass step rv spot${i === 2 ? ' step-key' : ''}" style="--n:${i}">
          <span class="step-n">${i + 1}</span>
          <h3>${t}</h3>
          <p>${d}</p>
        </li>`).join('')}
    </ol>`,

  industries: () => `
    ${head('07', 'Where we work', 'Built for the<br /><em>real world of business.</em>')}
    <div class="bento">
      ${INDUSTRIES.map(([t, d], i) => `
        <article class="glass tile bento-${i + 1} rv spot">
          <span class="tile-no">0${i + 1}</span>
          <h3>${t}</h3>
          <p>${d}</p>
        </article>`).join('')}
    </div>
    <p class="also rv"><small>Also</small>Recruitment<i></i>Commercial renting<i></i>E-sports & gaming<i></i>Data analysis & survey</p>`,

  clients: () => `
    ${head('08', 'Experience', 'Trusted with work that<br /><em>moves business forward.</em>')}
    <div class="marquee rv">
      ${[0, 1].map((row) => `
        <div class="marquee-row${row ? ' reverse' : ''}">
          <div class="marquee-track">
            ${[...Array(2)].map(() => (row ? [...CLIENTS].reverse() : CLIENTS).map(([n, s]) => `
              <div class="glass chip"><strong>${n}</strong>${s ? `<small>${s}</small>` : ''}</div>`).join('')).join('')}
          </div>
        </div>`).join('')}
    </div>
    <p class="fine rv">Account names are reproduced from VMS company material.</p>`,

  faq: () => `
    ${head('09', 'Questions', 'Straight answers to<br /><em>the questions that matter.</em>')}
    <div class="grid g3 faq">
      ${FAQS.map(([q, a]) => `
        <article class="glass tile rv spot"><h3>${q}</h3><p>${a}</p></article>`).join('')}
    </div>`,

  contact: () => `
    <div class="contact-grid">
      <div>
        <p class="eyebrow rv"><b>10</b>Start a conversation</p>
        <h2 class="rv">Let’s build an operation<br />that <em>works for you.</em></h2>
        <p class="lede rv">A short discovery call, then a pilot that proves the value.</p>
        <div class="actions rv">
          <a class="cta" href="mailto:support@vmsolutions.co.in?subject=VMS%20discovery%20call">Book a discovery call ${arrow}</a>
        </div>
        <div class="contact-list">
          <a class="glass row rv" href="tel:+917011812696">${icon('phone')}<span><small>Call</small><b>+91 7011 81 2696</b></span></a>
          <a class="glass row rv" href="mailto:support@vmsolutions.co.in">${icon('mail')}<span><small>Email</small><b>support@vmsolutions.co.in</b></span></a>
          <a class="glass row rv" href="https://maps.google.com/?q=B-7+Shankar+Garden,+Vikaspuri,+New+Delhi+110018" target="_blank" rel="noreferrer">${icon('pin')}<span><small>Visit</small><b>B-7 Shankar Garden, Vikaspuri, New Delhi 110018</b></span></a>
        </div>
      </div>
      <div class="glass qr rv">
        <img src="/static/qr-whatsapp.svg" alt="QR code to start a WhatsApp chat with VMS" />
        <b>Scan to chat on WhatsApp</b>
        <small>+91 7011 81 2696</small>
      </div>
    </div>`,
};

const deck = document.getElementById('site');
deck.innerHTML = `
  <div class="progress"><i id="progress"></i></div>
  <a class="brand" href="#home" data-go="home" aria-label="VMSolutions home">
    <img src="/static/logo-light.png" alt="" />
    <span>VMS<small>olutions</small></span>
  </a>
  <nav class="dots glass" aria-label="Scenes">
    ${SCENES.map((s) => `<button type="button" data-go="${s.id}" aria-label="${s.label}"><span>${s.label}</span></button>`).join('')}
  </nav>
  <div class="counter" aria-hidden="true"><b id="cur">01</b><span>/ ${String(SCENES.length).padStart(2, '0')}</span></div>
  ${SCENES.map((s) => `
    <section class="scene shade-${s.shade}" id="${s.id}" data-label="${s.label}" aria-label="${s.label}">
      <div class="bg" aria-hidden="true">
        <video muted loop playsinline preload="none" poster="/static/media/${s.video}.jpg" data-src="/static/media/${s.video}.mp4"></video>
      </div>
      <div class="scene-inner">${BODY[s.id]()}</div>
    </section>`).join('')}
`;

const scenes = [...deck.querySelectorAll('.scene')];
const dots = [...deck.querySelectorAll('.dots button')];
const cur = document.getElementById('cur');
const bar = document.getElementById('progress');
const leaving = new Map();
let index = 0;

scenes.forEach((scene) => scene.querySelectorAll('.rv').forEach((el, i) => el.style.setProperty('--i', i)));

function countUp(scene) {
  scene.querySelectorAll('[data-count]').forEach((el) => {
    const to = Number(el.dataset.count);
    const suffix = el.dataset.suffix ?? '';
    const start = performance.now() + 450;
    const tick = (now) => {
      const t = Math.min((now - start) / 1300, 1);
      if (t >= 0) el.textContent = Math.round(to * (1 - Math.pow(1 - t, 3))) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    };
    el.textContent = '0' + suffix;
    requestAnimationFrame(tick);
  });
}

// Load a scene's footage ahead of time so the next transition never shows a black frame.
function warm(i) {
  const v = scenes[i]?.querySelector('video');
  if (v && !v.src) { v.src = v.dataset.src; v.preload = 'auto'; v.load(); }
}

function go(target, { silent } = {}) {
  const next = typeof target === 'number' ? target : scenes.findIndex((s) => s.id === target);
  if (next < 0 || next >= scenes.length) return;
  const prev = scenes[index];
  const incoming = scenes[next];
  if (!silent && next === index) return;

  index = next;
  clearSpot();
  if (prev !== incoming) {
    // Keep the outgoing scene fully drawn while it fades, so content never vanishes mid-transition.
    prev.classList.remove('active');
    prev.classList.add('leaving');
    clearTimeout(leaving.get(prev));
    leaving.set(prev, setTimeout(() => {
      prev.classList.remove('leaving');
      prev.querySelector('video')?.pause();
    }, 750));
  }

  clearTimeout(leaving.get(incoming));
  incoming.classList.remove('leaving', 'active');
  void incoming.offsetWidth; // restart the entrance animations
  incoming.classList.add('active');
  warm(next);
  const iv = incoming.querySelector('video');
  iv.play().catch(() => {});
  countUp(incoming);
  warm(next + 1);

  dots.forEach((d, i) => d.classList.toggle('active', i === index));
  cur.textContent = String(index + 1).padStart(2, '0');
  bar.style.width = `${((index + 1) / scenes.length) * 100}%`;
  history.replaceState(null, '', `#${incoming.id}`);
}


// ---- Spotlight: follow Irfan's words ----
const escapeRe = (t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const SPOTS = new Map(scenes.map((scene) => {
  const keys = SPOT_KEYS[scene.id] ?? [];
  const items = [...scene.querySelectorAll('.spot')].map((el, i) => ({
    el,
    re: keys[i] ? new RegExp(`(?:^|[^a-z])(?:${keys[i].map(escapeRe).join('|')})`, 'gi') : null,
  }));
  return [scene.id, items];
}));

function clearSpot() {
  scenes.forEach((scene) => {
    scene.classList.remove('spotting');
    scene.querySelectorAll('.spot-on').forEach((el) => el.classList.remove('spot-on'));
  });
}

// Light up whichever item is mentioned last in the newest words Irfan has spoken.
function spotlight({ text }) {
  const scene = scenes[index];
  let best = null;
  let bestAt = -1;
  for (const item of SPOTS.get(scene.id) ?? []) {
    if (!item.re) continue;
    item.re.lastIndex = 0;
    let m;
    while ((m = item.re.exec(text))) if (m.index > bestAt) { best = item; bestAt = m.index; }
  }
  if (!best || best.el.classList.contains('spot-on')) return;
  clearSpot();
  scene.classList.add('spotting');
  best.el.classList.add('spot-on');
}

const SITE = {
  show_section({ section }) { go(section); },
  spotlight,
  clear_spot: clearSpot,
  next() { go(index + 1); },
  prev() { go(index - 1); },
};

deck.addEventListener('click', (e) => {
  const link = e.target.closest('[data-go]');
  if (!link) return;
  e.preventDefault();
  go(link.dataset.go);
});

document.addEventListener('keydown', (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); SITE.next(); }
  else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) { e.preventDefault(); SITE.prev(); }
  else if (e.key === 'Home') go(0);
  else if (e.key === 'End') go(scenes.length - 1);
});

go(Math.max(0, scenes.findIndex((s) => `#${s.id}` === location.hash)), { silent: true });
window.SITE = SITE;
