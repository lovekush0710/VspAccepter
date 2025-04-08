from pyrogram import filters
from Request import Mukesh
from pyrogram.types import BotCommand
from config import START_IMG
@Mukesh.on_message(filters.command("start"))
async def start_bot(b,m):
    
    await m.reply_photo(photo=START_IMG,caption=f"bot started  as @{Mukesh.username}")
    await Mukesh.set_bot_commands([
    BotCommand("start", "Start the bot")])