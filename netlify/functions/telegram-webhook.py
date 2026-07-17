"""Netlify Function for Telegram webhook."""

import json
import logging
import sys
import os

# Add parent directory to path to import bot modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from webhook import handler as webhook_handler


def handler(event, context):
    """Main Netlify Function entry point."""
    return webhook_handler(event, context)
