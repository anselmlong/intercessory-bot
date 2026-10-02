"""Intercessory bot entrypoint. Polling, systemd-managed."""

import logging

from skeleton import build_app, help_command, log, start
from telegram.ext import CommandHandler, MessageHandler, filters

log = logging.getLogger("intercessory")


async def echo(update, context):
    await update.message.reply_text("📿 Noted (stub). A real handler goes here.")


def main() -> None:
    app = build_app().build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT, echo))
    log.info("intercessory bot starting")
    app.run_polling()


if __name__ == "__main__":
    main()