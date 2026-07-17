# VeyraSupport Bot

Telegram support bot — users write to the bot, you reply as support agent.

## How it works

```
User  →  Bot  →  You (admin)
User  ←  Bot  ←  You (admin)
```

1. User sends a message to the bot
2. You receive a notification with **Open chat** button
3. Tap **💬 Chats** to see all conversations
4. Open a chat → reply directly — bot forwards your text
5. **← Back** returns to chat list
6. **🗑 Delete** removes chat from your list (user can write again)

## Setup

### 1. Create a bot

1. Open [@BotFather](https://t.me/BotFather) in Telegram
2. Send `/newbot`, follow prompts, copy the **token**

### 2. Get your Telegram ID

1. Open [@userinfobot](https://t.me/userinfobot)
2. Copy your numeric **Id**

### 3. Configure

```bash
cd E:\Projects\Saas_with_cursor\telegram_support_bot
copy .env.example .env
```

Edit `.env`:

```
BOT_TOKEN=123456:ABC-DEF...
ADMIN_IDS=987654321
```

### 4. Install & run

```bash
pip install -r requirements.txt
python bot.py
```

## Admin commands

| Action | How |
|--------|-----|
| Open panel | `/start` |
| Chat list | Tap **💬 Chats** |
| Reply to user | Open chat, type message |
| Exit chat | **← Back to chats** |
| Delete chat | **🗑 Delete chat** |

## Stack

- Python 3.10+
- [aiogram](https://docs.aiogram.dev/) 3.x
- SQLite (messages stored locally)
