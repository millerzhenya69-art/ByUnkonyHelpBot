"""Bot configuration from environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_IDS: set[int] = {
    int(x.strip())
    for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip().isdigit()
}

# Database path - use default only if not specified in environment
DB_PATH = os.getenv("DB_PATH") or "support_bot.db"
MESSAGES_PER_PAGE = 8
HISTORY_LIMIT = 15

# Webhook configuration for Netlify deployment
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")
