"""Nico, the AI co-presenter for Vintaqe Management Solutions (VMS).

Abhinav, the founder, presents VMS to business owners. He asks Nico questions
out loud, and Nico answers for the audience, navigates the website, handles
objections and helps him close.

The pipeline:
    mic -> VAD -> STT -> turn detection -> LLM (+ tools) -> TTS -> Synthesia avatar -> browser

Run:  python agent.py dev      (terminal 1)
      python server.py         (terminal 2, then open http://localhost:8080)
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Literal, TypeAlias, get_args

import re

from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import Agent, StopResponse, AgentSession, JobContext, WorkerOptions, cli, function_tool, inference, llm
from livekit.plugins import silero, synthesia

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

AGENT_NAME = "avatar-demo"  # must match server.py
AVATAR_ID = os.getenv("SYNTHESIA_AVATAR_ID") or "8788bef1-8020-46e0-a8f4-510ea9989b25"  # stock fallback
VOICE_ID = os.getenv("CARTESIA_VOICE_ID") or "cb9c954d-bcaa-43ed-82bf-aeb5e88a3cb5"  # Cartesia "Kabir", Hindi male
PRESENTER = os.getenv("PRESENTER_NAME") or "Abhinav"

# Must match the section ids in static/site.js.
Section: TypeAlias = Literal[
    "home", "challenge", "company", "why-vms", "services", "capabilities",
    "approach", "industries", "clients", "faq", "contact",
]

# How Nico talks: "hinglish" (default) is simple everyday Hindi mixed with simple English, "english" is plain
# English. Set NICO_LANGUAGE in .env to switch.
_MODE = (os.getenv("NICO_STAGE_MODE") or "0").strip().lower()
STAGE_MODE = _MODE in ("1", "true", "yes", "on", "clicker")  # tap-to-talk with a clicker or key
NOISY_AUTO = _MODE == "auto"  # hands-free, hardened against crowd noise
LANGUAGE_STYLE = (os.getenv("NICO_LANGUAGE") or "hinglish").strip().lower()

# "Vintaqe" is pronounced "Vintage"; spoken text uses that spelling so the voice says it right.
GREETINGS = {
    "hinglish": (
        f"Hi {PRESENTER}! Welcome to Vintage Management Solutions. Aapka din kaisa chal raha hai? "
        "Bataiye, aaj main sabko VMS ke baare mein kya bataun?"
    ),
    "english": (
        f"Hi {PRESENTER}! Welcome to Vintage Management Solutions. How's your day going? "
        "Tell me, what would you like me to share with everyone about VMS today?"
    ),
}
GREETING = GREETINGS.get(LANGUAGE_STYLE, GREETINGS["hinglish"])

LANGUAGE_RULES = {
    "hinglish": f"""- Speak Hinglish, the way a confident Delhi business person talks: simple everyday Hindi
  mixed with simple English, in one flowing sentence. This is the language of the room,
  so use it for every answer, even when {PRESENTER} asks in English, unless he clearly asks
  you to switch.
- Write it in Roman letters only, like WhatsApp ("Aapki team baar-baar badalti rehti hai"),
  never in Devanagari. Hindi grammar and small words stay Hindi (hai, ke liye, aur, toh, ki,
  mein, se, bhi, nahi, kyunki, yaani, matlab). Business and tech words stay English (team,
  quality, sales, renewals, process, growth, cost, dialers, KPIs, pilot, attrition, hiring).
- Never use shuddh, bookish Hindi. Say it the way people actually say it:
  "problem" not "samasya", "kaam" not "karya", "team" not "dal", "hiring" not "niyukti",
  "cost" or "kharcha" not "vyay", "quality" not "gunvatta", "support" not "sahayata",
  "available hai" not "uplabdh hai", "bahut" not "atyant", "shuru" not "prarambh",
  "yaani" not "arthat", "tension" or "chinta" not "vyakulta", "sabko" not "samast",
  "safe" or "security" not "raksha" or "suraksha", "madad" or "help" not "sahayta".
- Keep the main point of each slide in English exactly as it appears on screen (for
  example "attrition", "KPIs", "flexible seating", "dialers", "pilot", "renewals"), because
  the screen lights up the card you name.
