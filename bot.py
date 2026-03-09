from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

queue = {}

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("Music bot is running")

@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("give song name")

    query = message.text.split(None,1)[1]

    ydl_opts = {"format":"bestaudio"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        url = info["url"]

    await call.join_group_call(
        message.chat.id,
        AudioPiped(url)
    )

    await message.reply(f"playing {info['title']}")

app.start()
call.start()
app.idle()
