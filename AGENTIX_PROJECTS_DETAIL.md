# AI Agentix — Project Knowledge Base

> **Purpose.** This is the single source of truth for the AI Agentix voice agent. It describes everything AI Agentix has built or is building: products, client platforms, websites, CRMs, automations, concept sites and delivery infrastructure. The agent uses it to explain each project, answer detailed questions, compare products, recommend the right solution, and open the right link.
>
> **Compiled:** 2026-10-29, from the local source repositories, project documentation and the live public pages. No production app was logged into, so login-protected screens are described from source code and docs.

---

## How the voice agent should use this document

1. **Start with the short answer.** Every project has a **Spoken introduction** (2–4 sentences written to be said aloud) and a **Quick overview**. Use these first. Only go into **Features**, **Key workflows**, **User roles** or **Technical architecture** when the visitor asks for detail.
2. **Say only what is verified.** Each project and feature group carries a label:
   - **Verified**: confirmed in source code, the live public page or reliable project documentation.
   - **Partially verified**: partly confirmed; the details may be incomplete.
   - **Unverified**: no evidence; don't present it as fact.
   - **Unavailable**: the resource couldn't be accessed.

   Present planned items (under **Planned / in progress**) as plans, never as live features.
3. **Never invent numbers.** Don't promise revenue growth, speed-ups or guaranteed results. Prices are quoted only where the project's own public page states them.
4. **Use the right link, safely.**
   - **Safe demo (fictional data, actions simulated):** the AI Agentix portfolio, at `https://agentix-portfolio.vercel.app/` (planned hosted address). A project opens at `https://agentix-portfolio.vercel.app/#/demo/<slug>`. Tabs are `/overview`, `/walkthrough`, `/how`, `/screens` and `/tech`. A specific module opens at `/#/demo/<slug>/walkthrough/<moduleId>`. Prefer these links when a visitor wants to *see* a product.
   - **Safe demo deployment:** `https://redux-demo-iota.vercel.app/` runs on demo data.
   - **Public marketing sites:** fine to open and show.
   - **Production / login-protected apps:** real businesses' live systems. You may share the public URL, but **never perform actions** on them (no sign-ups, bookings, messages, payments or form submissions) to demonstrate a feature. Don't ask visitors for credentials, and never share any.
