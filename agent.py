"""Irfan, the AI co-presenter for AI Agentix.

Anant presents AI Agentix to business owners. He asks Irfan questions
out loud, and Irfan answers for the audience, navigates the website, handles
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

# Several LiveKit accounts: AGENT_ACCOUNT=<name> makes this process register with that account from
# accounts.json (the same file server.py reads). Run one agent process per account.
if os.getenv("AGENT_ACCOUNT"):
    _acc = next(a for a in json.loads((Path(__file__).parent / "accounts.json").read_text(encoding="utf-8"))
                if a["name"] == os.environ["AGENT_ACCOUNT"])
    os.environ.update(LIVEKIT_URL=_acc["url"], LIVEKIT_API_KEY=_acc["key"], LIVEKIT_API_SECRET=_acc["secret"])

AGENT_NAME = "avatar-demo"  # must match server.py
AVATAR_ID = os.getenv("SYNTHESIA_AVATAR_ID") or "8788bef1-8020-46e0-a8f4-510ea9989b25"  # stock fallback
VOICE_ID = os.getenv("CARTESIA_VOICE_ID") or "cb9c954d-bcaa-43ed-82bf-aeb5e88a3cb5"  # Cartesia "Kabir", Hindi male
PRESENTER = os.getenv("PRESENTER_NAME") or "Anant"

# Must match the section ids in static/site.js.
Section: TypeAlias = Literal[
    "home", "challenge", "company", "why-vms", "services", "capabilities",
    "approach", "industries", "clients", "faq", "contact",
]

# How Irfan talks: "hinglish" (default) is simple everyday Hindi mixed with simple English, "english" is plain
# English. Set NICO_LANGUAGE in .env to switch.
_MODE = (os.getenv("NICO_STAGE_MODE") or "0").strip().lower()
STAGE_MODE = _MODE in ("1", "true", "yes", "on", "clicker")  # tap-to-talk with a clicker or key
NOISY_AUTO = _MODE == "auto"  # hands-free, hardened against crowd noise
LANGUAGE_STYLE = (os.getenv("NICO_LANGUAGE") or "hinglish").strip().lower()

GREETINGS = {
    "hinglish": (
        f"Hi {PRESENTER}! Welcome to AI Agentix. Aapka din kaisa chal raha hai? "
        "Bataiye, aaj main sabko AI Agentix ke baare mein kya bataun?"
    ),
    "english": (
        f"Hi {PRESENTER}! Welcome to AI Agentix. How's your day going? "
        "Tell me, what would you like me to share with everyone about AI Agentix today?"
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
- Good: "Dekhiye, growth tabhi rukti hai jab operations sambhal nahi paate. AI Agentix ka agent
  aapke customers ko 24 ghante reply deta hai, toh leads slow reply ki wajah se nahi khote."
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
KNOWLEDGE = (Path(__file__).parent / "AGENTIX_COMPANY_KNOWLEDGE.md").read_text(encoding="utf-8")

INSTRUCTIONS = f"""You are Irfan, the AI co-presenter for AI Agentix, a New Delhi AI automation company
that builds AI agents for sales, marketing, support, HR, finance and operations
("AI Applied, Growth Multiplied"). You are on stage, live, with {PRESENTER}, in front
of business owners who could become clients. {PRESENTER} asks you questions so you can
explain what AI Agentix offers, and the products it has built, to the room. Your job is to make AI Agentix
impressive, credible and easy to say yes to, so {PRESENTER} can close.

HOW YOU SPEAK
- This is spoken and shown on a big screen. Answer in two to three short, confident
  sentences, about 35 words and never more than 50, so the room stays with you. If
  {PRESENTER} wants more, he will ask. No markdown, lists, emojis or URLs.
- Say "AI Agentix" aloud. Say product names naturally (AGENTiX, SocialFlow, VoiceCRM).
- Speak to the audience ("for everyone here", "for your business") and address
  {PRESENTER} by name now and then, like a sharp colleague, not a servant.
- Lead with the business outcome, then which AI Agentix product or project delivers
  it. One crisp example beats a long list. Where it fits, end with a short hook that
  hands the stage back to {PRESENTER} or invites the next step.
{LANGUAGE_RULES}
- Read phone numbers, emails and prices the way a person says them.

STAYING CREDIBLE
- Use only the knowledge below. Never invent prices, client counts, results, timelines
  or features. Quote a price only where the knowledge gives it, as "listed on the
  pricing page". If asked for anything else, say it depends on scope and is confirmed
  after a discovery call, then offer that next step.
- Respect the verification labels in the knowledge. Never present a "Planned / in
  progress", prototype, concept or "In development" item as a live product: say it is
  a prototype, a concept, or in development. The 20 concept brand sites are fictional
  showcase work, not real shops.
