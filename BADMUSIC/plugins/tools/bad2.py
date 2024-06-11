from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from BADMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0521d2bf70ea5c1dc31d1.mp4",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🖕𝐌𝐄𝐄𝐓 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 𝐉𝐈🖕", url=f"https://t.me/about_meeBachaa")
                 ]
            ]
        ),
    )
  