5. **Protect privacy.** This document contains no real customer, patient, member, guest or employee data, and no passwords, API keys or tokens. Example names (e.g. "Aarav Rao", "Riverside Dental Clinic") are fictional. Integrations are described conceptually; the actual credentials live in server environment variables that the agent never sees.
6. **When unsure, say so** and offer the portfolio demo or a call with the AI Agentix team (https://ai-agentix.com/contact).

---

## About AI Agentix (company overview)

**Spoken introduction:** "AI Agentix is an Indian AI and software studio. We build AI agents that talk to customers on WhatsApp, Instagram and voice; CRMs and operations platforms for hospitals, hotels, gyms and manufacturers; content automation for social media and YouTube; and premium websites and online stores. Our tagline is *AI Applied, Growth Multiplied.*"

**What we build:** these are the categories used throughout this document.

| Area | What it covers | Example projects |
|---|---|---|
| AI conversational agents | AI that answers, qualifies and books on WhatsApp, Instagram and voice; shared inbox and CRM | AGENTiX, SocialFlow, VoiceCRM, Riya |
| Content & social automation | Scheduling and publishing to many platforms; AI video creation and publishing | SocialPush, YT-Automation |
| CRM, sales & lead intelligence | Agency OS, manufacturer CRM with quotations and dealers, AI lead research, prototype CRMs | Agentix CRM, Eurobrass CRM, LeadForge, Santure AI CRM, Ekatva |
| Healthcare systems | Hospital information systems (OPD to IPD, government cockpits), hospital website + CMS | Agentix HIMS, Umang Hospital HIMS, Umang website |
| Hospitality | Property management for serviced apartments; resort booking platform | Woodpecker PMS, Kaaya Eco Resort |
| Fitness | Gym CRM with WhatsApp reminders and face check-in; gym websites | Max Register, Max Fitness website, Fitness First Dwarka |
| Multi-product business platforms | Several connected apps (site, CRM, portals, mobile) for one business | REDUX, Your Hair Company, Skinwise, NRI Trust |
| Business websites | Corporate and professional sites, some with admin panels | AI Agentix site, Dr. Shweta Diwan, Thames Wellness Spa, Eurobrass site |
| E-commerce & immersive concept sites | Showcase brand sites for fictional brands, demonstrating motion, 3D and storefront craft | 20 concept brands (Aurelle, Kanak, Meridian, Cairnline …) |
| Infrastructure & delivery | Docker/Coolify VPS, Vercel, cPanel/Apache, Supabase; showcase build pipeline | delivery-infra, showcase-pipeline |

**Contact / next step:** https://ai-agentix.com/ (corporate site) · https://ai-agentix.com/contact

## Master project index

49 projects. Status values come from the portfolio inventory; the live-site type (production, public site or demo) is in each project's **Links & access** table.

| Project | Slug | Category | Status | Live URL | Portfolio demo (safe, fictional data) |
|---|---|---|---|---|---|
| [AGENTiX](#agentix) | `agentix` | AI Conversational Agents | Live | <https://app.aiagentixdev.com/> | <https://agentix-portfolio.vercel.app/#/demo/agentix> |
| [SocialFlow](#socialflow) | `socialflow` | AI Conversational Agents | Live | <https://social-media.aiagentixdev.com/> | <https://agentix-portfolio.vercel.app/#/demo/socialflow> |
| [VoiceCRM](#voicecrm) | `voicecrm` | AI Conversational Agents | Prototype | <https://voice-crm-snowy.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/voicecrm> |
| [Riya, Fitness First WhatsApp CRM](#riya-fitness-first-whatsapp-crm) | `riya-crm` | AI Conversational Agents | Prototype | — | <https://agentix-portfolio.vercel.app/#/demo/riya-crm> |
| [SocialPush](#socialpush) | `socialpush` | Content & Social Automation | In development | — | <https://agentix-portfolio.vercel.app/#/demo/socialpush> |
| [YT-Automation](#yt-automation) | `yt-automation` | Content & Social Automation | Live | <https://yt-automation.aiagentixdev.com/> | <https://agentix-portfolio.vercel.app/#/demo/yt-automation> |
| [Agentix CRM](#agentix-crm) | `agentix-crm` | CRM, Sales & Lead Intelligence | Live | — | <https://agentix-portfolio.vercel.app/#/demo/agentix-crm> |
| [Eurobrass CRM](#eurobrass-crm) | `eurobrass-crm` | CRM, Sales & Lead Intelligence | In development | <https://eurobrass-seven.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/eurobrass-crm> |
| [LeadForge](#leadforge) | `leadforge` | CRM, Sales & Lead Intelligence | In development | — | <https://agentix-portfolio.vercel.app/#/demo/leadforge> |
| [Santure AI CRM](#santure-ai-crm) | `santure-crm` | CRM, Sales & Lead Intelligence | Prototype | <https://claude.ai/artifact/1aWGMS5ETqSCp4f1SV5JLD> | <https://agentix-portfolio.vercel.app/#/demo/santure-crm> |
| [Ekatva](#ekatva) | `ekatva` | CRM, Sales & Lead Intelligence | Prototype | <https://claude.ai/artifact/SPtLCBo9RcGfjE1FMAdwiw> | <https://agentix-portfolio.vercel.app/#/demo/ekatva> |
| [Agentix HIMS](#agentix-hims) | `agentix-hims` | Healthcare Systems | Prototype | <https://government-hims.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/agentix-hims> |
| [Umang Hospital HIMS](#umang-hospital-hims) | `umang-hims` | Healthcare Systems | Prototype | <https://umang-hospital-hims.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/umang-hims> |
| [Umang Hospital website + admin CMS](#umang-hospital-website--admin-cms) | `umang-website` | Healthcare Systems | Live | <https://www.umanghospitals.in/> | <https://agentix-portfolio.vercel.app/#/demo/umang-website> |
| [Woodpecker PMS](#woodpecker-pms) | `woodpecker-pms` | Hospitality | Live | <https://hotelmanagement.aiagentixdev.com/portal> | <https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms> |
| [Kaaya Eco Resort](#kaaya-eco-resort) | `kaaya-eco-resort` | Hospitality | Live | <https://kaayaecoresort.com/> | <https://agentix-portfolio.vercel.app/#/demo/kaaya-eco-resort> |
| [Max Register (Max Fitness gym CRM, kiosk and worker)](#max-register-max-fitness-gym-crm-kiosk-and-worker) | `max-register` | Fitness | Live | <https://maxfitnessgym.co.in/crm> | <https://agentix-portfolio.vercel.app/#/demo/max-register> |
| [Max Fitness website](#max-fitness-website) | `max-website` | Fitness | Live | <https://maxfitnessgym.co.in/> | <https://agentix-portfolio.vercel.app/#/demo/max-website> |
| [Fitness First Dwarka website](#fitness-first-dwarka-website) | `fitness-first` | Fitness | Live | <https://fitnessfirstdwarka.com/> | <https://agentix-portfolio.vercel.app/#/demo/fitness-first> |
| [REDUX Platform (by Eurobrass)](#redux-platform-by-eurobrass) | `redux` | Multi-Product Business Platforms | In development | <https://redux-demo-iota.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/redux> |
| [Your Hair Company (YHC)](#your-hair-company-yhc) | `yhc` | Multi-Product Business Platforms | In development | <https://yourhaircompany.com/> | <https://agentix-portfolio.vercel.app/#/demo/yhc> |
| [Skinwise](#skinwise) | `skinwise` | Multi-Product Business Platforms | Live | <https://myskinwise.com/> | <https://agentix-portfolio.vercel.app/#/demo/skinwise> |
| [NRI Trust](#nri-trust) | `nri-trust` | Multi-Product Business Platforms | Live | <https://nritrust.co/> | <https://agentix-portfolio.vercel.app/#/demo/nri-trust> |
| [AI Agentix corporate website](#ai-agentix-corporate-website) | `ai-agentix-site` | Business Websites | Live | <https://ai-agentix.com/> | <https://agentix-portfolio.vercel.app/#/demo/ai-agentix-site> |
| [Dr. Shweta Diwan website and PHP admin](#dr-shweta-diwan-website-and-php-admin) | `dr-shweta-diwan` | Business Websites | Live | <https://drshwetadiwan.com/> | <https://agentix-portfolio.vercel.app/#/demo/dr-shweta-diwan> |
| [Thames Wellness Spa](#thames-wellness-spa) | `thames-spa` | Business Websites | Live | <https://thameswellnessspa.com/> | <https://agentix-portfolio.vercel.app/#/demo/thames-spa> |
| [Eurobrass corporate site](#eurobrass-corporate-site) | `eurobrass-site` | Business Websites | Live | <https://eurobrass-seven.vercel.app/> | <https://agentix-portfolio.vercel.app/#/demo/eurobrass-site> |
| [Fruitivo (perfume)](#fruitivo-perfume) | `fruitivo` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/perfume/> | <https://agentix-portfolio.vercel.app/#/demo/fruitivo> |
| [DRIFY (streetwear)](#drify-streetwear) | `drify` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/drift/> | <https://agentix-portfolio.vercel.app/#/demo/drify> |
| [Movade (travel)](#movade-travel) | `movade` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/travel/> | <https://agentix-portfolio.vercel.app/#/demo/movade> |
| [AURELLE (sarees)](#aurelle-sarees) | `aurelle` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/aurelle/> | <https://agentix-portfolio.vercel.app/#/demo/aurelle> |
| [VARA Studio (fashion)](#vara-studio-fashion) | `vara` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/vara/> | <https://agentix-portfolio.vercel.app/#/demo/vara> |
| [Kanak Jewels](#kanak-jewels) | `kanak` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/kanak/> | <https://agentix-portfolio.vercel.app/#/demo/kanak> |
| [Meridian (watches)](#meridian-watches) | `meridian` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/meridian/> | <https://agentix-portfolio.vercel.app/#/demo/meridian> |
| [Dewlab (skincare)](#dewlab-skincare) | `dewlab` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/dewlab/> | <https://agentix-portfolio.vercel.app/#/demo/dewlab> |
| [Melt Theory (ice cream)](#melt-theory-ice-cream) | `melt` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/melt/> | <https://agentix-portfolio.vercel.app/#/demo/melt> |
| [Zip EV (e-scooter)](#zip-ev-e-scooter) | `zipev` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/zipev/> | <https://agentix-portfolio.vercel.app/#/demo/zipev> |
| [Crumb & Co (bakery)](#crumb--co-bakery) | `crumb` | E-commerce Experiences (concept brands) | Concept | <https://showcase-build-tau.vercel.app/crumb/> | <https://agentix-portfolio.vercel.app/#/demo/crumb> |
| [Cairnline Treks](#cairnline-treks) | `cairnline` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/cairnline/> | <https://agentix-portfolio.vercel.app/#/demo/cairnline> |
| [Saffron & Smoke](#saffron--smoke) | `saffron` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/saffron/> | <https://agentix-portfolio.vercel.app/#/demo/saffron> |
| [Aurelune Residences](#aurelune-residences) | `aurelune` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/aurelune/> | <https://agentix-portfolio.vercel.app/#/demo/aurelune> |
| [Halden (smartphone launch)](#halden-smartphone-launch) | `halden` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/halden/> | <https://agentix-portfolio.vercel.app/#/demo/halden> |
| [Iron Temple](#iron-temple) | `irontemple` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/irontemple/> | <https://agentix-portfolio.vercel.app/#/demo/irontemple> |
| [Marigold Noir](#marigold-noir) | `marigold` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/marigold/> | <https://agentix-portfolio.vercel.app/#/demo/marigold> |
| [Coral Bay](#coral-bay) | `coralbay` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/coralbay/> | <https://agentix-portfolio.vercel.app/#/demo/coralbay> |
| [Tallow & Tape](#tallow--tape) | `tallow-tape` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/tallow/> | <https://agentix-portfolio.vercel.app/#/demo/tallow-tape> |
| [Vaskaro](#vaskaro) | `vaskaro` | Immersive Brand Websites (concept brands) | Concept | <https://showcase-build-tau.vercel.app/vaskaro/> | <https://agentix-portfolio.vercel.app/#/demo/vaskaro> |
| [Deployment and hosting capabilities (delivery-infra)](#deployment-and-hosting-capabilities-delivery-infra) | `delivery-infra` | Infrastructure & Delivery | Live | — | <https://agentix-portfolio.vercel.app/#/demo/delivery-infra> |
| [Showcase pipeline (showcase-pipeline)](#showcase-pipeline-showcase-pipeline) | `showcase-pipeline` | Infrastructure & Delivery | In development | — | <https://agentix-portfolio.vercel.app/#/demo/showcase-pipeline> |

## Table of contents

- [How the voice agent should use this document](#how-the-voice-agent-should-use-this-document)
- [About AI Agentix (company overview)](#about-ai-agentix-company-overview)
- [Master project index](#master-project-index)
- [AI Conversational Agents](#ai-conversational-agents)
  - [AGENTiX](#agentix)
  - [SocialFlow](#socialflow)
  - [VoiceCRM](#voicecrm)
  - [Riya, Fitness First WhatsApp CRM](#riya-fitness-first-whatsapp-crm)
- [Content & Social Automation](#content--social-automation)
  - [SocialPush](#socialpush)
  - [YT-Automation](#yt-automation)
- [CRM, Sales & Lead Intelligence](#crm-sales--lead-intelligence)
  - [Agentix CRM](#agentix-crm)
  - [Eurobrass CRM](#eurobrass-crm)
  - [LeadForge](#leadforge)
  - [Santure AI CRM](#santure-ai-crm)
  - [Ekatva](#ekatva)
- [Healthcare Systems](#healthcare-systems)
  - [Agentix HIMS](#agentix-hims)
  - [Umang Hospital HIMS](#umang-hospital-hims)
  - [Umang Hospital website + admin CMS](#umang-hospital-website--admin-cms)
- [Hospitality](#hospitality)
  - [Woodpecker PMS](#woodpecker-pms)
  - [Kaaya Eco Resort](#kaaya-eco-resort)
- [Fitness](#fitness)
  - [Max Register (Max Fitness gym CRM, kiosk and worker)](#max-register-max-fitness-gym-crm-kiosk-and-worker)
  - [Max Fitness website](#max-fitness-website)
  - [Fitness First Dwarka website](#fitness-first-dwarka-website)
- [Multi-Product Business Platforms](#multi-product-business-platforms)
  - [REDUX Platform (by Eurobrass)](#redux-platform-by-eurobrass)
  - [Your Hair Company (YHC)](#your-hair-company-yhc)
  - [Skinwise](#skinwise)
  - [NRI Trust](#nri-trust)
- [Business Websites](#business-websites)
  - [AI Agentix corporate website](#ai-agentix-corporate-website)
  - [Dr. Shweta Diwan website and PHP admin](#dr-shweta-diwan-website-and-php-admin)
  - [Thames Wellness Spa](#thames-wellness-spa)
  - [Eurobrass corporate site](#eurobrass-corporate-site)
- [E-commerce Experiences (concept brands)](#e-commerce-experiences-concept-brands)
  - [Fruitivo (perfume)](#fruitivo-perfume)
  - [DRIFY (streetwear)](#drify-streetwear)
  - [Movade (travel)](#movade-travel)
  - [AURELLE (sarees)](#aurelle-sarees)
  - [VARA Studio (fashion)](#vara-studio-fashion)
  - [Kanak Jewels](#kanak-jewels)
  - [Meridian (watches)](#meridian-watches)
  - [Dewlab (skincare)](#dewlab-skincare)
  - [Melt Theory (ice cream)](#melt-theory-ice-cream)
  - [Zip EV (e-scooter)](#zip-ev-e-scooter)
  - [Crumb & Co (bakery)](#crumb--co-bakery)
- [Immersive Brand Websites (concept brands)](#immersive-brand-websites-concept-brands)
  - [Cairnline Treks](#cairnline-treks)
  - [Saffron & Smoke](#saffron--smoke)
  - [Aurelune Residences](#aurelune-residences)
  - [Halden (smartphone launch)](#halden-smartphone-launch)
  - [Iron Temple](#iron-temple)
  - [Marigold Noir](#marigold-noir)
  - [Coral Bay](#coral-bay)
  - [Tallow & Tape](#tallow--tape)
  - [Vaskaro](#vaskaro)
- [Infrastructure & Delivery](#infrastructure--delivery)
  - [Deployment and hosting capabilities (delivery-infra)](#deployment-and-hosting-capabilities-delivery-infra)
  - [Showcase pipeline (showcase-pipeline)](#showcase-pipeline-showcase-pipeline)
- [How AI Agentix builds](#how-ai-agentix-builds)
- [Cross-project intelligence](#cross-project-intelligence)
  - [Product families and ecosystems](#product-families-and-ecosystems)
  - [Comparison: AI messaging & CRM products](#comparison-ai-messaging--crm-products)
  - [Comparison: operations platforms](#comparison-operations-platforms)
  - [Which project to mention for a requirement](#which-project-to-mention-for-a-requirement)
  - [Shared technology (verified across repos; see "How AI Agentix builds")](#shared-technology-verified-across-repos-see-how-ai-agentix-builds)
- [Coverage checklist](#coverage-checklist)
  - [Safety audit of this document](#safety-audit-of-this-document)

---

Scope of this part: 11 projects. Portfolio base URL: https://agentix-portfolio.vercel.app/ (planned hosted URL). Portfolio demos are "Safe demo: fictional data, all actions simulated". Interactive walkthrough modules currently exist for AGENTiX, SocialFlow, VoiceCRM, SocialPush and YT-Automation. Riya, Agentix CRM, Eurobrass CRM, LeadForge, Santure AI CRM and Ekatva have a project page (overview, how it works, screens, tech) but no interactive module file in `js/demos/` at the time of writing, so a walkthrough link for them opens the guided tab, not a clickable simulation.

Evidence labels used: **Verified** (seen in code and/or live public page and/or reliable project doc), **Partially verified**, **Unverified**, **Unavailable**.

---

## AI Conversational Agents

### AGENTiX

**Slug:** `agentix` · **Also known as:** AGENTiX app, WhatsApp-Automation (folder name), "the flagship SaaS" · **Category:** AI Conversational Agents / **Subcategory:** WhatsApp + Instagram AI agent with CRM and Google growth tools · **Status:** Live (Verified, public marketing pages loaded; app behind login)
**Client / owner:** AI Agentix (own product, sold to small and medium businesses; also used for agency-managed client workspaces) · **Local folder:** `D:\Agentix Project\WhatsApp-Automation` · **Last activity:** 2026-10-28 (about 769 commits)

#### Spoken introduction
AGENTiX is our flagship product: an AI agent that answers your customers on WhatsApp and Instagram, qualifies them, and drops each one onto a hot, warm or cold board so your team calls the right person first. On top of that it has campaigns, bookings, a Google Business Profile and Google Ads toolkit, and a marketing ROI view. It is sold at flat monthly pricing in rupees, with a three day free trial.

#### Quick overview
AGENTiX is a multi-tenant SaaS built for growing Indian businesses. Each business gets its own workspace with a shared WhatsApp and Instagram inbox, a bundled live AI agent grounded in the business's own knowledge base, and a Kanban CRM that scores every conversation automatically. Around that core sit broadcast campaigns, message templates, a visual flow builder, bookings, a unified lead hub that collects leads from every channel, Google Business Profile management, Google Ads reporting and lead capture, local rank tracking, cross-channel marketing ROI, and a super-admin console for agencies. It solves lost leads from slow replies and the five-tool juggling of chat, CRM, campaigns, Google presence and reporting.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Main site / app | https://app.aiagentixdev.com/ | Production (real clients), marketing pages are a Public marketing site; app is Login required | Do not perform actions in the app; it holds real client conversations |
| Features | https://app.aiagentixdev.com/features | Public marketing site | Verified loaded |
| Pricing | https://app.aiagentixdev.com/pricing | Public marketing site | Verified loaded |
| Free Google Business Profile report | https://app.aiagentixdev.com/gbp-report | Public marketing site | Free, instant, no signup; health score for a Google Business Profile |
| Security | https://app.aiagentixdev.com/security | Public marketing site | |
| Docs and help | https://app.aiagentixdev.com/docs | Public marketing site | Getting-started and billing help topics |
| Login / signup | https://app.aiagentixdev.com/login (and /signup) | Login required | No credentials in this KB |
| Portfolio demo overview | https://agentix-portfolio.vercel.app/#/demo/agentix/overview | Safe demo | Fictional data |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough | Safe demo | Starts on the Dashboard module |
| Walkthrough: Conversations | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough/conversations | Safe demo | AI chat that qualifies and books |
| Walkthrough: CRM | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough/crm | Safe demo | Hot/warm/cold Kanban |
| Walkthrough: Flows | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough/flows | Safe demo | Flow builder canvas |
| Walkthrough: Campaigns | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough/campaigns | Safe demo | |
| Walkthrough: Marketing ROI | https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough/roi | Safe demo | |

Portfolio demo module ids (from `js/demos/agentix.js`): dashboard, conversations, crm, contacts, leads, campaigns, templates, flows, segments, winback, referrals, bookings, tasks, team, knowledge, ai-revenue, copilot, google-ads, gbp, local-rank, roi, analytics, billing.

#### Target users & business problem
Target users are owners and front-desk teams of local and service businesses in India (clinics, salons, gyms, studios, shops), plus agencies running many such clients. The problem: enquiries arrive on WhatsApp and Instagram at all hours, replies are slow, leads sit in personal phones, follow-up is manual, and ad spend and Google presence are managed in disconnected tools. AGENTiX answers instantly, sorts leads, and ties spend to leads.

#### Features (complete inventory)
Evidence for the feature inventory below: the Next.js route tree (`app/(dashboard)/*`, `app/(admin)/admin/*`, `app/(marketing)/*`, `app/(auth)/*`), API route folders (`app/api/*`), `modules/*`, `lib/*`, docs (`docs/agentix-vs-grexa-comparison.md`, `docs/phase1-unified-lead-hub-spec.md`, `docs/phase2-gbp-spec.md`, `docs/phase4-google-ads-spec.md`, `docs/google-integration-runbook.md`, `docs/platform-backlog.md`), and the live public pages. Status per group is given in each heading.

**Public marketing site (Verified).** Pages: home, features (WhatsApp automation, AI agent, campaigns and broadcasts, CRM with lead temperature, shared team inbox, analytics and reports), pricing, security, docs/help, FAQ, about, contact, integrations, Free GBP Report, referral landing (`/r/[code]`), legal pages (privacy, terms, data deletion). Marketing copy states: 3-day free trial with no card; the AI agent is bundled, not an add-on; no per-agent seats; no per-conversation Meta markup. Evidence: live pages fetched.

**Pricing (Verified from live /pricing page).** Core (WhatsApp) at Rs 2,999 per month excluding 18 percent GST (shown as Rs 3,539 including GST on the monthly term); terms offered: monthly, quarterly, 6-month, yearly. Add-ons: Instagram automation (+Rs 999 per month: auto-reply to DMs, comments and follow-first) and Google Growth (+Rs 999 per month: Business Profile, Ads, Local Rank and reviews). An All-in-One plan at Rs 4,999 is advertised. Core includes: live AI agent, shared inbox, Kanban CRM with automatic hot/warm/cold scoring, campaigns, broadcasts and templates, in-chat Razorpay payment links. Prices on the page can change; quote them as "listed on the pricing page at the time of the check".

**1. Shared inbox and conversations (Verified).** Route `/conversations` and `/conversations/[id]`; API `app/api/conversations`, `messages`, `quick-replies`, `labels`, `inbox-rules`, `sla`. One real-time inbox for WhatsApp and Instagram DMs. Per the comparison doc it supports assignment to team members, statuses, labels, spam and sentiment flags, snooze, internal notes, media and templates, a campaign-scoped chat view, bot pause and human handoff, auto CSAT, auto-resolve and auto-tagging. Inputs: inbound WhatsApp Cloud API and Instagram webhooks (`app/api/webhooks/whatsapp`, `/instagram`, `/meta`). Output: messages stored per workspace and shown live (Supabase realtime plus socket client). Business use: no more juggled phones. Limitation: requires a connected WhatsApp Business number via the official API. Evidence: routes, docs, live features page.

**2. AI agent (auto-reply bot) (Verified).** Code in `lib/ai-reply.ts`, `lib/ai-client.ts`, `lib/ai-router.ts`, `lib/embeddings.ts`, `services/ai`, `app/api/ai`. The agent answers in the business's own persona, grounded in the knowledge base (RAG with pgvector), supports English, Hindi, Hinglish and several Indian languages (per comparison doc), can send interactive buttons, fails over between AI providers, applies business-only guardrails (anti-hallucination prompts), qualifies leads and offers booking slots. Operators can pause the bot on a conversation and take over. The pricing and offer the bot quotes come from the Knowledge Base offer state (an offer needs an end date; see backlog). Evidence: code and docs; behaviour inside real workspaces not observed.

**3. Knowledge base (Verified).** Route `/knowledge-base`; API `knowledge-base`, `vector-kb`, `offer`. Upload services, pricing, policies and offers; documents are embedded and used by the AI. A recent change requires offers to have an end date, and the campaign wizard warns when the bot would quote an expired or not-started offer (backlog entries dated 2026-10-28). Evidence: `docs/platform-backlog.md`, code.

**4. CRM pipeline with hot/warm/cold scoring (Verified).** Route `/crm`; API `leads`, `lead-rules`. Kanban of leads by pipeline stage with AI lead scoring, temperature (hot, warm, cold) and cool-down, assignment and stage history. An internal analysis doc (2026-10-05) describes consolidating three separate classification systems (keyword temperature, AI stage classifier, AI score) into one score-driven engine with per-client thresholds and explainability; treat the unified engine as an in-progress direction, not confirmed shipped. Cron `reclassify-leads` exists. Evidence: code, docs.

**5. Contacts and Contact 360 (Verified).** Route `/contacts`; API `contacts`, `contact-lists`, `custom-fields`. Profiles with conversations, orders, CSAT, lifetime value, tags, temperature, VIP and lifecycle flags, CSV and bulk import, custom fields, and a cross-channel journey timeline.

**6. Unified lead hub (Verified).** Route `/leads` and `/meta-leads`; spec `docs/phase1-unified-lead-hub-spec.md`. Every lead from WhatsApp, Instagram, Meta Lead Ads, Google Ads lead forms, Google Business, website forms, chat widget, campaigns, public API and manual entry in one place, tagged with source/channel and first and last touch, with a source-breakdown chart, filters, export and a Google Sheets sync (`lib/lead-sheet-sync.ts`). Webhooks `google-ads-leads` and Meta lead ads feed it. Evidence: spec and code.

**7. Campaigns and broadcasts (Verified).** Routes `/campaigns`, `/campaigns/[id]`; crons `process-campaign-queue`, `run-scheduled-campaigns`, `sync-campaign-replies`. Template broadcasts to segmented audiences, scheduling, A/B testing, carousel, limited-time offers, media headers, per-recipient delivery/read/reply statistics, reply attribution, one-click retargeting and exports. A review step in the wizard shows what offer the bot will quote.

**8. Templates (Verified).** Route `/templates`; API `templates`, `wa-forms`. Manage WhatsApp message templates, submit to Meta for approval, header media, and native WhatsApp Flows/in-chat forms.

**9. Segments (Verified).** Route `/segments`. Audience filters reused by campaigns.

**10. Flow builder (Verified).** Routes `/flows`, `/flows/[id]`; code `lib/flow-engine.ts`, `lib/flow-nodes`, `lib/flow-validate.ts`; API `flows`, `flows-native`. Visual ReactFlow canvas with trigger, condition and action nodes, templates, validation and a flow session engine with cleanup cron.

**11. Automation (Verified).** API `automation-triggers`, `time-trigger-config`, `sequences`; crons `time-triggers`, `automation-triggers`, `process-follow-up-sequences`, `auto-assign`, `auto-csat`. Inbox rules, time-triggered messages, follow-up sequences, abandoned-cart and Shopify webhook (`webhooks/abandoned-cart`), birthday and re-engagement triggers, auto-assignment.

**12. Win-back (Verified).** Route `/win-back`. Targets leads that went quiet; offered as a campaign type using cool-down data.

**13. Referrals (Verified).** Route `/referrals` and public `/r/[code]`; API `referrals`. Referral codes and landing.

**14. Bookings and Google Calendar (Verified).** Route `/bookings`; API `bookings`, `business-hours`; `lib/google-calendar.ts`. Appointments created by the AI agent or staff, shown with a Google Calendar badge when synced. A runbook notes that a "Connect Google Calendar" button on the Bookings page was a pending UI item for Google's OAuth verification (see Planned).

**15. Tasks (Verified).** Route `/tasks`. Follow-up tasks for the team.

**16. Team and roles (Verified).** Routes `/team`, `/team/[id]`; accept-invite flow; roles and per-member permissions (see roles section); cron `check-sla-breaches`.

**17. AI revenue (Verified).** Route `/ai-revenue`; API `ai`. Lead scoring insights, revenue insights, best-send-hour and hot-lead detection.

**18. Growth Copilot (Partially verified).** Route `/growth-copilot`; API `growth-copilot`. An AI recommendations surface for growth; detailed behaviour not documented in files read.

**19. Google Business Profile (Partially verified: software built; live data gated by Google approval).** Route `/google-business`; API `gbp`, `gbp-report`; spec `docs/phase2-gbp-spec.md`. Connect a Business Profile; manage reviews (AI-drafted reply, human approve, then post), posts (offers, updates, events), Q&A, and performance insights (views, calls, directions). The comparison doc states live GBP data begins once Google approves the Business Profile API access request; the OAuth verification doc says the Business Profile API returns quota 0 until that separate approval, and the GBP connect button was to be hidden until then. Public `/gbp-report` free health-score tool is live.

**20. Google Ads (Partially verified).** Route `/google-ads`; API `google-ads`; spec `docs/phase4-google-ads-spec.md`. Lead capture from Google Ads lead forms works through a webhook into the lead hub; reporting (campaigns, spend, clicks, conversions) appears once the account is connected and running campaigns. Google's OAuth verification of the requested scopes was reported in progress (reply pending as of the doc dated after 2026-09-17).

**21. Local rank tracking (Verified in code).** Route `/local-rank`; `lib/local-rank.ts`. Tracks local search ranking for keywords; relies on a Google Places API key (a backlog item notes the key must be regenerated and restricted).

**22. Marketing ROI (Verified).** Route `/marketing-roi`; `lib/meta-ads-sync.ts`, `lib/google-ads-sync.ts`, `lib/lead-attribution.ts`. Cross-channel view: spend, leads, conversions, cost per lead and conversion rate per channel, joining Google Ads spend and WhatsApp messaging cost with leads.

**23. Analytics and reports (Verified).** Route `/analytics`; API `analytics`, `reports`, `dashboard-stats`; crons for daily, weekly and monthly digests. KPIs, message funnel, delivery/read/reply rates, CSAT, conversations, leads, campaigns, agents; CSV export.

**24. Dashboard (Verified).** Route `/dashboard`. Overview tiles, counts and recent activity.

**25. Billing and subscription (Verified).** Route `/billing`; `lib/billing.ts`, `billing-guard.ts`, `entitlements.ts`; Razorpay subscriptions, checkout, invoices, plans, plus pages `/payment-required` and `/session-limit`. A billing go-live runbook exists (`docs/billing-go-live-runbook.md`).

**26. Settings and onboarding (Verified).** Routes `/settings`, `/settings/profile`, `/onboarding`, `/onboarding/whatsapp`; workspace creation and selection; chat widget (`/widget/[workspaceId]`, API `chat-widgets`, `widget`); catalog and orders (`catalog`, `orders`); QR code (`qr-code`); public REST API (`app/api/v1`) with API keys; audit logs; support tickets.

**27. Super-admin console (Verified in code).** Routes under `/admin`: overview, clients and client detail, bot health, AI tokens, analytics, billing, revenue, Meta spend and Meta billing, communications, inboxes, health, settings and support. Used by AI Agentix staff to run many client workspaces. Crons `tenant-health`, `health-monitor`, `meta-spend-sync`.

#### Key workflows (end to end)
1. A business signs up (3-day trial), creates a workspace, connects a WhatsApp Business number through the official API, and optionally Instagram.
2. It uploads services, pricing, policies and offers to the Knowledge Base and sets the AI persona.
3. A customer messages on WhatsApp or Instagram; the webhook stores the message; the AI replies from the knowledge base, scores the lead and can offer booking slots.
4. The conversation appears in the shared inbox; staff can pause the bot, assign, label or add notes.
5. The lead lands on the Kanban as hot, warm or cold; staff are tasked to follow up; bookings go to the calendar.
6. Campaigns, templates, flows and win-back sequences bring customers back; replies are attributed to campaigns.
7. Meta Lead Ads, Google Ads lead forms and website forms feed the same lead hub; marketing ROI combines spend and leads.
8. Errors and limits: role permissions are enforced server-side (403 when denied), billing guard blocks unpaid workspaces, and session limits apply.

#### User roles & permissions
Roles verified in `types/auth.types.ts`: `super_admin`, `admin`, `manager`, `agent`. Permissions are a named list per role (for example manage workspace, view analytics, billing management); `resolveMemberAccess` also honours configured roles, per-member overrides and page grants. Workspace members can be suspended. A platform-level super admin sees the `/admin` console. Exact permission-by-role matrix beyond these names was not transcribed.

#### Technical architecture & integrations
Frontend: Next.js 16 App Router, React 19, Tailwind, ReactFlow, socket.io client. Backend: Next.js route handlers plus service modules; cron endpoints under `app/api/cron`. Database/auth: Supabase Postgres with row-level security, pgvector for the knowledge base, Supabase Auth with email verification and invites. AI: OpenAI via SDK with a provider router and failover. Integrations: WhatsApp Cloud API, Instagram messaging, Meta Lead Ads, Google Business Profile, Google Ads, Google Calendar, Google Places, Google Sheets, Razorpay, Shopify (abandoned cart). Hosting: Docker on a Coolify VPS (Dockerfile present); public domain app.aiagentixdev.com. Credentials are stored encrypted per workspace (`lib/crypto-vault.ts`) and platform secrets are server environment variables. Evidence: package.json, Dockerfile, code, security page. Limitations noted in docs: GBP API quota pending; Google OAuth verification pending; no SOC 2 or ISO 27001 certification (stated on the security page).

#### Business value & example scenarios
Owners no longer lose leads to slow replies; the team calls hot leads first; campaigns and Google tools sit in one place; the price is flat. Scenario 1: "Riverside Dental Clinic" gets an Instagram DM at 11 pm asking about whitening; the agent answers from the price list, collects a name and preferred slot, books it, and the lead shows as Booked next morning. Scenario 2: the same clinic sends a win-back broadcast to patients quiet for 30 days and sees replies attributed to the campaign.

#### Planned / in progress (not live)
From `docs/platform-backlog.md` (started 2026-10-28): rotating exposed credentials (security hygiene), dashboard warning for lapsed offers, remind-before-offer-lapse, fixing inflated conversation totals under filters, investigating conversations with multiple lead rows. From docs: Google Business Profile live data after Google API approval, Google Ads and Calendar OAuth verification, a "Connect Google Calendar" button on Bookings, unified lead classification engine. Native mobile apps are not built (the comparison doc lists this as a gap versus a competitor).

#### Example visitor questions & answers
- **What does AGENTiX do?** It is an AI agent for WhatsApp and Instagram with a shared inbox, hot/warm/cold CRM, campaigns, bookings and Google growth tools.
- **How much does it cost?** The pricing page lists Core (WhatsApp) at Rs 2,999 per month before 18 percent GST, with Instagram and Google Growth add-ons at Rs 999 each per month and an All-in-One plan at Rs 4,999; there is a 3-day free trial.
- **Is the AI an extra charge?** No, the pricing page says the live AI agent is bundled.
- **Can I see a demo?** Yes, a safe simulated one: https://agentix-portfolio.vercel.app/#/demo/agentix/walkthrough. All data is fictional.
- **Does it replace Google Business Profile tools?** It includes review replies, posts, Q&A and insights; live data depends on Google approving API access.
- **Is my data separated from other businesses?** Yes, each workspace is isolated with row-level security, per the security page.
- **Which languages?** English, Hindi, Hinglish and several Indian languages, according to project docs.

#### Related projects
SocialFlow focuses on Instagram, Facebook and Telegram content and comment-to-DM; AGENTiX is WhatsApp-first with CRM and Google tools. VoiceCRM and Riya are CRMs over voice and WhatsApp bots. Redux and Woodpecker in other parts use similar lead and WhatsApp ideas for specific clients.

#### Verification notes
Checked: full route tree, API folders, docs, package.json, git log count, and live public pages (features, pricing, security, docs, gbp-report). Not verified: any behaviour inside the logged-in app (no production login used); exact permission matrix; live Google data. Missing: demo workspace credentials or screenshots of the dashboard, the final All-in-One feature list on the pricing page, and a statement of how many clients are live.

---

### SocialFlow

**Slug:** `socialflow` · **Also known as:** AGENTiX SocialFlow, AI-Agentix SocialFlow, InstaAgent (v1 prototype in `Insta-agent`) · **Category:** AI Conversational Agents / **Subcategory:** Instagram, Facebook and Telegram social automation · **Status:** Live (Verified, public landing page loaded; app behind login; Meta App Review for Advanced Access in progress per docs)
**Client / owner:** AI Agentix (own product; first onboarded client workspace referenced in docs is a wellness-spa brand) · **Local folder:** `D:\Agentix Project\instagram-automation-platform` (current) and `D:\Agentix Project\Insta-agent` (v1) · **Last activity:** 2026-10-08 (about 99 commits) for the platform; 2026-05-25 (2 commits) for v1

#### Spoken introduction
SocialFlow is our social media operating system: one AI inbox for Instagram, Facebook and Telegram, comment-to-DM automation with a follow check, a content studio with scheduling, and a CRM behind it all. It started as a small Instagram DM bot called InstaAgent and grew into a full multi-tenant platform. You can try a simulated version in the portfolio.

#### Quick overview
SocialFlow lets a business connect its Instagram professional account (and Facebook and Telegram) and have AI answer DMs and comments from a knowledge base and brand persona. Public comments on a post can trigger a private DM, optionally gated on the user following the account. It also has visual automation flows, keyword rules and sequences, a content studio with a calendar and a design editor, a Reels studio, profile and post audits, a CRM with pipeline, bookings, commerce, influencer tracking and ads, and a platform admin console. It addresses DM overload, manual comment replies, missing CRM for Instagram, and inconsistent posting.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Landing page | https://social-media.aiagentixdev.com/ | Public marketing site (production app behind login) | Verified loaded: features, steps, plans |
| Login | https://social-media.aiagentixdev.com/login | Login required | No credentials in KB |
| Privacy | https://social-media.aiagentixdev.com/privacy | Public site | Needed for Meta review |
| Data deletion | https://social-media.aiagentixdev.com/data-deletion | Public site | |
| Portfolio demo overview | https://agentix-portfolio.vercel.app/#/demo/socialflow/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/socialflow/walkthrough | Safe demo | Starts on the inbox |
| Walkthrough: Unified inbox | .../walkthrough/inbox | Safe demo | AI reply from knowledge base |
| Walkthrough: Comment to DM | .../walkthrough/comment-dm | Safe demo | Follow-gate flow |
| Walkthrough: Profile score | .../walkthrough/profile-score | Safe demo | |
| Walkthrough: Content calendar | .../walkthrough/calendar | Safe demo | |

(Walkthrough links are under https://agentix-portfolio.vercel.app/#/demo/socialflow/. Module ids from `js/demos/socialflow.js`: inbox, comment-dm, rules, sequences, flows, health, contacts, leads, bookings, campaigns, products, orders, influencers, ads, studio, calendar, approvals, design, reels, profile-score, post-audit, analytics, knowledge, team, channels.)

#### Target users & business problem
Brands, creators, and agencies that sell through Instagram and receive hundreds of DMs and comments but can answer only a fraction. The platform automates the volume and leaves relationships to humans, while staying inside Meta's 24-hour messaging window rules.

#### Features (complete inventory)
Evidence: route tree in `instagram-automation-platform/app`, 29 numbered design docs in `docs/` (vision, architecture, multi-tenant, schema, inbox, AI, content studio, campaigns, workflows, CRM, analytics, influencer, commerce, ads, advanced AI, collaboration, PWA, security, API, background services, DevOps, roadmap, platform admin, multi-channel, content intelligence), the Meta App Review pack, and the live landing page. The design docs describe intended scope; the routes show what pages exist. Each group is labelled accordingly.

**Landing page (Verified).** Claims: unified AI inbox, comment-to-DM with follow-gate, visual automations, AI trained on your knowledge base and persona, content and scheduling, CRM and leads, analytics and reports, secure isolated tenants. Works across Instagram, Facebook, Telegram, LinkedIn and YouTube is displayed as a platform strip; only Instagram, Facebook and Telegram are described as connectable now (the multi-channel design doc says LinkedIn, YouTube and others are phased; treat those as planned). Plans shown on the landing page: Starter Rs 999 per month (1 social account, AI auto-reply, inbox and CRM, 5,000 messages), Pro Rs 2,999 (3 accounts, AI chatbot and comment-to-DM, campaigns and content scheduling, workflow automation, 25,000 messages), Enterprise Rs 7,999 (10 accounts, influencer, commerce and ads, priority support, 100,000 messages). Plans can change.

**Unified inbox (Verified in code and docs).** Route `/conversations`. DMs, story replies, story mentions and post comments; assignment, roles, 24-hour window countdown and guard, templates for re-engagement. Inputs: Instagram webhooks (HMAC-verified). Output: conversation threads in realtime.

**AI auto-reply (Verified).** Docs `07-ai-automation.md`; route `/knowledge-base`; settings brand and voice. Replies grounded in the knowledge base (pgvector) and a persona; human handoff. Brand voice settings (sample posts, positions, proof, never-say words, keyword CTA) feed every prompt.

**Comment to DM with follow-gate (Verified in design and landing; mechanics in code).** Keyword-triggered auto-DM and public comment reply; optional auto-like and a follow check before delivering the item. Routes under `/automation/rules`.

**Automation: rules, sequences, flows, health (Verified).** `/automation/rules` (keyword rules), `/automation/sequences` (timed message sequences), `/automation/flows` and `/automation/flows/[id]` (visual trigger, condition, action builder), `/automation/health` (account and automation health).

**Contacts, leads and CRM (Verified).** `/contacts`, `/contacts/[id]`, `/leads`. Every DM contact becomes a CRM record with lead score, temperature and pipeline stage; notes, tags, follow-ups.

**Bookings, commerce, influencers, ads (Verified as pages).** `/bookings`, `/commerce/products`, `/commerce/orders`, `/influencers`, `/ads`. Influencer CRM with deliverables, product and order management, Meta ads lead sync (design docs 13 to 15). The extent of commerce and ads integrations beyond pages is Partially verified.

**Campaigns (Verified).** `/campaigns`, `/campaigns/[id]`. Window-compliant broadcasts only (contacts with an active window), with policy violation guard at send time.

**Content studio and calendar (Verified).** `/content`, `/content/studio` (AI studio: captions, hooks, hashtags), `/content/plans` (auto-pilot content plans), `/content/design` (design canvas built on Fabric.js), `/content/reels` (Reels studio: idea to scored hooks to script to beat sheet to draft), approval queue, and a cron that publishes approved scheduled posts. Caption Coach lints captions live (hashtag cap of five, first 125 characters, humanizer removing stock AI phrases).

**Growth: Profile Score and Post Audit (Verified).** `/growth/profile` scores an account against a 12-item, 100-point rubric with fix-first rewrites and history; `/growth/audit` ranks the account's own posts by outlier multiple and explains why. Reach/views/saves need the `instagram_business_manage_insights` permission, enabled only after Meta approval.

**Analytics (Verified).** `/analytics`. KPI overview, agent performance, campaign funnels; exports.

**Settings (Verified).** Brand, channels (connect Instagram via Business Login; Telegram connect form), billing, API keys; team and invites; notifications; help center; setup wizard; onboarding by tokenised link (`/onboard/[token]`); embeddable chat widget.

**Platform admin (Verified in routes).** `/platform-admin`: workspaces, admins, AI, analytics, approvals, audit, automation, communication, feature flags, health, integrations, Meta, onboarding, payments, plans, reports, revenue, search, security and 2FA, settings, support tickets.

**InstaAgent v1 (Verified, small).** `Insta-agent`: Next.js app with a single dashboard page, webhook route receiving Instagram DMs, AI replies through OpenRouter with a model fallback chain, conversation and send routes, Supabase storage; privacy policy, terms and user-data-deletion documents. It was the proof of concept before SocialFlow.

#### Key workflows (end to end)
1. Agency creates a workspace (or sends a tokenised onboarding link); client logs in and connects Instagram with "Connect with Instagram" (one central Meta app model recommended; per-client Meta app is an alternative).
2. Add knowledge base and brand persona.
3. Create a comment-to-DM rule for a post keyword; a commenter triggers a public reply and a private DM, optionally after a follow check.
4. AI answers DMs; leads are created in the CRM; humans take over when needed.
5. Plan content in the studio, approve, schedule; the cron publishes at the scheduled time.
6. Review Profile Score and Post Audit; run window-compliant campaigns.

#### User roles & permissions
Roles in code: `super_admin`, `admin`, `manager`, `agent` (workspace); platform admins separately with 2FA. Exact permission matrix not transcribed.

#### Technical architecture & integrations
Next.js 16, React 19, Supabase (Postgres with RLS, pgvector, cron-driven background routes), Fabric.js for the design editor, Instagram Business Login and Graph API, Telegram Bot API, OpenAI-compatible AI providers. Docker deployment on Coolify (DEPLOYMENT.md, Dockerfile). Evidence: package.json, docs, route tree.

#### Business value & example scenarios
Replies to most DMs automatically, turns comments into leads, keeps a consistent posting schedule, and gives agencies one multi-tenant console. Scenario: "Lumen Skin Studio" runs a post saying "comment PRICE for the rate card"; each commenter gets a public thank-you and a DM; those who follow receive the rate card and appear as leads.

#### Planned / in progress (not live)
Meta App Review resubmission for Advanced Access (five Instagram permissions: basic, manage messages, manage comments, content publish, Human Agent), after earlier rejections for vague descriptions and incomplete screencasts; until approved each client's Instagram account must be added as a tester. Multi-channel expansion (LinkedIn, YouTube, X, TikTok, Pinterest) is a design, not live. Insights-based audit metrics wait on permission approval. No automated outreach DMs or scraping by design.

#### Example visitor questions & answers
- **Is SocialFlow the same as InstaAgent?** InstaAgent was the first small prototype; SocialFlow is the full platform.
- **Does it work on Instagram comments?** Yes, the comment-to-DM flow with optional follow check is a core feature.
- **Which platforms?** Instagram and Facebook and Telegram are the connectable channels now; others are planned.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/socialflow/walkthrough, simulated with fictional data.
- **What does it cost?** The landing page lists Starter Rs 999, Pro Rs 2,999 and Enterprise Rs 7,999 per month.
- **Will Meta ban my account for bulk DMs?** The design only allows window-compliant messages and avoids scraping or unsolicited outreach.

#### Related projects
AGENTiX is the WhatsApp equivalent; SocialPush publishes posts to many platforms but does not run inbox automation; YT-Automation does YouTube video production.

#### Verification notes
Checked: route tree, docs index, Meta review pack, landing page, v1 source tree. Not verified: logged-in dashboard, live Meta approval state today, actual client counts. Missing: demo login or screenshots of the dashboard, and the current outcome of the Meta App Review.

---

### VoiceCRM

**Slug:** `voicecrm` · **Also known as:** Voice-CRM, WhatsApp CRM (Supabase powered) in its README · **Category:** AI Conversational Agents / **Subcategory:** CRM for an AI voice bot's calls · **Status:** Prototype (Partially verified; login page reached, interior not seen)
**Client / owner:** AI Agentix (voice-bot sales calling for the team) · **Local folder:** `D:\Agentix Project\Voice-CRM` · **Last activity:** 2026-09-04 (about 102 commits)

#### Spoken introduction
VoiceCRM is the control room for an AI calling bot. It shows live calls, transcripts, summaries, sentiment and lead scores, and turns outcomes into follow-up tasks for the human team. It is a working prototype with a demo in the portfolio.

#### Quick overview
An AI voice bot places and receives sales calls and records results into a Google Sheet and Supabase. VoiceCRM reads that data and gives managers a dashboard, a live calls board, a call list with recordings, per-call insights, a lead explorer with detail pages, follow-up tasks, reports, exports and team management, and lets staff message a lead on WhatsApp from the lead page. Admins see everything; callers, validators and field agents see role-specific navigation.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| App | https://voice-crm-snowy.vercel.app/ | Login required | Title "VoiceCRM, AI-Powered Lead Management"; login page only |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/voicecrm/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/voicecrm/walkthrough | Safe demo | |
| Live calls | .../walkthrough/live-calls | Safe demo | |
| Call insights | .../walkthrough/insights | Safe demo | |
| Leads | .../walkthrough/leads | Safe demo | |
| Follow-up tasks | .../walkthrough/tasks | Safe demo | |

(Base for relative links: https://agentix-portfolio.vercel.app/#/demo/voicecrm/. Module ids: dashboard, live-calls, calls, insights, leads, tasks, reports, exports, employees.)

#### Target users & business problem
Sales managers and callers who use an AI voice bot to dial leads and need to see what happened on each call, who is hot, and what to do next. Problem: call outcomes live in spreadsheets and nobody follows up consistently.

#### Features (complete inventory)
Evidence: `frontend/src/app/routes.tsx`, pages under `frontend/src/pages`, `backend/src/routes.ts`, `frontend/src/data/types.ts`, README, a seeded mock provider in `frontend/src/mock`.

**Dashboard (Verified).** Route `/`. KPIs with a date-range picker (presets and custom) persisted locally; funnel and sentiment trend charts; hot-lead tracking.

**Live calls (Verified, admin only).** Route `/live-calls`; API `/live/activity`. Board of calls by status (To Call, Calling, Done, Missed, Demo Booked, Callback), summary counts for today, active, recent completed and failed calls, duration and sentiment (Hot, Warm, Cold), auto-refresh interval selectable.

**Calls (Verified, admin only).** Route `/calls`. Call history with recordings; `/recordings/download` proxies audio downloads.

**Call insights (Verified, admin only).** Route `/call-insights`. Transcript, AI summary, sentiment, score per call.

**Leads explorer and lead detail (Verified, all roles).** Routes `/leads`, `/leads/:id`. Search and filters, status updates, activity timeline, pipeline stage log, outcomes (Converted, Lost, No Response, Follow-up Needed, Reschedule), and WhatsApp messages and templates sent from the lead page (WhatsApp Cloud API webhook and send endpoints).

**Tasks and follow-ups (Verified, all roles).** Route `/tasks`. Create, bulk-create, update and delete tasks; stats; employees see their own.

**Reports (Verified, admin).** Route `/reports`. Conversion ratio, sentiment split, agent performance.

**Exports (Verified, admin).** Route `/exports`. CSV export with a history list of export jobs.

**Settings, profile, team (Verified).** `/settings` (theme, alert preferences for hot leads, completed calls and due tasks, refresh interval, data status including database and Google Sheet sync), `/profile`, employees management API.

**Login (Verified).** `/login`; protected routes; backend `/auth/login`; admin-only user management.

#### Key workflows (end to end)
1. The voice bot calls leads from a Google Sheet queue; call results (status, sentiment, recording URL, duration) land in Supabase.
2. Manager opens the dashboard and live board to watch calls in progress.
3. After a call ends, insights show summary and score; hot leads raise an alert.
4. Staff open the lead, review activity, send a WhatsApp follow-up, and create a task.
5. Outcomes are recorded and reports and exports are generated.

#### User roles & permissions
Roles in code: admin, employee, caller, validator, field_agent. Admin sees Calls, Live calls, Insights, Reports, Exports and Settings; all roles see Leads, Tasks (own tasks for non-admin) and Profile; each role has its own sidebar. Evidence: `routes.tsx` (AdminRoute guard), `Sidebar.tsx`.

#### Technical architecture & integrations
Frontend: Vite, React, TypeScript, TanStack Query, Tailwind, Framer Motion. Backend: Express (TypeScript) with Zod, deployed on Vercel (vercel.json). Database: Supabase Postgres. Data source: AI voice bot via Google Sheet and Supabase tables; WhatsApp Cloud API for messaging. Auth: backend login with API key header. The data provider is forced to the real backend in code (mock provider exists for demos).

#### Business value & example scenarios
One screen to see every call and act on it. Scenario: "Meera" a caller sees a Hot lead flagged after a demo-interested call, opens the lead, sends a WhatsApp brochure, and sets a follow-up task for tomorrow.

#### Planned / in progress (not live)
No roadmap file found. The repository README is partly generic and still describes a WhatsApp CRM, which indicates the product evolved from a WhatsApp CRM codebase.

#### Example visitor questions & answers
- **Does VoiceCRM make the calls?** No, an AI voice bot makes the calls; VoiceCRM is the CRM and monitoring layer.
- **What does it show about a call?** Transcript, summary, sentiment, score and recording.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/voicecrm/walkthrough with fictional data.
- **Who can use which screens?** Admins see everything; other roles see leads and tasks.
- **Can staff message leads on WhatsApp?** Yes, from the lead detail page.

#### Related projects
Riya CRM is the WhatsApp-bot version of the same idea for a gym; AGENTiX is the general WhatsApp and Instagram agent.

#### Verification notes
Checked: routes, page list, backend routes, types, live login page. Not verified: logged-in app, the exact voice-bot vendor, transcript source. Missing: demo credentials or screenshots, the name of the voice platform feeding the sheet.

---

### Riya, Fitness First WhatsApp CRM

**Slug:** `riya-crm` · **Also known as:** Fitness First CRM, Fitness First Dwarka WhatsApp CRM · **Category:** AI Conversational Agents / **Subcategory:** CRM dashboard over a WhatsApp sales bot · **Status:** Prototype (Verified in code and architecture doc; no public URL)
**Client / owner:** Fitness First Dwarka (a gym) · **Local folder:** `D:\Agentix Project\Fitness First CRM` · **Last activity:** 2026-03-01 (about 13 commits)

#### Spoken introduction
Riya is the WhatsApp assistant that talks to gym leads for Fitness First, and this project is the sales dashboard behind her. It replaces a Google Sheet with a live view of leads, conversations, tasks and trial bookings.

#### Quick overview
The bot "Riya" handles inbound enquiries on WhatsApp and logs each message to Supabase. The CRM turns those rows into leads, scores them, shows sentiment, and lets sales staff record outcomes (Trial Booked, Converted, Lost, Callback) and follow-up tasks. It is an internal dashboard without login, designed for a trusted network.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Public app | None | n/a | No deployment found |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/riya-crm/overview | Safe demo | Guided tab |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/riya-crm/walkthrough | Safe demo | Chat replay and KPI dashboard (tier B) |

#### Target users & business problem
Gym sales agents who follow up WhatsApp leads. Problem: lead tracking lived in a Google Sheet with no scoring, tasks or outcome tracking.

#### Features (complete inventory)
Evidence: `ARCHITECTURE.md` (generated 2026-04-11), `frontend/src/pages`, `backend/src/routes.ts`.

**Dashboard (Verified).** Route `/`. KPIs: total leads, today's counts, hot leads.
**Leads explorer and lead detail (Verified).** `/leads` with hot/warm/cold bucket filter, `/leads/:id` (id is the phone number). Notes, assignment to an agent, conversation history.
**Conversations (Verified).** `/conversations`: session list and message thread (Riya's responses and the lead's messages, with conversation stage: Initial Contact, Inquiry, Solution Provided, Conversion Attempt).
**Live inbox (Verified).** `/live-inbox`: polls every 30 seconds.
**Lead insights (Verified).** `/lead-insights`: bot performance analytics.
**Outcomes (Verified).** Mark TrialBooked, Converted, Lost, Callback.
**Tasks and follow-ups (Verified).** `/tasks` with a create form; statuses; overdue not auto-detected.
**Reports and exports (Verified).** `/reports` CSV downloads, `/exports` multi-format page; the xlsx format is stubbed.
**Settings (Partially verified).** Theme toggle; save button is a UI stub.
**Bot webhook (Verified).** `POST /webhook/whatsapp` lets the bot (an n8n workflow per the doc) insert conversation rows.

#### Key workflows (end to end)
1. A lead messages the gym on WhatsApp; Riya replies and each exchange is written to the conversation table with a session id and AI summary.
2. The CRM groups rows by phone into leads and scores them.
3. A sales agent reviews hot leads, adds notes, assigns the lead, creates a follow-up task.
4. The agent records an outcome (trial booked, converted, lost).
5. Reports export to CSV.

#### User roles & permissions
None implemented: no frontend login; backend uses a static API key header that can be disabled. The doc lists "CRM Agent" and "Bot" as actors.

#### Technical architecture & integrations
React 19, Vite, TanStack Query and Table, Recharts, Tailwind v4; Express backend with Zod; Supabase Postgres (four tables with permissive RLS). No deployment files. Known gaps from the architecture doc: no auth, scoring keywords copied from a grain CRM, export filename leftover, no tests.

#### Business value & example scenarios
Gives the front desk a priority list. Scenario: a hot lead asks about group classes; Riya answers; the agent sees it flagged and books a trial call.

#### Planned / in progress (not live)
Gap list in the architecture doc: authentication, database-level filtering, automated overdue tasks, realtime updates, xlsx export.

#### Example visitor questions & answers
- **Who is Riya?** The WhatsApp bot for Fitness First Dwarka.
- **Is the dashboard live?** No public URL; it is an internal prototype.
- **What outcomes does it track?** Trial Booked, Converted, Lost, Callback.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/riya-crm/walkthrough (fictional).

#### Related projects
VoiceCRM (same codebase lineage, voice calls); Fitness First Dwarka website and Max Register gym CRM in other parts.

#### Verification notes
Checked: README, ARCHITECTURE.md, route files, folder. Not verified: bot behaviour (lives in an n8n workflow outside the folder). Missing: live deployment or screenshots, and confirmation of whether the CRM is in daily use.

---

## Content & Social Automation

### SocialPush

**Slug:** `socialpush` · **Also known as:** Social Studio, auto-posting (folder name) · **Category:** Content & Social Automation / **Subcategory:** multi-platform scheduling and publishing · **Status:** In development, deployed login page (Partially verified)
**Client / owner:** AI Agentix · **Local folder:** `D:\Agentix Project\auto-posting` · **Last activity:** 2026-10-13 (about 32 commits)

#### Spoken introduction
SocialPush is write once, publish everywhere. You connect your social accounts, write a post with an image or video, pick the platforms, and publish now or schedule it. Background workers do the publishing and report back.

#### Quick overview
A scheduling and publishing tool for Facebook Pages, Instagram business accounts, YouTube, Threads, Pinterest and X (Twitter). Media is cropped per platform, scheduling is done through a queue with retries, analytics are synced back, and an AI assistant helps with captions. It is built as microservices with a Next.js dashboard.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| App login | https://pwolpx2j8r3vh5di5q1e0gdn.76.13.250.173.sslip.io/login | Login required | Verified: "Social Studio, Welcome back, Log in to manage your posts and channels", with links to About, Privacy, Terms |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/socialpush/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/socialpush/walkthrough | Safe demo | |
| Composer | .../walkthrough/composer | Safe demo | Platform toggles and previews |
| Calendar | .../walkthrough/calendar | Safe demo | |
| Posts | .../walkthrough/posts | Safe demo | Queued, Publishing, Published |

(Base: https://agentix-portfolio.vercel.app/#/demo/socialpush/. Module ids: overview, accounts, composer, posts, calendar, analytics, comments, assistant, team.)

#### Target users & business problem
Small teams and agencies who post the same content to several networks and want one composer, a calendar and reliable scheduled publishing.

#### Features (complete inventory)
Evidence: `README.md`, `docs/CURRENT_STATE.md` (snapshot 2026-09-21), `docs/KNOWN_ISSUES.md`, Next.js page tree, services folder.

**Accounts (Verified).** `/dashboard/accounts`. OAuth connect for Twitter/X, Facebook Pages, Instagram business, YouTube, Pinterest and Threads; LinkedIn is link-only and TikTok is a stub in the code per the state doc. Facebook uses the first Page, Instagram the first linked account (no picker).
**Composer and previews (Verified).** `/dashboard/posts`: text, media upload with transcoded preview, per-platform preview cards (Instagram, TikTok, Pinterest, generic), reel toggle, platform selection, publish now or schedule.
**Media processing (Verified).** media-service uses sharp for images and ffmpeg for video with per-platform aspect ratios (reels 9:16).
**Scheduling and queue (Verified).** scheduling-service plus BullMQ on Redis; one delayed job per platform; the worker retries transient failures up to three times (fixed 2026-09-22).
**Publishing adapters (Verified).** Facebook (text, photo, reel), Instagram (image, reel), YouTube (resumable chunked upload, Shorts), Threads (text, image, video), Pinterest (boards import and create), X (text only).
**Calendar (Verified).** `/dashboard/calendar`: FullCalendar month and week view with aggregate status including Partially Published, platform chips. Reschedule is not done.
**Analytics (Partially verified).** `/dashboard/analytics`: backend sync for YouTube, Pinterest and Threads; the state doc flagged the UI display of new data as broken.
**Comments (Partially verified).** `/dashboard/comments` page exists; depth not confirmed.
**AI assistant (Verified as a page and package).** `/dashboard/ai-assistant`; `packages/ai` with generate, classify and quota modules for captions.
**Overview, settings, team (Verified).** `/dashboard/overview`, `/dashboard/settings`, team-service with invites and basic roles.
**Notifications (Partially verified).** In-app via realtime; email mocked.
**Billing (Partially verified).** Plan toggle only, mocked.
**Legal pages (Verified).** About, privacy, terms, data deletion.

#### Key workflows (end to end)
1. Log in; connect accounts through OAuth.
2. Compose a post, upload media, choose platforms and view each preview.
3. Publish now or pick a time; scheduling-service creates delayed queue jobs per platform.
4. At the time, the worker calls publishing-service, which uses the platform adapter; the result updates post status and notifies the user.
5. Analytics sync periodically; the calendar shows queued, publishing and published states.

#### User roles & permissions
Teams with roles (auto-team on first login, invite existing users, role checks). No member removal or role editing yet.

#### Technical architecture & integrations
Next.js App Router, React, Tailwind, FullCalendar; Node/Express microservices (account, analytics, media, notification, post, publishing, scheduling, team, worker); Supabase Postgres/Auth/Storage; Redis and BullMQ; sharp and ffmpeg; Docker compose for Redis, k8s manifests present but marked as referencing nonexistent images. Frontend on Vercel earlier; the sslip.io URL suggests a VPS deployment. Evidence: package.json, docs. Known limits (KNOWN_ISSUES.md): no backend authentication on internal services at the time of the snapshot, a hardcoded fallback encryption key, tokens (other than YouTube) never refresh, localhost URLs in the frontend at that time, platform OAuth works for test users until app review.

#### Business value & example scenarios
One composer for six networks. Scenario: "Harbor Coffee" schedules a reel for Friday 6 pm to Instagram, Facebook and YouTube Shorts in one action.

#### Planned / in progress (not live)
Calendar steps beyond read-only (drag to reschedule), cancel/edit scheduled posts, token refresh for Meta and Pinterest, real billing, LinkedIn and TikTok connectors, Threads analytics scope, security hardening. Note: the 2026-10-13 commits state a security hardening and publishing fix, so parts of the older issue list may be resolved.

#### Example visitor questions & answers
- **Which platforms?** Facebook Pages, Instagram, YouTube, Threads, Pinterest and X; LinkedIn and TikTok are not real yet.
- **Can I schedule?** Yes, through a queue with retries.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/socialpush/walkthrough (simulated).
- **Is it production?** It is in active development; the login page is public.

#### Related projects
SocialFlow (inbox automation and content on Instagram), YT-Automation (YouTube video creation and approval).

#### Verification notes
Checked: README, state and known-issues docs, route tree, services, live login page. The state doc is a 2026-09-21 snapshot; later commits exist. Missing: logged-in screenshots, current fix status of known issues, whether platform app reviews are approved.

---

### YT-Automation

**Slug:** `yt-automation` · **Also known as:** Amber Light Stories pipeline (first tenant), amber-light · **Category:** Content & Social Automation / **Subcategory:** AI YouTube video production SaaS · **Status:** Live SaaS (Partially verified: public pages seen) and local pipeline/dashboard source (Verified in code)
**Client / owner:** AI Agentix product; "Amber Light Stories" is only the first tenant channel · **Local folder:** `E:\YouTube-Automation\amber-light` · **Last activity:** 2026-07-26 (about 165 commits)

Label note: the live SaaS at yt-automation.aiagentixdev.com was reviewed only through its public pages. The local folder contains a Python pipeline and a Next.js web app (`web/`) with pages that match a multi-tenant dashboard. Whether the deployed SaaS is built from exactly this web app was not confirmed.

#### Spoken introduction
YT-Automation turns an idea into a finished vertical video with AI visuals, a narrated voice and captions in Hindi or English, then waits for a human to approve it before uploading to YouTube. It has a hard cost cap per video. It is invite-only.

#### Quick overview
A multi-tenant SaaS for creators and agencies. Each client workspace brings its own provider keys, connects a YouTube channel, sets a content plan and brand, and reviews generated videos. The pipeline runs research, script, storyboard, scene breakdown, character assignment, keyframe images, motion clips, voice, music and effects, subtitles, render, thumbnail, metadata, human review, schedule and publish.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Welcome page | https://yt-automation.aiagentixdev.com/welcome | Public marketing site | Verified |
| Privacy | https://yt-automation.aiagentixdev.com/privacy | Public | Last updated 24 July 2026 |
| Terms | https://yt-automation.aiagentixdev.com/terms | Public | |
| App | https://yt-automation.aiagentixdev.com/ | Login required | Invite-only |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/yt-automation/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/yt-automation/walkthrough | Safe demo | |
| Generate | .../walkthrough/generate | Safe demo | Pipeline stages with a cost meter |
| Scenes | .../walkthrough/scenes | Safe demo | Keyframe grid |
| Approvals | .../walkthrough/approvals | Safe demo | |
| Calendar | .../walkthrough/calendar | Safe demo | |

(Base: https://agentix-portfolio.vercel.app/#/demo/yt-automation/. Module ids: generate, pipeline, scenes, characters, approvals, calendar, library, analytics, brand, prompts, api, logs, health.)

#### Target users & business problem
Creators, agencies and brands that publish daily short-form video and want it produced by AI without losing control or overspending.

#### Features (complete inventory)
Evidence for public claims: welcome, privacy and terms pages (live). Evidence for the rest: `web/src/app` route tree, `docs/PRODUCT-VISION.md`, `docs/product-bible/PART-*`, `pipeline/*.py`, `docs/PRODUCTION_DEPLOYMENT.md`.

**Live public claims (Verified).** Real AI video, not slideshows: each scene gets an AI keyframe animated into a clip, assembled into a 1080 by 1920 vertical video. Narration with ElevenLabs. Hindi and English burned-in captions that render Devanagari. Bring-your-own provider keys (OpenAI, Gemini, ElevenLabs, fal.ai), stored encrypted per workspace. A per-video budget ceiling with fallback to cheaper rendering. Nothing publishes without approval. Four steps: connect channel, set content plan, review, publish and track. Analytics flow back from YouTube.

**Client workspace screens (Verified in code).** analytics, api-management, approvals, assets, automation, billing, brand, calendar, characters, developer, generate, health, library, logs, manual mode, notifications, operations, pipeline, planner, profile, prompts, publishing, rendering, review (with stage review), roles, scenes, schedule, security, settings and model settings, stories (and story detail), strategy, style, support, team, uploads, usage, videos, voices, workers, workspace, youtube. Authentication pages: login, forgot and reset password, change password, onboarding by tokenised link with a waiting screen.

**Platform admin screens (Verified in code).** admin: clients and client detail, onboarding, plans, flags, gateway (AI gateway), routing, pipeline, queue and jobs, observability, health, maintenance, usage, reports, security, API, announcements, theme. Platform and workspace are deliberately separate systems.

**Pipeline (Verified).** Stage list in `pipeline/persist.py`: topic, research, script, storyboard, scene breakdown, character assignment, scene prompt generation, keyframe images, motion clips, voice, background music, sound effects, subtitles, transitions, render, thumbnail, metadata, human review, schedule, publish. Cost governor enforces a per-video budget and downgrades models; a model routing and asset library module reuse assets before generating; local motion fallback; FFmpeg render worker. Manual mode pauses at every stage; automatic mode proceeds.

**Phase 1 channel pipeline (Verified).** The README describes the original single-channel version: one video per day generated at 03:00 US Eastern, QA gate, published at 09:00, Gmail confirmation, QA API bound to localhost.

#### Key workflows (end to end)
1. Super admin creates a client; the client opens an onboarding link, changes password, and lands in its workspace.
2. Client adds provider keys, connects YouTube, defines brand, characters and content plan.
3. A story or idea is generated; the pipeline produces scenes, voice, captions and thumbnail with a live cost meter.
4. Reviewer approves, requests changes or rejects.
5. Approved videos are scheduled and uploaded; analytics return to the dashboard.

#### User roles & permissions
Design docs define a platform plane (Super Admin and operators) and a tenant plane (owner, admin, editor, reviewer, analyst, viewer and others, with custom roles planned); the two planes are disjoint. Exact implemented roles not transcribed.

#### Technical architecture & integrations
Next.js web app on Vercel (control plane) and a Python render worker with FFmpeg on an always-on host; Supabase (Postgres, Vault for per-tenant keys, a durable jobs table, cron drains); OpenAI and Gemini for text, fal.ai for images and video motion, ElevenLabs for voice, YouTube Data and Analytics APIs, Gmail for notifications. The live SaaS domain runs under aiagentixdev.com.

#### Business value & example scenarios
Cuts per-video production effort and keeps cost bounded. Scenario: "Little Lanterns" channel submits a bedtime story brief; the pipeline produces a 60-second Hindi short; the owner approves it and it is scheduled for 9 am.

#### Planned / in progress (not live)
The product bible describes white-label, enterprise and ecosystem parts and a migration backlog; the deployment doc lists unset values for a dedicated Web OAuth client for tenant YouTube connect at the time of writing. Treat these as roadmap.

#### Example visitor questions & answers
- **Does it publish automatically?** No, every video waits for your approval.
- **What does it cost to generate a video?** The pipeline enforces a per-video ceiling; the portfolio demo shows a sample cost breakdown, which is illustrative.
- **Can I sign up?** It is invite-only; accounts are created by a manager.
- **Hindi supported?** Yes, captions in Hindi and English.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/yt-automation/walkthrough.

#### Related projects
SocialPush publishes created content to other networks; SocialFlow covers Instagram.

#### Verification notes
Checked: public pages, local route tree, docs, pipeline files, git log. Not verified: logged-in SaaS, whether deployed code equals the local web folder, actual tenants. Missing: demo login, deployed commit or repo link.

---

## CRM, Sales & Lead Intelligence

### Agentix CRM

**Slug:** `agentix-crm` · **Also known as:** KanbanCRM, KanbanCRM-nodejs · **Category:** CRM, Sales & Lead Intelligence / **Subcategory:** internal agency operating system · **Status:** Internal (Verified in code; no public URL)
**Client / owner:** AI Agentix (internal) · **Local folder:** `D:\Agentix Project\KanbanCRM-nodejs` · **Last activity:** 2026-03-17 (about 89 commits)

#### Spoken introduction
Agentix CRM is the system we run our own agency on: clients, project tasks on a Kanban board, leads, invoices, revenue targets, announcements, and HR records, with AI help for proposals and status emails.

#### Quick overview
A desktop-first CRM with an Apple-style glass look. Teams manage clients, break work into stories on a global Kanban, discuss in comments, track invoices and revenue, and capture leads. Google Gemini analyzes uploaded proposals into tasks and drafts status emails. There is a founder-only internal area and HR-restricted salary and incentive pages.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| App | None | Internal | Not public |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/agentix-crm/overview | Safe demo | Fictional data |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/agentix-crm/walkthrough | Safe demo | Kanban, client detail, insights |

#### Target users & business problem
Agency founders, managers and employees who need one place for clients, delivery and money. Problem: scattered spreadsheets and chats for projects, invoices and incentives.

#### Features (complete inventory)
Evidence: `client/src/App.tsx` routes, `server/routes.ts`, `shared/schema.ts`, `replit.md`.

**Dashboard (Verified).** `/`.
**Global Kanban (Verified).** `/global-kanban`; stories with status (default To Do), priority, assignee, estimated and actual hours, due date, progress percent, tags; drag and drop; threaded comments; activity log; notifications; cron deadline reminders by email.
**Clients (Verified).** `/clients`, `/clients/:id`: company, owner, industry, stage, expected revenue, contract end date, contact details, proposal file, average progress, communications log, invoices with attachments.
**Proposal analysis (Verified).** `POST /api/analyze-proposal` (Gemini) extracts a summary and tasks; `create-tasks-from-proposal` converts to stories.
**Status emails (Verified).** `generate-email` with Gemini, saved in a sent-emails table.
**Leads (Verified).** `/leads`: contact, industry, stage, estimated value, owner, assignee.
**Insights (Verified).** `/insights/revenue`, `/insights/clients`, `/insights/stories`, `/insights/completion`; revenue targets endpoint.
**Announcements (Verified).** `/announcements`.
**Internal (Verified).** `/internal`: founder investments (with file attachments), internal documents, shareholding per co-founder; co-founder only.
**Salary and incentives (Verified).** `/salary`: salary records and incentives, restricted to owner or HR.
**Settings and login (Verified).** `/settings`, `/auth` (Google sign-in).

#### Key workflows (end to end)
1. Sign in with Google; the user type is co-founder, HR or employee based on configured emails.
2. Create a client and upload a proposal; Gemini turns it into tasks on the board.
3. Move stories across Kanban columns; comments and activity are logged; deadline reminders send.
4. Raise invoices against a client; revenue totals roll up into insights against targets.
5. Owner or HR manages salary and incentives; founders manage the internal area.

#### User roles & permissions
Roles: admin, editor, viewer, plus HR; user types: co-founder, employee, HR. Owner/HR guard on salary and incentive APIs (403 otherwise). Co-founder access to the internal area.

#### Technical architecture & integrations
React 18, Vite, Wouter, TanStack Query, Radix and shadcn/ui, Tailwind v4; Express with Passport Google OAuth and sessions in Postgres; Drizzle ORM on Postgres/Supabase; Gemini 2.0 Flash; email service; deployment scripts for a VPS and Hostinger; a Laravel migration plan exists but is a plan.

#### Business value & example scenarios
Single internal source of truth. Scenario: a signed proposal for "Bluebird Realty" is uploaded; fifteen tasks appear on the board; the first invoice moves revenue toward the monthly target.

#### Planned / in progress (not live)
Laravel/MySQL migration plan for shared hosting (plan only).

#### Example visitor questions & answers
- **Is this a product I can buy?** No, it is our internal tool; the portfolio shows a simulated version.
- **Does it use AI?** Yes, Gemini analyzes proposals and drafts emails.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/agentix-crm/walkthrough.

#### Related projects
Santure AI CRM is a larger operations concept; LeadForge could feed leads.

#### Verification notes
Checked: schema, routes, pages, replit.md. Not run live. Missing: current production URL (not public), screenshots.

---

### Eurobrass CRM

**Slug:** `eurobrass-crm` · **Also known as:** EuroBrass CRM, Eurobrass portal · **Category:** CRM, Sales & Lead Intelligence / **Subcategory:** manufacturer and dealer CRM · **Status:** In development (Verified code; public corporate site and demo login verified)
**Client / owner:** Eurobrass (brass fittings manufacturer) · **Local folder:** `D:\Agentix Project\EuroBrass` · **Last activity:** 2026-09-10 (about 110 commits)

Safety note: the project's seed data contained real client names; this KB uses none. Use only fictional examples.

#### Spoken introduction
The Eurobrass CRM runs sales for a brass fittings manufacturer: leads, dealers, a product catalogue, quotations, orders, inventory and service tickets. The public site presents the foundry and has a demo login.

#### Quick overview
It started as a frontend-only click-through demo and is moving to a real Supabase-backed system. Modules cover leads on a Kanban, customers by segment, a dealer network with a dealer portal view, products with series and finishes, a quotation builder with GST math and simulated send, orders, inventory, service tickets and technicians, employees, roles and permissions, audit log, analytics and reports.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Corporate site | https://eurobrass-seven.vercel.app/ | Public site | Verified: "Precision Brass Foundry and Machine Works, Est. 1974", process cast, machine, finish; six product lines |
| Login | https://eurobrass-seven.vercel.app/login | Safe demo environment | "Sign in to the CRM" with a "Continue as Demo User" button |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/eurobrass-crm/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/eurobrass-crm/walkthrough | Safe demo | Quotation to order |

#### Target users & business problem
Sales managers, executives, dealers, service technicians and auditors of a manufacturer who sells through dealers and projects. Problem: quotes, orders, dealers and service tracked in spreadsheets.

#### Features (complete inventory)
Evidence: `app/(app)/*` routes, `features/*`, `types/*`, design specs in `docs/superpowers/specs`.

**Dashboard (Verified).** `/dashboard`. **Analytics (Verified).** `/analytics`. **Reports (Verified).** `/reports` with date range filters (today, week, month, quarter, year, custom).
**Leads (Verified).** `/leads` Kanban with stages New, Contacted, Quoted, Negotiation, Won, Lost; create and edit manually; card and form dialogs.
**Customers (Verified).** `/customers`, `/customers/[id]`: segments (Architects, Builders, Hotels, Hospitals, OEM), order value, remarks, billing details, history.
**Dealers (Verified).** `/dealers`: business-model classification (Factory OEM, Channel OEM and others), create and edit. **Dealer portal (Verified).** `/dealer-portal`: portal-style view.
**Products (Verified).** `/products`, `/products/[id]`: series, finishes, SKUs; CSV product import with tests.
**Quotations (Verified).** `/quotations`, `/quotations/new`, `/quotations/[id]`: line items, GST math, statuses Draft, Sent, Approved, Converted, Rejected, simulated send by email, WhatsApp or PDF.
**Orders (Verified).** `/orders`: statuses Confirmed, In Production, Dispatched, Delivered; payment status Unpaid, Partially Paid, Paid; views by client, category and dealer.
**Inventory (Verified).** `/inventory`. **Service (Verified).** `/service`: tickets Open, Assigned, In Progress, Resolved, Closed and technicians.
**Employees, roles, audit, notifications, settings (Verified).** `/employees`, `/roles` (permission matrix per module: view, create, edit, remove), `/audit`, `/notifications`, `/settings`.

#### Key workflows (end to end)
1. Enter through the demo gate or real login.
2. Capture a lead, qualify it, assign it, move it through stages.
3. Build a quotation from the catalogue with GST; send (simulated) by email, WhatsApp or PDF.
4. Convert an approved quotation to an order; track production, dispatch and payment.
5. Raise service tickets for installed products and assign technicians.
6. Review dashboards and audit log.

#### User roles & permissions
Seeded roles: Administrator, Sales Manager, Sales Executive, Service Technician, Dealer, Auditor (read-only), each with a per-module permission matrix. Enforcement is planned (see below).

#### Technical architecture & integrations
Next.js App Router, React, TypeScript, Tailwind, shadcn/ui, Framer Motion, Zustand with localStorage persistence, Recharts, React Hook Form and zod, Vitest tests. Supabase foundation (migrations 0001 to 0005 for reference data, customers, sales, operations) with a mapping layer and product import was added in September 2026. Hosted on Vercel.

#### Business value & example scenarios
Faster quoting and one view of dealers and orders. Scenario: a dealer in "Northfield Hardware" requests a quote for a polished valve series; the sales executive builds it, sends it, and converts it to an order after approval.

#### Planned / in progress (not live)
Per the 2026-09-09 spec: Supabase server components migration (1b), enforced roles with region scoping (2), write-side gaps like product management, deletes, direct orders, employee CRUD and working audit log (3), cross-CRM search, tasks, file attachments (4). The Projects module was removed.

#### Example visitor questions & answers
- **Can I try the CRM?** The login page has a demo user button; the portfolio has a safe simulated version.
- **Does it send real quotations?** Sending is simulated in the demo.
- **Who are the roles?** Admin, sales manager, sales executive, technician, dealer, auditor.

#### Related projects
REDUX platform for the same client (another part) is a broader multi-product system; Agentix CRM is internal.

#### Verification notes
Checked: public site and login page, route tree, specs, types. Not verified: whether the live login uses real Supabase auth or the demo gate today. Missing: confirmation of which data the live deployment holds.

---

### LeadForge

**Slug:** `leadforge` · **Also known as:** lead-research-platform · **Category:** CRM, Sales & Lead Intelligence / **Subcategory:** AI lead research with provenance · **Status:** In development, phase 3 of 11 (Verified from PROGRESS.md and PHASES.md; no public URL)
**Client / owner:** AI Agentix · **Local folder:** `D:\Agentix Project\lead-research-platform` · **Last activity:** 2026-10-14 (about 130 commits)

#### Spoken introduction
LeadForge turns a plain-English request like "dental clinics in Delhi with a website" into a researched, deduplicated list of businesses, where every value shows its source and confidence. It is under active development and not yet public.

#### Quick overview
Describe the leads you need; the system compiles an editable research spec, discovers candidates from open and licensed sources, crawls their websites politely, extracts contact data, merges duplicates, and stores each field with provenance. The long-term product exports to Sheets, Excel, CSV or CRMs and bills in credits in INR.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| App | None | n/a | In development, internal |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/leadforge/overview | Safe demo | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/leadforge/walkthrough | Safe demo | Sentence to criteria chips to progress to leads table |

#### Target users & business problem
Indian SMB sales teams, agencies, consultants and founders prospecting local businesses, SaaS or hiring-signal leads. Problem: static databases are stale and unsourced.

#### Features (complete inventory)
Evidence: `docs/00-PRODUCT-BRIEF.md`, `phases/PHASES.md`, `PROGRESS.md`, `apps/web` pages, `services/workers`, `DEMO.md`.

**Built (Verified).**
- Sign up, login and onboarding; app pages: dashboard, new research, research history, research job detail.
- Natural-language research compiled into a ResearchSpec; job runs with live progress.
- Discovery from an open dataset (Overture Maps release on local disk, per decision ADR-0017) rather than paid APIs; a Delhi run returned 225 unique candidates with 13,663 values and no provenance gaps in about six minutes at zero credits.
- Crawling and extraction (phase 3 in progress): polite crawler, sitemap handling, raw page store with retention, JSON-LD and text extractors, phone normalisation, email validation and MX lookup, best-value selection, and a golden corpus of 50 labelled sites with 95.2 percent recall and zero false positives (2026-10-14).
- Provenance: every field value carries source URL, time and confidence; lead drawer shows grouped fields including technology.
- Admin area: connectors health, jobs and job detail, orgs, users, crawl health panel with metrics.
- Credits model: free plan with 50 credits, a standard lead costs 3 credits, quick depth 1 (per DEMO.md).

**Planned (not live):** see below.

#### Key workflows (end to end)
1. Sign in; type a request.
2. Review the parsed spec and credit estimate; start the job.
3. Watch discovery, crawl and extraction stream results into a table.
4. Open a lead and see source, time and confidence per value.

#### User roles & permissions
Customer users and organisations; a staff-only admin area gated by an audited function. Further roles not documented in detail.

#### Technical architecture & integrations
Monorepo (pnpm, Turbo): Next.js web app, API service, Python workers (crawl, extraction), Supabase Postgres with RLS and pg_cron, Redis, contract package. Deployed via Docker compose on a VPS. External: Overture Maps data, DNS lookups; Google Places is optional and was not funded.

#### Business value & example scenarios
Fast sourced prospect lists. Scenario: a marketing agency asks for gyms in Pune with a website and gets a list where each phone number links to the page it came from.

#### Planned / in progress (not live)
Phases 4 to 11: lead database and verification, enrichment, AI research and scoring, export and Sheets and billing for paid beta, automation and public API, CRM integrations (including Zoho), scaling, commercial launch. Phase 3 remaining: browser fetcher, page classifier, LLM extraction.

#### Example visitor questions & answers
- **Is LeadForge available?** Not yet; it is in development at phase 3 of 11.
- **What makes it different?** Every value shows where it came from and how sure we are.
- **Does it scrape social networks?** No; it avoids logged-in or protected views by policy.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/leadforge/walkthrough (simulated).

#### Related projects
Could feed Agentix CRM, AGENTiX leads and campaigns.

#### Verification notes
Checked: briefs, phases, progress log, web page tree. Not run. Missing: any deployed URL or recording.

---

### Santure AI CRM

**Slug:** `santure-crm` · **Also known as:** Santure AI operations platform · **Category:** CRM, Sales & Lead Intelligence / **Subcategory:** multi-brand operations prototype · **Status:** Prototype (Partially verified: page description and bundle strings read; not interactively run)
**Client / owner:** Santure AI (internal group) · **Local folder:** none (Claude artifact) · **Last activity:** artifact version 1793019894 (about late 2026)

#### Spoken introduction
Santure AI CRM is an interactive prototype of one operations platform for every team and brand at Santure AI, covering sales calling, orders, dispatch, inventory, accounts and agency delivery, all with demo data.

#### Quick overview
The page description reads: "one operations platform for every team and brand at Santure AI. Interactive prototype with demo data." The bundle shows a call-centre-style sales funnel for several D2C brands plus back-office and agency modules.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Prototype | https://claude.ai/artifact/1aWGMS5ETqSCp4f1SV5JLD | Safe demo environment | Claude artifact; demo data |
| Portfolio | https://agentix-portfolio.vercel.app/#/demo/santure-crm/overview | Safe demo | Embed or preview (tier C) |

#### Target users & business problem
Founders, sales callers, dispatch, accounts, HR and agency managers across several brands. Problem: each team and brand uses separate sheets and tools.

#### Features (complete inventory)
Evidence: strings extracted from the artifact's JavaScript bundle (Partially verified; labels only, behaviour not exercised).
- **Lead center and lead funnel:** sources listed as a WhatsApp automation platform, Meta lead ads, Google Ads lead forms, Shopify store, website forms, Google Sheets and CSV upload; funnel states from leads received through assigned, call attempted, connected, not interested, follow-ups, interested, orders created, confirmed by dispatch, delivered (verified) and fully paid.
- **Distribution and reshuffle:** allocate fresh leads to callers, caller load, lead rules.
- **Callers:** checkpoint reminders at 12, 2, 4 and 6, end-of-day report, follow-ups, my orders, my day.
- **Orders, dispatch, inventory and packing:** confirm orders, courier AWB and pickup, stock, production, handover.
- **Accounts:** invoices, to-pay, collections, budgets, compliance reminders, CA pack.
- **Reports and AI daily summary:** "Written by AI from today's numbers".
- **HR and people:** attendance from portal check-ins, appraisals.
- **Agency delivery:** proposals, pipeline, campaigns, approvals, dev board, deployments, freelancers, client changes, team board, tasks.
- **Voice agents:** a voice-agent page exists.
- **Brand pages:** per-brand views for a set of AI Agentix client brands.
- **Automations list:** attempt-limit rule, checkpoint reminders, low-stock alert, overdue follow-up nudge, approval reminder, courier status sync, incentive on delivered orders.
All people names in the bundle are demo data and are not reproduced here.

#### Key workflows (end to end)
Inferred: lead arrives, distribution assigns a caller, caller attempts and records status, order is created, dispatch confirms and ships, delivery is verified, accounts reconcile.

#### User roles & permissions
Role-oriented views (founder, callers, dispatch, accounts) appear in the bundle; exact permission model not verified.

#### Technical architecture & integrations
React single-page app bundled with Vite inside a Claude artifact; no backend; demo data only. Integrations named are illustrative (courier sync, Meta, Google).

#### Business value & example scenarios
Shows how one platform could replace scattered sheets. Scenario: a Meta lead for "Brand A" is auto-assigned, called at the 12 o'clock checkpoint, ordered, and dispatched.

#### Planned / in progress (not live)
Prototype only, not a deployed product.

#### Example visitor questions & answers
- **Is it a real product?** It is a clickable prototype with demo data.
- **What teams does it cover?** Sales calling, dispatch, inventory, accounts, HR and agency delivery.
- **Where is it?** The Claude artifact link above.

#### Related projects
Agentix CRM (real internal tool), Ekatva (sector-specific prototype).

#### Verification notes
Checked: artifact metadata and bundle strings. Not verified: screens visually, data model. Missing: screenshots or a run-through.

---

### Ekatva

**Slug:** `ekatva` · **Also known as:** Ekatva Prototype · **Category:** CRM, Sales & Lead Intelligence / **Subcategory:** insurance and wealth distributor platform · **Status:** Prototype (Partially verified: description and bundle module names read)
**Client / owner:** Ekatva (concept/prospect) · **Local folder:** none (Claude artifact) · **Last activity:** artifact version 1792356201

#### Spoken introduction
Ekatva is an interactive prototype of a relationship and operations platform for insurance and wealth distributors, built with fictional data. It covers households, policies, renewals, wealth products, service and more.

#### Quick overview
Per the page description: "relationship and operations platform for insurance and wealth distributors. Interactive prototype with fictional demo data." The code is split into role homes and about thirty pages.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Prototype | https://claude.ai/artifact/SPtLCBo9RcGfjE1FMAdwiw | Safe demo environment | Claude artifact; fictional data |
| Portfolio | https://agentix-portfolio.vercel.app/#/demo/ekatva/overview | Safe demo | tier C |

#### Target users & business problem
Insurance and wealth distribution firms: relationship managers, service desks, policy operations, renewals and accounts teams. Problem: client relationships, policies, renewals and servicing are scattered.

#### Features (complete inventory)
Evidence: code chunk names in the artifact bundle (Partially verified; names only).
- **Role homes:** operations, service desk, life insurance, wealth, mutual fund service, relationship manager, renewals, policy operations, service, quality, accounts, front office (with business card scan) and field (with route map and My Day).
- **Pages:** households and Household 360, leads and lead detail, opportunities, reviews, policies (new policy, policy detail), renewals, quotations and quotation builder, service, wealth, inbox, campaigns, calendar, calls, documents, approvals, team, office, reports, automations, client portal preview, settings, loans, work log, events, insights, bot flows, front desk, field, finance, referrals, performance, client health, feedback, status.
- **Other:** checkup booking, wallets, renewal modals and policy utilities.
Behaviour of each page was not exercised.

#### Key workflows (end to end)
Inferred only: lead to quotation to policy to renewal tracking, with households as the central record.

#### User roles & permissions
Role-based home screens (see above). Exact permissions not verified.

#### Technical architecture & integrations
React (Vite) single-page app inside a Claude artifact, about 263 published files, code-split by page; fictional data; no backend.

#### Business value & example scenarios
Gives distributors one household-centred view. Scenario: a renewal due in 30 days for a fictional household "Rao family" triggers a reminder and a quotation for upgrade.

#### Planned / in progress (not live)
Prototype only.

#### Example visitor questions & answers
- **What is Ekatva?** A prototype platform for insurance and wealth distributors.
- **Is the data real?** No, fictional demo data.
- **Where can I try it?** The Claude artifact link above.

#### Related projects
Santure AI CRM, Agentix CRM, Eurobrass CRM (other CRM builds).

#### Verification notes
Checked: artifact metadata and bundle structure. Not verified: UI, data, flows. Missing: screenshots or a run-through, and whether Ekatva is a real client or a concept.



Scope of this part: eight AI Agentix projects, grouped under three category headings (Healthcare Systems, Hospitality, Fitness).

Conventions used in every project section below:
- **Safe demo — fictional data, all actions simulated** is the label for the AI Agentix portfolio demos. Portfolio base URL: https://agentix-portfolio.vercel.app/ (planned hosted URL). Project demo: `/#/demo/<slug>`; tabs: `/overview`, `/walkthrough`, `/how`, `/screens`, `/tech`; module deep link: `/#/demo/<slug>/walkthrough/<moduleId>`.
- Status labels: **Verified**, **Partially verified**, **Unverified**, **Unavailable**. An "Evidence:" line follows each feature group.
- No credentials, keys, real people, real patients, members or guests, or real phone numbers appear here. All examples are fictional. Nothing here is medical advice; clinical items describe software features only.
- Live-URL types: Production (real business, do not perform actions), Public site, Safe demo, Login required.

---

## Healthcare Systems

### Agentix HIMS

**Slug:** `agentix-hims` · **Also known as:** Government HIMS, "kailash-hms-prototype" (package name), AI-first Hospital Information Management System · **Category:** Healthcare Systems / state-scale hospital information system · **Status:** Prototype with a public demo deployment (Verified)
**Client / owner:** AI Agentix (own product, aimed at government and multi-hospital health systems) · **Local folder:** `D:\Agentix Project\Gov-HIMS` · **Last activity:** 2026-09-02 (129 commits)

#### Spoken introduction
Agentix HIMS is our AI-first hospital information system, designed for state-scale public health in India. It gives every hospital team, from doctors and nurses to pharmacy, lab, billing and the blood bank, its own role portal, and gives health leaders a live cockpit over the whole state. You can try it in the portfolio demo, where one fictional patient moves from triage to discharge.

#### Quick overview
Agentix HIMS is a Next.js web application with one console per role: more than 24 staff and patient portals covering clinical care, operations, finance, management and support services. A patient record flows between departments, so triage, consultation, lab, pharmacy, billing and discharge stay in sync. AI assists with decision support (triage scoring, early-warning scores, drug-safety checks, sepsis watch), but deterministic safety rules sit underneath it and a human accepts or rejects AI suggestions. Two government cockpits, for the Chief Medical and Health Officer (CMO, district level) and the Health Secretary (state level), roll everything up into district rankings and approvals. It solves the problem of disconnected departments and leadership with no live picture.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Public landing + role picker | https://government-hims.vercel.app/ | Safe demo environment (public) | The landing says "Demo environment, pick a role to explore". Seeded fictional data. Includes a public patient self check-in kiosk. |
| Role sign-in | https://government-hims.vercel.app/login | Login required (demo) | Launcher cards go to a login per role; the landing page states any credentials work in the demo. No credentials are listed here. |
| Public patient check-in kiosk | https://government-hims.vercel.app/checkin | Public | Self check-in and intake flow, no login. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/agentix-hims | Safe demo, fictional data, all actions simulated | Interactive tier-A demo. |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/agentix-hims/walkthrough | Safe demo | Module picker. |
| Module: patient journey | https://agentix-portfolio.vercel.app/#/demo/agentix-hims/walkthrough/journey | Safe demo | Triage to discharge for one fictional patient. |
| Module: doctor workspace | https://agentix-portfolio.vercel.app/#/demo/agentix-hims/walkthrough/doctor | Safe demo | |
| Module: Health Secretary cockpit | https://agentix-portfolio.vercel.app/#/demo/agentix-hims/walkthrough/secretary | Safe demo | District ranking view. |
| Module: CMO cockpit | https://agentix-portfolio.vercel.app/#/demo/agentix-hims/walkthrough/cmo | Safe demo | |
Other portfolio module ids: `nurse`, `emergency`, `lab`, `pharmacy`, `beds`, `ot`, `bloodbank`, `billing`, `coo` (Admin command centre), `patient` (Patient portal), `audit` (NABH audit trail).

#### Target users & business problem
Government and large hospital networks where patient journeys stall between disconnected departments, and where state and district leadership lack a live operating picture. Users are clinicians, nurses, pharmacy and lab staff, billing and insurance desks, hospital administrators, and health officials. Patients use a patient portal and a public family-tracking page.

#### Features (complete inventory)
Status for the project: **Partially verified** (source code and public landing seen; staff portals not entered live; docs contain differing counts, see Verification notes).

**1. Role portals and navigation** · Status: Verified · Evidence: `src/app/<role>/*` route tree, `PROJECT-OVERVIEW.md` role table, live landing text "29 role-based consoles".
- What: a launcher shows roles grouped by Clinical (6), Operations (4), Finance (2), Management (7), Support Services (7), Patient (1) and Government (2). Each role has its own layout, dashboard and sidebar. The live landing counts 29 consoles; older docs describe 24 original roles plus a patient portal.
- How the user interacts: pick a role on the landing, sign in (demo: any credentials), and land on that role's dashboard. A role guard prevents opening other roles' pages.
- Dependency: the same patient record and cross-module audit log are used by all portals.

**2. Doctor portal** (`/doctor/*`: dashboard, consultation, schedule, ipd and ipd/[id], online, records, registries, emergencies, inbox, beds, analytics, ai-assistant, settings) · Status: Verified (code)
- OPD workspace, inpatient (IPD) command, online consultation, patient records, disease registries, an inbox, schedule, and analytics.
- AI pre-brief summarises a patient before a consult; drug-safety gating checks allergies and interactions when prescribing; a voice scribe is described in docs; an AI copilot floats on screen (suggestion with confidence, reasoning, accept/modify/reject).
- Limitations: AI services are largely simulated or mock functions in the original prototype (see Technical architecture).

**3. Nursing station** (`/nurse/*`: dashboard, patients, patients/[id], vitals-requests, tasks, rounds, medication, fluid-balance, handover, orders, messages, ai-assistant) · Status: Verified (code)
- Vitals capture, medication administration record (MAR), fluid balance, rounds, shift handover, tasks. Early-warning (NEWS2-style) escalation is a documented feature.

**4. Emergency room** (`/emergency/dashboard, floor, triage`) · Status: Verified (code)
- ER floor board and triage with ESI levels 1 to 5 (the portfolio demo shows an ESI Kanban). Sepsis alerts and trauma tracking are described on the landing and docs.
- Limitation: documentation notes ER triage severity was set manually in the original prototype rather than by the rules engine module.

**5. Laboratory** (`/lab/*`: dashboard, inbox, in-queue, benches, phlebotomy, verify, qc, reflex, microbiology, reports, analyzer-feed) · Status: Verified (code)
- Five-bench routing (haematology, biochemistry, immunology, urine, microbiology), multi-technician claim, QC gating, verification chain, reflex tests, and a multi-day microbiology workflow. A critical-value check exists in the rules engine.

**6. Radiology** (`/radiology/*`: dashboard, orders, arrival, in-queue, bench, reading, verification, critical, distribution, schedule, scans, templates, viewer, reports, analytics, ai-command, inbox) · Status: Verified (code)
- A full RIS-style command centre: orders, scan arrival, reading worklist, templated reports, critical-finding alerts, report distribution, and an image viewer.

**7. Pharmacy** (`/pharmacy/*`: dashboard, queue, inventory, master, narcotics, messages) · Status: Verified (code)
- Unified tagged queue (OPD, IPD, OT, ICU, discharge), claim model, bedside dispense, inventory and drug master, narcotics log. Dispensing checks allergy blocks and drug interactions.

**8. Reception** (`/reception/*`: dashboard, register, opd, queue, appointments, patients, beds, billing, diagnostics, referrals, tpa, ambulance, journey, messages, reports, downloads, setup) · Status: Verified (code)
- Registration, OPD queue, appointments, referrals, TPA, ambulance requests and a journey tracker per patient.

**9. Admission, discharge and OT** (`/admission/dashboard, beds, forecast`; `/discharge/dashboard, summary/[id]`; `/ot/dashboard, schedule, checklist`) · Status: Verified (code)
- Bed allocation and forecast, discharge summaries with human review, OT scheduling with a WHO-style checklist that blocks proceeding while critical items are pending.

**10. Billing and insurance** (`/billing/dashboard, discounts, packages, refunds, patient/[id]`; `/insurance/dashboard, claims, documents, pipeline, preauth`) · Status: Verified (code)
- Patient ledgers, packages, discounts, refunds, and an insurance pipeline with pre-authorisation. The landing and portfolio describe AB-PMJAY (government scheme) handling and ABHA identity as native, with pre-auth shown with a denial-risk score. Real submission to the government platform is not verified.

**11. Management and support services** · Status: Verified (code)
- Admin command centre (`/admin/*`): staff directory and onboarding, credentials and licence expiry, roster and shifts, coverage and sick-call workflow, finance (P&L, reconciliation, disputes), compliance cockpit (NABH, DISHA/DPDP audit, statutory calendar), AI performance dashboard, vendors, payroll, settings.
- Quality and safety (`/quality/*`: dashboard, incidents, NABH), audit officer (`/audit/*`), housekeeping, inventory, HR (`/hr/*`: employees, attendance, leave, recruitment, appraisals, onboarding), vendor manager (`/vendor-manager/*`: contracts, purchase orders, payments, performance).
- Blood bank (donors, inventory, requests), CSSD (instruments, cycles), dietary (plans, orders), bio-medical waste (log, reports), mortuary (records, clearances), ambulance (dispatch, log), feedback (responses, AI insights).

**12. Patient portal and public pages** (`/patient/*` about 25 pages; `/p/[uhid]`, `/family-track/[token]`, `/consent/[token]`, `/journey/[patientId]`, `/discovery`, `/abha`) · Status: Verified (code)
- Patient dashboard, appointments, queue and waiting status, teleconsult, medications, pathology and radiology results, records, billing, insurance, discharge, follow-up, feedback, AI care assistant, health story, downloads. Public pages let families follow a patient and let patients give consent via a tokenised link.

**13. Health Secretary cockpit** (`/secretary/*`: home, districts and districts/[id], ranking, mobilization, cabinet, niti-abdm, ayush, dme, cag-audit, fraud, mch, schemes, supply, surveillance, workforce, approvals, alerts, beds, emergency, quality, communication, ai-assistants, reports, audit-log) · Status: Verified (code, build spec)
- State-wide cockpit; the build spec calls district ranking "the killer feature" and defines five demo-star screens (home, map and district ranking, inter-district mobilisation, cabinet and assembly drafter, NITI Aayog and ABDM dashboard). Hindi labels appear alongside English.
- Limitation: the spec states data for this cockpit is mock.

**14. CMO cockpit** (`/cmo/*`: alerts, approvals, beds, ambulance, communication, disease-programs, emergency, equipment, facilities, field-visits, grievances, mch, postings, quality, reports, schemes, staff, supply, surveillance, ai-assistants, audit-log, profile, settings) · Status: Verified (code, build spec)
- District-level cockpit with 24 menu items: alerts, approvals, bed network, ambulance command, field visits, grievances, surveillance.

**15. AI layer and safety rules** · Status: Verified (docs and code)
- About 40 AI service functions, each returning an envelope with confidence, tier, reasoning and a "requires review" flag. A human-in-the-loop review card (accept, modify, reject with reason) logs every decision to the audit trail; thumbs up/down feedback feeds an AI-performance dashboard.
- Seven deterministic rules modules sit beneath the AI: triage thresholds, drug interactions, allergy block, dosage bounds, critical lab values, OT proceed-gate and billing math. Documentation notes the rules engine was only partly wired into the UI at the time it was written.
- A shadow mode can show suggestions with actions disabled.

**16. Compliance and audit** · Status: Verified (docs and code)
- A single audit fan-in records meaningful actions, mapped to the nine NABH chapters; consent and DPDP/DISHA scoring, BMW (bio-medical waste) logs, and statutory calendar items.

**17. Language support** · Status: Verified. English and Hindi (next-intl), toggle on the landing.

#### Key workflows (end to end)
1. Open the landing page and choose a role (or the patient self check-in kiosk).
2. Registration or kiosk intake creates the patient record (ABHA is shown as a native identity option).
3. Triage scores risk (ESI levels, NEWS2-style warning score) and routes the patient to OPD, emergency or admission.
4. The doctor reviews the AI pre-brief, consults, and orders labs, imaging and medicines. Drug-safety checks gate the prescription.
5. Lab and radiology fulfil orders; critical values raise alerts; results appear on the doctor and patient portals.
6. Pharmacy dispenses with allergy and interaction checks; billing builds the bill or an insurance pre-authorisation.
7. Admission and bed management, nursing rounds, OT checklist, then discharge with a reviewed summary and a follow-up.
8. Every action emits an audit event; outcomes roll up to the CMO and Health Secretary cockpits.
In the portfolio demo, "Patient journey" replays this flow for a fictional cardiac patient with simulated outcomes.

#### User roles & permissions
Roles in code (verified): doctor, nurse, pharmacy, lab, radiology, emergency, reception, bed manager (admission), discharge, OT, billing, insurance, admin (COO), quality, housekeeping, inventory, blood bank, CSSD, dietary, BMW, mortuary, ambulance, audit officer, HR, vendor manager, patient, CMO, Health Secretary (the live landing counts 29). A role guard shows each role only its own portal. Fine-grained permission matrix details were not enumerated beyond the admin RBAC matrix mentioned in the docs.

#### Technical architecture & integrations
- Frontend: Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4, Zustand state stores, Framer Motion, Recharts, next-intl, react-hook-form with Zod. (Verified: package docs.)
- Backend: the original prototype was frontend-only with in-memory stores and mock APIs. A 2026-07-13 architecture document and the repo's `supabase/migrations` show a later move to Supabase (Postgres with row-level security, auth users per role, realtime, API route handlers for OPD queue and orders). The doc itself marks what is "NOW" versus "TARGET". Status: Partially verified.
- Integrations: mock WhatsApp send and webhook routes; ABHA, Aadhaar and AB-PMJAY shown as simulated; voice text-to-speech and an AI completion route exist. External government integrations are not verified as live.
- Hosting: Vercel. Environment configuration (names only): Supabase URL and keys, AI provider key.
- Known limitations (from the project's own CTO review): backend gaps, concurrency control, multi-tenancy and real authentication were listed as target-state items at 2026-06; the marketing badges on the landing (NABH-ready, ABDM/DISHA, ISO 27001, HL7/FHIR) are landing-page claims, not certifications verified by us.

#### Business value & example scenarios
Replaces separate department software and paper with one patient record; reduces re-entry; surfaces risk early; gives officials a district-level view. Scenario 1: a fictional patient "Meera Joshi" arrives with chest pain at a district hospital; triage flags high acuity, the lab confirms a result, the pharmacy catches an interaction, and billing prepares a scheme pre-authorisation. Scenario 2: a fictional Health Secretary opens the district ranking, filters the bottom five districts and drills into one.

#### Planned / in progress (not live)
The architecture review lists multi-hospital tenancy, full real-time, transactions and crore-scale infrastructure as target-state; real government integrations (ABDM, NHA) are not claimed as live.

#### Example visitor questions & answers
- **What is Agentix HIMS?** An AI-first hospital information system with a console per role, plus state and district cockpits.
- **How many roles does it have?** The live landing shows 29 consoles; early docs list 24 roles plus a patient portal.
- **Is it live in a hospital?** No. It is a prototype with a public demo environment and fictional data.
- **Does the AI make clinical decisions?** No. It suggests, shows confidence and reasoning, and a human accepts, modifies or rejects; deterministic safety rules sit underneath.
- **Can I see a demo?** Yes: https://agentix-portfolio.vercel.app/#/demo/agentix-hims (safe demo, fictional data) or the public demo at https://government-hims.vercel.app/.
- **What is the difference from Umang Hospital HIMS?** Umang HIMS is a smaller single-hospital OPD system extracted from this one.
- **Does it support Hindi?** Yes, English and Hindi.
- **Which government schemes does it mention?** ABHA, AB-PMJAY, ABDM and NABH audit mapping, shown as simulated in the demo.

#### Related projects
Umang Hospital HIMS (`umang-hims`) is a single-hospital OPD extraction of this system. Woodpecker PMS is the hospitality sibling in method (role portals, folio billing).

#### Verification notes
Checked: repository structure, PROJECT-OVERVIEW, README, CTO review, 2026-07-13 architecture doc, route tree (about 260 pages), live landing text. Not verified: any signed-in portal on the live site; whether current deployment reads from a live database or in-memory demo data; real integrations. Missing: a current screenshot set and a statement from the owner on whether the deployed demo is database-backed.

---

### Umang Hospital HIMS

**Slug:** `umang-hims` · **Also known as:** Umang OPD system · **Category:** Healthcare Systems / single-hospital OPD system · **Status:** Prototype (Partially verified)
**Client / owner:** Umang Hospital (extracted from Agentix HIMS) · **Local folder:** `E:\Umang Hospital HIMS` · **Last activity:** 2026-09-07 (94 commits)

#### Spoken introduction
Umang Hospital HIMS follows an outpatient visit from registration to pharmacy on one live record. A patient can register by form or by talking to a voice agent called Asha, and anyone can follow the visit status on a public tracker. It works in English and Hindi.

#### Quick overview
It is a Next.js application extracted from the larger Agentix HIMS and trimmed to the outpatient (OPD) journey of a single private hospital: registration, reception queue, nurse vitals, doctor consultation with prescriptions and orders, billing and pharmacy. Six staff and patient consoles are live on the demo. It is backed by a real Postgres database through Supabase rather than a mock. It solves paper slips and unclear waiting by keeping every desk on the same visit record.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Public landing + role picker | https://umang-hospital-hims.vercel.app/ | Public site, demo; login required for consoles | Landing says six role-based consoles. Demo accounts exist (per the README); credentials are not listed here. |
| Staff/patient sign-in | https://umang-hospital-hims.vercel.app/login | Login required | |
| Patient self check-in kiosk | https://umang-hospital-hims.vercel.app/checkin | Public | |
| Public live visit tracker | https://umang-hospital-hims.vercel.app/p/<UHID> | Public | Needs a visit identifier; no login. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/umang-hims | Safe demo, fictional data, all actions simulated | |
| Walkthrough | https://agentix-portfolio.vercel.app/#/demo/umang-hims/walkthrough | Safe demo | |
| Module: register | https://agentix-portfolio.vercel.app/#/demo/umang-hims/walkthrough/register | Safe demo | Form or Asha voice agent. |
| Module: public tracker | https://agentix-portfolio.vercel.app/#/demo/umang-hims/walkthrough/tracker | Safe demo | |
| Module: doctor | https://agentix-portfolio.vercel.app/#/demo/umang-hims/walkthrough/doctor | Safe demo | |
Other module ids: `reception`, `nurse`, `billing`, `pharmacy`, `reports`.

#### Target users & business problem
A single private hospital's OPD: reception staff, nurses, doctors, billing and pharmacy counters, and patients and their families.

#### Features (complete inventory)
Status for the project: **Partially verified** (code and README read, public landing seen; signed-in screens not seen).

**1. Registration** (form, kiosk and the "Asha" voice agent) · Status: Verified (code, README) · Evidence: `/checkin`, `/api/intake/turn`, `/api/voice/tts`, `lib/intake`.
- A patient fills a form or talks to Asha, a voice registration agent built with an AI language model and text-to-speech. If the premium voice is unavailable it falls back to the browser voice. Aadhaar verification is mocked; the ABHA flow was removed on 2026-09-07 per git history.

**2. Reception** (`/reception/*`: dashboard, register, queue, opd, appointments, patients, billing, messages, reports, journey, downloads, setup) · Status: Verified (code)
- Walk-in registration, OPD queue and check-in, appointments, reporting. Limitation (README): appointments do not persist to the database and live in browser state only.

**3. Nurse** (`/nurse/*`: dashboard, patients, patients/[id], vitals-requests, tasks, messages, ai-assistant) · Status: Verified (code)
- OPD vitals capture and patient worklist.

**4. Doctor** (`/doctor/*`: dashboard, consultation, schedule, records, inbox, analytics, ai-assistant, settings) · Status: Verified (code)
- Consultation, prescriptions, lab and imaging orders. Limitation (README): lab and radiology fulfilment portals were removed, so orders are created and visible but nothing runs the test. Teleconsult was cut on both sides.

**5. Billing** (`/billing/*`: dashboard, patient/[id], packages, discounts, refunds) · Status: Verified (code)

**6. Pharmacy** (`/pharmacy/*`: dashboard, queue, inventory, master, narcotics, messages) · Status: Verified (code)
- Carries prescriptions through queued, preparing, ready and collected.

**7. Patient portal** (`/patient/*` about 20 pages) and **record claim** (`/claim`) · Status: Verified (code, README)
- A patient claims an existing record by UHID, phone and full name to create a portal account. The README explicitly calls this demo-grade assurance, not identity proofing. Billing is real per README; the dashboard's clinical cards are front-end simulation.

**8. Public live visit tracker** (`/p/[uhid]`) · Status: Verified (code, README) · The status advances Registered, Vitals, Consult, Prescription, Pharmacy ready.

**9. Bilingual UI** (English and Hindi). Status: Verified.

**10. WhatsApp routes** (mock send and webhook). Status: Verified (code); real sending not verified.

#### Key workflows (end to end)
1. Landing page, then registration (form, kiosk or Asha).
2. Reception checks the patient in and places them in the OPD queue.
3. The nurse records vitals.
4. The doctor consults and writes prescriptions and orders.
5. Billing raises the bill; pharmacy dispenses.
6. The patient or family follows each step on the public tracker.
Permission handling: queue access is gated to staff and patients are scoped to their own row (git commit 2026-09-07).

#### User roles & permissions
Reception, nurse, doctor, billing, pharmacy and patient consoles are shipped. An admin role is recognised for seeding and operations scripts but has no UI.

#### Technical architecture & integrations
Next.js 16, React 19, TypeScript, Tailwind v4, Zustand, Supabase (Postgres with row-level security, auth, realtime), AI language model and ElevenLabs text-to-speech for the voice agent (credentials held as server environment variables), next-intl, Vercel. Voice and AI features need paid provider keys to go beyond the fallback.

#### Business value & example scenarios
Fewer paper slips and a patient who can see where they are in the visit. Scenario: fictional patient "Kavita Nair" registers by voice, is queued, has vitals taken, sees the doctor, and her tracker shows "Pharmacy ready".

#### Planned / in progress (not live)
Not documented as planned: lab and radiology fulfilment, teleconsult, appointment persistence, and ABHA verification are deliberately out of this build.

#### Example visitor questions & answers
- **Who is it for?** A single hospital's outpatient department.
- **What is Asha?** A voice registration agent that collects patient details by conversation.
- **Can patients see their progress?** Yes, on a public tracker.
- **Is the data real?** The deployed demo uses seeded demo accounts; the portfolio demo is fictional.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/umang-hims (safe demo).
- **How does it differ from Umang's website?** The website is public marketing and a CMS; HIMS is an internal workflow tool.
- **Does it handle labs?** Orders can be created; lab and radiology fulfilment is not part of this build.

#### Related projects
Agentix HIMS (parent, 29 consoles), Umang Hospital website and CMS (`umang-website`).

#### Verification notes
Checked: README, package metadata, route list, git log, live landing. Not verified: signed-in consoles (demo accounts exist but were not used), voice agent behaviour live. Missing: confirmation whether Umang Hospital uses this system day to day (treated as a prototype).

---

### Umang Hospital website + admin CMS

**Slug:** `umang-website` · **Also known as:** umanghospitals.in · **Category:** Healthcare Systems / hospital website with lead capture and CMS · **Status:** Live (Verified)
**Client / owner:** Umang Superspeciality Hospital, Gurugram · **Local folder:** `D:\Agentix Project\Umang2.0` · **Last activity:** 2026-10-28 (149 commits)

#### Spoken introduction
This is the website for Umang Superspeciality Hospital in Gurugram. Patients can browse specialities, find doctors, read health information and request an appointment, and the hospital team manages the content and sees every lead in an admin panel. It also tracks which ad campaigns the enquiries came from.

#### Quick overview
A large React single-page site (roughly 70 routes) served from Apache/cPanel, with a Supabase back end for leads and content. Public pages cover specialities, doctors, infrastructure, services (telemedicine, health checkups, cashless insurance, elder care, home care, lab diagnostics, buy medicines), a health library, patient corner and media centre. Forms store each enquiry with its campaign tags (UTM and click identifier) and email or WhatsApp-notify staff. It replaces a static brochure site and lets staff change content without a developer.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Main site | https://www.umanghospitals.in/ | Production (real hospital; do not submit forms) | Public site, HTTP 200 checked. |
| Doctor search | https://www.umanghospitals.in/doctors | Production | |
| Specialities | https://www.umanghospitals.in/specialities | Production | |
| Cashless insurance | https://www.umanghospitals.in/cashless-insurance | Production | |
| Admin CMS login | https://www.umanghospitals.in/admin/login | Login required | Staff only. |
| Supabase proxy | https://umang-supabase-proxy.vercel.app | Infrastructure (not a page) | Pass-through used by the browser; see architecture. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/umang-website | Safe demo, fictional data, all actions simulated | A tier-B site preview. No interactive module file exists yet in the portfolio repo (js/demos/umang-website.js is absent), so only the overview link applies. |

#### Target users & business problem
Patients and families in Gurugram looking for a specialist, checkup, insurance help or a callback; hospital marketing and reception staff who need leads and content in one place; and a team running Google Ads who need to know which campaign produced which enquiry.

#### Features (complete inventory)
Status: **Verified** (code, live homepage load, changelog and developer handoff; admin not entered).

**1. Public site structure** · Evidence: `frontend/src/App.jsx` routes.
- Home with hero slides; About; Infrastructure (ICU units, OT, rooms, radiology, cafeteria, ambulance, help desk, parking); Specialities and per-speciality detail; Doctor search and doctor profile; Team (leadership, nursing, support staff); Careers; Gallery; Contact, emergency contact and an inquiry hub; Terms, privacy policy and a sitemap page.

**2. Services** (`/services/*`) · Telemedicine and consult booking; health checkup and checkup booking; lab diagnostics; buy medicines (categories and prescription upload); emergency; elder care; home care; second opinion; a generic service booking route; cashless insurance. Forms feed the leads table.

**3. Health library and patient corner** · Treatments, technologies and a virtual tour, ailments, knowledge centre, events and event registration, downloads; breakthrough cases, patient stories, blogs, podcasts, patient-information literature; media centre with press releases, coverage, newsletters and media connect. Note: the event registration form was flagged in Supabase notes as unbound inputs at one time.

**4. Lead capture** · Evidence: `src/api/api.js`, `supabase/migrations/0001_leads.sql`.
- Four lead types: callback, appointment, contact, insurance. Each stores name, phone, optional email and message, speciality, source page and an "extra" JSON block that includes campaign tags (utm source, medium, campaign, term, content and gclid) captured from the URL. Status values: new, contacted, converted, closed. A spam guard prevents duplicates and floods. A WhatsApp floating button is on every page.

**5. Google Ads landing page and thank-you pages** · A dedicated landing page (`/book-consultation`) and thank-you pages for conversion tracking; Google Ads tag and a Website Leads conversion were added 2026-08-12.

**6. Lead notifications** · A Supabase Edge Function (`notify-lead`) can send email through Resend and WhatsApp through Twilio on every new lead, if its secrets are set. Whether it is active in production is not confirmed.

**7. Admin CMS** (`/admin`) · Evidence: `frontend/src/admin/*`, `AdminLayout.jsx`.
- Sections: Dashboard (including native page-view analytics), Leads (view and update status, CSV archive then delete of old leads), Offers, Content, Hero Slides, Doctors, Specialities, Services, Testimonials, FAQs, Gallery, Media. Protected route with Supabase admin authentication. Content changes publish without code.

**8. Data retention** · Scheduled database jobs delete leads and page views older than six months (migration `0013_retention`).

**9. SEO and performance** · SEO head component and hospital JSON-LD schema, robots and sitemap, mobile hero image loop instead of video, lazy loading.

#### Key workflows (end to end)
1. A visitor lands (organically or from an ad) on the home or landing page.
2. They search specialities or doctors, or read service pages.
3. They submit a callback, appointment, contact or insurance form.
4. The browser writes the lead to the hospital's database; the campaign tags ride along in the lead.
5. Staff may be notified by email or WhatsApp; staff open `/admin/leads`, review, change status, add notes.
6. Content editors update doctors, offers and hero slides in the admin and the site reflects it.

#### User roles & permissions
Public visitors (can submit forms only); admin users via Supabase auth (database policies let the public insert leads only). Finer admin roles were not seen.

#### Technical architecture & integrations
- Frontend: React 18, Vite, Tailwind, deployed as static files on Apache/cPanel (the developer handoff notes a Vercel config too). A Laravel backend exists in the repo but the handoff states it was not deployed; Supabase is what the live forms and CMS use.
- Database and auth: Supabase Postgres with row-level security, `pg_cron` retention jobs, Edge Function for notifications.
- **Supabase proxy (change dated 2026-10-28):** browser Supabase traffic is routed through https://umang-supabase-proxy.vercel.app because some Indian internet providers hijack DNS for `*.supabase.co`, which caused "Failed to fetch" on admin login, lead forms and CMS content. The proxy is a pass-through rewrite that forwards every path, method and header, holds no secrets, and lives in the `supabase-proxy/` folder. A custom domain such as `api.umanghospitals.in` could replace it later.
- Framing: public pages may be framed by the AI Agentix portfolio (a content-security header allows it); the admin refuses framing.
- Environment names: `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY` (the anon key is public by design, protected by row-level security).

#### Business value & example scenarios
Visibility into which ad produced which enquiry and fewer lost callbacks. Scenario: a fictional visitor "Rohan Verma" clicks a Google Ad for a cardiology consult, submits a callback form, and the reception team sees the lead with the campaign name and calls back within the hour.

#### Planned / in progress (not live)
Per Supabase notes: a patient portal with login and appointments needing a dedicated phase; a Supabase custom domain to replace the proxy. Neither is live.

#### Example visitor questions & answers
- **Is the site live?** Yes, at https://www.umanghospitals.in/.
- **Can I book online?** The site collects appointment and callback requests; staff confirm.
- **Does it support insurance?** There is a cashless insurance page and form.
- **What is the proxy about?** It keeps the site working on networks that block Supabase.
- **Can I see a demo?** The live site is production; the portfolio overview is https://agentix-portfolio.vercel.app/#/demo/umang-website.
- **Who manages content?** Hospital staff through the admin CMS.
- **Does it track ads?** Yes, UTM and click identifiers are stored with each lead.

#### Related projects
Umang Hospital HIMS (internal OPD tool for the same hospital); Agentix HIMS.

#### Verification notes
Checked: site load, source routes, migrations, handoff docs, proxy README, git log. Not verified: admin screens (login-protected), whether email/WhatsApp notifications are active. Missing: admin screenshots or demo credentials for a safe copy; the project listing mentions PHP but the actual front end is React (the PHP backend is Laravel, undeployed).

---

## Hospitality

### Woodpecker PMS

**Slug:** `woodpecker-pms` · **Also known as:** HMS by Agentix, Woodpecker Apartments & Suites platform · **Category:** Hospitality / property management system · **Status:** Live (Verified: public portal and guest site; staff app not entered)
**Client / owner:** Woodpecker Apartments & Suites Pvt. Ltd. · **Local folder:** `D:\Agentix Project\HMS by Agentix` · **Last activity:** 2026-10-28 (353 commits)

#### Spoken introduction
Woodpecker PMS runs a group of serviced apartments end to end: bookings, front desk, billing with GST invoices, housekeeping, maintenance, kitchen and POS, payroll and an owner portal. It has a guest website for direct booking and a role-based staff platform sharing one data core. Note it is a hotel system, not a hospital one.

#### Quick overview
A mobile-first Next.js platform with 28 modules and 9 role portals. A guest site at the root domain handles browsing, direct booking and in-stay services; a staff app (sign-in required) runs the properties. The design rules are strict: money in integer paise, locking availability so double-booking is impossible, append-only folios and gap-free sequential GST invoices. It replaces spreadsheets, OTA extranets and paper folios.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Public platform portal | https://hotelmanagement.aiagentixdev.com/portal | Public site (marketing and role launcher) | Role cards link to the staff sign-in. |
| Guest website | https://hotelmanagement.aiagentixdev.com/ | Production (real business) | Online booking was marked "opening soon" on the page at check time. |
| Staff sign-in | https://hotelmanagement.aiagentixdev.com/start | Login required (production) | Real guests; do not log in or take screenshots. |
| Guest booking routes | https://hotelmanagement.aiagentixdev.com/book | Production | Per-property pages `/book/<slug>` and manage-booking pages exist. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms | Safe demo, fictional data, all actions simulated | |
| Walkthrough | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms/walkthrough | Safe demo | |
| Module: tape chart | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms/walkthrough/tape | Safe demo | |
| Module: folio and invoice | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms/walkthrough/folio | Safe demo | |
| Module: housekeeping | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms/walkthrough/housekeeping | Safe demo | |
| Module: owner portal | https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms/walkthrough/owner | Safe demo | |
Other module ids: `dashboard`, `bookings`, `new-booking`, `checkin`, `maintenance`, `pos`, `inventory`, `laundry`, `guests`, `messages`, `pricing`, `channels`, `booking-engine`, `ai`, `finance`, `gst`, `payroll`, `reports`, `audit`.

#### Target users & business problem
Owners and managers of multi-property serviced apartments; reception, accounts, housekeeping, maintenance, POS/kitchen and store staff; property owners (investors); and guests. Problem: overbookings, slow billing and scattered data.

#### Features (complete inventory)
Status: **Partially verified** (code routes, feature folders, integration catalog, demo guide, work report, public portal and guest site read; staff screens not seen).

**1. Property and room setup** (`/properties`, `/rooms`, `/rooms/categories`, `/design`) · Properties, room inventory and status, categories. Evidence: route tree, `src/features/properties`, `rooms`.

**2. Reservations and the tape chart** (`/bookings`, `/bookings/calendar`, `/bookings/new`, `/bookings/new/off-site`, `/bookings/[id]`) · Calendar tape chart, new booking (property first, then room category, with check-availability), group bookings, extend and mid-stay room move; recent commits harden overstay, transfer and extension edge cases. Occupancy is advisory rather than a hard gate (client decision 2026-10-23). Availability enforcement uses a locking transaction per the spec. Status: Verified (code, git log).

**3. Check-in, in-house and Form C** (`/bookings/[id]/check-in`, `/in-house`, `/bookings/form-c`) · Guest details and ID documents; Form C is the Indian foreigner registration form. Status: Verified (route/code).

**4. Folio, billing, GST invoices** (`/bookings/[id]/folio`, `/billing`, `/gst-claims`) · A running folio per stay, split payments (for example part cash, part UPI), extra charges, a "price includes GST" versus "add GST on top" toggle, and tax-invoice PDFs in the client's Tally-style format (company header, GSTIN, CGST/SGST by HSN/SAC, amount in words). Source: work report 2026-09-22 and demo guide. Status: Verified (docs, code).

**5. Guest CRM** (`/guests`, `/guests/[id]`, `/guests/new`) · Guest history, returning-guest matching, multiple ID documents with permission-gated viewing; ID numbers encrypted and masked. Status: Verified (docs, code).

**6. Data entry and import** (`/data-entry`, `/data-import`) · Back-entry of historical stays and bulk import for onboarding. Status: Verified (route, demo guide).

**7. Expenses** (`/expenses`) · Categories, bill photo, multi-item batch entry. Status: Verified (recent commit).

**8. Housekeeping, inspection, maintenance, lost and found** (`/housekeeping`, `/inspection`, `/maintenance`, `/lost-found`, `/requests`) · Room status from a phone, offline-capable for weak Wi-Fi; maintenance jobs and preventive reminders. Status: Verified (route and portal copy).

**9. POS and kitchen** (`/pos`, `/pos/kitchen`, public `/order/[token]`) · Restaurant POS, QR self-ordering and a live kitchen ticket board that settles to the folio. Status: Verified (route).

**10. Inventory and laundry** (`/inventory`, `/inventory/laundry`) · Six stock domains, purchase and issue, laundry reconciliation. Status: Verified (portal copy, route).

**11. People and payroll** (`/people`, `/payroll`, `/payroll/[runId]`, `/staff/field`, `/approvals`) · Staff management, payroll runs, field-staff access. Status: Verified (route).

**12. Channels and pricing** (`/channels`, `/pricing`, `/booking-site`, `/corporate`, `/add-ons`) · OTA channel manager, dynamic pricing suggestions that need approval, direct booking site configuration, corporate CRM, add-ons. **Integration reality:** OTA two-way sync needs certified partnership with each OTA or an aggregator; until then a mock adapter runs. Status: Partially verified (live OTA connection not confirmed).

**13. Communications and guest experience** (`/communications`, `/messages`, `/messages/[reservationId]`, `/notifications`, `/feedback`, `/guest-experience`) · WhatsApp, email and SMS through a provider interface; sandbox by default. Live WhatsApp needs a Meta-approved account and templates; Indian SMS needs DLT registration. Status: Partially verified.

**14. Analytics, finance and accounting** (`/dashboard`, `/overview`, `/overview/[propertyId]`, `/insights`, `/reports`, `/finance`, `/accounting`, `/search`) · Occupancy, ADR, RevPAR, profit per property and consolidated; natural-language search; accounting sync (Tally or Zoho) behind a mock provider until the client connects. Status: Verified (code), live accounting sync Unverified.

**15. Owner portal** (`/owner`, `/owner/documents`, `/owner/payouts`, `/owner/schedule`) · Read-mostly financials, document vault, compliance schedule, payout statements. Status: Verified (route).

**16. AI** (`/ai`) · Guest enquiry chatbot (read-only), natural-language data search, revenue forecast narrative, dynamic rate suggestions, sentiment and segmentation. The model proposes; validated server code executes. Provider-agnostic; mock by default. Status: Partially verified.

**17. Settings and security** (`/settings`, `/settings/users`, `/settings/security`, `/settings/audit`, `/settings/integrations`, `/profile`) · Users and roles, TOTP two-factor, database-backed sessions with revocation, immutable audit trail, integrations. Status: Verified (route, portal copy).

**18. Guest site and guest account** (`/`, `/book/[slug]`, `/book/[slug]/manage`, `/account/*`, `/track/[token]`, `/review/[token]`) · Browse stays, direct booking, self check-in, in-stay orders, rewards account, booking tracking and review links. Status: Verified (public page, route).

**19. Mobile PWA** · Installable on phone, designed phone-first. Status: Verified (manifest, portal copy).

#### Key workflows (end to end)
1. Guest books via the guest site, an OTA (when connected) or the front desk.
2. The reservation lands on the tape chart; availability is locked.
3. At arrival, reception checks the guest in, captures IDs and Form C.
4. During the stay, housekeeping, maintenance and POS operate; charges post to the folio.
5. At check-out, payments are split as needed and a GST tax invoice is generated.
6. Accounts reconciles; accounting sync pushes to Tally or Zoho when connected.
7. Owner and manager dashboards show occupancy, ADR, RevPAR and payout statements.
Access control is enforced server-side per role and property, with audit rows for each change.

#### User roles & permissions
Portal roles on the public page: Super Admin, Manager, Property Owner, Reception, Accounts, Housekeeping, Maintenance, Outlet/POS, Store/Inventory (nine). The database role enum is larger: Administrator, Manager, Assistant Manager, Reception, Accounts, HR, Inventory Manager, Purchase Manager, POS Manager, Housekeeping, Maintenance, Security Supervisor, Laundry Supervisor, Owner. Permissions are checked server-side and scoped to property, deny by default.

#### Technical architecture & integrations
Next.js 15, React, TypeScript, Prisma with PostgreSQL (70-model schema), pg-boss job queue and a separate worker, react-pdf for invoices, exceljs for exports, otplib for two-factor, Docker with Coolify on a VPS. Integrations are interfaces with mock adapters by default: payments (Razorpay or Cashfree), WhatsApp, SMS, email, OTA channel manager, accounting (Tally, Zoho), AI model, S3-compatible storage. Credentials are server environment variables. The README still says "pre-implementation" and is stale; the git history (353 commits) and live sites show the system is built and deployed.

#### Business value & example scenarios
One data core for four-plus properties; no double entry between website and desk; GST invoices in seconds. Scenario: fictional guest "Ishaan Mehta" books a two-night stay, arrives, orders room service through a QR link, and receives a GST invoice at check-out; the owner sees the revenue the same day.

#### Planned / in progress (not live)
Live OTA connectivity, live WhatsApp/SMS templates, accounting connectors and live online payment depend on client accounts and partner approval (integration catalog). The guest site states online booking is opening soon.

#### Example visitor questions & answers
- **Is this a hospital system?** No, it is a hotel and serviced-apartment PMS.
- **How many modules and roles?** 28 modules and 9 role portals.
- **Does it prevent double booking?** Yes by design, through locking availability.
- **Does it connect to Booking.com or MakeMyTrip?** It has a channel manager interface; live connection needs OTA approval and was not confirmed.
- **Does it generate GST invoices?** Yes.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/woodpecker-pms (safe demo). The live staff app is production.
- **Is there an owner view?** Yes, the owner portal.
- **Is it mobile friendly?** Yes, it is a mobile-first PWA.

#### Related projects
Kaaya Eco Resort (a resort website with its own simple booking engine, different codebase); Agentix HIMS (similar role-portal approach for hospitals).

#### Verification notes
Checked: CLAUDE.md, README, handover, demo guide, work report, integration catalog, route and feature folders, git log, public portal and guest site text. Deliberately not opened: root audit CSV and JSON files and environment files. Not verified: staff app screens, live integrations, GSTIN or company details. Missing: demo-safe screenshots or a seeded demo login, and confirmation of which integrations run live.

---

### Kaaya Eco Resort

**Slug:** `kaaya-eco-resort` · **Also known as:** kaayaecoresort.com · **Category:** Hospitality / resort website with booking engine · **Status:** Live (Verified: public site and public room data; admin not seen)
**Client / owner:** Kaaya Eco Resort, Yala, Sri Lanka · **Local folder:** `D:\Agentix Project\kaaya eco resort` · **Last activity:** 2026-06-15 (37 commits)

#### Spoken introduction
Kaaya Eco Resort is a luxury eco-resort near Yala National Park in Sri Lanka. Our website lets guests browse rooms, check availability for their dates, create an account and pay by card, and the resort manages bookings, rooms, photos and reviews from an admin dashboard.

#### Quick overview
A React front end with an Express and MySQL back end. Guests see rooms, dining, experiences, groups and events, a gallery and reviews, then book through a three-step flow (choose room, your details, payment). The server checks for overlapping bookings before creating one. An admin area manages bookings and content. It reduces dependence on OTAs and phone bookings.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Main site | https://kaayaecoresort.com/ | Production (real resort; do not create bookings) | Page title "Your Gateway to Yala's Wild Heart". |
| Rooms | https://kaayaecoresort.com/accommodation | Production | |
| Booking flow | https://kaayaecoresort.com/book | Login required (guest account) | |
| Guest sign-in/register | https://kaayaecoresort.com/login | Login required | |
| Admin | https://kaayaecoresort.com/admin | Login required (staff) | |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/kaaya-eco-resort | Safe demo, fictional data, all actions simulated | No interactive module file exists yet (js/demos/kaaya-eco-resort.js is absent); overview link only. |

#### Target users & business problem
Overseas and local leisure guests, families, groups, and the resort's operators who needed direct bookings without OTA commissions or manual availability.

#### Features (complete inventory)
Status: **Verified** (code and public API; admin and payments not exercised).

**1. Guest pages** · Home, About, Accommodation and room detail, Experiences, Dining, Gallery, Groups and events, Contact. Experiences include safari at Yala, lake experience, cultural immersion, bird watching, resort activities and private resort hire. Dining mentions a bar with a bring-your-own-bottle policy. Group types include family reunions, weddings and honeymoons, corporate retreats, birthdays, wellness retreats and photography tours. Evidence: `client/src/pages/*`.

**2. Rooms and pricing** · Seven rooms were visible via the public rooms endpoint (family rooms with garden or lake view, a family chalet with jacuzzi, and standard chalets), priced in Sri Lankan rupees per night. Room type, capacity, beds and amenities are shown. Evidence: public rooms API, `server/src/routes/rooms.js`.

**3. Availability** · `/api/rooms/:id/availability` and booking checks consider existing bookings (confirmed, pending, checked-in) and blocked dates. Overlapping dates return a conflict.

**4. Booking flow** · Three steps: Choose Room, Your Details, Payment. Guests must be signed in; the server validates dates, adult count against room capacity, and calculates the total as nights times price.

**5. Online payment** · Card payments through Stripe (payment intent plus signed webhook that marks the booking confirmed). Whether it runs in live mode was not verified. Status: Partially verified.

**6. Guest accounts** · Register, sign in, "My bookings", booking detail, a booking success page. Authentication uses signed tokens and hashed passwords.

**7. Reviews** · Guests post reviews; an admin approves them before display.

**8. Enquiries** · A public enquiry form stores inquiries and sends email (nodemailer).

**9. Admin** (`/admin`, tabs) · Overview (stats and analytics), Bookings (view and change status), Rooms (create, edit, delete), Gallery (uploads through Cloudinary), Reviews (approve), Inquiries (mark read), Users (change role). A one-time "claim admin" route exists for the first administrator. Blocked dates are stored in the database (table exists); the UI path for managing them was not confirmed in the admin tabs. Evidence: `server/src/routes/admin.js`, `Admin.jsx`.

#### Key workflows (end to end)
1. Guest explores rooms and picks dates.
2. The site checks availability and blocked dates.
3. Guest signs in or registers, enters details.
4. Stripe takes the card payment; the webhook confirms the booking.
5. The booking appears in admin; the guest sees it in My bookings and later can leave a review.
Rate limiting and security headers are applied on the API.

#### User roles & permissions
Guest user, administrator (role change in admin; first admin claimed by a one-time route). Other roles were not seen.

#### Technical architecture & integrations
React and Vite front end; Express API (helmet, rate limit, compression); MySQL accessed through `mysql2` (a git commit on 2026-06-15 replaced Prisma because the host container restricted its engine); Stripe; Cloudinary; Nodemailer; JWT auth; deployed on a shared host and Vercel config present. Tables (names only): User, Room, Booking, Review, GalleryImage, Inquiry, BlockedDate.

#### Business value & example scenarios
Direct booking without commission and an accurate calendar. Scenario: fictional guest "Anika Fernando" books a lake-view family room for three nights, pays by card, and receives it in My bookings; the resort sees it in the admin overview.

#### Planned / in progress (not live)
None documented.

#### Example visitor questions & answers
- **Can guests book online?** Yes, with an account and card payment.
- **What rooms exist?** Family rooms, a jacuzzi family chalet, and standard chalets.
- **How is double booking prevented?** The server rejects overlapping bookings and honours blocked dates.
- **Who manages content?** The resort via an admin dashboard.
- **Can I see a demo?** The live site (production) or the portfolio overview at https://agentix-portfolio.vercel.app/#/demo/kaaya-eco-resort.
- **What currency?** Prices display in Sri Lankan rupees.
- **How does it differ from Woodpecker PMS?** Kaaya is a single-resort website with simple booking; Woodpecker runs multi-property operations.

#### Related projects
Woodpecker PMS (operations platform); Thames Wellness Spa and other hospitality-adjacent sites (Part elsewhere).

#### Verification notes
Checked: source routes, server routes, public site, public rooms data, git log. The database setup file was inspected for table names only and no environment file was opened. Not verified: payment mode, admin UI, whether blocked-date management has an admin screen. Missing: admin screenshots or confirmation of live payment mode.

---

## Fitness

### Max Register (Max Fitness gym CRM, kiosk and worker)

**Slug:** `max-register` · **Also known as:** Max Fitness Platform CRM, Max Haazri (the attendance kiosk idea) · **Category:** Fitness / gym CRM · **Status:** Live in production with real members (Verified for code and docs; login page seen; app not entered)
**Client / owner:** Max Fitness Gym, Indirapuram, Ghaziabad · **Local folder:** `E:\max-fitness` (`apps/web` `/crm`, `apps/worker`, `apps/face`) · **Last activity:** 2026-10-27 (237 commits)

#### Spoken introduction
Max Register is the gym owner's phone-first, Hindi-first register: who has paid, who is due, who to call, who walked in today. It sends WhatsApp renewal reminders by itself, lets reception renew a member in a few taps with a receipt, and includes a face-recognition check-in page. It is in production at Max Fitness.

#### Quick overview
A Next.js CRM inside the web app (the `/crm` area) with a background worker and a Python face service. Staff log in with a mobile number and a 4 to 6 digit PIN. Members carry a fee state shown by colour (green paid, amber due within seven days, red expired, grey none). The worker schedules WhatsApp reminders and an owner digest. It replaces notebooks and loose WhatsApp follow-ups.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| CRM login | https://maxfitnessgym.co.in/crm | Production, login required | Real members; do not log in or screenshot. Login by mobile or email plus PIN, 30-day sessions on a trusted phone. |
| Check-in kiosk page | https://maxfitnessgym.co.in/checkin | Production | Browser-based face/phone check-in used with the face service. |
| Public renewal link | https://maxfitnessgym.co.in/renew/<token> | Production | Per-member tokenised link. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/max-register | Safe demo, fictional data, all actions simulated | Tier A. |
| Walkthrough | https://agentix-portfolio.vercel.app/#/demo/max-register/walkthrough | Safe demo | |
| Module: Today | https://agentix-portfolio.vercel.app/#/demo/max-register/walkthrough/today | Safe demo | |
| Module: renew | https://agentix-portfolio.vercel.app/#/demo/max-register/walkthrough/renew | Safe demo | Three-tap renewal and receipt. |
| Module: reminders | https://agentix-portfolio.vercel.app/#/demo/max-register/walkthrough/reminders | Safe demo | |
| Module: kiosk | https://agentix-portfolio.vercel.app/#/demo/max-register/walkthrough/kiosk | Safe demo | |
Other module ids: `members`, `new-member`, `calls`, `leads`, `verify`, `attendance`, `messages`, `bot`, `announcements`, `reports`, `diet`, `gallery`, `plans`, `audit`.

#### Target users & business problem
Gym owners and reception staff (low-tech, Hindi speakers) who track fees in notebooks, miss renewals and lose members. Members receive reminders and renewal links.

#### Features (complete inventory)
Status: **Partially verified**: strong evidence from code, a very detailed progress log and business rules; the signed-in app was not opened because it holds real members.

**1. Today (home)** (`/crm`) · Tiles for who is due, who needs a call, new arrivals and attendance; the starting point each day. Evidence: `crm/(app)/page.tsx`.

**2. Members** (`/crm/members`, `/new`, `/waiting`, `/[id]`, `/[id]/edit`, export) · List with fee colour bands, member profile with payments, attendance and personal training, correcting details, adding a member, a waiting list for pending signups, and a per-member data export. Fee state is derived from the end date (paid more than 7 days left; due soon 0 to 7; expired; none). Status: Verified (business rules, code).

**3. Renew** (`/crm/members/[id]/renew`) · Pick plan and payment mode, confirm; a receipt with a tokenised PDF link is generated and can be shared. Prices are copied onto each membership so later price changes do not alter past records. Evidence: `api/v1/receipts/[token]/pdf`.

**4. Plans and pricing** (`/crm/settings`) · Plans are one, three, six and twelve months, with separate male and female prices; the public website shows current fees. Status: Verified.

**5. Calls** (`/crm/calls`) · Automatic "calls to make" list with reasons (expired but visiting, signup not paid, new lead, verification pending, expired not renewed, due soon with no response, absent seven days, unsubscribed) and outcomes (will renew, call later, no answer, left gym, wrong number, done). A Done tab shows outcome counts.

**6. Leads** (`/crm/leads`) · Funnel from new to contacted, trial booked, visited, converted or lost, with sources (website, WhatsApp, walk-in, phone, Instagram, Google Business Profile, referral) and conversion rate.

**7. Verify** (`/crm/verify`) · Queue of existing customers who self-declared a fee-paid-till date via the reception QR; the owner approves or rejects.

**8. Attendance and kiosk** (`/crm/attendance`, `/crm/settings/kiosk`, public `/checkin`, `api/v1/checkin/*`, `api/v1/kiosk/*`) · Face check-in compares a live frame against the selfie from signup using an open-licence face engine (a separate Python service); fee state drives the greeting (green welcome, amber with days left, red asks to see reception and creates a call task); manual attendance by staff is always allowed; one event per member per cooldown (180 minutes default). Faces are used only with consent. The planned dedicated Android kiosk app folder is empty; the working kiosk is the browser page. Attendance export exists. Status: Verified (code, progress log); no attendance data seen.

**9. WhatsApp reminder engine** (worker `reminders`, `/crm/messages`, `/crm/messages/simulator`, webhooks) · Default rules: seven, three, two and one day before expiry and on the day at 10:00 IST, then daily at 19:00 IST for up to seven days after expiry; eligibility is rechecked at send time (active, opted in, not paused, not already renewed, within quiet hours); idempotent keys prevent duplicates; unsubscribing stops them. Production went live with WhatsApp and Razorpay on 2026-10-16. A message simulator exists for demo mode. Messages screen is an inbox with replies (`api/v1/crm/messages/reply`). Status: Verified (docs, code); live sends not independently observed.

**10. Bot** (`/crm/bot`) · A WhatsApp assistant with owner-configured documents and replies for gym questions. Status: Partially verified (code, progress log).

**11. Announcements** (`/crm/announcements`) · Broadcast notices to audiences.

**12. Diet** (`/crm/diet`, public `/diet/[token]`) · Diet profiles and plans shared through a tokenised page, with follow-ups. Content is operational; not medical advice.

**13. Gallery** (`/crm/gallery`) · Owner-managed photos used on the website.

**14. Reports** (`/crm/reports`, export) · Reports over a day, week, year or custom range; shared period picker.

**15. Import** (`/crm/import`, template) · Bulk member import from a spreadsheet.

**16. Settings, staff, PIN, audit** (`/crm/settings/staff`, `/crm/more/pin`, `/crm/more/audit`) · Staff accounts with roles (owner, reception, trainer, super admin), PIN management, and an audit trail screen of sensitive actions such as voiding a payment.

**17. Online payments and autopay** (`api/v1/checkout/*`, `webhooks/razorpay`) · Razorpay orders and signed webhooks; recurring e-mandate (autopay) was built and deployed 2026-10-05. Demo mode simulates payments.

**18. Offline and PWA** (`/crm/offline`, web manifest) · Installable on the owner's phone.

**19. Languages** · Hindi by default for the CRM, English toggle; website English by default with Hindi.

#### Key workflows (end to end)
1. Reception logs in with mobile and PIN and opens Today.
2. Members arrive; face check-in or manual attendance records the visit.
3. A member nears expiry; the worker sends WhatsApp reminders; the member opens the tokenised renewal link or pays at the desk.
4. Reception renews in a few taps; a receipt is produced; reminders stop.
5. Unpaid or lapsed members appear on the Calls list; outcomes are logged.
6. Website enquiries and QR signups enter Leads or Verify; the owner confirms.
7. The owner reads reports and the nightly digest.
Permissions: staff sign in with PIN; lockouts and rate limits exist (security review noted).

#### User roles & permissions
Owner, reception, trainer, super admin (staff role enum); fine-grained access per role was not enumerated. Members have no CRM login; they use tokenised links and the QR flow.

#### Technical architecture & integrations
Turborepo monorepo: Next.js 16 and React 19 web app with next-intl (Hindi and English), Tailwind 4 and Radix; Prisma 7 on Postgres (Supabase, Mumbai); a pg-boss worker app; a Python face service (OpenCV YuNet and SFace, commercially licensed models); WhatsApp Cloud API; Razorpay; browser-side face detection (MediaPipe); Docker on Coolify. Environment names include demo mode, WhatsApp allowlist, face service token (values never shown). Tests: unit, integration and accessibility suites reported in the progress log. Known open items per the log: end-to-end suite not completed cleanly, a stricter content-security policy untested in browser, and server-to-database distance causing latency.

#### Business value & example scenarios
Fewer missed renewals and less owner time on phone follow-up. Scenario: fictional member "Neha Arora" has seven days left; she gets a WhatsApp reminder, taps the renewal link, pays, and reminders stop; reception sees the receipt.

#### Planned / in progress (not live)
The dedicated Android kiosk app ("Max Haazri" Phase 7) is unbuilt (folder empty per the 2026-10-07 log). A UI refresh branch (`design/crm-refresh`) was prepared for review.

#### Example visitor questions & answers
- **Who uses it?** The gym owner and reception.
- **Does it support Hindi?** Yes, default.
- **How do renewals work?** Three taps in the CRM or a tokenised link; a receipt follows.
- **Does it recognise faces?** A face service compares to the member's signup selfie, with consent.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/max-register (safe demo, fictional data).
- **Is the live CRM open?** No, it is login-protected and holds real members.
- **Does it send WhatsApp reminders automatically?** Yes, per documented rules.

#### Related projects
Max Fitness website (`max-website`, the public side of the same app); Fitness First Dwarka (a different gym website).

#### Verification notes
Checked: CLAUDE.md, business rules, progress log, face README, routes, git log, public login page. Not opened: the signed-in CRM and any member data. Missing: sanitized screenshots or a seeded demo-mode instance; confirmation of how many gyms use it (the code is built single-gym).

---

### Max Fitness website

**Slug:** `max-website` · **Also known as:** maxfitnessgym.co.in · **Category:** Fitness / gym website with signup · **Status:** Live (Verified)
**Client / owner:** Max Fitness Gym, Indirapuram, Ghaziabad · **Local folder:** `E:\max-fitness` (`apps/web` public routes) · **Last activity:** 2026-10-27

#### Spoken introduction
This is the public website of Max Fitness Gym in Indirapuram. Visitors can read about the gym, compare fees, request a call back, sign up online with a selfie, or use a reception QR code to register. Everything feeds the gym's Max Register CRM.

#### Quick overview
A bilingual (English and Hindi) Next.js site on the same application as Max Register. It presents the gym (since 2000, owner-coached, Google rating shown), facilities, plans, personal training and supplements, then offers a call-back form, a three-step online sign-up, and a QR page for walk-ins. It turns local searches into members.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Home (English) | https://maxfitnessgym.co.in/ | Production, public site | |
| Hindi | https://maxfitnessgym.co.in/hi | Public site | |
| Sign up | https://maxfitnessgym.co.in/join | Production | Writes a real member record; do not submit test data. |
| Reception QR | https://maxfitnessgym.co.in/qr | Production | Existing member or new visitor options. |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/max-website | Safe demo, fictional data, all actions simulated | No module file exists yet (js/demos/max-website.js absent); the walkthrough in the Max Register demo covers the public side. |

#### Target users & business problem
People near Indirapuram looking for a gym, and walk-ins at the desk. Problem: local gyms rely on walk-ins and word of mouth.

#### Features (complete inventory)
Status: **Verified** (live pages and code).

**1. Content sections** · About, facilities (strength zone, cardio zone, functional floor, personal training, diet plans, supplements at the counter, lockers, water, parking, air-conditioning), owner story with reviews, working hours, contact. Evidence: live home text.

**2. Plans and fees** · Monthly, three, six and twelve months for men and women, with effective monthly rate and savings, plus personal-training pricing. Prices are on the live page and can change; this guide does not quote them.

**3. Call-back form** · Name, mobile, goal; a hidden honeypot field blocks bots; creates a lead (`api/v1/leads`) in the CRM.

**4. Online sign-up** (`/join`, `/join/plan`, `/join/pay`, `/join/done`) · Step one: details, date of birth, gender, live selfie, consents (terms, WhatsApp updates, optional face use for attendance); then plan selection; then payment. Mobile verification by OTP routes exist. Opens as a modal over the page or as full pages.

**5. Reception QR** (`/qr`, `/qr/existing`, `/qr/new`, `/qr/done/[ref]`) · "I am already a member" sends details and the date fees are paid until for the owner's Verify queue; "I am new here" shows plans and details and pays at reception.

**6. Member links** · Renewal (`/renew/[token]`) and short links (`/r/[token]`), diet plan page (`/diet/[token]`), legal pages (terms, privacy, refund and cancellation).

**7. Language switch and SEO** · Hindi and English with a toggle; Google rating, local-business metadata.

#### Key workflows (end to end)
1. Visitor lands, reads, compares plans.
2. They request a call back, sign up online, or scan the QR at the desk.
3. A lead or pending member appears in Max Register; reception follows up or verifies.
4. Payment (online or desk) activates the membership.

#### User roles & permissions
Public visitors only; staff use the CRM.

#### Technical architecture & integrations
Same Next.js app and Postgres database as Max Register, Razorpay for payments, WhatsApp Cloud API for messages, Coolify hosting; the site can be framed by the AI Agentix portfolio (added 2026-10-27).

#### Business value & example scenarios
More enquiries captured and fewer desk data entries. Scenario: fictional visitor "Riya Sethi" scans the QR, picks "I am new here", fills her details, and reception collects the fee.

#### Planned / in progress (not live)
Ads and assistant content briefs exist as documents (2026-10-27) but are not site features.

#### Example visitor questions & answers
- **Can I join online?** Yes, via /join.
- **Is Hindi supported?** Yes, /hi.
- **What if I am already a member?** Use the reception QR; the owner verifies.
- **Are fees listed?** Yes, on the live page; check there for current prices.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/max-website (overview) and the Max Register demo.
- **Does it connect to the CRM?** Yes, same system.

#### Related projects
Max Register (`max-register`).

#### Verification notes
Checked: live English, Hindi, join and QR pages; route list. Not verified: payment completion (production). Missing: none critical; no dedicated portfolio module yet.

---

### Fitness First Dwarka website

**Slug:** `fitness-first` · **Also known as:** Fitness First Dwarka, fitnessfirstdwarka.com · **Category:** Fitness / premium gym website · **Status:** Live (Verified)
**Client / owner:** Fitness First Dwarka, West Delhi · **Local folder:** `D:\Agentix Project\Fitness First` · **Last activity:** no git repository; newest source file dated 2026-08-19

#### Spoken introduction
This is the website for Fitness First Dwarka, a premium gym in West Delhi. It leads with video, lists programmes, trainers and membership plans, and sends every enquiry to the gym by email and into a database, with a "Book Your Free Trial" pop-up.

#### Quick overview
A Next.js site exported as static files and hosted on Apache/cPanel, with PHP form handlers and MySQL. Pages: home, programmes, trainers, membership, FAQs, contact, thank-you and a printable membership application form. It turns visitors into trial bookings and enquiries.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Main site | https://fitnessfirstdwarka.com/ | Production public site | Do not submit test enquiries. |
| Programmes | https://fitnessfirstdwarka.com/programs/ | Public site | |
| Membership | https://fitnessfirstdwarka.com/membership/ | Public site | |
| Trainers | https://fitnessfirstdwarka.com/trainers/ | Public site | |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/fitness-first | Safe demo, fictional data, all actions simulated | No module file yet (js/demos/fitness-first.js absent). |

#### Target users & business problem
People in Dwarka considering a premium gym. Problem: match a premium brand and turn browsers into trial bookings.

#### Features (complete inventory)
Status: **Verified** (live pages and source).

**1. Home** · Hero video, offers section (two time-limited offers were shown at check time with dates in August 2026, so they may be outdated), brand pillars (equipment, certified trainers, structured programmes, interiors), member transformation stories, month-on-month membership plans, address, hours, newsletter.

**2. Programmes** · Personal training, HIIT, yoga and meditation, Zumba, strength and conditioning, spin, corporate wellness, fitness certifications. Group classes by an international fitness brand are named only in the page's search description, not as program cards.

**3. Trainers** · Eleven trainer profiles with a know-more detail (per the client's change list).

**4. Membership** · Plan cards and a month-on-month (EMI) structure with an initial bundle and automatic monthly debits set up by the gym through an authorisation link. Amounts are on the live page and change; this guide does not quote them. A downloadable membership application form with health questions and signatures posts to the PHP API.

**5. Lead capture** · Floating "Book Your Free Trial" widget that auto-opens on the home page and sends the lead to a PHP handler, then opens a thank-you page for conversion tracking; enquiry and contact forms post to `submit-form.php`, store in MySQL (table `form_submissions`) and send email via PHPMailer. A WhatsApp widget and click-to-call exist.

**6. Analytics** · Google Tag Manager and Google Ads tags.

**7. FAQs, contact, legal links.** Terms, privacy and refund links are present in the footer.

#### Key workflows (end to end)
1. Visitor watches the hero, reads programmes and trainers.
2. They compare plans and offers.
3. They click Enquire or the free-trial widget.
4. The form is stored and emailed; the visitor lands on a thank-you page.
5. The sales desk follows up.

#### User roles & permissions
Public visitors only; there is no admin in the repo beyond the database and email.

#### Technical architecture & integrations
Next.js 14 (static export), Tailwind, Framer Motion; PHP 8 handlers using PDO and MySQL; PHPMailer; the shared lead-widget (popup form) pattern; Apache/cPanel; GTM and Google Ads. Credentials are in server config files (not read).

#### Business value & example scenarios
Brand-led conversion and traceable enquiries. Scenario: fictional visitor "Devansh Rao" opens the page, watches the video, claims a free trial in the pop-up and receives a call.

#### Planned / in progress (not live)
None documented.

#### Example visitor questions & answers
- **What does the site offer?** Programmes, trainers, plans and a free-trial request.
- **Where do enquiries go?** To the gym's email and a MySQL database.
- **Is there online payment?** No; plans are enquiry-led.
- **Can I see a demo?** Live site, or https://agentix-portfolio.vercel.app/#/demo/fitness-first.
- **How does it differ from Max Fitness?** Fitness First is a marketing site only; Max Fitness has signup, payments and a CRM.

#### Related projects
Max Fitness website and Max Register.

#### Verification notes
Checked: live home and subpages (HTTP 200 for programs, membership, trainers, faqs, contact), source routes, API docs and schema. Not verified: leads actually received, any admin. Missing: git history/last-activity date; the site names Les Mills only in meta text, so the portfolio does not claim it; confirm with the client before mentioning it.



Conventions for this part: "Portfolio" means https://agentix-portfolio.vercel.app/ (planned hosted URL). Portfolio demos are "Safe demo - fictional data, all actions simulated". Labels: Verified / Partially verified / Unverified / Unavailable. No credentials, keys or real personal data appear here. Evidence was gathered on 2026-10-28/29 from local source folders and public pages loaded in Chrome (no logins).

---

## Multi-Product Business Platforms

### REDUX Platform (by Eurobrass)
**Slug:** `redux` · **Also known as:** REDUX - Bath Restorations by Eurobrass · **Category:** Multi-Product Business Platforms / B2B restoration operations · **Status:** In development (active build, client demo deployment live) - Verified
**Client / owner:** Eurobrass (New Delhi) · **Local folder:** `D:\Agentix Project\Redux` · **Last activity:** 2026-10-20 (106 commits)

#### Spoken introduction
REDUX is a platform we built for Eurobrass's bathroom-fittings restoration service. It connects a public website, a lead CRM, a staff portal, an offline Android survey app, a customer portal and an admin console, so one hotel's enquiry can be followed all the way from first contact to invoice and warranty. The link we share is a safe demo with sample data.

#### Quick overview
REDUX restores worn hotel and home bath fittings (taps, mixers, showers) instead of replacing them. The platform removes the hand-offs between enquiry, site survey, quotation, approval, job, invoice and after-care by keeping one record from start to finish. It is aimed at the REDUX sales/care team, surveyors, the owner, and the hotel or home-owner customers. The deployed link is a demo deployment: WhatsApp, OTP and payments are simulated.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Public website | https://redux-demo-iota.vercel.app/ | Safe demo environment | Banner says "Demo - sample data. WhatsApp, OTP and payments are simulated." |
| Demo outbox | https://redux-demo-iota.vercel.app/demo/outbox | Safe demo environment | Shows every simulated WhatsApp message with its buttons |
| Staff login | https://redux-demo-iota.vercel.app/staff/login | Login required (demo personas) | One-click persona cards exist on the demo; credentials not reproduced here |
| Customer portal login | https://redux-demo-iota.vercel.app/portal/login | Login required (demo) | Phone + code; the demo shows the code on screen |
| Book assessment form | https://redux-demo-iota.vercel.app/book-assessment | Safe demo environment | Public enquiry form |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/redux/overview | Safe demo - fictional data | Tabs: /overview /walkthrough /how /screens /tech |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough | Safe demo | Modules below |
| Module: journey | https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough/journey | Safe demo | Enquiry to warranty as one animated pipeline |
| Module: leads | https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough/leads | Safe demo | Lead Kanban with city routing |
| Module: survey-app | https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough/survey-app | Safe demo | Mobile surveyor app |
| Module: quotes | https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough/quotes | Safe demo | Quote built from survey |
| Other module ids | website, inbox, portal, jobs, invoices, payments, campaigns, rate-card, catalog, stock, outbox | Safe demo | `/#/demo/redux/walkthrough/<id>` |

#### Target users & business problem
Hotels, home owners and dealers who want fittings restored; and the Eurobrass/REDUX team (care executives, surveyors, super admin). Before, enquiry-to-invoice crossed about five hand-offs in separate tools, so jobs stalled and customers chased for updates.

#### Features (complete inventory)
**1. Public website (Verified).** Home with promise ("Your existing fittings may have more service life ahead"), before/after, three services (restore function, restore finish, improve water efficiency), process, "Why REDUX", pages for hotels, homes, work/case studies, process, how-we-restore, assessment, demo programme, referral programme, dealers/dealer enquiry, products catalogue (Eurobrass 2025 range, about 469 products per DEMO-GUIDE, browsed by type/series/code search, finishes, "Assess this fitting"), contact, legal pages, floating WhatsApp button. Enquiry form records DPDP consent (marketing consent separate and unticked by default). Evidence: live page text and links, `app/(marketing)/*`, DEMO-GUIDE.md.
**2. Lead CRM (Verified in code + guide).** Leads arrive from the website form, and the build includes Meta lead-ads, Google Ads and WhatsApp intake (webhook handlers in `lib/webhooks`, `lib/integrations/meta-graph.ts`; these are simulated in the demo). Leads are routed by city to the right care executive, get a 1-hour call-back SLA timer, call logging with outcomes, and a status flow (New, Contacted, Survey booked, Quoted, Won, Lost). B2B qualification: lead scoring tiers A/B/C with a 150 km service-area rule, tier x distance table and a "test a lead" tool. Evidence: `app/staff/(shell)/leads`, supabase migrations `leads`, `scoring`, `profiling`.
**3. WhatsApp inbox and outbox (Verified, simulated).** Staff inbox with a 24-hour customer-service window; every outbound template message appears in the demo outbox with buttons. Utility templates are not offered for campaigns (they would be billed as marketing). Evidence: DEMO-GUIDE, `app/staff/(shell)/inbox`, `app/demo/outbox`.
**4. Survey booking and surveyor app (Verified).** Care executive finds a free surveyor (same city first, least busy), double-booking in a slot is blocked, customer gets a WhatsApp confirmation. The Android surveyor app (Expo SDK 57, in `mobile/`) lets the surveyor check in with GPS (poor accuracy flagged, not blocked), add rooms and fittings (type, brand, finish, condition), take four mandatory photos (front, side, top, close-up), choose a recommendation and see three prices live (REDUX price, new Eurobrass, market replacement) and "customer saves". It works offline: every write goes through an outbox, and a local photo is deleted only after the server confirms it exists. Evidence: `mobile/src/*`, CLAUDE.md rules 7-8, DEMO-GUIDE Act 3. Limitation: run via Expo Go on a phone in the demo.
**5. Self-assessment (B2B) and demo programme (Verified in guide).** Customers can photograph their own fittings from the portal; staff price it and create a quotation within a 24-hour target. A free single-fitting demo can be proposed, must be approved by the super admin, is scheduled as a no-quotation, never-invoiced demo job, and tracks cost and conversion. Evidence: DEMO-GUIDE section 4, migrations `self_assessment`, `demos`.
**6. Quotations (Verified).** Builder pulls every line from the survey (nothing re-typed), tax split, market total and "You save"; discounts above 5% need super-admin approval; A4 preview and print/PDF (Gotenberg service for PDFs); issuing freezes validity and terms and fingerprints the document; sent on WhatsApp with a "View and approve" button. Rate card is versioned: an active version is frozen and changes create a new version so old quotes never re-price. Evidence: `app/staff/quotes`, `docker/gotenberg`, migration `rate_cards_assessments`, `quotations`.
**7. Customer portal (Verified).** Phone + OTP sign-in (code shown on screen in demo). Pages: quotes (approve with an OTP, which records who/when/which document and converts the prospect into a customer, marks the lead Won and opens a job in one transaction), jobs, invoices (pay now), warranty cards, service requests, fittings, history ("request again"), reports, team, referrals, privacy, self-assessment. Evidence: `app/portal/(app)/*`.
**8. Jobs and operations (Verified).** Job board by room through stages: removal and pickup, at Eurobrass, quality check, refit and test, handover. Each stage sends a WhatsApp update. Rooms can be blocked (for example waiting on civil work) with the delay clock stopped; room board for meetings with the hotel; handover checks (no leaks, operates smoothly, finish as promised) then warranty cards are generated. Evidence: `app/staff/(shell)/jobs`, DEMO-GUIDE Act 6.
**9. Invoices and payments (Verified, simulated payments).** Gap-free GST numbering, CGST/SGST or IGST by place of supply. Above 50,000 rupees the invoice routes to bank transfer (avoids a 2% card fee), below it a payment link. Payments are reconciled against invoices, receipt sent on WhatsApp. Approved quotations, quote approvals and invoices are immutable (versioned or credit-noted). Razorpay is the planned/configured gateway; in the demo payment is simulated. Evidence: CLAUDE.md stack and rules, `lib/actions/invoices.ts`, migration `invoices`.
**10. Service requests and after-care (Verified).** Customer raises a request from a warranty; staff see acknowledge-by and resolve-by clocks (acknowledge, start, resolve).
**11. Accounts, referrals, campaigns (Verified in guide).** Account 360 (lifetime billed, next action, requirements, timeline, work and money, demos, referrals); referral codes and links with pre-approved 5% first-order discount for referred businesses and a credit ledger; campaigns to lost leads only for contacts with marketing consent (the count shown equals the number sent; STOP withdraws consent; scheduler checks every 5 minutes); follow-up cadences per tier. Evidence: migrations `accounts`, `referrals`, `outreach`.
**12. Admin console (Verified).** Dashboard (leads, conversion, quoted value, rooms at factory, cost per won job, leads by source), reports with CSV export (tiers and sources, assessments, demos, people, accounts, referrals, campaigns, products), rate card, catalog import from spreadsheet, stock with low-stock alerts and movement ledger, audit log, privacy (DPDP consent ledger and data requests), integrations health (Meta, WhatsApp, Google Ads, Razorpay), discount approvals, lead scoring settings.

#### Key workflows (end to end)
1. A hotel submits the website form (consent recorded) and a lead appears with an SLA timer for the Delhi care executive; an enquiry WhatsApp goes out.
2. The executive logs the call, books a free survey and picks a surveyor; confirmation WhatsApp sent.
3. The surveyor checks in, records fittings and four photos each, submits (works offline, syncs later).
4. A quotation is created from the survey, discount approval if above 5%, issued and sent.
5. The customer approves with an OTP in the portal; lead becomes Won and a job is created.
6. The job moves through stages with WhatsApp updates; rooms can be blocked and unblocked; handover issues warranty cards.
7. An invoice is raised and issued; the customer pays; receipt and (for referred hotels) referral credit follow.
8. After-care: warranty cards and service requests with SLA clocks.

#### User roles & permissions
Verified enum in code: `super_admin`, `cc_exec` (care executive), `surveyor`, `customer`. Super admin approves discounts and demos and sees admin settings; care executives own leads, calls, surveys, follow-ups and service requests (demo personas: one Delhi, one Gurugram executive); surveyors use the web (and the Android app) for their visits and quotations; customers see only their own quotes, jobs, invoices and warranty (row-level security on every table).

#### Technical architecture & integrations
Next.js 16 App Router and React 19, Tailwind v4, shadcn/ui, TanStack Table/Query, react-hook-form + Zod. Supabase (Postgres, Auth, Storage; Mumbai region) with row-level security on every table, pgmq + pg_cron queue, a separate worker process (`worker/` with notification, webhook and CAPI processors), Gotenberg for PDFs, Expo SDK 57 Android app, Razorpay and Meta Cloud API (direct, no BSP) and MSG91 for OTP SMS as the intended integrations. Production target: Docker on a Mumbai VPS via Coolify; the demo is on Vercel (`vercel.json` region bom1). Env config is in `.env.local` (names only; never in the repo). Webhook rule: verify raw body, persist, return 200 fast, process in the queue; Google Ads webhook must never get a 4XX. Money is stored as numeric and shown in Indian grouping. Evidence: CLAUDE.md, package.json, migrations (33 files), `worker/`, `mobile/`. Not confirmed: whether live Meta/WhatsApp/Razorpay are connected in any production environment (the tracker's phase 0 shows Meta App Review, WABA, DLT and Razorpay KYC still TODO).

#### Business value & example scenarios
Removes re-typing between survey, quote, job and invoice; makes SLA, discount and approval rules enforceable; gives customers self-service visibility. Scenario: "Riverside Heritage Hotel" in Delhi enquires on the website, is surveyed on site by an offline app, receives a quote that shows it saves money versus replacing, approves with an OTP, and sees its rooms progress on a board.

#### Planned / in progress (not live)
Per the task tracker (last updated 2026-09-29) Phase 0 mobilisation items are open: Meta Business Verification and App Review, WhatsApp number/WABA, DLT registration, Razorpay KYC, production Supabase project, VPS/Coolify, Sentry/uptime, blueprint sign-off. Branch protection on main is blocked. The client site uses the Eurobrass office phone and email temporarily and some imagery is generated and labelled illustrative.

#### Example visitor questions & answers
- **What is REDUX?** A restoration service by Eurobrass; our platform connects the website, lead CRM, staff portal, surveyor app, customer portal and admin.
- **Can I see a demo?** Yes: https://redux-demo-iota.vercel.app/ (safe demo) or the portfolio walkthrough https://agentix-portfolio.vercel.app/#/demo/redux/walkthrough.
- **Are messages and payments real?** No. In the demo, WhatsApp, OTP and payments are simulated; messages show in the demo outbox.
- **Does the surveyor app work without internet?** Yes, writes are queued and photos are only deleted locally after the server confirms them.
- **How are leads routed?** By city to a care executive, with a 1-hour call-back timer.
- **How does the customer approve a quote?** In the customer portal with a one-time code; this records the evidence and opens the job.
- **Who sees what?** Four roles: super admin, care executive, surveyor, customer, enforced with database row-level security.

#### Related projects
Eurobrass CRM (`eurobrass-crm`) is a separate dealer/manufacturing CRM for the same company; REDUX is the restoration service. Eurobrass corporate site (`eurobrass-site`) is the foundry brand page.

#### Verification notes
Verified: DEMO-GUIDE.md, CLAUDE.md, tracker, package.json, folder structure, migrations list, live homepage text and links. Not logged into the demo staff or portal. Not verified: live third-party integrations, number of catalog products on the live demo (taken from guide). Missing: confirmation which integrations are live outside the demo.

---

### Your Hair Company (YHC)
**Slug:** `yhc` · **Also known as:** YHC · **Category:** Multi-Product Business Platforms / doctor-led hair D2C · **Status:** Live site; platform backend in development (demo-mode prototype) - Partially verified
**Client / owner:** Your Hair Company (a product of Santure AI Private Limited, per site footer) · **Local folder:** `D:\Agentix Project\yhc-platform` · **Last activity:** 2026-10-27 (39 commits)

#### Spoken introduction
Your Hair Company is a doctor-led hair care brand. Visitors take a free guided 3D scalp scan with their phone, book a 30-minute video consult with a dermatologist for 500 rupees, and a doctor decides whether a treatment plan is needed. We built the website, shop, doctor portal, sales CRM and guarantee tracking around that journey.

#### Quick overview
The brand's rule is "scalp first, medicine only if it helps". The platform covers a cinematic public site, a scan-to-booking funnel, a doctor portal, a sales CRM, a customer account with plan progress, an admin area, and a tracked money-back guarantee. The code currently runs in an in-memory DEMO_MODE with a role-switcher at `/demo`; the production phases (real database, payments, messaging) are logged as not yet built.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Website | https://yourhaircompany.com/ | Production (real business - do not submit forms or book) | Public marketing site |
| Plans | https://yourhaircompany.com/plans | Production | 1, 2, 3 month plans |
| Guarantee | https://yourhaircompany.com/guarantee | Production | Conditions listed |
| Doctor | https://yourhaircompany.com/doctor-tyagi | Production | Doctor profile |
| Customer account | https://yourhaircompany.com/account | Login required | Not accessed |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/yhc/overview | Safe demo - fictional data | |
| Portfolio walkthrough | https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough | Safe demo | |
| Module: scan | https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough/scan | Safe demo | Scan funnel |
| Module: book | https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough/book | Safe demo | Slot and payment |
| Module: consult | https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough/consult | Safe demo | Doctor writes prescription |
| Module: sales-leads | https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough/sales-leads | Safe demo | Sales Kanban |
| Other module ids | site, account, shop, doctor-calendar, patients, followups, revenue, care, guarantee, admin-orders, catalog, audit | Safe demo | `/#/demo/yhc/walkthrough/<id>` |

#### Target users & business problem
People with hair loss who distrust generic products and want a doctor, a plan and follow-through; plus the doctor, sales/care team and admins. The platform replaces scattered booking, prescribing, sales follow-up and guarantee spreadsheets.

#### Features (complete inventory)
**1. Public site (Verified live).** Cinematic scroll-story home (Lenis smooth scroll, pinned hero, scroll-scrubbed films, WebGL light per PROGRESS), pages: Science, How it works, Results, Plans, Guarantee, Doctor (Dr. Anil Tyagi, dermatologist), FAQs, hair concerns (receding hairline, crown thinning, dandruff/scalp), products, journal/blog, about, contact, and legal pages (privacy, terms, refund, shipping, guarantee, medical disclaimer, grievance officer).
**2. Free 3D scalp scan funnel (Verified).** Name + mobile + consent, then up to 7 guided photos (hairline left/right, top, parting, crown, back) with on-screen guidance, result with reasons, and "a first check, not a diagnosis - the doctor decides". Evidence: live text; `src/components/journey/scan`; PROGRESS 2026-10-10 (7 guided zones). Limitation: in demo mode the scan result is simulated.
**3. Consultation booking (Verified).** Journey: details, scan, assessment, health form, slot selection and 500-rupee payment ("Razorpay (demo)" in demo), then portal and consult room route `/consult/[appointmentId]`. Availability engine in `src/lib/domain`.
**4. Plans and products (Verified live).** Three products, each in men's and women's packs: Hair Regrowth Solution (prescription only), Hair Nourishing Tablets, Hair Regrowth Capsules. Plans chosen after consultation: 1 month 5,999, 2 months 10,999, 3 months 14,999 (prices include GST per site); 500-rupee consult fee credited if bought within 7 days; the 3-month plan carries the guarantee. Prices are as printed on the live site and may change.
**5. Money-back guarantee (Verified live + code).** Conditions: use the prescribed plan for 3+ months without a break, reply to 75% of weekly check-ins, send monthly photos, join the follow-up consult, claim within 30 days of finishing; a doctor checks. Guarantee tracking pages exist for doctor, sales and admin (`src/app/doctor/guarantee`, `admin/guarantee`).
**6. Doctor portal (Verified in code, demo).** Availability, calendar, consult room, patients (profiles), prescriptions/plan, follow-ups, guarantee, revenue. Doctor and admin roles require MFA (aal2) at the database level.
**7. Sales CRM (Verified in code, demo).** Leads Kanban (new, contacted, interested, consult suggested, link sent and so on), tasks, care queue, performance; lead created automatically from scan/booking.
**8. Customer account (Verified in code).** Consultations, orders, plan progress, progress photos, scan, guarantee, support, profile.
**9. Admin (Verified in code).** Appointments, catalog, content, customers, guarantee, jobs, messaging templates, orders, settings, users, audit.
**10. WhatsApp/refills (Partially verified).** WhatsApp templates and reorder/refill logic exist in docs (`08_Messaging_Templates.md`) and domain code (reorder guard); live WhatsApp sending is not confirmed.

#### Key workflows (end to end)
1. Visitor starts the free scan, takes guided photos and sees a first result. 2. Books a 30-minute video consult and pays 500 rupees. 3. Doctor reviews history and photos, consults, and prescribes only if treatment can help. 4. Plan sent on WhatsApp, customer buys (consult fee credited within 7 days). 5. A sales lead is created and tracked; care follow-ups and weekly check-ins are scheduled. 6. Guarantee eligibility is tracked; claims are reviewed by a doctor. 7. Refills prompted before the plan ends.

#### User roles & permissions
Verified enum: `customer`, `doctor`, `sales`, `ops`, `admin`. Doctor and admin need MFA. Staff roles are granted by an admin (new auth users default to customer).

#### Technical architecture & integrations
Next.js 16.3 App Router, React 19, Tailwind 4, shadcn/ui, Lenis, Framer-style scroll scenes, Supabase (hosted `yhc-dev`, Mumbai) schema with RLS (single migration), Zod, pino logging, Vercel hosting. Intended integrations per README/TRD: Razorpay, WhatsApp (BSP/Meta Cloud API), MSG91, Resend, LiveKit (video), Google Calendar, Shiprocket. The demo store is in memory (single process; not suitable for serverless; resets on restart); demo access gate and signed sessions exist. Evidence: README, PROGRESS.md, package.json.

#### Business value & example scenarios
Turns a cold visitor into a booked, paid consult and a tracked plan with fewer manual follow-ups. Scenario: "Aarav Rao" scans his hairline at home, books a consult, receives a 3-month plan, and sees his day-30 photo check due in his account.

#### Planned / in progress (not live)
PROGRESS.md marks phases 01-12 (data layer, OTP/catalog/checkout, booking, doctor portal, recommendation, CRM, messaging, fulfilment, account, admin, hardening) as not started as production work; open client inputs include guarantee terms, product regulatory categories, refund rules, WhatsApp provider, Razorpay keys, doctor photos/registration number.

#### Example visitor questions & answers
- **How does it work?** Free scan, doctor consult, plan only if it helps.
- **How much is a consult?** 500 rupees for 30 minutes on video (per the site).
- **Is there a guarantee?** Yes for the 3-month plan, with listed conditions.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/yhc/walkthrough (the live site is a real business; please do not submit forms).
- **Is the scan a diagnosis?** No, the site says it is a first check and the doctor decides.
- **Who is the doctor?** The site presents Dr. Anil Tyagi, a dermatologist.

#### Related projects
Skinwise (`skinwise`) is a similar D2C concept for skin with an AI scan; YHC is doctor-led with video consults.

#### Verification notes
Verified: PROGRESS, README, package.json, folder structure, live public pages. Not accessed: `/demo` role switcher on production (not probed), account area. Unclear: whether the live site is running demo mode or real backends. Missing: confirmation of production data backend status and WhatsApp integration.

---

### Skinwise
**Slug:** `skinwise` · **Also known as:** myskinwise.com · **Category:** Multi-Product Business Platforms / skin-concern D2C · **Status:** Live - Verified
**Client / owner:** Skinwise (site footer: Razorbill Private Limited) · **Local folder:** `D:\Agentix Project\myskinwise` · **Last activity:** 2026-10-28

#### Spoken introduction
Skinwise is a skincare brand whose site lets you answer a guided skin check, upload a photo for an AI skin scan, or chat with a text assistant called Dr. Vivek. Every routine is reviewed by a real Skinwise expert. Note that the voice agent was removed from the site on 28 October 2026, so the assistant is text-only now.

#### Quick overview
Skinwise guides visitors from concern to a safe routine: a rules-based quiz and recommendation engine with safety exclusions, an AI photo scan, a grounded text assistant in 12 Indian languages, expert consultations, and a catalogue with orders placed through WhatsApp. An internal workspace lets experts review scans, leads and consultations.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Home | https://myskinwise.com/ | Production (real business) | Hindi/English toggle |
| Skin Check | https://myskinwise.com/skin-check | Production | Guided questions |
| Skin Analyzer | https://myskinwise.com/skin-check/analyzer | Production | Photo upload, needs consent |
| Assistant | https://myskinwise.com/assistant | Production | Text chat; /voice redirects here (301) |
| Formulations | https://myskinwise.com/products | Production | 13 products listed live |
| Consultation lookup | https://myskinwise.com/consultation | Production | Reference + phone |
| Admin | https://myskinwise.com/admin/login | Login required | Not accessed |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/skinwise/overview | Safe demo - fictional data | No voice module by design |
| Module: quiz | https://agentix-portfolio.vercel.app/#/demo/skinwise/walkthrough/quiz | Safe demo | Routine with caution flags |
| Module: scan | https://agentix-portfolio.vercel.app/#/demo/skinwise/walkthrough/scan | Safe demo | Mocked scan scorecard |
| Module: assistant | https://agentix-portfolio.vercel.app/#/demo/skinwise/walkthrough/assistant | Safe demo | Chat with Dr. Vivek |
| Other module ids | site, products, consultation, admin-leads, admin-orders, admin-consults | Safe demo | |

#### Target users & business problem
Shoppers overwhelmed by skincare choice or worried a product will not suit them (acne, pigmentation, dark circles, dryness, oily skin, scars). The brand team gets structured leads instead of loose chats.

#### Features (complete inventory)
**1. Concern pages and content (Verified).** Pigmentation, acne, acne scars, dark circles, oily skin, dry skin, other issues, plus concerns, skin types, ingredients, learn, about, contact, legal pages. English and Hindi.
**2. Skin Check quiz (Verified).** One question per screen (17 questions migrated from three older quizzes), required "why we ask" explainer, server-side validation, rules-based recommendation engine over the brand's real catalogue, never an LLM. Hard safety exclusions (pregnancy, sensitive skin) and doctor escalation; result is explicitly non-diagnostic with WhatsApp hand-off. Evidence: `docs/status/stage-2-completion.md`, `lib/assessment`, `lib/recommend/engine.ts`.
**3. AI Skin Analyzer (Verified).** Camera/photo upload with explicit AI-analysis consent, quality check, MediaPipe face geometry on the client for marker placement, and an AI vision observation (currently an OpenAI vision call) marking visible features like shine, redness, tone, texture on the face; always labelled a starting point reviewed by an expert; photos retained 90 days then purged by a daily cron. A deterministic Python service (`skin-cv-service`, OpenCV/MediaPipe/ONNX, FastAPI) and a `/skin-check/scan` route exist but its docs say the OpenAI-based scan stays live until the new engine passes acceptance (Phase 1 scaffold). Evidence: `docs/REMOVAL_AUDIT.md`, `skin-cv-service/README.md`, `vercel.json` cron.
**4. Text assistant "Dr. Vivek"/Skinwise AI (Verified).** Grounded in product knowledge and the recommendation engine so it never invents products; supports 12 conversation languages (English, Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Odia, Assamese); rate-limited; can be personalised with a consultation reference + phone; uses an OpenAI or Anthropic model depending on configured key. **Voice is no longer offered**: commit 7a6d463 on 2026-10-28 deleted the /voice route, API, STT/TTS/ElevenLabs code and every voice entry point; `/voice` permanently redirects to `/assistant`; microphone permission is disabled (camera kept for the scan).
**5. Formulations/products (Verified live).** 13 customised formulations across Cleanse, Treat, Eye care, Moisturise, Protect (for example anti-acne cleanser, depigmentation cream, acne gel, skin lightening gel, pigmentation serum, eye cream, day care cream, SPF-30, D-Tan pack) with real packaging and ingredient lists, product detail pages.
**6. Cart and checkout (Verified in code).** Review, contact details, then "Place order" opens WhatsApp with the order summary; there is no online payment by design. (The portfolio demo's "payments gateway" tag does not describe the live site.)
**7. Consultations (Verified).** Skin Check results create a consultation with a reference; customers look it up by reference + mobile; experts publish a reviewed routine.
**8. Expert workspace (Verified in code).** Login per expert (signed httpOnly session, HMAC cookie checked at the edge), leads, consultations, review queue of AI scans, orders, audit log of who acted.
**9. Analytics (Verified).** Event logging (events table, GA-style) in `lib/analytics.ts`.

#### Key workflows (end to end)
1. Visitor picks a concern or starts the Skin Check. 2. Answers guided questions; safety rules apply. 3. Optionally uploads a photo for the Skin Analyzer. 4. Result and a routine appear with caution flags; lead stored. 5. Expert reviews and publishes; customer looks up the consultation. 6. Customer places an order via WhatsApp.

#### User roles & permissions
Visitor (public); expert/admin accounts for the internal workspace. Admin pages are protected by middleware-verified signed sessions.

#### Technical architecture & integrations
Next.js 16, React 19, TypeScript strict, Tailwind v4, Framer Motion, Supabase (Postgres, private `skin-photos` bucket; 7 migrations), Zod; MediaPipe tasks-vision in browser; OpenAI vision and chat, optional Anthropic Claude Haiku for chat; Vercel (daily purge cron) or self-hosted via Dockerfile (standalone output) on Coolify; skin-cv-service Docker on Coolify. Secrets live in server environment variables.

#### Business value & example scenarios
Replaces generic product browsing with a guided, safe, expert-reviewed path. Scenario: "Meera" with breakouts completes the Skin Check, is steered away from a strong retinoid because she mentions pregnancy, and gets an expert-reviewed routine.

#### Planned / in progress (not live)
Deterministic skin-cv-service replacing the vision-LLM scan (Phase 1 scaffold); voice has been removed and is not planned.

#### Example visitor questions & answers
- **Does Skinwise have a voice agent?** No. It was removed on 28 October 2026; the text assistant is at /assistant.
- **Can I see a demo?** https://agentix-portfolio.vercel.app/#/demo/skinwise/walkthrough (fictional data).
- **Is the scan a diagnosis?** No, it is a starting point reviewed by an expert.
- **Can I pay online?** The live checkout places the order through WhatsApp; there is no online payment.
- **Which languages?** Site in English and Hindi; the chat in 12 languages.
- **How are photos handled?** Consent is required, stored privately and deleted after 90 days.

#### Related projects
YHC (doctor-led hair D2C), Dr. Shweta Diwan site (nutrition).

#### Verification notes
Verified: git log and removal commit, source, docs, live pages. Not accessed: admin. Note the root README.md is outdated (describes only the first static phase). Unconfirmed: which AI provider is active in production.

---

### NRI Trust
**Slug:** `nri-trust` · **Category:** Multi-Product Business Platforms / advisory · **Status:** Live - Partially verified
**Client / owner:** NRI Trust · **Local folder:** `D:\Agentix Project\NRI trust` · **Last activity:** 2026-05-26

#### Spoken introduction
NRI Trust is an advisory firm website for non-resident Indians who want to protect their parents' financial and legal life in India. We built a 3D globe experience, a risk-assessment engine that returns a GREEN, ORANGE or RED verdict with a prioritised action playbook and a PDF brief, and a client portal.

#### Quick overview
The firm manages insurance, bank accounts and KYC, property and tenancy, legal succession and emergency access for families abroad. The site funnels visitors by parent age group into zone pages and an assessment, captures leads, and emails the advisor.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Website | https://nritrust.co/ | Production (real business) | Preloader first |
| Pricing | https://nritrust.co/pricing | Production | |
| Services | https://nritrust.co/services | Production | Five practice areas |
| Client portal | https://nritrust.co/portal | Login required | Not accessed |
| Zone pages | https://nritrust.co/zone/green (also /orange, /red) | Production | |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/nri-trust/overview | Safe demo - fictional data | No interactive module file exists; overview only |

#### Target users & business problem
NRIs with ageing parents in India facing scattered accounts, unclear nominees and no emergency plan.

#### Features (complete inventory)
**1. Marketing site (Verified live).** Home with age-group selector (parents 55-65 planning zone, 65-75 active watch, 75+ critical care), problem cards, promise steps, how-it-works (discovery, diagnosis, onboarding, governance; 4-step process), pricing, services (banking, legal, property, insurance, emergency access), emergency response, resources, success stories, contact, terms, privacy, cookies. Plans shown: Essential Care 12,000 per month, Comprehensive 24,000, Premium Legacy 36,000 (retainer, as printed on the site). Evidence: live pages, `client/src/pages`.
**2. 3D globe and scroll motion (Verified in code).** three.js scenes (`Global3DScene`, `UnifiedGlobe`), GSAP, Framer Motion.
**3. Risk assessment engine (Verified in code).** Version 2.0 question bank by persona; the parent age bracket picks the persona (under 55 GREEN "Plan Ahead", 55-65 ORANGE "Plan Now", 65+ RED "Act Immediately"); answers score points and raise flags (for example nomination gap, health exposure, liquidity trap); score under 30 CRITICAL urgency, under 60 MODERATE; outputs persona, score, per-category risk (legal, health, asset, financial; status Protected/At risk/Review), a prioritised action playbook (CRITICAL/HIGH/MEDIUM) and a narrative summary. Playbook content was sourced from three advisory spreadsheets. Evidence: `shared/assessment-engine.ts`, `api/assessment-engine.ts`.
**4. Assessment submission, PDF and email (Verified in code).** `POST /api/assessment` stores the result in a MySQL table, emails the user a confirmation and the advisor a lead alert via Brevo, and returns a PDF link (`GET /api/assessment/:id/pdf`, generated with pdfkit). Contact form `POST /api/contact`.
**5. Client portal (Partially verified).** Tabs: dashboard, my services, document vault, upcoming deadlines, my manager, plus onboarding steps. In the code the portal user and data are client-side (no server fetch found in the auth context), so it appears to be a front-end prototype rather than a backed portal. Evidence: `AuthContext.tsx`, `PortalDashboard.tsx`.

#### Key workflows (end to end)
Visitor selects an age group, reads the zone page, completes the assessment, receives a verdict and playbook with a PDF, advisor gets an email lead, free consultation is booked, tier recommended, onboarding.

#### User roles & permissions
Visitor and portal client only (no staff roles in code).

#### Technical architecture & integrations
React 18 + Vite, wouter, Tailwind, Radix UI, TanStack Query, three.js, GSAP, Framer Motion; Express server (`server.ts`, `infra/`) and serverless `api/index.ts` on Vercel (`vercel.json` rewrites); Drizzle and MySQL driver; Brevo transactional email; pdfkit; `web.config` present (Windows/IIS style hosting file). Env: database URL, Brevo key, advisor email (names only). Not confirmed: which host serves production.

#### Business value & example scenarios
Gives a vague worry a measurable score and a to-do list. Scenario: "Nisha" in Toronto answers questions about her father (68) and gets a RED verdict with critical actions on Will, nominations and health cover.

#### Planned / in progress (not live)
A real authenticated portal backend is not evidenced.

#### Example visitor questions & answers
- **What do GREEN, ORANGE, RED mean?** Planning, urgent-planning and act-immediately zones based on parents' age and answers.
- **Is the assessment free?** The site offers a free consultation; assessment output includes a PDF brief.
- **Does it give legal advice?** The site describes the services as financial and legal, non-medical; advice itself comes from the firm.
- **Can I see a demo?** Portfolio overview: https://agentix-portfolio.vercel.app/#/demo/nri-trust/overview.
- **What does it cost?** Plans on the site range from 12,000 to 36,000 per month.

#### Related projects
Ekatva (relationship platform for insurance/wealth distributors).

#### Verification notes
Verified: code, engine, endpoints, live public pages. Not verified: portal real backend, hosting provider. Site statistics (families protected, assets managed) are marketing copy and differ between pages (500+ vs 200+ families); not independently verified. Missing: portal demo credentials or screenshots; production hosting.

---

## Business Websites

### AI Agentix corporate website
**Slug:** `ai-agentix-site` · **Category:** Business Websites · **Status:** Live - Verified
**Client / owner:** AI Agentix (AGENTiX) · **Local folder:** `D:\Agentix Project\AI AGENTIX` · **Last activity:** 2026-10-28

#### Spoken introduction
This is our own agency website. It presents our services, solutions, industries and case studies, captures leads through five forms, and has an "Ask AI" assistant that answers from the site's content and takes visitors to the right page, in English, Hinglish or Hindi.

#### Quick overview
A React single-page site with an Express API that handles leads and the assistant. The assistant uses retrieval over a site knowledge base and falls back to a rule-based mode if no language model is available.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Website | https://ai-agentix.com/ | Public marketing site | |
| Solutions | https://ai-agentix.com/solutions | Public site | 10 solutions |
| Technology | https://ai-agentix.com/technology | Public site | Eight-agent fleet |
| AI Studio | https://ai-agentix.com/ai-studio | Public site | Content studio |
| Contact | https://ai-agentix.com/contact | Public site | Audit, demo, partnership forms |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/ai-agentix-site/overview | Safe demo | No interactive module file; overview only |

#### Target users & business problem
Indian businesses evaluating AI automation. Problem: visitors skim and leave, and earlier forms lost leads.

#### Features (complete inventory)
**1. Pages (Verified).** Home, About, Solutions plus detail pages (sales, marketing, HRMS, operations, supply chain, finance, AI voice and chat, manufacturing), Industries plus detail pages (real estate, healthcare, education, hospitality, retail, manufacturing, logistics), Technology plus agent detail pages, Case Studies, AI Studio, legal pages, thank-you.
**2. Lead capture (Verified).** Five forms (Free AI Audit, Book a Demo, Partnership, floating consultation widget, newsletter) post to `/api/leads`; the lead is saved first on the server, then emailed and added to a Google Sheet, with automatic retry; origin check, honeypot, rate limit; DPDP consent stored; visitors reach the thank-you page only after the server confirms. Evidence: `WEBSITE_FIXES_COMPLETION_REPORT.md`, `server/src/leads.mjs`.
**3. RAG assistant "Ask AI" (Verified).** `POST /api/chat` with same-origin check and rate limit; retrieves from `knowledge.json` chunks using cosine similarity over embeddings (text-embedding-3-small) or a lexical fallback; model defaults to gpt-4o-mini; replies carry a navigate action so the page opens; intent answers work with no model key (free rule-based mode) and a daily cap applies to AI use; replies in English, Hinglish and Hindi. Evidence: `server/src/rag.mjs`, `app.mjs`, `intents.mjs`.
**4. Analytics and consent (Verified).** GA4 behind a cookie-consent banner; `generate_lead` conversion.
**5. SEO (Verified).** Prerendered meta, sitemap, compressed assets.

#### Key workflows (end to end)
Visitor asks a question, assistant retrieves, answers and navigates; visitor submits a form, lead is stored, emailed and sheeted, then thank-you page.

#### User roles & permissions
Public visitors only.

#### Technical architecture & integrations
React 18 + Vite + Tailwind + Framer Motion + react-router + helmet; Express 4 API (Node 20+); OpenAI SDK; Nodemailer (Gmail SMTP app password); Google Apps Script web app for Sheet; deployed on a VPS with nginx and pm2 (`deploy/deploy.sh` does a zero-downtime swap with rollback to `dist-prev`). Env names live in `server/.env` (not documented here).

#### Business value & example scenarios
No lead loss and answers around the clock. Scenario: a clinic owner asks "do you do WhatsApp automation for hospitals?" and is taken to the healthcare industry page.

#### Planned / in progress (not live)
None evidenced.

#### Example visitor questions & answers
- **Does the website have an AI assistant?** Yes, Ask AI, grounded on site content.
- **Which languages?** English, Hinglish, Hindi.
- **What happens when I submit a form?** The lead is saved, emailed to the team, added to a sheet, and a thank-you page appears.
- **Can I see a demo?** Visit https://ai-agentix.com/ directly.

#### Related projects
All AI Agentix products; the site itself markets them.

#### Verification notes
Verified: code, deployment docs, live pages. The performance claims on the live site (for example "340% more qualified meetings", "98% task automation") are marketing copy and not independently verified. Missing: nothing material.

---

### Dr. Shweta Diwan website and PHP admin
**Slug:** `dr-shweta-diwan` · **Category:** Business Websites · **Status:** Live - Partially verified
**Client / owner:** Dr. Shweta Diwan (nutritionist, emotional wellness coach) · **Local folder:** `D:\Agentix Project\well-known` (no git history) · **Last activity:** about 2026-10-23 (an update package in the folder is dated that day; `index.php` modified 2026-10-07)

#### Spoken introduction
This is the website for Dr. Shweta Diwan, a nutritionist and disease-reversal and emotional-wellness expert in Delhi. It has service pages, brain-wave analysis, blogs, transformations, calculators and an appointment form, plus a PHP admin panel that the team uses to manage content, orders and invoices.

#### Quick overview
A PHP and MySQL site where almost every page section is editable from an admin panel. It serves lead capture for Google Ads with a floating appointment form and a thank-you page for conversion tracking.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Website | https://drshwetadiwan.com/ | Production (real business) | |
| Blogs | https://drshwetadiwan.com/blogs | Production | 8 posts listed |
| Transformation | https://drshwetadiwan.com/transformation | Production | Before/after gallery |
| Contact | https://drshwetadiwan.com/contact | Production | |
| Admin | not documented here | Login required | Never opened |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/dr-shweta-diwan/overview | Safe demo | Overview only; no module file |

#### Target users & business problem
Clients aged 5 to 95 seeking nutrition and wellness plans; the clinic needs credibility, lead capture and content/billing control without a developer.

#### Features (complete inventory)
**1. Public site (Verified live + code).** Home (services: emotional wellness counselling, clinical nutrition support, disease reversal plans, sports nutrition, personalised fat-loss plans, brain analysis), "Book Your Brain Wave Scan", BMI calculator and calorie calculator forms on the home page, why-choose, media and awards, blogs (for example gut health, blood sugar, immune booster, brain waves), transformation before/after gallery, contact, privacy, terms, `llms.txt`, sitemap. Several service route names return pages (disease-reversal, fat-loss, sports-nutrition, brain).
**2. Lead widget (Verified in code).** Floating "Book an Appointment" form with thank-you page, as built with the lead-widget kit; GTM container present.
**3. Admin panel (Verified by file names only; contents not opened).** About 119 PHP files: banner, blogs, case studies, certificates, clients, expertise, gallery, health pages, team, testimonials, videos, quick links, breadcrumb, shipping, discount, orders (all, pending, success, details), invoice generation, users, profile, plus delete/ajax helpers. This indicates content management plus order/invoice handling. Anything about login, roles or data is Unverified.

#### Key workflows (end to end)
Visitor reads, submits the appointment form, reaches the thank-you page (conversion event); staff edit content in admin; orders and invoices are handled in admin (inferred from file names).

#### User roles & permissions
Unverified (admin not inspected).

#### Technical architecture & integrations
PHP (page templates plus shared `inc/`), MySQL (inferred from the admin and schema file existence; not inspected), Apache, cPanel-style hosting, PHPMailer mail folder, Google Tag Manager. Secrets and config deliberately not read.

#### Business value & example scenarios
A self-managed brand site. Scenario: the team publishes a new blog post from admin and the post appears on /blogs without a developer.

#### Planned / in progress (not live)
None evidenced.

#### Example visitor questions & answers
- **What does the site offer?** Nutrition, disease reversal, emotional wellness, sports nutrition, fat loss, brain wave analysis.
- **Is there an admin?** Yes, a PHP admin for the team; it is login-protected.
- **Can I see a demo?** The live site is public: https://drshwetadiwan.com/ (do not submit the form).

#### Related projects
Thames Wellness Spa (same lead-widget approach).

#### Verification notes
Verified: public pages, file layout. Not verified, by design: admin functionality, database, credentials. The stated "8K success stories" and "15 years" are the site's claims. `/services` returns a 404 on the live site. Missing: admin screenshots or demo login to describe screens.

---

### Thames Wellness Spa
**Slug:** `thames-spa` · **Category:** Business Websites · **Status:** Live - Verified
**Client / owner:** Thames Wellness Spa, Pimple Saudagar, Pune · **Local folder:** `D:\monum\Downloads\thameswellnessspa` (static HTML, 29 entries) · **Last activity:** 2026-10-26 (file dates; no git)

#### Spoken introduction
Thames Wellness Spa is a luxury spa in Pune. We built a calm static website with therapies, signature packages, a gallery, a franchise enquiry form and a floating appointment form.

#### Quick overview
A static HTML/CSS/JS site with a PHP mail handler, themed on the River Thames and five water elements (Tide, Drift, Ripple, Mist, Shell). It supports enquiries and franchise leads, with Google Ads and analytics tags.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Website | https://thameswellnessspa.com/ | Production (real business) | |
| Services | https://thameswellnessspa.com/services.html | Public site | |
| Packages | https://thameswellnessspa.com/signature-wellness-packages.html | Public site | |
| Franchise enquiry | https://thameswellnessspa.com/franchise-enquiry.html | Public site | |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/thames-spa/overview | Safe demo | Overview only |

#### Target users & business problem
Guests in Pune and prospective franchisees; a generic site fails to convey atmosphere or capture enquiries.

#### Features (complete inventory)
**1. Therapy pages (Verified).** Thames Wellness Voyage packages, traditional wellness therapies, modern wellness therapies, exfoliation and glow, targeted therapies, signature facials, luxury add-ons, gallery, testimonials, about.
**2. Signature packages (Verified).** For example Thames Signature (60 min Balinese plus 30 min head, neck, shoulder), Deep Sleep (60 min deep tissue plus 30 min back), Blissful Home Maker (60 min Swedish plus 30 min foot), Aromatic Radiance, Radiance and Sole, Couple's Package (90 min). Prices were not captured.
**3. Franchise enquiry (Verified).** Form with state, investment capacity (30-40 lakh to 50 lakh and above), start timeline, consent.
**4. Contact and floating appointment widget (Verified in code).** Widget auto-shows on the home page, posts to a lead endpoint and opens a thank-you page; contact and franchise forms go through `mail.php` (PHPMailer, reCAPTCHA-capable; settings come from a config file or server environment, not stored in the file).
**5. SEO and tracking (Verified).** Schema.org DaySpa JSON-LD, GTM and Google Ads tags, sitemap and robots.

#### Key workflows (end to end)
Guest browses therapies and packages, calls/WhatsApps or fills the form, the team calls to book.

#### User roles & permissions
Public only.

#### Technical architecture & integrations
Static HTML, Bootstrap, jQuery, GSAP, Swiper, Isotope; PHP/PHPMailer for mail; `web.config` (IIS-style hosting config) and `.user.ini` present; hosting provider not confirmed.

#### Business value & example scenarios
Fast static pages that rank locally and route every enquiry to the team. Scenario: a guest picks the Couple's Package and sends a callback request.

#### Planned / in progress (not live)
None.

#### Example visitor questions & answers
- **Where is it?** Pimple Saudagar, Pune (as printed on the site).
- **Can I buy a package online?** No online checkout; enquiries and calls.
- **Is there a franchise?** Yes, an enquiry form exists.
- **Can I see a demo?** Visit the live site.

#### Related projects
Dr. Shweta Diwan site.

#### Verification notes
Verified: folder and live pages. Not verified: hosting provider; package prices. Phone and email are on the public site (not repeated here).

---

### Eurobrass corporate site
**Slug:** `eurobrass-site` · **Category:** Business Websites · **Status:** Live - Verified
**Client / owner:** Eurobrass · **Local folder:** `D:\Agentix Project\EuroBrass` (landing part: `app/page.tsx`, `features/landing/*`) · **Last activity:** 2026-09-10

#### Spoken introduction
This is the Eurobrass brand landing page: a dark, crafted page that explains how a brass fitting is made, from cast to machine to finish, shows six product lines, and leads dealers to the dealer portal login.

#### Quick overview
The landing is the front door of the same Next.js app that hosts the Eurobrass CRM and dealer portal; the root path shows the marketing page and "Dealer login" opens the app.

#### Links & access
| Purpose | URL | Type | Notes |
|---|---|---|---|
| Landing | https://eurobrass-seven.vercel.app/ | Public marketing site | |
| Dealer login | https://eurobrass-seven.vercel.app/login | Login required | CRM; not accessed |
| Portfolio overview | https://agentix-portfolio.vercel.app/#/demo/eurobrass-site/overview | Safe demo | Overview only |
| CRM demo | https://agentix-portfolio.vercel.app/#/demo/eurobrass-crm/overview | Safe demo | Separate project |

#### Target users & business problem
Dealers and buyers who need to see craft and capacity and find their way to the portal.

#### Features (complete inventory)
**1. Landing sections (Verified).** Nav (Process, What we make, Dealer login), hero ("Solid brass, machined to the thread") with facts (finish: polished/satin/antique, alloy CuZn39Pb3, network, reach), process (Cast, Machine, Finish), six product lines (valves and cocks, pipe fittings, architectural hardware, sanitaryware, cable glands, custom machining), footer CTA to the portal.

#### Key workflows (end to end)
Visitor scrolls the process, browses lines, clicks Enter the Portal to /login.

#### User roles & permissions
Landing is public; the CRM has roles (see CRM entry).

#### Technical architecture & integrations
Next.js 16, React 19, Tailwind, Framer Motion; Vercel. The same app includes Supabase-related folders, zustand and Recharts for the CRM.

#### Business value & example scenarios
Gives a manufacturer a credible web presence tied to its dealer system.

#### Planned / in progress (not live)
None.

#### Example visitor questions & answers
- **What does Eurobrass make?** Six lines per the site: valves and cocks, pipe fittings, architectural hardware, sanitaryware, cable glands, custom machining.
- **Where do dealers log in?** /login.

#### Related projects
`eurobrass-crm` (the portal behind the login) and `redux` (restoration service).

#### Verification notes
Verified: landing code and live page. The site's "est. 1974" and "240+ dealers across Europe and South Asia" are page copy; the REDUX site separately says "50 years of Eurobrass". Not independently verified.

---
## E-commerce Experiences (concept brands)

**Important for every entry in this section and the next:** these brands are FICTIONAL. AI Agentix built them as showcase/concept websites to demonstrate design and interaction craft. They are not real shops; prices are sample prices, carts and bookings are simulated in the browser (no server calls were found in the source), and nothing can actually be bought or reserved. All are hosted under https://showcase-build-tau.vercel.app/<path>/ and are embedded in the portfolio. Portfolio link pattern: https://agentix-portfolio.vercel.app/#/demo/<slug>/overview (overview only; these concept sites have no interactive demo-module files). Type for every URL: Concept site (public, safe to explore). Status: Concept. All verified by loading the live page in Chrome and checking the source folder.

Common tech (Verified in each package.json unless noted): Next.js static export (React 19, Tailwind 4) using the in-house "Showreel Kit" engine: GSAP with ScrollTrigger, Lenis smooth scroll, custom cursor, loaders, reveal animations, and a "record mode" for filming; most kit sites also include three.js via React Three Fiber. Exceptions are called out.

### Fruitivo (perfume)
**Slug:** `fruitivo` · **Path:** `/perfume/` · **URL:** https://showcase-build-tau.vercel.app/perfume/ · **Source:** `E:\perfume-AS` · **Last activity:** 2026-09-27
**Spoken intro:** Fruitivo is a fictional organic perfume brand we made to show a mood-led way of choosing a fragrance. You click a mood such as The Romantic or The Rebel and discover a scent.
**Overview:** A single-page store with best sellers, offers (a sample code FRUITIVO20), and a "Find your fragrance mood" selector with seven moods, reviews and a refer-a-friend block. Verified (live text and `MoodSelector.jsx`).
**Signature features:** Mood selector (Verified); four signature scents Ruby Oud, Lavender, Blue Wave, Oud Wood with buy-now buttons (Verified); offers strip and testimonials (Verified). Checkout is not real.
**Tech stack:** React 19 + Vite 7, GSAP, Lenis, Framer Motion (Verified; not Next.js).
**Q&A:** Is Fruitivo real? No, concept brand. What is special? The mood selector. Can I see it? Link above or portfolio overview `/#/demo/fruitivo/overview`.
**Related:** Dewlab, Aurelle (other product-led concepts).

### DRIFY (streetwear)
**Slug:** `drify` · **Path:** `/drift/` · **URL:** https://showcase-build-tau.vercel.app/drift/ · **Source:** `E:\drift-ecommerce` · **Last activity:** 2026-09-27
**Spoken intro:** DRIFY is a fictional streetwear store with a drop-style hero and a product page you can quick-view and add to cart.
**Overview:** Home with new-drop banner, popular picks, categories (new arrivals, outerwear, activewear), a product viewer with size and colour pickers and ratings, and a cart. Verified. The product data file lists about 24 products (Verified by name count in `data/products.js`).
**Signature features:** Scroll-driven hero with canvas and two videos (Verified), product view with sizes XS-XL and add to cart (Verified), search box and categories (Verified).
**Tech stack:** Next.js 14, React 18, Tailwind 3, GSAP, Lenis (Verified).
**Q&A:** How many products? About 24 in the data file. Is checkout real? No.
**Related:** VARA Studio (fashion).

### Movade (travel)
**Slug:** `movade` · **Path:** `/travel/` · **URL:** https://showcase-build-tau.vercel.app/travel/ · **Source:** `E:\travel-agency` · **Last activity:** 2026-08-12
**Spoken intro:** Movade is a fictional travel agency site with a 3D depth hero, a property search bar and a popular-destinations section.
**Overview:** Hero "Explore the World, One Journey at a Time", search with location, dates, participants and type filters (All, Hotel, Apartment, Villa), coastal/water/cultural/mountain categories, popular destination cards with sample fares, how-it-works steps, testimonials. Verified (live).
**Signature features:** 3D depth scene (React Three Fiber) and scroll canvas hero (Verified in `components/3d`, `hero-scroll-canvas.tsx`); search form Verified, fake results not exercised.
**Tech stack:** Next.js 14, React 18, three.js with React Three Fiber and drei, GSAP, Lenis, Framer Motion (Verified).
**Q&A:** Are the fares real? No. Does it book trips? No.
**Related:** Cairnline Treks, Coral Bay.

### AURELLE (sarees)
**Slug:** `aurelle` · **Path:** `/aurelle/` · **URL:** https://showcase-build-tau.vercel.app/aurelle/ · **Source:** `E:\aurelle` · **Last activity:** 2026-10-08
**Spoken intro:** AURELLE is a fictional saree house with a cinematic hero, six mood-based edits and a cart drawer.
**Overview:** Hero "More than a Saree", six moods (for example Bridal red), new arrivals, best sellers, bridal collection, seasonal edit, trend sections, promo ribbon (free shipping, 7-day returns). Verified live. 17 products in `lib/products.ts` (Verified).
**Signature features:** Frame-sequence hero that loads an image sequence progressively and scrubs on scroll (Verified in `Hero.tsx`); cart drawer with checkout component (Verified `CartDrawer.tsx`); search and many interactive controls (live page).
**Tech stack:** Next.js 14, React 18, Tailwind 3, GSAP, Lenis, Framer Motion (Verified).
**Q&A:** How many products? 17. Real checkout? No.
**Related:** VARA Studio, Kanak Jewels.

### VARA Studio (fashion)
**Slug:** `vara` · **Path:** `/vara/` · **URL:** https://showcase-build-tau.vercel.app/vara/ · **Source:** `E:\vara-studio` (static `dist/`) · **Last activity:** not captured (no git date)
**Spoken intro:** VARA Studio is a fictional Gen Z fashion label with a canvas-drawn denim drape and a drag-to-select looks carousel.
**Overview:** "Eight looks, zero rules" with edits (denim, tailoring, going out, essentials), collection, product view, bag. Rupee sample prices. Verified (live and README). It began as a saree concept and was relaunched as fashion (README note).
**Signature features:** Canvas denim drape art and confetti/sparkle ornaments (Verified in `denim-art.js`, `ornaments.js`); collection search/sort, wishlist; bag drawer saved in browser localStorage (Verified in `app.js`); custom motion engine and fabric loupe (README).
**Tech stack:** Vanilla HTML, CSS and ES modules (no framework, no build), custom scroll engine (Verified; differs from the kit). Photos and fonts are not committed to the repo.
**Q&A:** Is the bag saved? Yes, in the browser only.
**Related:** DRIFY, Aurelle.

### Kanak Jewels
**Slug:** `kanak` · **Path:** `/kanak/` · **URL:** https://showcase-build-tau.vercel.app/kanak/ · **Source:** `E:\triozen\day-16-kanak` · **Last activity:** 2026-10-10
**Spoken intro:** Kanak Jewels is a fictional 22K gold jeweller where every price is itemised into gold value, making charge and GST.
**Overview:** Bridal, temple, daily wear and gifting collections; hero piece Mayuri Haar; "a piece for every hour" daily-wear clock; hallmark ring; reviews; bag. Verified live.
**Signature features:** Itemised price: sample rate 7,240 per gram for 22K (5,930 for 18K), 12% making, 3% GST, with a 22K/18K toggle that swaps the piece image (Verified in `content.ts`). The rate is a fixed sample constant labelled "Sample rate - concept site"; no moving live feed was found, so do not claim the rate updates in real time. Try-on view on a plain bust; Add to bag (Verified).
**Tech stack:** Next.js 16, React 19, Tailwind 4, GSAP, Lenis, three.js (Verified).
**Q&A:** Does the price move with the gold rate? The price is computed from a sample rate and itemised; the rate is fixed in code.
**Related:** Meridian, Aurelle.

### Meridian (watches)
**Slug:** `meridian` · **Path:** `/meridian/` · **URL:** https://showcase-build-tau.vercel.app/meridian/ · **Source:** `E:\triozen\day-1-watch-brand` · **Last activity:** 2026-10-14
**Spoken intro:** Meridian is a fictional luxury watch brand that takes a skeleton tourbillon apart layer by layer and lets you configure a dial and strap.
**Overview:** Hero "Time, taken apart", anatomy in five layers, collection of four featured references (fourteen claimed), configurator, workshop story, boutiques, care FAQ, bag. Sample prices in rupees. Verified live.
**Signature features:** Exploded anatomy on scroll (live text, `PlateHero`, `Specsheet`); Dial Studio configurator with dials and straps (Verified in `DialStudio.tsx`); reserve buttons and bag count (Verified).
**Tech stack:** Next.js 16, React 19, Tailwind 4, GSAP, Lenis (no three.js) (Verified).
**Q&A:** Can I buy? No; reserve is simulated.
**Related:** Halden, Kanak Jewels.

### Dewlab (skincare)
**Slug:** `dewlab` · **Path:** `/dewlab/` · **URL:** https://showcase-build-tau.vercel.app/dewlab/ · **Source:** `E:\triozen\day-12-dewlab` · **Last activity:** 2026-10-07
**Spoken intro:** Dewlab is a fictional serum brand where a single drop travels down the page and a Day 1 versus Day 28 slider shows results.
**Overview:** "Dew. Drop. Glow." with four actives (triple hyaluronic, niacinamide, apricot-kernel peptides, petal water), morning and night ritual, results panel, shop with add button. Verified live.
**Signature features:** Drop that travels the page (`DropTraveller`, `Drop`, `BeadLoop`), before/after slider (`BeforeAfter`), animated counters, ritual steps (Verified). Results figures are sample copy on a concept brand.
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Q&A:** Are the results real? No, concept copy.
**Related:** Fruitivo, Melt Theory.

### Melt Theory (ice cream)
**Slug:** `melt` · **Path:** `/melt/` · **URL:** https://showcase-build-tau.vercel.app/melt/ · **Source:** `E:\triozen\day-3-melt` · **Last activity:** 2026-10-05
**Spoken intro:** Melt Theory is a fictional Hyderabad ice-cream parlour with a scoop stacker that adds up the price as you build.
**Overview:** Small-batch hand-churned story, flavour of the week, today's six flavours, build your cone, treats, deals, parlours, order counter. Verified live.
**Signature features:** Scoop stacker with a running total (Verified: total from scoop prices in `ScoopStacker.tsx`; the portfolio's "live receipt" wording is not confirmed literally), flavour wave marquee, drip edge animation (Verified components).
**Tech stack:** Next.js 16, React 19, Tailwind 4, GSAP, Lenis (no three.js) (Verified).
**Q&A:** Can I order? No, simulated.
**Related:** Crumb & Co.

### Zip EV (e-scooter)
**Slug:** `zipev` · **Path:** `/zipev/` · **URL:** https://showcase-build-tau.vercel.app/zipev/ · **Source:** `E:\triozen\day-13-zip-ev` · **Last activity:** 2026-10-08
**Spoken intro:** Zip EV is a fictional electric-scooter brand where you ride through the city with your trackpad and watch range and speed change.
**Overview:** Hero "Ride through the city with your trackpad", true range (City 151 km, Eco 172 km, Sport 118 km), charging options, corner light, four colours at one price, rider notes, pick-your-model section with EMI note, test-ride CTA, shop row. All sample numbers. Verified live.
**Signature features:** Throttle ride scene (`ThrottleRide`), count-up spec rows, battery swap, colour picker (`ColourPicker`), test-ride tunnel and a "Jump to" command palette (Verified components and text); test-ride booking confirmation is simulated.
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Q&A:** Are specs real? No, sample specs. Can I book a test ride? The form is simulated.
**Related:** Vaskaro.

### Crumb & Co (bakery)
**Slug:** `crumb` · **Path:** `/crumb/` · **URL:** https://showcase-build-tau.vercel.app/crumb/ · **Source:** `E:\triozen\day-8-Crumb` · **Last activity:** 2026-10-05
**Spoken intro:** Crumb and Co is a fictional Hyderabad bakery where you build a cake base by scrolling and then build your own cake with live pricing.
**Overview:** "Build a base by scrolling" with seven layers, today's counter (Chocolate Crown, Vanilla Cloud, Pistachio Rose, Strawberry Shortcake, priced per kg), add-ons, build-your-own, visit, pickup and delivery. Verified live.
**Signature features:** Build Your Own cake with shape, sponge, finish and size chips and a live rupee total (from 525; Verified in `BuildYourOwn.tsx`); scroll-built layered cake; "Just ordered" strip (Verified). The live page is a cake builder, not a box builder as the portfolio card says.
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Q&A:** Can I order? No, simulated.
**Related:** Melt Theory.

---

## Immersive Brand Websites (concept brands)

(Same notes as above: fictional brands, simulated actions, sample prices.)

### Cairnline Treks
**Slug:** `cairnline` · **Path:** `/cairnline/` · **URL:** https://showcase-build-tau.vercel.app/cairnline/ · **Source:** `E:\cairnline` · **Last activity:** 2026-10-12
**Spoken intro:** Cairnline Treks is a fictional Himalayan trekking company whose home page lets you fly over a route before you book.
**Overview:** Six sample treks (Everest Base Camp 12 days, Annapurna Circuit 16, Markha Valley 9, Valley of Flowers 6, Kedarkantha 5, Goecha La 11) with altitude, best months and sample prices; scroll-linked altitude chart, when to go, stays, next departures, trip bag. Verified live.
**Signature features:** Flyover films with an Everest/Annapurna/Ladakh switcher; altitude climb with temperatures per stage; departures board; trip bag (Verified). It is the Showreel Kit v2 reference (README: one showcase site a day).
**Tech stack:** Next.js 16, React 19, Tailwind 4, GSAP, Lenis, three.js with React Three Fiber (Verified).
**Q&A:** Are the prices real? Sample.
**Related:** Movade, Vaskaro.

### Saffron & Smoke
**Slug:** `saffron` · **Path:** `/saffron/` · **URL:** https://showcase-build-tau.vercel.app/saffron/ · **Source:** `E:\triozen\day-10-saffron` · **Last activity:** 2026-10-06
**Spoken intro:** Saffron and Smoke is a fictional fire-kitchen restaurant whose tasting menu cooks as you scroll.
**Overview:** Nine-course tasting at a sample 7,500 per guest, course plating scenes, tandoor facts (480 degrees, lit at five), the 14-hour shank signature, pairings, reservation section. Verified live.
**Signature features:** Scroll-cooked course rail (`CourseRail`, `TandoorFire`), animated numbers, pairing sheet, reserve-a-table component (`ReserveTable`, simulated) (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Q&A:** Can I reserve? The booking is simulated.
**Related:** Crumb & Co, Coral Bay.

### Aurelune Residences
**Slug:** `aurelune` · **Path:** `/aurelune/` · **URL:** https://showcase-build-tau.vercel.app/aurelune/ · **Source:** `E:\triozen\day-21-aurelune` · **Last activity:** 2026-10-15
**Spoken intro:** Aurelune is a fictional coastal villa development where rooms light up as you scroll and a map shows the four coves.
**Overview:** Three villas (Lunessa available, Aldevar reserved, Cassiane coming soon) with room-by-room views and sample prices in crore; amenities; four coves with travel times. It is a residences brand, not a hotel. Verified live.
**Signature features:** Room-by-room lighting, villa detail (`VillaDetail`), locations map (`Locations`), booking component (simulated) (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Related:** Coral Bay.

### Halden (smartphone launch)
**Slug:** `halden` · **Path:** `/halden/` · **URL:** https://showcase-build-tau.vercel.app/halden/ · **Source:** `E:\triozen\day-19-halden-phone` · **Last activity:** 2026-10-15
**Spoken intro:** Halden is a fictional phone launch page where a product film is scrubbed by your scroll through layers, camera, display and finishes.
**Overview:** Nav of Layers, Camera, Display, Finishes and "Where to buy?"; from a sample price 49,900. Initial text is minimal because content builds with the film. Verified live (partial text).
**Signature features:** Scroll-scrubbed film (`Film`); finishes section where the active finish follows the film (a click colour picker was not confirmed); prices (`HaldenPrices`) (Verified in components).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Related:** Meridian.

### Iron Temple
**Slug:** `irontemple` · **Path:** `/irontemple/` · **URL:** https://showcase-build-tau.vercel.app/irontemple/ · **Source:** `E:\triozen\day-11-iron-temple` · **Last activity:** 2026-10-06
**Spoken intro:** Iron Temple is a fictional strength gym where you load the bar plate by plate and see a live rep counter.
**Overview:** "Lift heavy. Rest. Repeat.", floor facts, house rules, four programmes (strength, Olympic lifting, hypertrophy, conditioning), coaches, memberships, weekly floor schedule, book a trial. Verified live.
**Signature features:** Load-the-bar interaction (`LoadTheBar`, `Plates`), split-flap board (`FlapBoard`), floor plan and plan list (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).
**Related:** Vaskaro.

### Marigold Noir
**Slug:** `marigold` · **Path:** `/marigold/` · **URL:** https://showcase-build-tau.vercel.app/marigold/ · **Source:** `E:\triozen\day-24-marigold-noir` · **Last activity:** 2026-10-19
**Spoken intro:** Marigold Noir is a fictional wedding photographer whose site tells four functions and seven ceremony rounds as a film.
**Overview:** Haldi, Mehendi, Sangeet and Wedding chapters; seven rounds; details; portfolio; three packages (sample 95,000, 240,000, 480,000); album option; FAQ; hold-your-date enquiry. The portfolio calls it a seven-chapter film; the live structure is four functions plus a seven-round ceremony. Verified live.
**Signature features:** Chapters, album viewer (`Album`), packages (`Packages`), booking enquiry (simulated) (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).

### Coral Bay
**Slug:** `coralbay` · **Path:** `/coralbay/` · **URL:** https://showcase-build-tau.vercel.app/coralbay/ · **Source:** `E:\triozen\day-14-coral-bay` · **Last activity:** 2026-10-08
**Spoken intro:** Coral Bay is a fictional South Goa villa resort whose home page puts the holiday one scroll away, with a stay planner.
**Overview:** 24 villas on a quiet bay; four villa types with nightly sample rates (16,500 to 58,000); dining (The Deck, Laterite, Sunset Bar); spa menu; a day-at-the-bay triptych; guest notes; a local-conditions strip. Verified live.
**Signature features:** Check-in/out and villa planner (`StayPlanner`, simulated availability), villa postcards, dining index, spa pebble (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).

### Tallow & Tape
**Slug:** `tallow-tape` · **Path:** `/tallow/` · **URL:** https://showcase-build-tau.vercel.app/tallow/ · **Source:** `E:\triozen\day-22-tallow-tape` · **Last activity:** 2026-10-16
**Spoken intro:** Tallow and Tape is a fictional recording and rehearsal studio with a record-light loader and a booking section.
**Overview:** Three rooms (control room, live room, vocal booth), four services (recording, mixing, mastering, rehearsal) with sample starting prices, gear list, session log, book-a-day. Verified live. No audio-track player was confirmed (the portfolio mention of tracks is unverified).
**Signature features:** Hover-a-room panels, session rail, shutter and wipe transitions, booking (simulated) (Verified components).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).

### Vaskaro
**Slug:** `vaskaro` · **Path:** `/vaskaro/` · **URL:** https://showcase-build-tau.vercel.app/vaskaro/ · **Source:** `E:\triozen\day-23-vaskaro` · **Last activity:** 2026-10-16
**Spoken intro:** Vaskaro is a fictional mountain motorcycle brand where scrolling shifts gears up a mountain pass.
**Overview:** Passo 650 (sample 6.9 lakh), six chapters, engine spec counters, gear shop (jacket, helmet, gloves, tank bag with add to cart), five road routes with bend counts, test-ride booking. Verified live.
**Signature features:** Scroll-as-gear dial, roads section, gear shop cart, booking (`Booking`, simulated) (Verified).
**Tech stack:** Next.js 16, React 19, GSAP, Lenis, three.js (Verified).

---

## Infrastructure & Delivery

### Deployment and hosting capabilities (delivery-infra)
**Slug:** `delivery-infra` · **Category:** Delivery · **Status:** Live capability (not a product) - Partially verified
There is no cPanel or hosting-management product at AI Agentix. What exists is deployment capability shown across repos. Portfolio: https://agentix-portfolio.vercel.app/#/demo/delivery-infra/overview.

#### Spoken introduction
We deploy on whatever suits the client: Vercel for fast front ends, a Docker-based VPS managed with Coolify for apps that need background workers, classic Apache/cPanel hosting for PHP and static sites, Supabase for database and storage, and Kubernetes manifests for our SocialPush microservices.

#### Capabilities and evidence
- **Coolify VPS plus Docker (Verified).** Dockerfiles and docs exist for SocialFlow, AGENTiX, Woodpecker PMS (production image; a second worker resource runs `npm run worker`), LeadForge (`deploy/docker-compose.yml`: Redis, workers, API and web, with Postgres on Supabase), SocialPush (compose file notes Coolify routing), Max Fitness (`docs/09-operations/coolify-setup.md`: web and worker built from Dockerfiles so the reminder worker can run), REDUX (production target Docker on a Mumbai VPS via Coolify per CLAUDE.md) and Skinwise (standalone Dockerfile; the CV service on Coolify). The recurring reason in the docs: Vercel cannot hold long-running workers.
- **Vercel (Verified).** `vercel.json` in Umang, Kaaya, Voice-CRM, NRI Trust, Redux, YHC, Skinwise (with a cron) and others; the showcase is a Vercel project.
- **cPanel / Apache / PHP and MySQL (Verified in part).** The Umang hospital frontend is documented as deployed on "Apache/cPanel hosting"; the Dr. Shweta Diwan site is PHP; Thames Wellness Spa uses a PHP mail handler plus static pages (its `web.config` hints at IIS). DirectAdmin was not found in any document and is unverified. The Fitness First Dwarka `.htaccess` is also Apache but that project is outside this part.
- **VPS with nginx and pm2 (Verified).** The AI Agentix corporate site deploys by script to a VPS (nginx security headers, pm2, zero-downtime swap with rollback to `dist-prev`).
- **Supabase (Verified).** Postgres, auth and storage for many projects; a `supabase-proxy` folder exists in Umang and SocialPush.
- **Kubernetes (Verified).** `auto-posting/k8s/deployments.yaml` defines a secret plus deployments and services for account-service (2 replicas), post-service (2) and bullmq-worker (3); `docker-compose.yml` runs the stack on a single host.
- **Hostinger (Partially verified).** Agentix CRM has a `deploy_hostinger/.htaccess` folder.

#### Example Q&A
- Do you offer hosting management? There is no product for that; we deploy and operate each project on the right host.
- Do you use cPanel? Yes, for PHP and static client sites.
- Why not Vercel for everything? Apps with background workers (queues, reminders) need a long-running process, so those go on Docker/Coolify.

#### Verification notes
Verified from files. Not verified: the current live host of each production site; DirectAdmin; whether the k8s manifests are running anywhere.

### Showcase pipeline (showcase-pipeline)
**Slug:** `showcase-pipeline` · **Category:** Delivery · **Status:** Internal tooling, active - Verified
**Local folder:** `E:\showcase-tools` (changed 2026-10-21/22). Portfolio: https://agentix-portfolio.vercel.app/#/demo/showcase-pipeline/overview.

#### Spoken introduction
Behind the concept sites is a small internal pipeline that builds each kit site, adds it to one combined showcase, audits it at seven screen widths, and deploys it.

#### What the scripts do (Verified)
- `add-kit-site.ps1`: patches the site's `next.config.ts` for a sub-path static export (only when `SHOWCASE_BASE` is set), installs dependencies, builds, copies only the site pages and its public assets into `E:\showcase-build\<slug>`, refuses to overwrite assets owned by another site, and runs sanity scans for broken base paths.
- `add-card.py`: adds or replaces the site's card on the showcase landing page and updates the site count text.
- `check-site.js`: loads a site in Chrome via Playwright, scrolls it, and reports title, page height and every console error, page error, failed request and HTTP 400 or higher.
- `audit.js`: responsive audit at 320, 390, 768, 1024, 1366, 1920 and 2560 pixels, reporting horizontal overflow, elements sticking out of the viewport, page errors, and six screenshots per width.
- `sheet.py`: makes a contact sheet of the audit screenshots.
- `deploy.sh`: deploys `E:\showcase-build` to Vercel production (project `showcase-build`), removes older deployments to save storage, and checks the live site returns 200.
- Showreel Kit v2 (README in `E:\cairnline`): one showcase site a day on a shared engine (smooth scroll, scroll-driven video, loader, cursor, reveals, record mode) with a new design each time.

#### Example Q&A
- How are concept sites tested? Automatically at seven widths plus a console-error check.
- Where are they hosted? All on one Vercel project, each under its own path.

#### Verification notes
Verified from script source. Not verified: the content of `runs/` (36 output entries, not opened).

---

## How AI Agentix builds

Patterns verified from package.json files and source across the repos. "Verified" means a dependency or API call was found in code; marketing copy is not counted.

- **Next.js and React (App Router):** AGENTiX, SocialFlow, Redux, YHC, Skinwise, Eurobrass CRM and site, Gov-HIMS, Umang HIMS, Woodpecker PMS, Max Fitness, LeadForge, SocialPush web, and all kit concept sites. Vite + React: Voice-CRM, Riya CRM, Agentix CRM, NRI Trust, AI Agentix site, Umang website, Kaaya, Fruitivo.
- **Supabase (Postgres, Auth, Storage, RLS):** AGENTiX, SocialFlow, Redux (RLS on every table), YHC, Skinwise, Umang, LeadForge, Gov-HIMS, Umang HIMS, SocialPush. **Prisma/Postgres:** Woodpecker PMS, Max Fitness; Kaaya uses Prisma with MySQL. **Drizzle:** Agentix CRM, NRI Trust. **PHP/MySQL:** Dr. Shweta Diwan site.
- **Queues and workers:** BullMQ with Redis (SocialPush, LeadForge), pg-boss (Woodpecker, Max Fitness), pgmq with pg_cron (Redux).
- **Meta APIs (WhatsApp Cloud, Instagram, Facebook Graph):** AGENTiX, SocialFlow, SocialPush, Redux (integration modules), Max Fitness (partial). **Google Ads, Business Profile and Maps:** AGENTiX.
- **Payments:** Razorpay in AGENTiX, SocialFlow, Max Fitness, Woodpecker and Redux (simulated in its demo); Stripe is a dependency in Kaaya.
- **LLMs:** OpenAI (AI Agentix site assistant and embeddings, AGENTiX, Skinwise scan and chat), Anthropic Claude (optional Skinwise chat model; also found in AGENTiX, LeadForge, Woodpecker, Gov-HIMS code), Gemini (Agentix CRM, SocialPush), OpenRouter (AGENTiX, SocialFlow), Groq and Whisper (AGENTiX; Whisper also LeadForge). RAG with embeddings: AI Agentix site. Deterministic rule engines beside the LLMs: Skinwise recommendations, NRI Trust assessment.
- **Voice:** ElevenLabs speech-to-text/text-to-speech was used in the Skinwise voice agent until its removal on 2026-10-28 (per the removal commit) and appears in Gov-HIMS code; Deepgram appears in Gov-HIMS. The portfolio's voice product is VoiceCRM (another part).
- **Face and vision:** MediaPipe tasks-vision (Skinwise, Max Fitness check-in); OpenCV/ONNX Python service (Skinwise CV service).
- **Motion and 3D:** GSAP with ScrollTrigger and Lenis (kit concept sites, YHC, NRI Trust, Umang website), three.js and React Three Fiber (most kit sites, NRI Trust globe, Movade), Framer Motion widely, Fabric.js (SocialFlow design editor), ReactFlow (AGENTiX flow builder), Recharts for dashboards.
- **Documents and email:** pdfkit (NRI Trust), Gotenberg (Redux PDFs), Nodemailer, PHPMailer, Brevo and Resend for email.
- **Mobile:** Expo SDK 57 Android app (Redux surveyor).
- **Quality and process:** Vitest, Playwright, pgTAP database tests (Redux), CI gates, written decision records and business-rule IDs in code (Redux), responsive audits (showcase pipeline).
- **Hosting:** see Deployment and hosting capabilities above.

#### Example Q&A
- What stack do you usually use? Next.js/React front ends, Supabase or Postgres, and queue workers for background jobs; Meta, Razorpay and LLM APIs where the product needs them.
- Do you build with AI models? Yes; models are used where they help and plain rules where safety matters, as in Skinwise.

#### Verification notes
Package.json scans covered 20 repos; the source keyword scan did not finish for every repo before the session limit (Skinwise, YHC, NRI, Redux, AI Agentix site, Umang HIMS, YouTube Automation results were not collected by script, so those integrations rely on the per-project checks above). Absences, such as no integrations found for Voice-CRM or Riya CRM beyond Supabase, are unconfirmed rather than disproved.

---

## Cross-project intelligence

### Product families and ecosystems

| Family | Projects | How they relate |
|---|---|---|
| **AGENTiX messaging family** | AGENTiX → SocialFlow (incl. InstaAgent v1) | AGENTiX is the flagship multi-tenant AI agent for **WhatsApp + Instagram** with a shared inbox, lead-temperature CRM, campaigns, flows and Google growth tools. SocialFlow is a separate **Instagram-first** automation platform: comment→DM with follow-gate, content studio, reels, profile score and post audit. InstaAgent was SocialFlow's single-tenant first version. |
| **WhatsApp bot + CRM pairs** | Riya (Fitness First CRM), VoiceCRM | Both are dashboards that sit on top of an AI bot's conversations. Riya reads a WhatsApp gym bot's chats and tracks trials and conversions. VoiceCRM reads an AI **voice** bot's calls, with transcripts, summaries and sentiment. AGENTiX bundles the bot and the CRM in one product. |
| **Eurobrass group** | Eurobrass corporate site, Eurobrass CRM, REDUX platform | The same manufacturer. The corporate site presents the brass foundry, Eurobrass CRM runs sales (leads, dealers, quotations, orders, service), and REDUX is the separate **bath-fittings restoration** business with its own website, lead CRM, surveyor app, customer portal and admin. |
| **Umang Hospital** | Umang website + CMS, Umang Hospital HIMS, (Agentix HIMS) | The website handles patient acquisition: specialities, doctors, appointment and insurance leads, and an admin CMS. Umang HIMS runs the hospital's OPD journey. Umang HIMS was carved out of **Agentix HIMS**, the larger state-scale system built for government health with 24+ role portals and Secretary/CMO cockpits. |
| **Max Fitness** | Max Fitness website, Max Register | The public bilingual website (plans, sign-up, QR onboarding) and the owner's Hindi-first CRM (members, renewals, reminders, attendance, face check-in kiosk, reports). They share one codebase and database. |
| **Fitness First Dwarka** | Fitness First website, Riya CRM | The marketing site collects leads; the Riya WhatsApp bot and CRM handle lead conversations and trial bookings. |
| **Hospitality** | Woodpecker PMS, Kaaya Eco Resort | Woodpecker is a full multi-property **operations platform**: front desk, folios and GST invoicing, housekeeping, POS, payroll, OTA channels, owner portal, guest booking site. Kaaya is a resort's **website with booking**: rooms, availability, payments, guest accounts and an admin. |
| **D2C health & beauty** | Your Hair Company, Skinwise | Both are consumer brands that combine content with tools. YHC offers a scalp scan, paid video consultations, a doctor portal and a sales CRM. Skinwise offers a skin quiz, photo scan, text assistant, store and consultations. Skinwise no longer has a voice agent (removed 2026-10-28). |
| **Content automation** | SocialPush, YT-Automation, SocialFlow's content studio | SocialPush schedules and publishes **one post to many platforms**. YT-Automation **creates** short videos with AI and publishes them to YouTube after human approval. SocialFlow's studio and calendar are Instagram-focused. |
| **Showcase / concept brands** | 20 concept sites + showcase-pipeline | Fictional brands built to demonstrate design and motion craft, all deployed together on showcase-build-tau.vercel.app by the showcase pipeline tools. |

### Comparison: AI messaging & CRM products

| Need | AGENTiX | SocialFlow | VoiceCRM | Riya CRM |
|---|---|---|---|---|
| Channel | WhatsApp + Instagram | Instagram (+ Facebook, Telegram) | Voice calls (+ WhatsApp follow-up) | WhatsApp |
| AI agent included | Yes, live agent replies and books | Yes, AI DM replies grounded in a knowledge base | Consumes calls from a separate voice bot | Consumes chats from the separate "Riya" bot |
| CRM | Kanban with hot/warm/cold lead temperature | Contacts, leads, bookings | Leads with score, sentiment, tasks | Leads with outcomes and tasks |
| Campaigns / broadcasts | Yes | Yes | No (tasks and follow-ups) | No |
| Visual flow builder | Yes | Yes | No | No |
| Best for | Businesses selling over WhatsApp/IG | Instagram growth and creators | Teams running AI calling | A single gym's WhatsApp lead desk |

### Comparison: operations platforms

| Need | Woodpecker PMS | Agentix HIMS | Umang HIMS | Max Register | Eurobrass CRM |
|---|---|---|---|---|---|
| Industry | Serviced apartments / hotels | Government hospitals, state health | Single hospital OPD | Neighbourhood gym | Fittings manufacturer |
| Core loop | Booking → check-in → folio → GST invoice | Triage → consult → lab → pharmacy → billing → discharge | Registration → vitals → consult → billing → pharmacy | Member → fee due → reminder → renew → receipt | Lead → quotation → order → service |
| Distinctive | Tape chart, owner portal, OTA channels, payroll | Role portals, NEWS2, AB-PMJAY/ABHA, Secretary/CMO cockpits | Voice registration agent "Asha", public visit tracker, Hindi | Hindi-first, face check-in kiosk, WhatsApp reminder engine | Dealer portal, quotation PDF, technician tickets |

### Which project to mention for a requirement

| Visitor says… | Point to | Why |
|---|---|---|
| "I want an AI to reply to WhatsApp/Instagram leads and book appointments" | **AGENTiX** (`#/demo/agentix/walkthrough/conversations`) | Live AI agent, shared inbox, CRM and bookings in one product |
| "Instagram comments → DMs, follow-gate, content planning" | **SocialFlow** | Comment-to-DM automation, follow-gate, studio, profile score |
| "Post the same content to all my social accounts" | **SocialPush** | One composer, many platforms, scheduling, retries, analytics |
| "Faceless YouTube channel / AI shorts" | **YT-Automation** | Idea → script → voice → visuals → captions → human QA → publish, with a cost ceiling |
| "We use an AI calling bot and need a CRM for the calls" | **VoiceCRM** | Transcripts, summaries, sentiment, scoring, tasks |
| "Hotel / serviced apartments software" | **Woodpecker PMS**; for a resort website with booking, **Kaaya** | Full PMS vs website-plus-booking |
| "Hospital management / HIMS" | **Agentix HIMS** (multi-hospital or government scale) or **Umang HIMS** (single-hospital OPD) | Scale and scope differ |
| "Gym software" | **Max Register** (+ Max Fitness website) | Members, renewals, WhatsApp reminders, face check-in |
| "Sales CRM with quotations and dealers" | **Eurobrass CRM** | Quotation builder with GST, dealer portal, orders, service |
| "Find B2B leads from a plain-English request" | **LeadForge** (in development) | Sentence → research plan → businesses with sourced contact data |
| "Field-service business with surveys, quotes and a customer portal" | **REDUX** | Lead CRM, offline surveyor app, quotes, portal, invoices |
| "Doctor-led D2C with consultations" | **Your Hair Company** | Scan funnel, paid consults, doctor portal, sales CRM |
| "Skincare quiz and recommendations" | **Skinwise** | Rules-based quiz with safety cautions, photo scan, store |
| "NRI financial/property protection advisory" | **NRI Trust** | Risk assessment → persona → playbook → PDF report |
| "A premium, animated brand website or online store" | Concept brands, e.g. **Aurelle** (store), **Meridian** (configurator), **Cairnline** (immersive story) | Show design and motion craft |
| "Internal agency/project tracking" | **Agentix CRM** | Kanban stories, clients, invoices, revenue insights |

### Shared technology (verified across repos; see "How AI Agentix builds")
- **Next.js / React** with **Tailwind** for most web apps; **Supabase** (Postgres, auth, storage, RLS) is the most common backend; **Prisma + Postgres** is used for Woodpecker and Max.
- **Meta WhatsApp Cloud API / Instagram Graph API** for AGENTiX, SocialFlow, REDUX and Max; **Razorpay** for payments in India; **OpenAI / OpenRouter / Gemini** for AI features; **ElevenLabs** for the voices in YT-Automation and Umang HIMS's "Asha".
- Hosting: **Coolify on a VPS (Docker)** for AGENTiX, SocialFlow, Woodpecker, Max and Skinwise; **Vercel** for many frontends and demos; **Apache/cPanel or DirectAdmin** for Umang, Fitness First and Dr. Shweta Diwan.

---

## Coverage checklist

Verification levels below are taken from each project's own **Verification notes**. "Missing" lists exactly what would let the documentation be completed.

| # | Project (slug) | Level | What is missing |
|---|---|---|---|
| 1 | AGENTiX (`agentix`) | Verified (code, docs, public pages) | Logged-in app not viewed; exact per-role permission matrix; current Meta App Review / Google OAuth / GBP API approval status; "All-in-One" plan feature list |
| 2 | SocialFlow (`socialflow`) | Verified (code, docs, landing) | Logged-in app not viewed; per-role permissions; Meta Advanced Access status |
| 3 | VoiceCRM (`voicecrm`) | Partially verified | Logged-in app; which voice-bot platform feeds it |
| 4 | Riya — Fitness First CRM (`riya-crm`) | Verified (code, docs) | Whether it is in daily production use |
| 5 | SocialPush (`socialpush`) | Partially verified | Logged-in app; status of known issues (X media, Pinterest video, Meta test-users) after 2026-09-21 |
| 6 | YT-Automation (`yt-automation`) | Partially verified | Whether the live SaaS runs the local `web/` code; logged-in app |
| 7 | Agentix CRM (`agentix-crm`) | Verified (code) | None for features; internal tool, no public URL |
| 8 | Eurobrass CRM (`eurobrass-crm`) | Verified | Whether the live login uses Supabase auth or the demo gate |
| 9 | LeadForge (`leadforge`) | Verified (docs, code tree) | In development; phases 4–11 not built |
| 10 | Santure AI CRM (`santure-crm`) | Partially verified | Prototype run-through; also available as a local mirror in the portfolio |
| 11 | Ekatva (`ekatva`) | Partially verified | Whether it is a real client or a concept; prototype run-through |
| 12 | Agentix HIMS (`agentix-hims`) | Partially verified | Staff portals not entered; whether the demo reads a live DB; role count (landing says 29, older docs 24) |
| 13 | Umang Hospital HIMS (`umang-hims`) | Partially verified | Signed-in screens (demo accounts exist; not used) |
| 14 | Umang website + CMS (`umang-website`) | Verified | Admin CMS not entered; whether the notify-lead email/WhatsApp function is active |
| 15 | Woodpecker PMS (`woodpecker-pms`) | Partially verified | Staff app not entered; which integrations (payments, WhatsApp, OTA, accounting) are live vs mock |
| 16 | Kaaya Eco Resort (`kaaya-eco-resort`) | Verified (site + code) | Whether Stripe is in live mode; whether blocked dates have an admin screen; admin not entered |
| 17 | Max Register (`max-register`) | Partially verified | Production CRM (real members) deliberately not entered |
| 18 | Max Fitness website (`max-website`) | Verified | None |
| 19 | Fitness First website (`fitness-first`) | Verified | No git history; Les Mills mention only in page metadata (needs client confirmation); seasonal offers may be outdated |
| 20 | REDUX (`redux`) | Verified (code, demo) | Which integrations are live outside the demo; staff/portal screens not viewed |
| 21 | Your Hair Company (`yhc`) | Partially verified | Whether production runs demo mode or the real backend; `/demo` and `/account` not probed |
| 22 | Skinwise (`skinwise`) | Verified | Admin not accessed; which AI provider is active in production |
| 23 | NRI Trust (`nri-trust`) | Partially verified | Portal appears client-side only; production host; portal screens |
| 24 | AI Agentix corporate site (`ai-agentix-site`) | Verified | None |
| 25 | Dr. Shweta Diwan (`dr-shweta-diwan`) | Partially verified | Admin deliberately not opened (database, roles, billing unverified); no git history |
| 26 | Thames Wellness Spa (`thames-spa`) | Verified | Hosting provider; package prices |
| 27 | Eurobrass corporate site (`eurobrass-site`) | Verified | None |
| 28–47 | 20 concept brands (`aurelle`, `vara`, `drify`, `fruitivo`, `kanak`, `meridian`, `dewlab`, `melt`, `zipev`, `crumb`, `movade`, `cairnline`, `saffron`, `aurelune`, `halden`, `irontemple`, `marigold`, `coralbay`, `tallow-tape`, `vaskaro`) | Verified (live pages + source) | None for documentation. |
| 48 | Deployment & hosting (`delivery-infra`) | Partially verified | Current host of each production site; whether the SocialPush k8s manifests are in use |
| 49 | Showcase pipeline (`showcase-pipeline`) | Verified | None |

**Totals:** 49 projects documented. 36 are Verified (including the 20 concept brands), and 13 are Partially verified, mostly because their logged-in production screens were intentionally not accessed. 0 projects are blocked entirely.

**To complete the partially verified entries**, the owner can provide safe demo logins or screenshots containing only demo data for:
- AGENTiX, SocialFlow, VoiceCRM, SocialPush and the YT-Automation app
- the Woodpecker staff app and the Max Register CRM (with demo members)
- the Umang HIMS / Umang CMS admin, the Kaaya admin, the Dr. Shweta Diwan admin and the NRI Trust portal

They can also confirm which integrations are live in production.

### Safety audit of this document
- No passwords, API keys, tokens, database URLs or `.env` values are included. Integrations are named and described conceptually.
- No real customer, patient, member, guest or employee records are included. All example names are fictional.
- Production systems are labelled. The voice agent must not perform actions on them, and should use the portfolio demo (fictional data, simulated actions) to show functionality.
