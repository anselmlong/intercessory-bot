"""Shared scaffolding for the intercessory bot: token loading and bot construction."""

import logging
import os
from pathlib import Path

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes

logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO)
log = logging.getLogger("intercessory")

ENV_FILE = Path(__file__).parent / ".env"


def load_token() -> str:
    """Read the bot token from the environment, falling back to .env."""
    token = os.environ.get("INTERCESSORY_BOT_TOKEN")
    if token:
        return token
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("INTERCESSORY_BOT_TOKEN="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError("INTERCESSORY_BOT_TOKEN not set and no .env found")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🙏 Intercessory bot. Reply with a prayer request and it'll be logged here once implemented."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start - get started\n/help - show this\n\nSend a message to leave an intercessory request (stub)."
    )


def build_app() -> ApplicationBuilder:
    return ApplicationBuilder().token(load_token())