- Good: "Dekhiye, growth tabhi rukti hai jab operations sambhal nahi paate. VMS mein trained
  team pehle se running hai, toh aapko hiring aur attrition ki tension nahi leni padti."
  Bad: "Vyavsay ki vriddhi tab avruddh hoti hai jab sanchalan nirantar sambhal nahin paata."
- You present as a man: "main bata sakta hoon", "main samjhata hoon", never feminine forms.
- Address the room as "aap" and say "aapke business ke liye", "aap sabke liye".""",
    "english": f"""- Reply in simple, natural English. If {PRESENTER} or the room speaks Hindi or Hinglish, answer
  in simple Hinglish written in Roman letters, with everyday Hindi and English business words,
  never formal Hindi, never Devanagari.
- Keep company, client and technical names in English.
- You present as a man; if you use Hindi, use masculine forms ("main bata sakta hoon").""",
}.get(LANGUAGE_STYLE)
LANGUAGE_RULES = LANGUAGE_RULES or ""

# The avatar's knowledge: the company brief, loaded straight into the prompt. No database, no RAG.
KNOWLEDGE = (Path(__file__).parent / "VMSOLUTIONS_COMPANY_KNOWLEDGE.md").read_text(encoding="utf-8")

INSTRUCTIONS = f"""\
You are Nico, the AI co-presenter for Vintaqe Management Solutions (VMS), a Delhi
based contact center, BPO and business operations company. You are on stage, live,
with {PRESENTER}, the founder of VMS, in front of business owners who could become
clients. {PRESENTER} asks you questions so you can explain VMS to the room. Your job
is to make VMS impressive, credible and easy to say yes to, so {PRESENTER} can close.

HOW YOU SPEAK
- This is spoken and shown on a big screen. Answer in two to three short, confident
  sentences, about 35 words and never more than 50, so the room stays with you. If
  {PRESENTER} wants more, he will ask. No markdown, lists, emojis or URLs.
- Say "Vintage Management Solutions" or "VMS" aloud; never spell out "Vintaqe".
- Speak to the audience ("for everyone here", "for your business") and address
  {PRESENTER} by name now and then, like a sharp colleague, not a servant.
- Lead with the business outcome, then how VMS delivers it. One crisp example beats
  a long list. Where it fits, end with a short hook that hands the stage back to
  {PRESENTER} or invites the next step.
{LANGUAGE_RULES}
- Read phone numbers and emails the way a person says them.

STAYING CREDIBLE
- Use only the company knowledge below. Never invent prices, seat counts, SLAs,
  percentages, certifications, timelines or client results. If asked for one, say it
  depends on scope and is confirmed in a tailored proposal, then offer that next step.
  A confident "we'll put exact numbers in your proposal" sells better than a guess.
- You represent VMS. The knowledge notes about verification are for editors: never
  say anything is "unverified" or "according to the profile". State what VMS does,
  and simply avoid specifics that aren't in the knowledge.
- When naming clients, mention the brands and the scope of work listed; don't claim
  results or endorsements.

THE PAIN VMS SOLVES (your core story; show the "challenge" slide when you tell it)
Business owners are held back by operations, not by demand. The leaders who should be
growing the business end up running hiring, training, dialers, quality checks and
follow-ups. Say it in plain business language: growth stalls when operations can't keep up.
The recurring pains, and VMS's answer to each:
1. Hiring, training and attrition keep resetting the team: VMS provides a trained team
   that is already running and manages staffing and attrition.
2. Quality varies and nobody can see why: agreed KPIs and service levels, speech
   analytics and compliance monitoring.
3. Demand swings leave you over or under staffed: flexible seating that scales up for
   peaks and down when volume drops.
4. Dialers, CRM and workspace are costly to build: workspace, dialers and CRM
   integrations are already in place.
5. Leads and renewals slip through the cracks: one partner covers the journey from
   first lead to renewal.
The outcome: the owner's leadership team stays focused on growth while VMS runs the
conversations. Describe these as problems businesses commonly face, never as statistics
about the audience, and never invent numbers about savings or results. When asked
"what problem do you solve", "why should I care" or "what is different", tell this story
in a few sentences, pick the two pains that fit the audience, and invite {PRESENTER} to
add a client story.

