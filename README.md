# Vintaqe Management Solutions: a company website with a voice assistant

A presentation site for AI Agentix, with a Synthesia avatar (Irfan) that answers questions about AI Agentix's products and projects. The agent's knowledge is [AGENTIX_COMPANY_KNOWLEDGE.md](./AGENTIX_COMPANY_KNOWLEDGE.md) (built from the ai-agentix.com website plus a project summary; full project detail is in AGENTIX_PROJECTS_DETAIL.md). The slide deck (HTML) is still the old one and will be replaced.

```
mic → VAD → STT → turn detection → LLM (+ navigation tool) → TTS → Synthesia avatar → browser
```

## Setup
1. Create a free LiveKit Cloud project at https://cloud.livekit.io and create an API key (Settings → API Keys).
2. Get a Synthesia API key with Interactive Avatars enabled: https://www.synthesia.io/features/avatars/interactive-avatars
3. Copy `.env.example` to `.env` and fill in your own values. `SYNTHESIA_AVATAR_ID` is optional; it defaults to a stock avatar.

```bash
cp .env.example .env    # then fill it in

python agent.py dev     # terminal 1
python server.py        # terminal 2 → open http://localhost:8080
```
Click **Start** and allow the mic. The first join can take a while on a cold start. Don't use `python agent.py console`, because the avatar never appears in console mode.

Try: *"What does VMS do?"* · *"Tell me about your AI capabilities."* · *"What industries do you serve?"* · *"How do I contact you?"*

## Files
| File | What it is |
|---|---|
| `agent.py` | The AI: behaviour prompt, page-navigation tool and voice pipeline |
| `index.html` | The company page shell plus the avatar widget |
| `server.py` | Serves the page and creates a room token that sends the agent in |
| `static/site.js` | Company page content, rendering and the `SITE` navigation API |
| `static/site.css` | Responsive company-site and avatar styling |
| `AGENTIX_COMPANY_KNOWLEDGE.md` | Company facts and source notes; `agent.py` loads it into the assistant's prompt, so edit facts here |

The company site and avatar remain separate. `static/site.js` knows nothing about LiveKit or Synthesia; it exposes the `SITE` method used by the agent. `index.html` forwards tool calls into it:

```js
const { action, ...args } = JSON.parse(new TextDecoder().decode(payload));
SITE[action]?.(args);
```

The page content works without the agent running; the voice feature requires the LiveKit and Synthesia configuration above.

## Presenting
Irfan is a co-presenter for the founder. Click **Start presentation**, and Irfan greets the presenter by name (`PRESENTER_NAME` in `.env`, default "Abhinav") and asks what to share. The presenter then asks questions out loud; Irfan answers for the audience, handles objections, scrolls the page to the matching section, and steers towards a discovery call. Live captions appear under the avatar. Keep `agent.py`'s objection guidance and `AGENTIX_COMPANY_KNOWLEDGE.md` up to date; Irfan won't quote prices, SLAs or results that aren't in them.

## The deck
The site is a full-screen keynote deck of eleven scenes (the second one, "The real problem", pairs each pain business owners feel with how VMS removes it) (`static/site.js`), styled in `static/site.css` with a glass look and the brand colour from the logo (`--petrol`). Arrow keys, the dots on the left, or Irfan's `show_section` tool move between scenes. All sizes are in `rem`, so it scales to any projector.

- **Footage:** ten looping background clips in `static/media/` (about 55 MB) come from [Mixkit](https://mixkit.co/free-stock-video/), downloaded locally so the pitch doesn't depend on venue Wi-Fi. Check the [Mixkit license](https://mixkit.co/license/#videoFree) before using them commercially, or swap in your own footage by replacing the files (keep the names, or change `video` in `SCENES`).
- **Fonts:** Inter and Fraunces are served from `static/fonts/`, so text never jumps while fonts load and nothing depends on Google.
- **Logo:** `static/logo.png` (dark) and `static/logo-light.png` (white) are cleaned-up versions of the supplied logo.
- **QR code:** `static/qr-whatsapp.svg` opens a WhatsApp chat with +91 7011 81 2696.

### How the screen follows Irfan
- **Slide choice:** `route_slide()` in `agent.py` reads each question and switches the slide about a second later, before Irfan speaks. The AI's `show_section` tool is the backup for unusual questions. To teach it new topics, add keywords to `ROUTES`.
- **Spotlight:** as Irfan speaks, `SPOT_KEYS` in `static/site.js` lights up the card he's naming and dims the rest. Add keywords there when you add or reword a card.
- **Layout:** while presenting, Irfan has a column of his own and the slides end where it begins, at any window width from about 720 px up. Press F11 for full screen and Ctrl+0 to reset browser zoom before you start.

## Language, voice and avatar
- **Hinglish by default:** Irfan speaks simple everyday Hindi mixed with simple English, written in Roman letters ("Aapki team baar-baar badalti rehti hai"), never formal Hindi. Speech is transcribed with `deepgram/flux-general-multi`, so Abhinav can ask in Hindi, English or Hinglish. Set `NICO_LANGUAGE=english` in `.env` for plain English. The wording rules, including the list of formal words to avoid, are in `LANGUAGE_RULES` in `agent.py`.
- **Voice:** defaults to Cartesia "Kabir", a male Hindi voice that also reads English. Set `CARTESIA_VOICE_ID` in `.env` to use a different one from https://play.cartesia.ai/voices.
- **Avatar:** in Synthesia, open **Avatars**, choose an avatar, then **••• → Copy Interactive ID** and put the result in `SYNTHESIA_AVATAR_ID`. Stock actor avatars and avatars outside your plan aren't accepted (`UNKNOWN_AVATAR`). Restart `agent.py` after changing `.env`.

## Adding a tool
1. Add a `@function_tool` to `agent.py` that calls `self._ui(action="your_tool", ...)`.
2. Add a matching `your_tool({ ... })` method to `SITE` in `static/site.js`.
3. Mention it in `INSTRUCTIONS` so the model knows when to use it.

New page sections also need adding to the `Section` type in `agent.py`, so the assistant can navigate to them.

## If it breaks
| Error | Fix |
|---|---|
| `SynthesiaError` `AUTH` / `FEATURE_NOT_IN_PLAN` | Bad key, or your workspace doesn't have Interactive Avatars enabled |
| `LIVEKIT_CREDENTIALS_REJECTED` | The LiveKit URL, key and secret aren't all from the same project |
| `UNKNOWN_AVATAR` | That `SYNTHESIA_AVATAR_ID` isn't in your workspace |
| Avatar never appears | You used console mode, or `AGENT_NAME` doesn't match in `agent.py` and `server.py` |
| Page loads unstyled | `static/` isn't next to `server.py` |
| The assistant never hears you | Watch the dot next to the status text. Green while you talk means LiveKit is getting your mic, so the problem is downstream in the agent: check its terminal for STT errors. Never green means the browser is capturing the wrong input; pick the right mic in Chrome's site settings (the camera icon in the address bar) and reload. |

Built on Synthesia's official quickstarts: https://github.com/synthesia-ai/interactive-avatar-quickstarts
