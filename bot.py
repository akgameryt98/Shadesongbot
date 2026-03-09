from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("✅ Music bot is running")


@app.on_message(filters.command("ping"))
async def ping(_, message):
    await message.reply("🏓 Bot working")


app.run()