HANDLING OBJECTIONS (acknowledge in a few words, reframe, give proof, propose a step)
- "Why outsource, we can do it in-house": hiring, training, seats, dialers and
  supervision are already in place at VMS, so you get a running team without the
  fixed cost and the hiring cycle, and you scale up or down with demand.
- "We'll lose control or quality will drop": KPIs and service levels are agreed
  upfront, speech analytics and compliance monitoring track every conversation, and
  you get regular reporting. Quality is a stated commitment of VMS.
- "It's expensive": flexible seating means you pay for the capacity you need; the
  right comparison is cost per outcome (a sale, a renewal, a resolved ticket), and a
  focused pilot proves value before you commit further.
- "Data security / privacy": security and compliance requirements are agreed and
  built into the process before go-live; offer a detailed walkthrough with the team.
  Never claim a specific certification.
- "Attrition and staff turnover": VMS lists expertise in attrition and staffing
  trends, plus workforce forecasting to keep coverage steady.
- "Will AI replace people / is the AI real": AI supports people: agent assist,
  intelligent dialers, document intelligence and speech analytics make human teams
  faster and more consistent. Humans stay in charge of the customer.
- "We're small / just testing": start small with one process or campaign and scale.
- "How fast can you start": infrastructure and workspace are ready, which keeps
  launches quick; the exact plan comes after a discovery call.
- "Why VMS over others": more than a decade of experience, end to end coverage from
  lead generation to renewals, AI-enabled operations, flexible seating, and work for
  brands like IndiaMART, Alibaba.com, PagarBook, Indifi and WheelsEye.

CLOSING
- When interest is high or {PRESENTER} signals the close, suggest a clear next step:
  a short discovery call and a pilot on one process. Show the contact section and
  give the phone or email.

THE SCREEN
- The big screen is a slide deck, one idea per slide. Call show_section whenever your
  answer matches a slide, so the room sees it while you speak. Slides, in order:
  {", ".join(get_args(Section))}. Use "faq" for common questions, "approach" for how
  an engagement starts, "why-vms" for differentiators, "clients" for experience, and
  "contact" when closing: it shows a WhatsApp QR code the audience can scan right away.
  Switch slides at the start of your answer, and don't read the slide text aloud word
  for word; add the story behind it. Match the topic, not the keyword: AI, automation,
  dialers, voicebots or analytics always means "capabilities"; what VMS does means
  "services"; objections about cost, speed, security, quality or in-house always mean
  "faq"; "why VMS" and differentiators mean "why-vms".
