import asyncio
import importlib
import threading
import time
import requests

from pyrogram import idle
from flask import Flask

import config
from SONALI import LOGGER, app, userbot
from SONALI.core.call import RAUSHAN
from SONALI.misc import sudo
from SONALI.plugins import ALL_MODULES
from SONALI.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Music Bot is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

def keep_alive():
    while True:
        try:
            requests.get("https://sonali-music-d3ki.onrender.com")
            LOGGER.info("Pinged host URL successfully ✅")
        except Exception as e:
            LOGGER.error(f"Ping error : {e}")
        time.sleep(300) 

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

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
        importlib.import_module("SONALI.plugins" + all_module)
    LOGGER("SONALI.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("SONALI").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗟𝗣𝗛𝗔♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SONALI").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗟𝗣𝗛𝗔♨️\n╚═════ஜ۩۞۩ஜ════╝")


if __name__ == "__main__":
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.daemon = True
    keep_alive_thread.start()

    
    asyncio.get_event_loop().run_until_complete(init())
