"""Webhook handler for Telegram bot on Netlify."""

import logging
import json
import asyncio
from typing import Any

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update

from config import BOT_TOKEN, ADMIN_IDS
from database import init_db
from handlers import admin, user

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Global instances
_bot: Bot | None = None
_dp: Dispatcher | None = None


async def setup_bot() -> tuple[Bot, Dispatcher]:
    """Initialize bot and dispatcher."""
    global _bot, _dp
    
    if _bot is not None and _dp is not None:
        return _bot, _dp
    
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN missing from environment variables")
    if not ADMIN_IDS:
        raise ValueError("ADMIN_IDS missing from environment variables")
    
    await init_db()
    
    _bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    _dp = Dispatcher()
    
    _dp.include_router(admin.router)
    _dp.include_router(user.router)
    
    logger.info("Bot initialized. Admins: %s", ADMIN_IDS)
    
    return _bot, _dp


async def handle_update(update_data: dict[str, Any]) -> None:
    """Process a single Telegram update."""
    bot, dp = await setup_bot()
    
    try:
        update = Update(**update_data)
        await dp.feed_update(bot, update)
    except Exception as e:
        logger.error("Error processing update: %s", e, exc_info=True)


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Netlify Function handler for webhook updates."""
    try:
        logger.info("Received webhook event")
        
        # Parse the request body
        if isinstance(event.get("body"), str):
            body = json.loads(event["body"])
        else:
            body = event.get("body", {})
        
        logger.info("Update data: %s", body)
        
        # Process the update asynchronously
        asyncio.run(handle_update(body))
        
        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True}),
        }
    
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON: %s", e)
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"}),
        }
    except Exception as e:
        logger.error("Webhook error: %s", e, exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
