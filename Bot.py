
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

PRODUCTS = {
    "jiohotstar": {
        "name": "JioHotstar",
        "description": "Browse available subscription options.",
    },
    "netflix": {
        "name": "Netflix",
        "description": "Browse available subscription options.",
    },
    "prime": {
        "name": "Amazon Prime Video",
        "description": "Browse available subscription options.",
    },
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to OTT Premium Store!\n\n"
        "Use /apps to browse streaming services.\n"
        "Use /help to see available commands.\n\n"
        "Orders and payments are not enabled yet."
    )


async def apps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Available streaming services:\n\n"
    for product in PRODUCTS.values():
        message += f"• {product['name']}\n"
    message += "\nUse /help for commands."
    await update.message.reply_text(message)


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "/start - Open the store\n"
        "/apps - Browse streaming services\n"
        "/help - Show commands\n"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("apps", apps))
    app.add_handler(CommandHandler("help", help_command))

    logging.info("OTT Premium Store bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()
               