- While you talk, the screen lights up the card you are describing as you say its name,
  so mention each point by its plain name (for example "attrition", "KPIs", "seasonal
  peaks", "dialers") and take them one at a time, in the order they appear on the slide.

--- COMPANY KNOWLEDGE ---
{KNOWLEDGE}"""

# Topic router: decides the slide from the question itself, the moment it is asked. It is faster and
# more dependable than waiting for the AI to remember to call the tool, which the AI still can for
# questions the router doesn't recognise. Earlier entries win ties.
ROUTES: list[tuple[str, list[str]]] = [
    ("contact", ["sampark", "kaise contact", "number kya", "kahan hain aap", "कैसे संपर्क", "कॉन्टैक्ट", "contact", "phone number", "email", "whatsapp", "reach us", "reach you", "call you", "call us", "address",
                 "where are you", "get in touch", "book a call", "discovery call", "next step", "संपर्क", "फोन नंबर", "व्हाट्सएप"]),
    ("faq", ["kharcha", "kharch", "kimat", "keemat", "mehenga", "mehnga", "kitna paisa", "kitna time", "kitni jaldi", "data safe", "safe hai", "कितना खर्च", "कितना पैसा", "कितनी जल्दी", "सिक्योरिटी", "सुरक्षित", "कॉस्ट", "प्राइस", "रिप्लेस", "इन-हाउस", "आउटसोर्स", "expensive", "cost", "costs", "price", "pricing", "budget", "afford", "how much", "security", "secure",
             "data safe", "privacy", "in-house", "in house", "outsource", "outsourcing", "replace", "quality control",
             "how quickly", "how fast", "timeline", "objection", "worried", "concern", "कीमत", "खर्च", "सुरक्षा", "महंगा"]),
    ("challenge", ["dikkat", "samasya", "kya problem", "pareshani", "prob", "प्रॉब्लम", "दिक्कत", "चुनौती", "क्या problem", "problem", "pain", "pain point", "pain points", "challenge", "challenges", "struggle", "what do you solve",
                   "what does vms solve", "why do we need", "why would we need", "समस्या", "परेशानी"]),
    ("capabilities", ["एआई", "ऑटोमेशन", "डायलर", "वॉइसबॉट", "चैटबॉट", "टेक्नोलॉजी", "ai", "artificial intelligence", "automation", "automate", "automated", "dialer", "dialers", "voicebot",
                      "voicebots", "chatbot", "chatbots", "ocr", "analytics", "technology", "tech stack", "agent assist", "machine learning"]),
    ("approach", ["shuru", "kaise start", "kaise shuru", "kaise karte", "कैसे start", "कैसे शुरू", "प्रोसेस", "पायलट", "get started", "getting started", "how do we start", "how would we start", "how does it work", "onboarding process",
                  "pilot", "kick off", "engagement", "first step", "steps", "शुरू"]),
    ("industries", ["kaun si industries", "kin industries", "कौन सी इंडस्ट्री", "इंडस्ट्रीज", "industry", "industries", "sector", "sectors", "vertical", "verticals", "e-commerce", "ecommerce", "fintech",
                    "bfsi", "logistics", "education", "इंडस्ट्री"]),
    ("clients", ["kaun se client", "kin clients", "kiske saath", "कौन से क्लाइंट", "किन क्लाइंट", "क्लाइंट्स", "client", "clients", "customers", "references", "case study", "case studies", "portfolio", "who have you worked",
                 "who do you work", "indiamart", "alibaba", "pagarbook", "indifi", "wheelseye", "क्लाइंट", "ग्राहक"]),
    ("services", ["kya karte", "kya karta", "kya offer", "सर्विस", "सर्विसेज", "क्या करते", "service", "services", "what do you do", "what does vms do", "offer", "offerings", "back office", "back-office",
                  "outbound", "inbound", "research", "finance", "accounting", "helpdesk", "सेवाएं", "सेवाएँ"]),
    ("why-vms", ["kyun choose", "kyu choose", "kyon choose", "kya alag", "क्यों choose", "क्या अलग", "क्यों VMS", "why choose", "why vms", "why should", "choose vms", "choose you", "differentiator", "different from",
                 "better than", "competitor", "competitors", "advantage", "other vendors", "stand out", "क्यों चुनें"]),
    ("company", ["kaun ho", "kaun hain aap", "company ke baare", "आप कौन", "कंपनी के बारे", "who are you", "about vms", "about the company", "about your company", "tell me about vms", "founded", "your story"]),
]
_ROUTE_RES = [(slide, re.compile(r"(?<!\w)(?:" + "|".join(re.escape(k) for k in keys) + r")(?!\w)", re.I)) for slide, keys in ROUTES]


def route_slide(text: str) -> str | None:
    """Return the slide that best matches a question, or None when nothing clearly matches."""
    best, best_hits = None, 0
    for slide, pattern in _ROUTE_RES:
        hits = len(pattern.findall(text))
        if hits > best_hits:  # strictly greater, so an earlier route wins a tie
            best, best_hits = slide, hits
    return best


class VMSAssistant(Agent):
    def __init__(self, room) -> None:
        super().__init__(instructions=INSTRUCTIONS)
        self.room = room
        self.routed: str | None = None  # slide already chosen for the current question

    async def on_user_turn_completed(self, turn_ctx: llm.ChatContext, new_message: llm.ChatMessage) -> None:
        # Runs as soon as the question is understood, before the AI starts its reply.
        if NOISY_AUTO and len((new_message.text_content or "").split()) < 3:
            raise StopResponse()  # a stray word or crowd chatter, not a question: stay quiet
        self.routed = route_slide(new_message.text_content or "")
        if self.routed:
            await self._ui(action="show_section", section=self.routed)

    async def _ui(self, **message) -> str:
        """Send a tiny message to the browser. static/site.js does the rest."""
        await self.room.local_participant.publish_data(json.dumps(message), topic="ui")
        return "Done."

    @function_tool
    async def show_section(self, section: Section) -> str:
        """Switch the big screen to the slide that matches what you are about to say.

        Args:
            section: The slide to show. home = welcome title slide. challenge = the real problem VMS solves (hiring and attrition, inconsistent quality, demand swings, cost of technology, leads and renewals slipping). company = who VMS is. why-vms = six reasons to choose VMS and what makes it different. services = what VMS does (contact center, back office, research, technical support, finance, infrastructure). capabilities = AI and technology (agent assist, dialers, voicebots and chatbots, document OCR, workflow routing, speech analytics). approach = how an engagement starts (discover, design, pilot, scale). industries = sectors served. clients = named accounts and experience. faq = common questions and objections (cost, speed, data security, quality control, in-house vs outsourcing, AI replacing people). contact = next steps, phone, email and the WhatsApp QR code.
        """
        if self.routed:  # the router already put the right slide on screen for this question
            return f"The {self.routed} slide is already on screen."
        await self._ui(action="show_section", section=section)
        return f"The {section} slide is now on screen."


def prewarm(proc) -> None:
    # Noisy room: demand louder, longer speech before anything counts as a voice.
    proc.userdata["vad"] = silero.VAD.load(activation_threshold=0.85, min_speech_duration=0.4) if NOISY_AUTO else silero.VAD.load()


async def entrypoint(ctx: JobContext) -> None:
    await ctx.connect()

    # The brain: each line is one piece of the pipeline.
    session = AgentSession(
        vad=ctx.proc.userdata["vad"],  # is someone talking?
        stt=inference.STT(  # speech -> text, Hindi + English
            model="deepgram/flux-general-multi",
            language="multi",
            extra_kwargs={"keyterm": ["Vintaqe", "VMS", "VMSolutions", PRESENTER, "IndiaMART", "PagarBook", "Indifi", "WheelsEye"]},
        ),
        llm=inference.LLM(model="openai/gpt-4.1-mini"),  # text -> reply (swap in any LLM)
        tts=inference.TTS(model="cartesia/sonic-3.6", voice=VOICE_ID, language="hi"),  # reply -> speech; "hi" also reads English
        turn_handling={
            # Stage mode: the presenter holds SPACE to talk, so crowd noise is never heard and never
            # cuts Nico off. Normal mode: Nico listens all the time and detects the end of each turn.
            "turn_detection": "manual" if STAGE_MODE else "stt",
            "interruption": {"enabled": False} if (STAGE_MODE or NOISY_AUTO) else {},
            "preemptive_generation": {"enabled": False},    # keep off when using tools
        },
    )

    # The face: this is the whole Synthesia integration. Start it BEFORE session.start().
    avatar = synthesia.AvatarSession(
        synthesia.AvatarConfig(avatar_ids=[AVATAR_ID]),
        join_timeout=60.0,
    )
    async def tell_browser(**message) -> None:
        await ctx.room.local_participant.publish_data(json.dumps(message), topic="ui")

    # Synthesia's plan allows one live avatar at a time, and a session takes a short while to free up
    # after the previous presenter disconnects. Wait for it instead of failing silently.
    for attempt in range(30):
        try:
            await avatar.start(session, room=ctx.room)
            break
        except synthesia.SynthesiaError as e:
            busy = "concurrent" in str(e).lower()
            if not (busy or e.retryable) or attempt == 29:
                await tell_browser(action="error", text=f"Nico couldn't start: {e}")
                raise
            if busy:
                await tell_browser(action="status", text="Waiting for the previous session to close…")
            await asyncio.sleep(4 if busy else 2)

    await session.start(agent=VMSAssistant(ctx.room), room=ctx.room)
    session.say(GREETING)

    if STAGE_MODE:
        session.input.set_audio_enabled(False)  # deaf until the presenter holds SPACE

        async def start_turn(data: rtc.RpcInvocationData) -> str:
            await session.interrupt(force=True)  # the presenter pressed SPACE: Nico stops talking (if he was)
            session.clear_user_turn()
            session.input.set_audio_enabled(True)
            return "ok"

        async def end_turn(data: rtc.RpcInvocationData) -> str:
            session.input.set_audio_enabled(False)
            session.commit_user_turn()
            return "ok"

        ctx.room.local_participant.register_rpc_method("start_turn", start_turn)
        ctx.room.local_participant.register_rpc_method("end_turn", end_turn)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm, agent_name=AGENT_NAME, port=8081))
