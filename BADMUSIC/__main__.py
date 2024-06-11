import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BADMUSIC import LOGGER, app, userbot
from BADMUSIC.core.call import BAD
from BADMUSIC.misc import sudo
from BADMUSIC.plugins import ALL_MODULES
from BADMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝗔𝗕𝗘 𝗟𝗢𝗗𝗘 𝗦𝗧𝗥𝗜𝗡𝗚 𝗧𝗘𝗥𝗔 𝗕𝗔𝗣 𝗗𝗔𝗟𝗘 𝗚𝗔 𝗞𝗬𝗔 😑")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BADMUSIC.plugins" + all_module)
    LOGGER("BADMUSIC.plugins").info("𝗔𝗕𝗘 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘 𝗕𝗔𝗖𝗛𝗘 𝗥𝗘𝗣𝗢 𝗘𝗗𝗜𝗧 𝗞𝗔𝗥 𝗟𝗜𝗔  👿 ...")
    await userbot.start()
    await BAD.start()
    await BAD.decorators()
    LOGGER("BADMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐙𝐈𝐃𝐃𝐈 𝐌𝐔𝐊𝐇𝐈𝐘𝐀♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BADMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐙𝐈𝐃𝐃𝐈 𝐌𝐔𝐊𝐇𝐈𝐘𝐀♨️\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
