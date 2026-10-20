"""Serves the web page and hands the browser a token to join a LiveKit room.

Run: python server.py, then open http://localhost:8080
"""

import json
import logging
import os
import time
import uuid
from datetime import timedelta
from pathlib import Path

from aiohttp import web
from dotenv import load_dotenv
from livekit import api

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

AGENT_NAME = "avatar-demo"  # must match agent.py
STAGE_MODE = (os.getenv("NICO_STAGE_MODE") or "0").strip().lower() in ("1", "true", "yes", "on", "clicker")  # tap-to-talk for noisy rooms

log = logging.getLogger("vms.accounts")
ROOT = Path(__file__).parent
ACCOUNTS_FILE = Path(os.getenv("ACCOUNTS_FILE", ROOT / "accounts.json"))
STATE_FILE = Path(os.getenv("STATE_FILE", ROOT / "data" / "state.json"))
ADMIN_KEY = os.getenv("ADMIN_KEY", "")
SHORT_BLOCK = 10 * 60       # a failed connect: skip this account for 10 minutes, then try it again
QUOTA_BLOCK = 6 * 60 * 60   # explicit quota / 4xx error: skip it for 6 hours


def load_accounts() -> list[dict]:
    """accounts.json = [{"name", "url", "key", "secret", "limit"}], tried in order.
    Without the file, the single LIVEKIT_* account from .env is used (no limit)."""
    if ACCOUNTS_FILE.exists():
        return json.loads(ACCOUNTS_FILE.read_text(encoding="utf-8"))
    return [{"name": "main", "url": os.environ["LIVEKIT_URL"], "key": os.environ["LIVEKIT_API_KEY"],
             "secret": os.environ["LIVEKIT_API_SECRET"], "limit": None}]


ACCOUNTS = load_accounts()


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_state() -> None:
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(STATE), encoding="utf-8")
    except OSError:
        log.exception("could not save account state")


STATE: dict = load_state()


def usage(name: str) -> dict:
    return STATE.setdefault(name, {"used": 0, "blocked_until": 0})


def pick(skip: set[str]) -> dict | None:
    """First account that is not skipped, not blocked, and still has sessions left."""
    now = time.time()
    for acc in ACCOUNTS:
        st = usage(acc["name"])
        if acc["name"] in skip or st["blocked_until"] > now:
            continue
        if acc.get("limit") is not None and st["used"] >= acc["limit"]:
            continue
        return acc
    return None


async def token(request: web.Request) -> web.Response:
    # Demo only: no auth. Put this behind your app's login in anything real.
    skip = {n for n in request.query.get("skip", "").split(",") if n}
    acc = pick(skip)
    if acc is None:
        return web.json_response({"error": "Irfan is at capacity right now. Please try again in a few minutes."}, status=503)
    usage(acc["name"])["used"] += 1
    save_state()
    room = f"avatar-demo-{uuid.uuid4().hex[:8]}"  # fresh room per visit
    jwt = (
        api.AccessToken(acc["key"], acc["secret"])
        .with_identity(f"user-{uuid.uuid4().hex[:8]}")
        .with_ttl(timedelta(minutes=15))
        .with_grants(api.VideoGrants(room_join=True, room=room))
        .with_room_config(
            api.RoomConfiguration(
                sync_streams=True,  # keeps the avatar's lips in sync with its audio
                agents=[api.RoomAgentDispatch(agent_name=AGENT_NAME)],  # sends our agent in
            )
        )
        .to_jwt()
    )
    return web.json_response({"url": acc["url"], "token": jwt, "stage": STAGE_MODE, "account": acc["name"]})


async def report(request: web.Request) -> web.Response:
    """The browser says an account failed (connect error, agent never joined, 4xx). Park it and move on."""
    body = await request.json()
    name, reason = str(body.get("account", "")), str(body.get("reason", ""))[:200]
    if name in {a["name"] for a in ACCOUNTS}:
        quota = any(w in reason.lower() for w in ("400", "402", "403", "429", "quota", "limit", "exhaust", "credit"))
        usage(name)["blocked_until"] = time.time() + (QUOTA_BLOCK if quota else SHORT_BLOCK)
        save_state()
        log.warning("account %s blocked (%s): %s", name, "quota" if quota else "temporary", reason)
    return web.json_response({"ok": True})


async def admin(request: web.Request) -> web.Response:
    """GET /admin?key=...            -> usage of every account
    GET /admin?key=...&reset=name   -> clear that account's counter and block"""
    if not ADMIN_KEY or request.query.get("key") != ADMIN_KEY:
        raise web.HTTPNotFound()
    reset = request.query.get("reset")
    if reset in {a["name"] for a in ACCOUNTS}:
        STATE[reset] = {"used": 0, "blocked_until": 0}
        save_state()
    now = time.time()
    return web.json_response([
        {"name": a["name"], "limit": a.get("limit"), "used": usage(a["name"])["used"],
         "blocked_for_s": max(0, int(usage(a["name"])["blocked_until"] - now))}
        for a in ACCOUNTS
    ])


async def index(request: web.Request) -> web.FileResponse:
    return web.FileResponse(
        Path(__file__).parent / "index.html", headers={"Cache-Control": "no-store"}
    )


app = web.Application()
app.router.add_get("/", index)
app.router.add_get("/token", token)
app.router.add_post("/report", report)
app.router.add_get("/admin", admin)
app.router.add_static("/static", Path(__file__).parent / "static")  # site.css + site.js

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8080")))