- The knowledge notes about verification are for editors: never say "unverified" or
  "according to the document". State what AI Agentix has built and simply avoid
  specifics that aren't in the knowledge.
- Never talk about business numbers: how many clients or projects AI Agentix has, money
  or revenue made for clients, ROI, percentages, growth or satisfaction figures,
  testimonials or case-study results. Describe only what AI Agentix does and what it has
  built. If asked for numbers, redirect to what we build and offer the free audit. They are marketing claims. Never name
  the testimonial or case-study businesses. Never promise revenue growth, speed-ups or
  guaranteed results.
- Client projects marked Production are real businesses. Never offer to log in, submit
  forms or take actions on them. To show a product, point to the safe portfolio demo.
- Never share credentials, keys or any personal data. Example names are fictional.
- When unsure, say so and offer the demo or a call with the AI Agentix team.

RECOMMENDING THE RIGHT PRODUCT
Listen for the visitor's need, then name the best-fit project from the knowledge's
"Which project to mention for a requirement" table, say in one sentence why, and offer
to show it. Compare two products only when asked. Typical fits: WhatsApp and Instagram
AI replies with a CRM is AGENTiX; Instagram comment automation is SocialFlow; hospital
software is Agentix HIMS or Umang HIMS; hotels is Woodpecker PMS; gyms is Max Register.

HANDLING OBJECTIONS (acknowledge in a few words, reframe, give proof, propose a step)
- "Is it real or just a demo": say plainly whether the project is Live, a prototype or
  a concept, and offer the safe demo for anything live.
- "How much does it cost": quote only listed prices (the three AI Content Studio
  packages, and the AGENTiX and SocialFlow product plans); anything else is a tailored
  quote after a free audit or discovery call.
- "Is my data safe": each workspace is isolated and credentials are encrypted and kept
  server side. Never claim a certification; the AGENTiX security page says it has no
  SOC 2 or ISO 27001 yet.
- "Will AI replace my team": AI handles the repetitive replies and sorting, and a human
  can pause the bot and take over any conversation.

CLOSING
- When interest is high or {PRESENTER} signals the close, suggest a clear next step:
  a short discovery call, or opening the portfolio demo of the product they liked.

THE SCREEN
- The big screen is a slide deck, one idea per slide. Call show_section whenever your
  answer matches a slide, so the room sees it while you speak. Slides, in order:
  {", ".join(get_args(Section))}. Switch slides at the start of your answer, and don't
  read the slide text aloud word for word; add the story behind it.
- While you talk, the screen lights up the card you are describing as you say its name,
  so mention each point by its plain name and take them one at a time, in the order
  they appear on the slide.

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


class AgentixAssistant(Agent):
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
            extra_kwargs={"keyterm": ["Irfan", "AI Agentix", "AGENTiX", "SocialFlow", "VoiceCRM", "SocialPush", "LeadForge", "Woodpecker", "Redux", "Skinwise", PRESENTER]},
        ),
        llm=inference.LLM(model="openai/gpt-4.1-mini"),  # text -> reply (swap in any LLM)
        tts=inference.TTS(model="cartesia/sonic-3.6", voice=VOICE_ID, language="hi"),  # reply -> speech; "hi" also reads English
        turn_handling={
            # Stage mode: the presenter holds SPACE to talk, so crowd noise is never heard and never
            # cuts Irfan off. Normal mode: Irfan listens all the time and detects the end of each turn.
            "turn_detection": "manual" if STAGE_MODE else "stt",
            "interruption": {"enabled": False} if (STAGE_MODE or NOISY_AUTO) else {},
            "preemptive_generation": {"enabled": False},    # keep off when using tools
        },
    )

    # If the account runs out of credit mid-session (a 4xx from LiveKit), tell the page so it can move to the next account.
    @session.on("error")
    def _on_error(ev) -> None:
        err = str(getattr(ev, "error", ev))
        fatal = getattr(getattr(ev, "error", None), "recoverable", True) is False  # a TTS/STT/LLM that gave up
        if fatal or re.search(r"(400|402|403|429)|quota|exhaust|limit", err, re.I):
            asyncio.ensure_future(ctx.room.local_participant.publish_data(
                json.dumps({"action": "failover", "text": err[:200]}), topic="ui"))

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
                await tell_browser(action="error", text=f"Irfan couldn't start: {e}")
                raise
            if busy:
                await tell_browser(action="status", text="Waiting for the previous session to close…")
            await asyncio.sleep(4 if busy else 2)

    await session.start(agent=AgentixAssistant(ctx.room), room=ctx.room)
    session.say(GREETING)

    if STAGE_MODE:
        session.input.set_audio_enabled(False)  # deaf until the presenter holds SPACE

        async def start_turn(data: rtc.RpcInvocationData) -> str:
            await session.interrupt(force=True)  # the presenter pressed SPACE: Irfan stops talking (if he was)
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
