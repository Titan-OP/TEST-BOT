#Credits to @Pika_Pika_Pikachuuu
#Credits to @TeamGladiators
#Credits to Yukki for curses


import re
import asyncio
import random
import os
from typing import Optional
from telethon import events
from telegram import Update, Bot
from spambot.modules.helper_funcs.alternate import typing_action

from spambot import (
    DEV_USERS,
    OWNER_ID,
    SUDO_USERS,
    dispatcher,
)
from spambot.modules.helper_funcs.chat_status import (
    sudo_plus,
)
from spambot.modules.helper_funcs.extraction import extract_user
from spambot.modules.helper_funcs.filters import CustomFilters
from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler, run_async, MessageHandler
from telegram.utils.helpers import mention_html
from spambot.events import gladiator
from spambot import telethn as tbot

def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That's not a user stupid!!"

    elif user_id == bot.id:
        reply = "Why should I abuse an innocent bot -_-!!"

    else:
        reply = None
    return reply


replies = [
    "𝐓𝐔𝐌𝐇𝐀𝐑𝐈 𝐀𝐀𝐌𝐀 𝐁𝐀𝐇𝐔𝐓 𝐊𝐀𝐌𝐉𝐎𝐑 𝐇𝐀𝐈 𝐄𝐊 𝐁𝐀𝐀𝐑 𝐃𝐈𝐀 𝐔𝐒𝐊𝐎 𝐓𝐎𝐇 𝐀𝐀𝐇𝐇𝐇🥴 𝐊𝐀𝐑 𝐃𝐈𝐈🥵🥵",
    "𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐙𝐀𝐈𝐃🥵🥵",
    "𝐀𝐔𝐊𝐀𝐓 𝐌 𝐑𝐀𝐇 𝐁𝐒𝐃𝐊 🔥",
    "𝐌𝐀𝐀𝐀𝐀𝐑 𝐊𝐈 𝐉𝐇𝐀𝐀𝐀𝐀𝐓 𝐊𝐄 𝐁𝐁𝐁𝐁𝐁𝐀𝐀𝐀𝐀𝐀𝐋𝐋𝐋𝐋𝐋",
    "𝐓𝐞𝐫𝐢 𝐚𝐦𝐦𝐚 𝐃𝐚𝐢𝐥𝐲 𝐙𝐚𝐢𝐝 𝐊 𝐬𝐚𝐦𝐧𝐞 𝐚𝐚𝐡 𝐚𝐚𝐡 𝐤𝐚𝐫𝐭𝐢 𝐡",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓..",
    "𝐋𝐖𝐃𝐄 𝐊𝐄 𝐁𝐀𝐀𝐀𝐋𝐋𝐋.",
    "𝐌𝐀𝐂𝐇𝐀𝐑 𝐊𝐈 𝐉𝐇𝐀𝐀𝐓 𝐊𝐄 𝐁𝐀𝐀𝐀𝐋𝐋𝐋𝐋",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌 𝐃𝐔 𝐓𝐀𝐏𝐀 𝐓𝐀𝐏?",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀𝐀",
    "𝐓𝐄𝐑𝐈 𝐁𝐇𝐍 𝐒𝐁𝐒𝐁𝐄 𝐁𝐃𝐈 𝐑𝐀𝐍𝐃𝐈.",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐎𝐒𝐒𝐄 𝐁𝐀𝐃𝐈 𝐑𝐀𝐍𝐃𝐃𝐃𝐃𝐃",
    "𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐂𝐇𝐊𝐀𝐀𝐀𝐀",
    "𝐊𝐈𝐓𝐍𝐈 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐀𝐁 𝐎𝐑..",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐂𝐇𝐎𝐃 𝐃𝐈 𝐇𝐌 𝐍𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐄 𝐒𝐓𝐇 𝐑𝐄𝐄𝐋𝐒 𝐁𝐍𝐄𝐆𝐀 𝐑𝐎𝐀𝐃 𝐏𝐄𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐄𝐊 𝐃𝐀𝐌 𝐓𝐎𝐏 𝐒𝐄𝐗𝐘",
    "𝐌𝐀𝐋𝐔𝐌 𝐍𝐀 𝐏𝐇𝐑 𝐊𝐄𝐒𝐄 𝐋𝐄𝐓𝐀 𝐇𝐔 𝐌 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐓𝐀𝐏𝐀 𝐓𝐀𝐏𝐏𝐏𝐏𝐏",
    "𝐋𝐔𝐍𝐃 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 𝐓𝐔 𝐊𝐄𝐑𝐄𝐆𝐀 𝐓𝐘𝐏𝐈𝐍",
    "𝐒𝐏𝐄𝐄𝐃 𝐏𝐊𝐃 𝐋𝐖𝐃𝐄𝐄𝐄𝐄",
    "𝐁𝐀𝐀𝐏 𝐊𝐈 𝐒𝐏𝐄𝐄𝐃 𝐌𝐓𝐂𝐇 𝐊𝐑𝐑𝐑",
    "𝐋𝐖𝐃𝐄𝐄𝐄",
    "𝐏𝐀𝐏𝐀 𝐊𝐈 𝐒𝐏𝐄𝐄𝐃 𝐌𝐓𝐂𝐇 𝐍𝐇𝐈 𝐇𝐎 𝐑𝐇𝐈 𝐊𝐘𝐀",
    "𝐀𝐋𝐄 𝐀𝐋𝐄 𝐌𝐄𝐋𝐀 𝐁𝐂𝐇𝐀𝐀𝐀𝐀",
    "𝐂𝐇𝐔𝐃 𝐆𝐘𝐀 𝐏𝐀𝐏𝐀 𝐒𝐄𝐄𝐄",
    "𝐊𝐈𝐒𝐀𝐍 𝐊𝐎 𝐊𝐇𝐎𝐃𝐍𝐀 𝐎𝐑",
    "𝐒𝐀𝐋𝐄 𝐑𝐀𝐏𝐄𝐊𝐋 𝐊𝐑𝐃𝐊𝐀 𝐓𝐄𝐑𝐀",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐀𝐀𝐀𝐀",
    "𝐊𝐈𝐃𝐒𝐒𝐒𝐒",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐂𝐇𝐔𝐃 𝐆𝐘𝐈 𝐀𝐁 𝐅𝐑𝐀𝐑 𝐌𝐓 𝐇𝐎𝐍𝐀",
    "𝐘𝐄 𝐋𝐃𝐍𝐆𝐄 𝐁𝐀𝐏𝐏 𝐒𝐄",
    "𝐊𝐈𝐃𝐒𝐒𝐒 𝐅𝐑𝐀𝐑 𝐇𝐀𝐇𝐀𝐇𝐇",
    "𝐁𝐇𝐄𝐍 𝐊𝐄 𝐋𝐖𝐃𝐄 𝐒𝐇𝐑𝐌 𝐊𝐑",
    "𝐊𝐈𝐓𝐍𝐈 𝐆𝐋𝐈𝐘𝐀 𝐏𝐃𝐖𝐄𝐆𝐀 𝐀𝐏𝐍𝐈 𝐌𝐀 𝐊𝐎",
    "𝐍𝐀𝐋𝐋𝐄𝐄",
    "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐒𝐀𝐃𝐀𝐊 𝐏𝐑 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 😂😆🤤",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐑 𝐏𝐈𝐋𝐋𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔 😼😂🤤",
    "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐍𝐄 𝐒𝐇𝐎𝐑 𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐑𝐀𝐍𝐃𝐈 𝐂𝐇𝐎𝐑 𝐇𝐄 💋💋💦",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 😂👻🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐃 𝐏𝐄𝐇𝐈 𝐌𝐔𝐓𝐇 𝐃𝐈𝐀 💦💦💦💦",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐀𝐀𝐆 𝐋𝐀𝐆𝐀𝐃𝐈𝐀 𝐌𝐄𝐑𝐀 𝐌𝐎𝐓𝐀 𝐋𝐔𝐍𝐃 𝐃𝐀𝐋𝐊𝐄 🔥🔥💦😆😆",
    "𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐂𝐇𝐀𝐋 𝐍𝐈𝐊𝐀𝐋",
    "𝐊𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐁𝐇𝐄𝐉 😆👻🤤",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎𝐓𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐏𝐔𝐑𝐀 𝐅𝐀𝐀𝐃 𝐃𝐈𝐀 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉 😆💦🤤",
    "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐄𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐓𝐎 𝐌𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐁𝐀𝐍𝐆𝐀𝐘𝐈 𝐀𝐁𝐁 𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐓𝐀 𝐅𝐈𝐑𝐒𝐄 ♥️💦😆😆😆😆",
    "𝐇𝐀𝐑𝐈 𝐇𝐀𝐑𝐈 𝐆𝐇𝐀𝐀𝐒 𝐌𝐄 𝐉𝐇𝐎𝐏𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 🤣🤣💋💦",
    "𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐄 𝐁𝐀𝐀𝐏 𝐊𝐎 𝐁𝐇𝐄𝐉 𝐓𝐄𝐑𝐀 𝐁𝐀𝐒𝐊𝐀 𝐍𝐇𝐈 𝐇𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐁𝐎𝐌𝐁 𝐃𝐀𝐋𝐊𝐄 𝐔𝐃𝐀 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐀𝐖𝐃𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐓𝐑𝐀𝐈𝐍 𝐌𝐄 𝐋𝐄𝐉𝐀𝐊𝐄 𝐓𝐎𝐏 𝐁𝐄𝐃 𝐏𝐄 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 🤣🤣💋💋",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐕𝐈𝐃𝐄𝐎 𝐁𝐀𝐍𝐀𝐊𝐄 𝐗𝐍𝐗𝐗.𝐂𝐎𝐌 𝐏𝐄 𝐍𝐄𝐄𝐋𝐀𝐌 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦💋",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐊𝐎 𝐏𝐎𝐑𝐍𝐇𝐔𝐁.𝐂𝐎𝐌 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 🤣💋💦",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐄𝐊𝐎 𝐂𝐇𝐀𝐊𝐊𝐎 𝐒𝐄 𝐏𝐈𝐋𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 🤣🤣",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐅𝐀𝐀𝐃𝐊𝐄 𝐑𝐀𝐊𝐃𝐈𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐎𝐃𝐄 𝐉𝐀𝐀 𝐀𝐁𝐁 𝐒𝐈𝐋𝐖𝐀𝐋𝐄 👄👄",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐔𝐍𝐃 𝐊𝐀𝐀𝐋𝐀",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐋𝐄𝐓𝐈 𝐌𝐄𝐑𝐈 𝐋𝐔𝐍𝐃 𝐁𝐀𝐃𝐄 𝐌𝐀𝐒𝐓𝐈 𝐒𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐌𝐄𝐍𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐁𝐎𝐇𝐎𝐓 𝐒𝐀𝐒𝐓𝐄 𝐒𝐄",
    "𝐁𝐄𝐓𝐄 𝐓𝐔 𝐁𝐀𝐀𝐏 𝐒𝐄 𝐋𝐄𝐆𝐀 𝐏𝐀𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄 𝐍𝐀𝐍𝐆𝐀 💦💋",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐇 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐀𝐆𝐋𝐈 𝐁𝐀𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐓 𝐎𝐑 𝐌𝐄𝐑𝐄 𝐌𝐎𝐓𝐄 𝐋𝐔𝐍𝐃 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑",
    "𝐂𝐇𝐀𝐋 𝐁𝐄𝐓𝐀 𝐓𝐔𝐉𝐇𝐄 𝐌𝐀𝐀𝐅 𝐊𝐈𝐀 🤣 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉",
    "𝐒𝐇𝐀𝐑𝐀𝐌 𝐊𝐀𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐊𝐈𝐓𝐍𝐀 𝐆𝐀𝐀𝐋𝐈𝐀 𝐒𝐔𝐍𝐖𝐀𝐘𝐄𝐆𝐀 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐔𝐏𝐄𝐑",
    "𝐀𝐁𝐄 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐀𝐔𝐊𝐀𝐓 𝐍𝐇𝐈 𝐇𝐄𝐓𝐎 𝐀𝐏𝐍𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑 𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀",
    "𝐊𝐈𝐃𝐙 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐓𝐄𝐑𝐑 𝐋𝐈𝐘𝐄 𝐁𝐇𝐀𝐈 𝐃𝐄𝐃𝐈𝐘𝐀",
    "𝐉𝐔𝐍𝐆𝐋𝐄 𝐌𝐄 𝐍𝐀𝐂𝐇𝐓𝐀 𝐇𝐄 𝐌𝐎𝐑𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐃𝐄𝐊𝐊𝐄 𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 🤣🤣💦💋",
    "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐌𝐄 𝐑𝐄𝐇𝐓𝐀 𝐇𝐄 𝐒𝐀𝐍𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐎𝐑 𝐁𝐀𝐍𝐀 𝐃𝐈𝐀 𝐑𝐀𝐍𝐃 🤤🤣",
    "𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐌𝐔𝐉𝐇𝐊𝐎 𝐏𝐀𝐏𝐀 𝐊𝐘𝐎𝐔𝐍𝐊𝐈 𝐌𝐄𝐍𝐄 𝐁𝐀𝐍𝐀𝐃𝐈𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐏𝐑𝐄𝐆𝐍𝐄𝐍𝐓 🤣🤣",
    "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐒𝐔𝐀𝐑 𝐊𝐀 𝐋𝐎𝐔𝐃𝐀 𝐎𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐎𝐃𝐀",
    "𝐂𝐇𝐀𝐋 𝐂𝐇𝐀𝐋 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐂𝐇𝐈𝐘𝐀 𝐃𝐈𝐊𝐀",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐈𝐀 𝐍𝐀𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄",
    "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐇𝐄 𝐁𝐀𝐃𝐈 𝐒𝐄𝐗𝐘 𝐔𝐒𝐊𝐎 𝐏𝐈𝐋𝐀𝐊𝐄 𝐂𝐇𝐎𝐎𝐃𝐄𝐍𝐆𝐄 𝐏𝐄𝐏𝐒𝐈",
    "𝟐 𝐑𝐔𝐏𝐀𝐘 𝐊𝐈 𝐏𝐄𝐏𝐒𝐈 𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐒𝐀𝐁𝐒𝐄 𝐒𝐄𝐗𝐘 💋💦",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐄𝐄𝐌𝐒 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦🤣",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐔𝐓𝐇𝐊𝐄 𝐅𝐀𝐑𝐀𝐑 𝐇𝐎𝐉𝐀𝐕𝐔𝐍𝐆𝐀 𝐇𝐔𝐈 𝐇𝐔𝐈 𝐇𝐔𝐈",
    "𝐒𝐏𝐄𝐄𝐃 𝐋𝐀𝐀𝐀 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💋💦🤣",
    "𝐀𝐑𝐄 𝐑𝐄 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐊𝐘𝐎𝐔𝐍 𝐒𝐏𝐄𝐄𝐃 𝐏𝐀𝐊𝐀𝐃 𝐍𝐀 𝐏𝐀𝐀𝐀 𝐑𝐀𝐇𝐀 𝐀𝐏𝐍𝐄 𝐁𝐀𝐀𝐏 𝐊𝐀 𝐇𝐀𝐇𝐀𝐇🤣🤣",
    "𝐒𝐔𝐍 𝐒𝐔𝐍 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐉𝐇𝐀𝐍𝐓𝐎 𝐊𝐄 𝐒𝐎𝐔𝐃𝐀𝐆𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐍𝐔𝐃𝐄𝐒 𝐁𝐇𝐄𝐉",
    "𝐀𝐁𝐄 𝐒𝐔𝐍 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐅𝐀𝐀𝐃 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐊𝐇𝐔𝐋𝐄 𝐁𝐀𝐉𝐀𝐑 𝐌𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 🤣🤣💋",
    "𝐒𝐇𝐑𝐌 𝐊𝐑",
    "𝐌𝐄𝐑𝐄 𝐋𝐔𝐍𝐃 𝐊𝐄 𝐁𝐀𝐀𝐀𝐀𝐀𝐋𝐋𝐋𝐋𝐋",
    "𝐊𝐈𝐓𝐍𝐈 𝐆𝐋𝐈𝐘𝐀 𝐏𝐃𝐖𝐘𝐆𝐀 𝐀𝐏𝐍𝐈 𝐌𝐀 𝐁𝐇𝐄𝐍 𝐊𝐎",
    "𝐑𝐍𝐃𝐈 𝐊𝐄 𝐋𝐃𝐊𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄𝐄",
    "𝐊𝐈𝐃𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒",
    "𝐀𝐩𝐧𝐢 𝐠𝐚𝐚𝐧𝐝 𝐦𝐞𝐢𝐧 𝐦𝐮𝐭𝐡𝐢 𝐝𝐚𝐚𝐥",
    "𝐀𝐩𝐧𝐢 𝐥𝐮𝐧𝐝 𝐜𝐡𝐨𝐨𝐬",
    "𝐀𝐩𝐧𝐢 𝐦𝐚 𝐤𝐨 𝐣𝐚 𝐜𝐡𝐨𝐨𝐬",
    "𝐁𝐡𝐞𝐧 𝐤𝐞 𝐥𝐚𝐮𝐝𝐞",
    "𝐁𝐡𝐞𝐧 𝐤𝐞 𝐭𝐚𝐤𝐤𝐞",
    "𝐀𝐛𝐥𝐚 𝐓𝐄𝐑𝐀 𝐊𝐇𝐀𝐍 𝐃𝐀𝐍 𝐂𝐇𝐎𝐃𝐍𝐄 𝐊𝐈 𝐁𝐀𝐑𝐈𝐈𝐈",
    "𝐁𝐄𝐓𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐒𝐁𝐒𝐄 𝐁𝐃𝐈 𝐑𝐀𝐍𝐃",
    "𝐋𝐔𝐍𝐃 𝐊𝐄 𝐁𝐀𝐀𝐀𝐋 𝐉𝐇𝐀𝐓 𝐊𝐄 𝐏𝐈𝐒𝐒𝐒𝐔𝐔𝐔𝐔𝐔𝐔𝐔",
    "𝐋𝐔𝐍𝐃 𝐏𝐄 𝐋𝐓𝐊𝐈𝐓 𝐌𝐀𝐀𝐀𝐋𝐋𝐋𝐋 𝐊𝐈 𝐁𝐎𝐍𝐃 𝐇 𝐓𝐔𝐔𝐔",
    "𝐊𝐀𝐒𝐇 𝐎𝐒 𝐃𝐈𝐍 𝐌𝐔𝐓𝐇 𝐌𝐑𝐊𝐄 𝐒𝐎𝐉𝐓𝐀 𝐌 𝐓𝐔𝐍 𝐏𝐀𝐈𝐃𝐀 𝐍𝐀 𝐇𝐎𝐓𝐀𝐀",
    "𝐆𝐋𝐓𝐈 𝐊𝐑𝐃𝐈 𝐓𝐔𝐉𝐖 𝐏𝐀𝐈𝐃𝐀 𝐊𝐑𝐊𝐄",
    "𝐒𝐏𝐄𝐄𝐃 𝐏𝐊𝐃𝐃𝐃",
    "𝐆𝐚𝐚𝐧𝐝 𝐦𝐚𝐢𝐧 𝐋𝐖𝐃𝐀 𝐃𝐀𝐋 𝐋𝐄 𝐀𝐏𝐍𝐈 𝐌𝐄𝐑𝐀𝐀𝐀",
    "𝐆𝐚𝐚𝐧𝐝 𝐦𝐞𝐢𝐧 𝐛𝐚𝐦𝐛𝐮 𝐃𝐄𝐃𝐔𝐍𝐆𝐀𝐀𝐀𝐀𝐀𝐀",
    "𝐆𝐀𝐍𝐃 𝐅𝐓𝐈 𝐊𝐄 𝐁𝐀𝐋𝐊𝐊𝐊",
    "𝐆𝐨𝐭𝐞 𝐤𝐢𝐭𝐧𝐞 𝐛𝐡𝐢 𝐛𝐚𝐝𝐞 𝐡𝐨, 𝐥𝐮𝐧𝐝 𝐤𝐞 𝐧𝐢𝐜𝐡𝐞 𝐡𝐢 𝐫𝐞𝐡𝐭𝐞 𝐡𝐚𝐢",
    "𝐇𝐚𝐳𝐚𝐚𝐫 𝐥𝐮𝐧𝐝 𝐭𝐞𝐫𝐢 𝐠𝐚𝐚𝐧𝐝 𝐦𝐚𝐢𝐧",
    "𝐉𝐡𝐚𝐚𝐧𝐭 𝐤𝐞 𝐩𝐢𝐬𝐬𝐮-",
    "𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐊𝐀𝐋𝐈 𝐂𝐇𝐔𝐓",
    "𝐊𝐡𝐨𝐭𝐞𝐲 𝐤𝐢 𝐚𝐮𝐥𝐝𝐚",
    "𝐊𝐮𝐭𝐭𝐞 𝐤𝐚 𝐚𝐰𝐥𝐚𝐭",
    "𝐊𝐮𝐭𝐭𝐞 𝐤𝐢 𝐣𝐚𝐭",
    "𝐊𝐮𝐭𝐭𝐞 𝐤𝐞 𝐭𝐚𝐭𝐭𝐞",
    "𝐓𝐄𝐓𝐈 𝐌𝐀 𝐊𝐈.𝐂𝐇𝐔𝐓 , 𝐭𝐄𝐑𝐈 𝐌𝐀 𝐑𝐍𝐃𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈",
    "𝐋𝐚𝐯𝐝𝐞 𝐤𝐞 𝐛𝐚𝐥",
    "𝐦𝐮𝐡 𝐦𝐞𝐢 𝐥𝐞𝐥𝐞",
    "𝐋𝐮𝐧𝐝 𝐊𝐞 𝐏𝐚𝐬𝐢𝐧𝐞",
    "𝐌𝐄𝐑𝐄 𝐋𝐖𝐃𝐄 𝐊𝐄 𝐁𝐀𝐀𝐀𝐀𝐀𝐋𝐋𝐋",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐀𝐀𝐀𝐀𝐀",
    "𝐂𝐇𝐔𝐃 𝐆𝐘𝐀𝐀𝐀𝐀𝐀",
    "𝐑𝐚𝐧𝐝𝐢 𝐤𝐡𝐚𝐧𝐄 𝐊𝐈 𝐔𝐋𝐀𝐃𝐃𝐃",
    "𝐒𝐚𝐝𝐢 𝐡𝐮𝐢 𝐠𝐚𝐚𝐧𝐝",
    "𝐓𝐞𝐫𝐢 𝐠𝐚𝐚𝐧𝐝 𝐦𝐚𝐢𝐧 𝐤𝐮𝐭𝐞 𝐤𝐚 𝐥𝐮𝐧𝐝",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 𝐤𝐚 𝐛𝐡𝐨𝐬𝐝𝐚",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 𝐤𝐢 𝐜𝐡𝐮𝐭",
    "𝐓𝐞𝐫𝐞 𝐠𝐚𝐚𝐧𝐝 𝐦𝐞𝐢𝐧 𝐤𝐞𝐞𝐝𝐞 𝐩𝐚𝐝𝐚𝐲",
    "𝐔𝐥𝐥𝐮 𝐤𝐞 𝐩𝐚𝐭𝐡𝐞",
    "𝐒𝐔𝐍𝐍 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀",
    "𝐁𝐄𝐇𝐄𝐍 𝐊 𝐋𝐔𝐍𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐂𝐇𝐔𝐓 𝐊𝐈 𝐂𝐇𝐓𝐍𝐈𝐈𝐈𝐈",
    "𝐌𝐄𝐑𝐀 𝐋𝐀𝐖𝐃𝐀 𝐋𝐄𝐋𝐄 𝐓𝐔 𝐀𝐆𝐀𝐑 𝐂𝐇𝐀𝐈𝐘𝐄 𝐓𝐎𝐇",
    "𝐆𝐀𝐀𝐍𝐃𝐔",
    "𝐂𝐇𝐔𝐓𝐈𝐘𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐏𝐄 𝐉𝐂𝐁 𝐂𝐇𝐀𝐃𝐇𝐀𝐀 𝐃𝐔𝐍𝐆𝐀",
    "𝐒𝐀𝐌𝐉𝐇𝐀𝐀 𝐋𝐀𝐖𝐃𝐄",
    "𝐘𝐀 𝐃𝐔 𝐓𝐄𝐑𝐄 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐓𝐀𝐏𝐀𝐀 𝐓𝐀𝐏��",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐌𝐄𝐑𝐀 𝐑𝐎𝐙 𝐋𝐄𝐓𝐈 𝐇𝐀𝐈",
    "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊 𝐒𝐀𝐀𝐓𝐇 𝐌𝐌𝐒 𝐁𝐀𝐍𝐀𝐀 𝐂𝐇𝐔𝐊𝐀 𝐇𝐔���不�不",
    "𝐓𝐔 𝐂𝐇𝐔𝐓𝐈𝐘𝐀 𝐓𝐄𝐑𝐀 𝐊𝐇𝐀𝐍𝐃𝐀𝐀𝐍 𝐂𝐇𝐔𝐓𝐈𝐘𝐀",
    "𝐀𝐔𝐑 𝐊𝐈𝐓𝐍𝐀 𝐁𝐎𝐋𝐔 𝐁𝐄𝐘 𝐌𝐀𝐍𝐍 𝐁𝐇𝐀𝐑 𝐆𝐀𝐘𝐀 𝐌𝐄𝐑𝐀�不",
    "𝐓𝐄𝐑𝐈𝐈𝐈𝐈𝐈𝐈 𝐌𝐀𝐀𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓𝐓𝐓 𝐌𝐄 𝐀𝐁𝐂𝐃 𝐋𝐈𝐊𝐇 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐀 𝐊𝐄 𝐋𝐎𝐃𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐋𝐄𝐊𝐀𝐑 𝐌𝐀𝐈 𝐅𝐀𝐑𝐀𝐑",
    "𝐑𝐀𝐍𝐈𝐃𝐈𝐈𝐈",
    "𝐁𝐀𝐂𝐇𝐄𝐄",
    "𝐂𝐇𝐎𝐃𝐔",
    "𝐑𝐀𝐍𝐃𝐈",
    "𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄",
    "𝐓𝐄𝐑𝐈𝐈𝐈𝐈𝐈 𝐌𝐀𝐀𝐀 𝐊𝐎 𝐁𝐇𝐄𝐉𝐉𝐉",
    "𝐓𝐄𝐑𝐀𝐀 𝐁𝐀𝐀𝐀𝐀𝐏 𝐇𝐔",
    "𝐭𝐞𝐫𝐢 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐇𝐀𝐀𝐓 𝐃𝐀𝐀𝐋𝐋𝐊𝐄 𝐁𝐇𝐀𝐀𝐆 𝐉𝐀𝐀𝐍𝐔𝐆𝐀",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 𝐊𝐎 𝐒𝐀𝐑𝐀𝐊 𝐏𝐄 𝐋𝐄𝐓𝐀𝐀 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐆𝐁 𝐑𝐎𝐀𝐃 𝐏𝐄 𝐋𝐄𝐉𝐀𝐊𝐄 𝐁𝐄𝐂𝐇 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌É 𝐊𝐀𝐀𝐋𝐈 𝐌𝐈𝐓𝐂𝐇",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐒𝐀𝐒𝐓𝐈 𝐑𝐀𝐍𝐃𝐈 𝐇𝐀𝐈",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐊𝐀𝐁𝐔𝐓𝐀𝐑 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐒𝐎𝐔𝐏 𝐁𝐀𝐍𝐀𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐑𝐀𝐍𝐃𝐈 𝐇𝐀𝐈",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐃𝐄𝐓𝐎𝐋 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀𝐀𝐀 𝐁𝐇𝐎𝐒𝐃𝐀𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐋𝐀𝐏𝐓𝐎𝐏",
    "𝐓𝐞𝐫𝐢 𝐦𝐚𝐚 𝐑𝐀𝐍𝐃𝐈 𝐇𝐀𝐈",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐁𝐈𝐒𝐓𝐀𝐑 𝐏𝐄 𝐋𝐄𝐓𝐀𝐀𝐊𝐄 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐀𝐌𝐄𝐑𝐈𝐂𝐀 𝐆𝐇𝐔𝐌𝐀𝐀𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐍𝐀𝐀𝐑𝐈𝐘𝐀𝐋 𝐏𝐇𝐎𝐑 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐆𝐀𝐍𝐃 𝐌𝐄 𝐃𝐄𝐓𝐎𝐋 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐊𝐎 𝐇𝐎𝐑𝐋𝐈𝐂𝐊𝐒 𝐏𝐈𝐋𝐀𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐒𝐀𝐑𝐀𝐊 𝐏𝐄 𝐋𝐄𝐓𝐀𝐀𝐀 𝐃𝐔𝐍𝐆𝐀𝐀𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀𝐀 𝐁𝐇𝐎𝐒𝐃𝐀",
    "𝐌𝐄𝐑𝐀𝐀𝐀 𝐋𝐔𝐍𝐃 𝐏𝐀𝐊𝐀𝐃 𝐋𝐄 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐂𝐇𝐔𝐏 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐀𝐊𝐀𝐀 𝐁𝐇𝐎𝐒𝐃𝐀𝐀",
    "𝐓𝐄𝐑𝐈𝐈𝐈 𝐌𝐀𝐀 𝐂𝐇𝐔𝐅 𝐆𝐄𝐘𝐈𝐈 𝐊𝐘𝐀𝐀𝐀 𝐋𝐀𝐖𝐃𝐄𝐄𝐄",
    "𝐓𝐄𝐑𝐈𝐈𝐈 𝐌𝐀𝐀 𝐊𝐀𝐀 𝐁𝐉𝐒𝐎𝐃𝐀𝐀𝐀",
    "𝐌𝐀𝐃𝐀𝐑𝐗𝐇𝐎𝐃𝐃𝐃",
    "𝐓𝐄𝐑𝐈𝐔𝐔𝐈 𝐌𝐀𝐀𝐀 𝐊𝐀𝐀 𝐁𝐇𝐒𝐎𝐃𝐀𝐀𝐀",
    "𝐓𝐄𝐑𝐈𝐈𝐈𝐈𝐈𝐈 𝐁𝐄𝐇𝐄𝐍𝐍𝐍𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐃𝐃𝐔𝐔𝐔𝐔 𝐌𝐀𝐃𝐀𝐑𝐗𝐇𝐎𝐃𝐃𝐃𝐃",
    "𝐍𝐈𝐊𝐀𝐋 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃",
    "𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄",
    "𝐓𝐄𝐑𝐀 𝐌𝐀𝐀 𝐌𝐄𝐑𝐈 𝐅𝐀𝐍",
    "𝐓𝐄𝐑𝐈 𝐒𝐄𝐗𝐘 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐎𝐏",
    "Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..",
    "तेरी छोटी बहन साली कुतिया की चिकनी चिकनी बिना बाल वाली चूत के चिथड़े उड़ा डालूंगा अपने 9 इंच लंबे लंड से , समझा बेटीचोद साले बहन के लौड़े** \n\nतेरा बाप हूं मैं मादरचोद साले gandu , तू मेरी नाजायज औलाद है , जा जाके पूछ अपनी मम्मी साली रंडी से \n\nतेरी अप्पी बता रही थी कि तू बहुत बड़ा मादर चोद है, तूने ही अपनी अम्मी को चोद कर अपनी अप्पी पैदा की, और तू बहुत बड़ा गांडू भी है, कितने रेट है तेरे गाड़ मरवाने के ??\nतेरी मां की चूत को पिकाचू और ग्लेडिएटर्स हमेशा पेलते हैं।\nऔर ये भी बता कि गाड़ मरवाता है, कंडोम लगा के या बिना कण्डोम के ? तेल लेकर तू आएगा या मैं ही जापानी तेल लेकर आउ ?",
    "Teri ammy ke sath mai role play karunga🤣🤣🤣🤣🤣🤣usko malik ki wife banaunga aur khud driver banke pelunga usko!",
    "TERI MAA KI GAAAAND ME DANDAA DAAL KE DANDDA TODD DUNGAA MADARCHOD BAAP HU TERA BEHEN KE LUNDDD",
    "Phool murjhate achhe nahi lagte aap land khujate acche nahi lagte yehi umar hai chodne ki yaaro aap bathroom mein hilaate acche nahi lagte.",
    "Teri behn ko bolunga ki mere liye paani lao aur jb wo paani lene ke liye jhukegi tbi peeche se utha ke pel dunga",
    "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
    "Teri maa ki gaand mein abhi bhar bhar ke gaali deta hun madarchod bhosdike ruk teri maa ka bhosda randi ka pilla madarchod chus le mera loda bhosdike",
    "Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.",
    "Hey mere bete kaise ho beta tum\nUss raat jab maine teri maa choda tha jiske 9 mahine baad tum paida hue bhot maza aaya tha mujhe aur teri maa ko bhi!!",
    "Teri maa ki gaand mein abhi bhar bhar ke gaali deta hun madarchod bhosdike ruk teri maa ka bhosda randi ka pilla madarchod chus le mera loda bhosdike",
    "TERIIIIIIII MAAAAAAAAAA KI CHUTTTTT MEEEEEEEEE GHODEEEE KA LUNDDDDDDD MADARCHODDDDDDD GASTI KE BAXHEEEEE",
    "TERI MAA KA MARS PE KOTHA KHULWAAUNGA 🔥😂",
    "G4ND😈 M3 TERI ᏞᎾhᎬ🥒🥒  KI ᏒᎾᎠ D4LDUNGA😸😸bᎥᏞᏞᎥ 😺 bᎪᏁᎪ  K3 CH0DUNG4💦💦👅👅 T3R ᎪmmᎽ  K0👻👻ᏆᎬᏃᎪb😍😍  ᎠᎪᎪᏞ  ᎠuᏁᎶᎪ T3R1👄B3HN K3😜😜😜 B00R 👙👙MEM4D3RCH0D🙈🙈JH4NT3🖕 ᏁᎾᏟhᏞuᏁᎶᎪ🥳🥳  ᏆᎬᎬ1 bᎬhᏁ  K1🍌🍌SU4R K1 😈ᏁᎪsᎪᏞ Ꮮ0ᎳᎠu 🙈T3R1 ᎪmmᎽ😺😺😺  K0 F4NS1 LAGA DUNG4😹😹💦💦 G44ND 💣ME TER1 AC1D🍆🍆 D44LDUNG4🍒ThᎪᏁᎠᎬ 😹 ᏢᎪᎪᏁᎥ SE 👙ᏁᎬhᏞᎪ K3 CH0DUNG4 🥳🥳TER1 CHHOT1💦💦 B3HN KO😹TATT1💩💩 KRDUNG4 TER1  Ꮆf  KE😺😺 muh  ᏢᎬ 👅👅😈",
    "MADARCHOODOO.••>___βħΔG βΣτΔ βħΔG τΣRΔΔΔ βΔPPP ΔΥΔΔ___<•••🔥ΔΨUSH HΣRΣ🔥RυKKKK RυKK βΣτΔΔ βHΔGGG KΔHΔ RΔHΔΔ HΔII ΔβHI τΟ τΣRI мΔΔ ζHυδΣGII RυKK☜☜☜мΔτLΔββ βΔβΥ мΔRVΔJΣΣΣ мΔПΣGIII👅👅👅👅>>>>◑︿◐JHΔПτ βHΔRR KI ΔυKΔτ  ПΔHI τΣRI ΔυR βΔPPP ςΣ LΔδΣGΔΔΔ◑︿◐<<<<<τΣRI βΣHΣП KI GΔПδ мΣ LΟHΣ KΔ RΟδδ δΔL δυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀▄τΣRI мΔΔ KI GΔПδδ мΣ βΣΔR KI βΟττLΣ δΔL KΣ FΟδδ δυПGΔ🍾🍾🍾________βHΔGGG δΔRLIПG βHΔGGG___GΔПδδ βΔζζHΔ KΣΣ βHΔGGGG____βΔP ΔΥΔ τΣRΔ 😎ΔΨUSH HΣRΣ😎>>>>>◑︿◐JHΔПτ βHΔRR KI ΔυKΔτ  ПΔHI τΣRI ΔυR βΔPPP ςΣ LΔδΣGΔΔΔ◑︿◐<<<<<τΣRI βΣHΣП KI GΔПδ мΣ LΟHΣ KΔ RΟδδ δΔL δυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀▄ΨΩUR ҒΔTHΣR #Pika_Pika_Pikachuuu HΣRΣ😎😎",
    "MADARCHODD😁-):-P:-\:'(:3:'(:'((^-)(^-):3:3:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/ BHEN KE LODE APNE BAAP KO🤥🤥 B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)(^o^)(^o^)GAALI DEGA RANDI WALE 🤒🤒🤒(^o^)(^o^)(^o^)(^o^)(^o^)APNI MA SE PHUCH KI TERI MAAA NE MERI MUTH KAISE MARI THI SALE BHOT BAD TARIKE SE TERI MAA KI GHAND MARI  THI😂😂😂😂 -/:-/:-/:-/:-/:-/:-/:-/:-/:-/:B-)B-)B-)B-)B-)B-)B-)TERI MAA KO LOCAL CONDOM SE CHODA 🌎🌎🌎🌎🌎🌎HA TO GHAND KE ANDAR CONDOM BLAST HOGYA OR BBHADWE TU LODA PAKAD KE BHAR AAGYA BHOSDIKE MADARCHODB-):-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/ CHALL ABB NIKKL BBHAADWEE😒😒",
    "Uss raat bada Maza aaya Jab glคdiatør͢͢͢𝓼 Teri maa ke upar aur teri maa glคdiatør͢͢͢𝓼 ke neeche\n\nOh yeah!! Oh yeah!!",
    "Teri Maa ki chut mein diya Gladiators ne moot!!",
    "Kaali Chut Ke Safed Jhaant…",
    "Abla Naari, Tere Bable Bhaari… ",
    "Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain… ",
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩",
    "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT",
    "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙",
    "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍",
    "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI VAHEEN DHANDHE VAALI 😋😛",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩",
    "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈",
    "TERA PEHLA BAAP HU MADARCHOD ",
    "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹",
    "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ",
    "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭",
    "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 ",
    "TERI MAA KI CHUT MEI BATTERY LAGA KE POWERBANK BANA DUNGA 🔋 🔥🤩",
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA BAHTI HUYI CHUT RUK JAYEGIIII😈🔥😍",
    "TERI MAA KE GAAND MEI JHAADU DAL KE MOR 🦚 BANA DUNGAA 🤩🥵😱",
    "TERI CHUT KI CHUT MEI SHOULDERING KAR DUNGAA HILATE HUYE BHI DARD HOGAAA😱🤮👺",
    "TERI MAA KO REDI PE BAITHAL KE USSE USKI CHUT BILWAUNGAA 💰 😵🤩",
    "BHOSDIKE TERI MAA KI CHUT MEI 4 HOLE HAI UNME MSEAL LAGA BAHUT BAHETI HAI BHOFDIKE👊🤮🤢🤢",
    "TERI BAHEN KI CHUT MEI BARGAD KA PED UGA DUNGAA CORONA MEI SAB OXYGEN LEKAR JAYENGE🤢🤩🥳",
    "TERI MAA KI CHUT MEI SUDO LAGA KE BIGSPAM LAGA KE 9999 FUCK LAGAA DU 🤩🥳🔥",
    "TERI VAHEN KE BHOSDIKE MEI BESAN KE LADDU BHAR DUNGA🤩🥳🔥😈",
    "TERI MAA KI CHUT KHOD KE USME CYLINDER ⛽️ FIT KARKE USMEE DAL MAKHANI BANAUNGAAA🤩👊🔥",
    "TERI MAA KI CHUT MEI SHEESHA DAL DUNGAAA AUR CHAURAHE PE TAANG DUNGA BHOSDIKE😈😱🤩",
    "TERI MAA KI CHUT MEI CREDIT CARD DAL KE AGE SE 500 KE KAARE KAARE NOTE NIKALUNGAA BHOSDIKE💰💰🤩",
    "TERI MAA KE SATH SUAR KA SEX KARWA DUNGAA EK SATH 6-6 BACHE DEGI💰🔥😱",
    "TERI BAHEN KI CHUT MEI APPLE KA 18W WALA CHARGER 🔥🤩",
    "TERI BAHEN KI GAAND MEI ONEPLUS KA WRAP CHARGER 30W HIGH POWER 💥😂😎",
    "TERI BAHEN KI CHUT KO AMAZON SE ORDER KARUNGA 10 rs MEI AUR FLIPKART PE 20 RS MEI BECH DUNGA🤮👿😈🤖",
    "TERI MAA KI BADI BHUND ME ZOMATO DAL KE SUBWAY KA BFF VEG SUB COMBO [15cm , 16 inches ] ORDER COD KRVAUNGA OR TERI MAA JAB DILIVERY DENE AYEGI TAB USPE JAADU KRUNGA OR FIR 9 MONTH BAAD VO EK OR FREE DILIVERY DEGI🙀👍🥳🔥",
    "TERI BHEN KI CHUT KAALI🙁🤣💥",
    "TERI MAA KI CHUT ME CHANGES COMMIT KRUGA FIR TERI BHEEN KI CHUT AUTOMATICALLY UPDATE HOJAAYEGI🤖🙏🤔",
    "TERI MAUSI KE BHOSDE MEI INDIAN RAILWAY 🚂💥😂",
    "TU TERI BAHEN TERA KHANDAN SAB BAHEN KE LAWDE RANDI HAI RANDI 🤢✅🔥",
    "TERI BAHEN KI CHUT MEI IONIC BOND BANA KE VIRGINITY LOOSE KARWA DUNGA USKI 📚 😎🤩",
    "TERI RANDI MAA SE PUCHNA BAAP KA NAAM BAHEN KE LODEEEEE 🤩🥳😳",
    "TU AUR TERI MAA DONO KI BHOSDE MEI METRO CHALWA DUNGA MADARXHOD 🚇🤩😱🥶",
    "TERI MAA KO ITNA CHODUNGA TERA BAAP BHI USKO PAHCHANANE SE MANA KAR DEGA😂👿🤩",
    "TERI BAHEN KE BHOSDE MEI HAIR DRYER CHALA DUNGAA💥🔥🔥",
    "TERI MAA KI CHUT MEI TELEGRAM KI SARI RANDIYON KA RANDI KHANA KHOL DUNGAA👿🤮😎",
    "TERI MAA KI CHUT ALEXA DAL KEE DJ BAJAUNGAAA 🎶 ⬆️🤩💥",
    "TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA 🤩👊👤😍",
    "TERI BAHEN KA VPS BANA KE 24*7 BASH CHUDAI COMMAND DE DUNGAA 🤩💥🔥🔥",
    "TERI MUMMY KI CHUT MEI TERE LAND KO DAL KE KAAT DUNGA MADARCHOD 🔪😂🔥",
    "SUN TERI MAA KA BHOSDA AUR TERI BAHEN KA BHI BHOSDA 👿😎👊",
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE 👿💥🤩🔥",
    "SUN MADARCHOD JYADA NA UCHAL MAA CHOD DENGE EK MIN MEI ✅🤣🔥🤩",
    "APNI AMMA SE PUCHNA USKO US KAALI RAAT MEI KAUN CHODNEE AYA THAAA! TERE IS PAPA KA NAAM LEGI 😂👿😳",
    "TOHAR BAHIN CHODU BBAHEN KE LAWDE USME MITTI DAL KE CEMENT SE BHAR DU 🏠🤢🤩💥",
    "TUJHE AB TAK NAHI SMJH AYA KI MAI HI HU TUJHE PAIDA KARNE WALA BHOSDIKEE APNI MAA SE PUCH RANDI KE BACHEEEE 🤩👊👤😍",
    "TERI MAA KE BHOSDE MEI SPOTIFY DAL KE LOFI BAJAUNGA DIN BHAR 😍🎶🎶💥",
    "TERI MAA KA NAYA RANDI KHANA KHOLUNGA CHINTA MAT KAR 👊🤣🤣😳",
    "TERA BAAP HU BHOSDIKE TERI MAA KO RANDI KHANE PE CHUDWA KE US PAISE KI DAARU PEETA HU 🍷🤩🔥",
    "TERI BAHEN KI CHUT MEI APNA BADA SA LODA GHUSSA DUNGAA KALLAAP KE MAR JAYEGI 🤩😳😳🔥",
    "TOHAR MUMMY KI CHUT MEI PURI KI PURI KINGFISHER KI BOTTLE DAL KE TOD DUNGA ANDER HI 😱😂🤩",
    "TERI MAA KO ITNA CHODUNGA KI SAPNE MEI BHI MERI CHUDAI YAAD KAREGI RANDI 🥳😍👊💥",
    "TERI MUMMY AUR BAHEN KO DAUDA DAUDA NE CHODUNGA UNKE NO BOLNE PE BHI LAND GHUSA DUNGA ANDER TAK 😎😎🤣🔥",
    "TERI MUMMY KI CHUT KO ONLINE OLX PE BECHUNGA AUR PAISE SE TERI BAHEN KA KOTHA KHOL DUNGA 😎🤩😝😍",
    "TERI MAA KE BHOSDA ITNA CHODUNGA KI TU CAH KE BHI WO MAST CHUDAI SE DUR NHI JA PAYEGAA 😏😏🤩😍",
    "SUN BE RANDI KI AULAAD TU APNI BAHEN SE SEEKH KUCH KAISE GAAND MARWATE HAI😏🤬🔥💥",
    "TERI MAA KA YAAR HU MEI AUR TERI BAHEN KA PYAAR HU MEI AJA MERA LAND CHOOS LE 🤩🤣💥",
    "MADARCHOD",
    "BHOSDIKE",
    "LAAAWEEE KE BAAAAAL",
    "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL",
    "MADRCHOD..",
    "TERI MA KI CHUT..",
    "LWDE KE BAAALLL.",
    "MACHAR KI JHAAT KE BAAALLLL",
    "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA",
    "TERI BHN SBSBE BDI RANDI.",
    "TERI MA OSSE BADI RANDDDDD",
    "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..",
    "TERI MA CHOD DI HM NE",
    "TERI MA KE STH REELS BNEGA ROAD PEE",
    "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP",
    "LUND KE CHODE TU KEREGA TYPIN",
    "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR",
    "LWDEEE",
    "PAPA KI SPEED MTCH NHI HO RHI KYA",
    "ALE ALE MELA BCHAAAA",
    "CHUD GYA PAPA SEEE",
    "KISAN KO KHODNA OR",
    "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA",
    "KIDSSSS",
    "TERI MA CHUD GYI AB FRAR MT HONA",
    "YE LDNGE BAPP SE",
    "KIDSSS FRAR HAHAHH",
    "BHEN KE LWDE SHRM KR",
    "KITNI GLIYA PDWEGA APNI MA KO",
    "NALLEE",
    "SHRM KR",
    "MERE LUND KE BAAAAALLLLL",
    "KITNI GLIYA PDWYGA APNI MA BHEN KO",
    "RNDI KE LDKEEEEEEEEE",
    "KIDSSSSSSSSSSSS",
    "Apni gaand mein muthi daal",
    "Apni lund choos",
    "Apni ma ko ja choos",
    "Bhen ke laude",
    "Bhen ke takke",
    "Abla TERA KHAN DAN CHODNE KI BARIII",
    "BETE TERI MA SBSE BDI RAND",
    "LUND KE BAAAL JHAT KE PISSSUUUUUUU",
    "LUND PE LTKIT MAAALLLL KI BOND H TUUU",
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA",
    "GLTI KRDI TUJW PAIDA KRKE",
    "SPEED PKDDD",
    "Gaand main LWDA DAL LE APNI MERAAA",
    "Gaand mein bambu DEDUNGAAAAAA",
    "GAND FTI KE BALKKK",
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai",
    "Hazaar lund teri gaand main",
    "Jhaant ke pissu-",
    "TERI MA KI KALI CHUT",
    "Khotey ki aulda",
    "Kutte ka awlat",
    "Kutte ki jat",
    "Kutte ke tatte",
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII",
    "Lavde ke bal",
    "muh mei lele",
    "Lund Ke Pasine",
    "MERE LWDE KE BAAAAALLL",
    "HAHAHAAAAAA",
    "CHUD GYAAAAA",
    "Randi khanE KI ULADDD",
    "Sadi hui gaand",
    "Teri gaand main kute ka lund",
    "Teri maa ka bhosda",
    "Teri maa ki chut",
    "Tere gaand mein keede paday",
    "Ullu ke pathe",
    "SUNN MADERCHOD",
    "TERI MAA KA BHOSDA",
    "BEHEN K LUND",
    "TERI MAA KA CHUT KI CHTNIIII",
    "MERA LAWDA LELE TU AGAR CHAIYE TOH",
    "GAANDU",
    "CHUTIYA",
    "TERI MAA KI CHUT PE JCB CHADHAA DUNGA",
    "SAMJHAA LAWDE",
    "YA DU TERE GAAND ME TAPAA TAP��",
    "TERI BEHEN MERA ROZ LETI HAI",
    "TERI GF K SAATH MMS BANAA CHUKA HU���不�不",
    "TU CHUTIYA TERA KHANDAAN CHUTIYA",
    "AUR KITNA BOLU BEY MANN BHAR GAYA MERA�不",
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE",
    "TERI MAA KO LEKAR MAI FARAR",
    "RANIDIII",
    "BACHEE",
    "CHODU",
    "RANDI",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT MÉ KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "TERIII MAA KAA BJSODAAA",
    "MADARXHODDD",
    "TERIUUI MAAA KAA BHSODAAA",
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD",
    "NIKAL MADARCHOD",
    "RANDI KE BACHE",
    "TERA MAA MERI FAN",
    "TERI SEXY BAHEN KI CHUT OP",
]

curses = [
    "𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐆𝐇𝐔𝐓𝐊𝐀 𝐊𝐇𝐀𝐀𝐊𝐄 𝐓𝐇𝐎𝐎𝐊 𝐃𝐔𝐍𝐆𝐀 🤣🤣",
    "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐍𝐇𝐈 𝐇𝐀𝐈 𝐊𝐘𝐀? 𝟗 𝐌𝐀𝐇𝐈𝐍𝐄 𝐑𝐔𝐊 𝐒𝐀𝐆𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐃𝐄𝐓𝐀 𝐇𝐔 🤣🤣🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐄𝐑𝐎𝐏𝐋𝐀𝐍𝐄𝐏𝐀𝐑𝐊 𝐊𝐀𝐑𝐊𝐄 𝐔𝐃𝐀𝐀𝐍 𝐁𝐇𝐀𝐑 𝐃𝐔𝐆𝐀 ✈️🛫",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐔𝐓𝐋𝐈 𝐁𝐎𝐌𝐁 𝐅𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐉𝐇𝐀𝐀𝐓𝐄 𝐉𝐀𝐋 𝐊𝐄 𝐊𝐇𝐀𝐀𝐊 𝐇𝐎 𝐉𝐀𝐘𝐄𝐆𝐈💣",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐂𝐎𝐎𝐓𝐄𝐑 𝐃𝐀𝐀𝐋 𝐃𝐔𝐆𝐀👅",
    "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀",
    "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐀𝐊𝐓𝐄 🤱 𝐆𝐀𝐋𝐈 𝐊𝐄 𝐊𝐔𝐓𝐓𝐎 🦮 𝐌𝐄 𝐁𝐀𝐀𝐓 𝐃𝐔𝐍𝐆𝐀 𝐏𝐇𝐈𝐑 🍞 𝐁𝐑𝐄𝐀𝐃 𝐊𝐈 𝐓𝐀𝐑𝐇 𝐊𝐇𝐀𝐘𝐄𝐍𝐆𝐄 𝐖𝐎 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓",
    "𝐃𝐔𝐃𝐇 𝐇𝐈𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐄 𝐔𝐏𝐑 𝐍𝐈𝐂𝐇𝐄 🆙🆒😙",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 ✋ 𝐇𝐀𝐓𝐓𝐇 𝐃𝐀𝐋𝐊𝐄 👶 𝐁𝐀𝐂𝐂𝐇𝐄 𝐍𝐈𝐊𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 😍",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐊𝐄𝐋𝐄 𝐊𝐄 𝐂𝐇𝐈𝐋𝐊𝐄 🍌🍌😍",
    "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐋𝐀𝐆𝐀𝐀𝐔𝐍𝐆𝐀 𝐒𝐀𝐒𝐓𝐄 𝐒𝐏𝐀𝐌 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐃𝐇𝐀𝐍𝐃𝐇𝐄 𝐕𝐀𝐀𝐋𝐈 😋😛",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐂 𝐋𝐀𝐆𝐀 𝐃𝐔𝐍𝐆𝐀 𝐒𝐀𝐀𝐑𝐈 𝐆𝐀𝐑𝐌𝐈 𝐍𝐈𝐊𝐀𝐋 𝐉𝐀𝐀𝐘𝐄𝐆𝐈",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐇𝐎𝐑𝐋𝐈𝐂𝐊𝐒 𝐏𝐄𝐄𝐋𝐀𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😚",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐒𝐀𝐑𝐈𝐘𝐀 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐔𝐒𝐈 𝐒𝐀𝐑𝐈𝐘𝐄 𝐏𝐑 𝐓𝐀𝐍𝐆 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐇𝐎𝐍𝐆𝐄 😱😱",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐊𝐎𝐋𝐊𝐀𝐓𝐀 𝐕𝐀𝐀𝐋𝐄 𝐉𝐈𝐓𝐔 𝐁𝐇𝐀𝐈𝐘𝐀 𝐊𝐀 𝐋𝐔𝐍𝐃 𝐌𝐔𝐁𝐀𝐑𝐀𝐊 🤩🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐅𝐀𝐍𝐓𝐀𝐒𝐘 𝐇𝐔 𝐋𝐀𝐖𝐃𝐄, 𝐓𝐔 𝐀𝐏𝐍𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐒𝐌𝐁𝐇𝐀𝐀𝐋 😈😈",
    "𝐓𝐄𝐑𝐀 𝐏𝐄𝐇𝐋𝐀 𝐁𝐀𝐀𝐏 𝐇𝐔 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 ",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐗𝐕𝐈𝐃𝐄𝐎𝐒.𝐂𝐎𝐌 𝐂𝐇𝐀𝐋𝐀 𝐊𝐄 𝐌𝐔𝐓𝐇 𝐌𝐀𝐀𝐑𝐔𝐍𝐆𝐀 🤡😹",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐆𝐑𝐎𝐔𝐏 𝐕𝐀𝐀𝐋𝐎𝐍 𝐒𝐀𝐀𝐓𝐇 𝐌𝐈𝐋𝐊𝐄 𝐆𝐀𝐍𝐆 𝐁𝐀𝐍𝐆 𝐊𝐑𝐔𝐍𝐆𝐀🙌🏻☠️ ",
    "𝐓𝐄𝐑𝐈 𝐈𝐓𝐄𝐌 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐋𝐔𝐍𝐃 𝐃𝐀𝐀𝐋𝐊𝐄,𝐓𝐄𝐑𝐄 𝐉𝐀𝐈𝐒𝐀 𝐄𝐊 𝐎𝐑 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃🤘🏻🙌🏻☠️ ",
    "𝐀𝐔𝐊𝐀𝐀𝐓 𝐌𝐄 𝐑𝐄𝐇 𝐕𝐑𝐍𝐀 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐃𝐀𝐍𝐃𝐀 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐌𝐔𝐇 𝐒𝐄 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐒𝐇𝐀𝐑𝐈𝐑 𝐁𝐇𝐈 𝐃𝐀𝐍𝐃𝐄 𝐉𝐄𝐒𝐀 𝐃𝐈𝐊𝐇𝐄𝐆𝐀 🙄🤭🤭",
    "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐄 𝐒𝐀𝐀𝐓𝐇 𝐋𝐔𝐃𝐎 𝐊𝐇𝐄𝐋𝐓𝐄 𝐊𝐇𝐄𝐋𝐓𝐄 𝐔𝐒𝐊𝐄 𝐌𝐔𝐇 𝐌𝐄 𝐀𝐏𝐍𝐀 𝐋𝐎𝐃𝐀 𝐃𝐄 𝐃𝐔𝐍𝐆𝐀☝🏻☝🏻😬",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐀𝐏𝐍𝐄 𝐋𝐔𝐍𝐃 𝐏𝐑 𝐈𝐓𝐍𝐀 𝐉𝐇𝐔𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐊𝐈 𝐉𝐇𝐔𝐋𝐓𝐄 𝐉𝐇𝐔𝐋𝐓𝐄 𝐇𝐈 𝐁𝐀𝐂𝐇𝐀 𝐏𝐀𝐈𝐃𝐀 𝐊𝐑 𝐃𝐄𝐆𝐈👀👯 ",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐁𝐀𝐓𝐓𝐄𝐑𝐘 𝐋𝐀𝐆𝐀 𝐊𝐄 𝐏𝐎𝐖𝐄𝐑𝐁𝐀𝐍𝐊 𝐁𝐀𝐍𝐀 𝐃𝐔𝐍𝐆𝐀 🔋 🔥🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐂++ 𝐒𝐓𝐑𝐈𝐍𝐆 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐎𝐍 𝐋𝐀𝐆𝐀 𝐃𝐔𝐍𝐆𝐀 𝐁𝐀𝐇𝐓𝐈 𝐇𝐔𝐘𝐈 𝐂𝐇𝐔𝐓 𝐑𝐔𝐊 𝐉𝐀𝐘𝐄𝐆𝐈𝐈𝐈𝐈😈🔥😍",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄𝐈 𝐉𝐇𝐀𝐀𝐃𝐔 𝐃𝐀𝐋 𝐊𝐄 𝐌𝐎𝐑 🦚 𝐁𝐀𝐍𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 🤩🥵😱",
    "𝐓𝐄𝐑𝐈 𝐂𝐇𝐔𝐓 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐇𝐎𝐔𝐋𝐃𝐄𝐑𝐈𝐍𝐆 𝐊𝐀𝐑 𝐃𝐔𝐍𝐆𝐀𝐀 𝐇𝐈𝐋𝐀𝐓𝐄 𝐇𝐔𝐘𝐄 𝐁𝐇𝐈 𝐃𝐀𝐑𝐃 𝐇𝐎𝐆𝐀𝐀𝐀😱🤮👺",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐑𝐄𝐃𝐈 𝐏𝐄 𝐁𝐀𝐈𝐓𝐇𝐀𝐋 𝐊𝐄 𝐔𝐒𝐒𝐄 𝐔𝐒𝐊𝐈 𝐂𝐇𝐔𝐓 𝐁𝐈𝐋𝐖𝐀𝐔𝐍𝐆𝐀𝐀 💰 😵🤩",
    "𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝟒 𝐇𝐎𝐋𝐄 𝐇𝐀𝐈 𝐔𝐍𝐌𝐄 𝐌𝐒𝐄𝐀𝐋 𝐋𝐀𝐆𝐀 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐇𝐄𝐓𝐈 𝐇𝐀𝐈 𝐁𝐇𝐎𝐅𝐃𝐈𝐊𝐄👊🤮🤢🤢",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐁𝐀𝐑𝐆𝐀𝐃 𝐊𝐀 𝐏𝐄𝐃 𝐔𝐆𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐂𝐎𝐑𝐎𝐍𝐀 𝐌𝐄𝐈 𝐒𝐀𝐁 𝐎𝐗𝐘𝐆𝐄𝐍 𝐋𝐄𝐊𝐀𝐑 𝐉𝐀𝐘𝐄𝐍𝐆𝐄🤢🤩🥳",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐔𝐃𝐎 𝐋𝐀𝐆𝐀 𝐊𝐄 𝐁𝐈𝐆𝐒𝐏𝐀𝐌 𝐋𝐀𝐆𝐀 𝐊𝐄 𝟗𝟗𝟗𝟗 𝐅𝐔𝐂𝐊 𝐋𝐀𝐆𝐀𝐀 𝐃𝐔 🤩🥳🔥",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐌𝐄𝐈 𝐁𝐄𝐒𝐀𝐍 𝐊𝐄 𝐋𝐀𝐃𝐃𝐔 𝐁𝐇𝐀𝐑 𝐃𝐔𝐍𝐆𝐀🤩🥳🔥😈",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐇𝐎𝐃 𝐊𝐄 𝐔𝐒𝐌𝐄 𝐂𝐘𝐋𝐈𝐍𝐃𝐄𝐑 ⛽️ 𝐅𝐈𝐓 𝐊𝐀𝐑𝐊𝐄 𝐔𝐒𝐌𝐄𝐄 𝐃𝐀𝐋 𝐌𝐀𝐊𝐇𝐀𝐍𝐈 𝐁𝐀𝐍𝐀𝐔𝐍𝐆𝐀𝐀𝐀🤩👊🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐇𝐄𝐄𝐒𝐇𝐀 𝐃𝐀𝐋 𝐃𝐔𝐍𝐆𝐀𝐀𝐀 𝐀𝐔𝐑 𝐂𝐇𝐀𝐔𝐑𝐀𝐇𝐄 𝐏𝐄 𝐓𝐀𝐀𝐍𝐆 𝐃𝐔𝐍𝐆𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄😈😱🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐃𝐀𝐋 𝐊𝐄 𝐀𝐆𝐄 𝐒𝐄 𝟓𝟎𝟎 𝐊𝐄 𝐊𝐀𝐀𝐑𝐄 𝐊𝐀𝐀𝐑𝐄 𝐍𝐎𝐓𝐄 𝐍𝐈𝐊𝐀𝐋𝐔𝐍𝐆𝐀𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄💰💰🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐒𝐀𝐓𝐇 𝐒𝐔𝐀𝐑 𝐊𝐀 𝐒𝐄𝐗 𝐊𝐀𝐑𝐖𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐄𝐊 𝐒𝐀𝐓𝐇 𝟔-𝟔 𝐁𝐀𝐂𝐇𝐄 𝐃𝐄𝐆𝐈💰🔥😱",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐀𝐏𝐏𝐋𝐄 𝐊𝐀 𝟏𝟖𝐖 𝐖𝐀𝐋𝐀 𝐂𝐇𝐀𝐑𝐆𝐄𝐑 🔥🤩",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄𝐈 𝐎𝐍𝐄𝐏𝐋𝐔𝐒 𝐊𝐀 𝐖𝐑𝐀𝐏 𝐂𝐇𝐀𝐑𝐆𝐄𝐑 𝟑𝟎𝐖 𝐇𝐈𝐆𝐇 𝐏𝐎𝐖𝐄𝐑 💥😂😎",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐎 𝐀𝐌𝐀𝐙𝐎𝐍 𝐒𝐄 𝐎𝐑𝐃𝐄𝐑 𝐊𝐀𝐑𝐔𝐍𝐆𝐀 𝟏𝟎 𝐫𝐬 𝐌𝐄𝐈 𝐀𝐔𝐑 𝐅𝐋𝐈𝐏𝐊𝐀𝐑𝐓 𝐏𝐄 𝟐𝟎 𝐑𝐒 𝐌𝐄𝐈 𝐁𝐄𝐂𝐇 𝐃𝐔𝐍𝐆𝐀🤮👿😈🤖",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐁𝐀𝐃𝐈 𝐁𝐇𝐔𝐍𝐃 𝐌𝐄 𝐙𝐎𝐌𝐀𝐓𝐎 𝐃𝐀𝐋 𝐊𝐄 𝐒𝐔𝐁𝐖𝐀𝐘 𝐊𝐀 𝐁𝐅𝐅 𝐕𝐄𝐆 𝐒𝐔𝐁 𝐂𝐎𝐌𝐁𝐎 [𝟏𝟓𝐜𝐦 , 𝟏𝟔 𝐢𝐧𝐜𝐡𝐞𝐬 ] 𝐎𝐑𝐃𝐄𝐑 𝐂𝐎𝐃 𝐊𝐑𝐕𝐀𝐔𝐍𝐆𝐀 𝐎𝐑 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐉𝐀𝐁 𝐃𝐈𝐋𝐈𝐕𝐄𝐑𝐘 𝐃𝐄𝐍𝐄 𝐀𝐘𝐄𝐆𝐈 𝐓𝐀𝐁 𝐔𝐒𝐏𝐄 𝐉𝐀𝐀𝐃𝐔 𝐊𝐑𝐔𝐍𝐆𝐀 𝐎𝐑 𝐅𝐈𝐑 𝟗 𝐌𝐎𝐍𝐓𝐇 𝐁𝐀𝐀𝐃 𝐕𝐎 𝐄𝐊 𝐎𝐑 𝐅𝐑𝐄𝐄 𝐃𝐈𝐋𝐈𝐕𝐄𝐑𝐘 𝐃𝐄𝐆𝐈🙀👍🥳🔥",
    "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐀𝐀𝐋𝐈🙁🤣💥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐍𝐆𝐄𝐒 𝐂𝐎𝐌𝐌𝐈𝐓 𝐊𝐑𝐔𝐆𝐀 𝐅𝐈𝐑 𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐀𝐔𝐓𝐎𝐌𝐀𝐓𝐈𝐂𝐀𝐋𝐋𝐘 𝐔𝐏𝐃𝐀𝐓𝐄 𝐇𝐎𝐉𝐀𝐀𝐘𝐄𝐆𝐈🤖🙏🤔",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐔𝐒𝐈 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐈𝐍𝐃𝐈𝐀𝐍 𝐑𝐀𝐈𝐋𝐖𝐀𝐘 🚂💥😂",
    "𝐓𝐔 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐓𝐄𝐑𝐀 𝐊𝐇𝐀𝐍𝐃𝐀𝐍 𝐒𝐀𝐁 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐖𝐃𝐄 𝐑𝐀𝐍𝐃𝐈 𝐇𝐀𝐈 𝐑𝐀𝐍𝐃𝐈 🤢✅🔥",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐈𝐎𝐍𝐈𝐂 𝐁𝐎𝐍𝐃 𝐁𝐀𝐍𝐀 𝐊𝐄 𝐕𝐈𝐑𝐆𝐈𝐍𝐈𝐓𝐘 𝐋𝐎𝐎𝐒𝐄 𝐊𝐀𝐑𝐖𝐀 𝐃𝐔𝐍𝐆𝐀 𝐔𝐒𝐊𝐈 📚 😎🤩",
    "𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇𝐍𝐀 𝐁𝐀𝐀𝐏 𝐊𝐀 𝐍𝐀𝐀𝐌 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄𝐄𝐄𝐄𝐄 🤩🥳😳",
    "𝐓𝐔 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐃𝐎𝐍𝐎 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐌𝐄𝐓𝐑𝐎 𝐂𝐇𝐀𝐋𝐖𝐀 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐗𝐇𝐎𝐃 🚇🤩😱🥶",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐁𝐇𝐈 𝐔𝐒𝐊𝐎 𝐏𝐀𝐇𝐂𝐇𝐀𝐍𝐀𝐍𝐄 𝐒𝐄 𝐌𝐀𝐍𝐀 𝐊𝐀𝐑 𝐃𝐄𝐆𝐀😂👿🤩",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐇𝐀𝐈𝐑 𝐃𝐑𝐘𝐄𝐑 𝐂𝐇𝐀𝐋𝐀 𝐃𝐔𝐍𝐆𝐀𝐀💥🔥🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐊𝐈 𝐒𝐀𝐑𝐈 𝐑𝐀𝐍𝐃𝐈𝐘𝐎𝐍 𝐊𝐀 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐀 𝐊𝐇𝐎𝐋 𝐃𝐔𝐍𝐆𝐀𝐀👿🤮😎",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐀𝐋𝐄𝐗𝐀 𝐃𝐀𝐋 𝐊𝐄𝐄 𝐃𝐉 𝐁𝐀𝐉𝐀𝐔𝐍𝐆𝐀𝐀𝐀 🎶 ⬆️🤩💥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐆𝐈𝐓𝐇𝐔𝐁 𝐃𝐀𝐋 𝐊𝐄 𝐀𝐏𝐍𝐀 𝐁𝐎𝐓 𝐇𝐎𝐒𝐓 𝐊𝐀𝐑𝐔𝐍𝐆𝐀𝐀 🤩👊👤😍",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐕𝐏𝐒 𝐁𝐀𝐍𝐀 𝐊𝐄 𝟐𝟒*𝟕 𝐁𝐀𝐒𝐇 𝐂𝐇𝐔𝐃𝐀𝐈 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐃𝐄 𝐃𝐔𝐍𝐆𝐀𝐀 🤩💥🔥🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐓𝐄𝐑𝐄 𝐋𝐀𝐍𝐃 𝐊𝐎 𝐃𝐀𝐋 𝐊𝐄 𝐊𝐀𝐀𝐓 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 🔪😂🔥",
    "𝐒𝐔𝐍 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐈 𝐁𝐇𝐎𝐒𝐃𝐀 👿😎👊",
    "𝐓𝐔𝐉𝐇𝐄 𝐃𝐄𝐊𝐇 𝐊𝐄 𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐁𝐀𝐇𝐄𝐍 𝐏𝐄 𝐓𝐀𝐑𝐀𝐒 𝐀𝐓𝐀 𝐇𝐀𝐈 𝐌𝐔𝐉𝐇𝐄 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄𝐄𝐄𝐄 👿💥🤩🔥",
    "𝐒𝐔𝐍 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐉𝐘𝐀𝐃𝐀 𝐍𝐀 𝐔𝐂𝐇𝐀𝐋 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐄𝐍𝐆𝐄 𝐄𝐊 𝐌𝐈𝐍 𝐌𝐄𝐈 ✅🤣🔥🤩",
    "𝐀𝐏𝐍𝐈 𝐀𝐌𝐌𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇𝐍𝐀 𝐔𝐒𝐊𝐎 𝐔𝐒 𝐊𝐀𝐀𝐋𝐈 𝐑𝐀𝐀𝐓 𝐌𝐄𝐈 𝐊𝐀𝐔𝐍 𝐂𝐇𝐎𝐃𝐍𝐄𝐄 𝐀𝐘𝐀 𝐓𝐇𝐀𝐀𝐀! 𝐓𝐄𝐑𝐄 𝐈𝐒 𝐏𝐀𝐏𝐀 𝐊𝐀 𝐍𝐀𝐀𝐌 𝐋𝐄𝐆𝐈 😂👿😳",
    "𝐓𝐎𝐇𝐀𝐑 𝐁𝐀𝐇𝐈𝐍 𝐂𝐇𝐎𝐃𝐔 𝐁𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐖𝐃𝐄 𝐔𝐒𝐌𝐄 𝐌𝐈𝐓𝐓𝐈 𝐃𝐀𝐋 𝐊𝐄 𝐂𝐄𝐌𝐄𝐍𝐓 𝐒𝐄 𝐁𝐇𝐀𝐑 𝐃𝐔 🏠🤢🤩💥",
    "𝐓𝐔𝐉𝐇𝐄 𝐀𝐁 𝐓𝐀𝐊 𝐍𝐀𝐇𝐈 𝐒𝐌𝐉𝐇 𝐀𝐘𝐀 𝐊𝐈 𝐌𝐀𝐈 𝐇𝐈 𝐇𝐔 𝐓𝐔𝐉𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐊𝐀𝐑𝐍𝐄 𝐖𝐀𝐋𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄𝐄 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄𝐄𝐄𝐄 🤩👊👤😍",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐃𝐀𝐋 𝐊𝐄 𝐋𝐎𝐅𝐈 𝐁𝐀𝐉𝐀𝐔𝐍𝐆𝐀 𝐃𝐈𝐍 𝐁𝐇𝐀𝐑 😍🎶🎶💥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐍𝐀𝐘𝐀 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐀 𝐊𝐇𝐎𝐋𝐔𝐍𝐆𝐀 𝐂𝐇𝐈𝐍𝐓𝐀 𝐌𝐀𝐓 𝐊𝐀𝐑 👊🤣🤣😳",
    "𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐇𝐔 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐄 𝐏𝐄 𝐂𝐇𝐔𝐃𝐖𝐀 𝐊𝐄 𝐔𝐒 𝐏𝐀𝐈𝐒𝐄 𝐊𝐈 𝐃𝐀𝐀𝐑𝐔 𝐏𝐄𝐄𝐓𝐀 𝐇𝐔 🍷🤩🔥",
    "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐀𝐏𝐍𝐀 𝐁𝐀𝐃𝐀 𝐒𝐀 𝐋𝐎𝐃𝐀 𝐆𝐇𝐔𝐒𝐒𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐊𝐀𝐋𝐋𝐀𝐀𝐏 𝐊𝐄 𝐌𝐀𝐑 𝐉𝐀𝐘𝐄𝐆𝐈 🤩😳😳🔥",
    "𝐓𝐎𝐇𝐀𝐑 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐏𝐔𝐑𝐈 𝐊𝐈 𝐏𝐔𝐑𝐈 𝐊𝐈𝐍𝐆𝐅𝐈𝐒𝐇𝐄𝐑 𝐊𝐈 𝐁𝐎𝐓𝐓𝐋𝐄 𝐃𝐀𝐋 𝐊𝐄 𝐓𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐀𝐍𝐃𝐄𝐑 𝐇𝐈 😱😂🤩",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐊𝐈 𝐒𝐀𝐏𝐍𝐄 𝐌𝐄𝐈 𝐁𝐇𝐈 𝐌𝐄𝐑𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐘𝐀𝐀𝐃 𝐊𝐀𝐑𝐄𝐆𝐈 𝐑𝐀𝐍𝐃𝐈 🥳😍👊💥",
    "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐀𝐔𝐑 𝐁𝐀𝐇𝐄𝐍 𝐊𝐎 𝐃𝐀𝐔𝐃𝐀 𝐃𝐀𝐔𝐃𝐀 𝐍𝐄 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐔𝐍𝐊𝐄 𝐍𝐎 𝐁𝐎𝐋𝐍𝐄 𝐏𝐄 𝐁𝐇𝐈 𝐋𝐀𝐍𝐃 𝐆𝐇𝐔𝐒𝐀 𝐃𝐔𝐍𝐆𝐀 𝐀𝐍𝐃𝐄𝐑 𝐓𝐀𝐊 😎😎🤣🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐎 𝐎𝐍𝐋𝐈𝐍𝐄 𝐎𝐋𝐗 𝐏𝐄 𝐁𝐄𝐂𝐇𝐔𝐍𝐆𝐀 𝐀𝐔𝐑 𝐏𝐀𝐈𝐒𝐄 𝐒𝐄 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐊𝐎𝐓𝐇𝐀 𝐊𝐇𝐎𝐋 𝐃𝐔𝐍𝐆𝐀 😎🤩😝😍",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐀 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐊𝐈 𝐓𝐔 𝐂𝐀𝐇 𝐊𝐄 𝐁𝐇𝐈 𝐖𝐎 𝐌𝐀𝐒𝐓 𝐂𝐇𝐔𝐃𝐀𝐈 𝐒𝐄 𝐃𝐔𝐑 𝐍𝐇𝐈 𝐉𝐀 𝐏𝐀𝐘𝐄𝐆𝐀𝐀 😏😏🤩😍",
    "𝐒𝐔𝐍 𝐁𝐄 𝐑𝐀𝐍𝐃𝐈 𝐊𝐈 𝐀𝐔𝐋𝐀𝐀𝐃 𝐓𝐔 𝐀𝐏𝐍𝐈 𝐁𝐀𝐇𝐄𝐍 𝐒𝐄 𝐒𝐄𝐄𝐊𝐇 𝐊𝐔𝐂𝐇 𝐊𝐀𝐈𝐒𝐄 𝐆𝐀𝐀𝐍𝐃 𝐌𝐀𝐑𝐖𝐀𝐓𝐄 𝐇𝐀𝐈😏🤬🔥💥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐘𝐀𝐀𝐑 𝐇𝐔 𝐌𝐄𝐈 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐏𝐘𝐀𝐀𝐑 𝐇𝐔 𝐌𝐄𝐈 𝐀𝐉𝐀 𝐌𝐄𝐑𝐀 𝐋𝐀𝐍𝐃 𝐂𝐇𝐎𝐎𝐒 𝐋𝐄 🤩🤣💥",
    "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐋𝐀𝐆𝐀𝐀𝐔𝐍𝐆𝐀 𝐒𝐀𝐒𝐓𝐄 𝐒𝐏𝐀𝐌 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐒𝐀𝐑𝐈𝐘𝐀 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐔𝐒𝐈 𝐒𝐀𝐑𝐈𝐘𝐄 𝐏𝐑 𝐓𝐀𝐍𝐆 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐇𝐎𝐍𝐆𝐄 😱😱",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 ✋ 𝐇𝐀𝐓𝐓𝐇 𝐃𝐀𝐋𝐊𝐄 👶 𝐁𝐀𝐂𝐂𝐇𝐄 𝐍𝐈𝐊𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 😍",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐊𝐄𝐋𝐄 𝐊𝐄 𝐂𝐇𝐈𝐋𝐊𝐄 🤤🤤",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐔𝐓𝐋𝐈 𝐁𝐎𝐌𝐁 𝐅𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐉𝐇𝐀𝐀𝐓𝐄 𝐉𝐀𝐋 𝐊𝐄 𝐊𝐇𝐀𝐀𝐊 𝐇𝐎 𝐉𝐀𝐘𝐄𝐆𝐈💣💋",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐇𝐎𝐑𝐋𝐈𝐂𝐊𝐒 𝐏𝐄𝐄𝐋𝐀𝐊𝐄 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😚",
    "𝐓𝐄𝐑𝐈 𝐈𝐓𝐄𝐌 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐋𝐔𝐍𝐃 𝐃𝐀𝐀𝐋𝐊𝐄,𝐓𝐄𝐑𝐄 𝐉𝐀𝐈𝐒𝐀 𝐄𝐊 𝐎𝐑 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😆🤤💋",
    "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐀𝐏𝐍𝐄 𝐋𝐔𝐍𝐃 𝐏𝐑 𝐈𝐓𝐍𝐀 𝐉𝐇𝐔𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐊𝐈 𝐉𝐇𝐔𝐋𝐓𝐄 𝐉𝐇𝐔𝐋𝐓𝐄 𝐇𝐈 𝐁𝐀𝐂𝐇𝐀 𝐏𝐀𝐈𝐃𝐀 𝐊𝐑 𝐃𝐄𝐆𝐈 💦💋",
    "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐒𝐀𝐃𝐀𝐊 𝐏𝐑 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 😂😆🤤",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐑 𝐏𝐈𝐋𝐋𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔 😼😂🤤",
    "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐍𝐄 𝐒𝐇𝐎𝐑 𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐑𝐀𝐍𝐃𝐈 𝐂𝐇𝐎𝐑 𝐇𝐄 💋💋💦",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 😂👻🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐃 𝐏𝐄𝐇𝐈 𝐌𝐔𝐓𝐇 𝐃𝐈𝐀 💦💦💦💦",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐀𝐀𝐆 𝐋𝐀𝐆𝐀𝐃𝐈𝐀 𝐌𝐄𝐑𝐀 𝐌𝐎𝐓𝐀 𝐋𝐔𝐍𝐃 𝐃𝐀𝐋𝐊𝐄 🔥🔥💦😆😆",
    "𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐂𝐇𝐀𝐋 𝐍𝐈𝐊𝐀𝐋",
    "𝐊𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐁𝐇𝐄𝐉 😆👻🤤",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎𝐓𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐏𝐔𝐑𝐀 𝐅𝐀𝐀𝐃 𝐃𝐈𝐀 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉 😆💦🤤",
    "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐄𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐓𝐎 𝐌𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐁𝐀𝐍𝐆𝐀𝐘𝐈 𝐀𝐁𝐁 𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐓𝐀 𝐅𝐈𝐑𝐒𝐄 ♥️💦😆😆😆😆",
    "𝐇𝐀𝐑𝐈 𝐇𝐀𝐑𝐈 𝐆𝐇𝐀𝐀𝐒 𝐌𝐄 𝐉𝐇𝐎𝐏𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 🤣🤣💋💦",
    "𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐄 𝐁𝐀𝐀𝐏 𝐊𝐎 𝐁𝐇𝐄𝐉 𝐓𝐄𝐑𝐀 𝐁𝐀𝐒𝐊𝐀 𝐍𝐇𝐈 𝐇𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐁𝐎𝐌𝐁 𝐃𝐀𝐋𝐊𝐄 𝐔𝐃𝐀 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐀𝐖𝐃𝐄",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐓𝐑𝐀𝐈𝐍 𝐌𝐄 𝐋𝐄𝐉𝐀𝐊𝐄 𝐓𝐎𝐏 𝐁𝐄𝐃 𝐏𝐄 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 🤣🤣💋💋",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐕𝐈𝐃𝐄𝐎 𝐁𝐀𝐍𝐀𝐊𝐄 𝐗𝐍𝐗𝐗.𝐂𝐎𝐌 𝐏𝐄 𝐍𝐄𝐄𝐋𝐀𝐌 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦💋",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐊𝐎 𝐏𝐎𝐑𝐍𝐇𝐔𝐁.𝐂𝐎𝐌 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 🤣💋💦",
    "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐄𝐊𝐎 𝐂𝐇𝐀𝐊𝐊𝐎 𝐒𝐄 𝐏𝐈𝐋𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 🤣🤣",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐅𝐀𝐀𝐃𝐊𝐄 𝐑𝐀𝐊𝐃𝐈𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐎𝐃𝐄 𝐉𝐀𝐀 𝐀𝐁𝐁 𝐒𝐈𝐋𝐖𝐀𝐋𝐄 👄👄",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐔𝐍𝐃 𝐊𝐀𝐀𝐋𝐀",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐋𝐄𝐓𝐈 𝐌𝐄𝐑𝐈 𝐋𝐔𝐍𝐃 𝐁𝐀𝐃𝐄 𝐌𝐀𝐒𝐓𝐈 𝐒𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐌𝐄𝐍𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐁𝐎𝐇𝐎𝐓 𝐒𝐀𝐒𝐓𝐄 𝐒𝐄",
    "𝐁𝐄𝐓𝐄 𝐓𝐔 𝐁𝐀𝐀𝐏 𝐒𝐄 𝐋𝐄𝐆𝐀 𝐏𝐀𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄 𝐍𝐀𝐍𝐆𝐀 💦💋",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐇 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐀𝐆𝐋𝐈 𝐁𝐀𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐓 𝐎𝐑 𝐌𝐄𝐑𝐄 𝐌𝐎𝐓𝐄 𝐋𝐔𝐍𝐃 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑",
    "𝐂𝐇𝐀𝐋 𝐁𝐄𝐓𝐀 𝐓𝐔𝐉𝐇𝐄 𝐌𝐀𝐀𝐅 𝐊𝐈𝐀 🤣 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉",
    "𝐒𝐇𝐀𝐑𝐀𝐌 𝐊𝐀𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐊𝐈𝐓𝐍𝐀 𝐆𝐀𝐀𝐋𝐈𝐀 𝐒𝐔𝐍𝐖𝐀𝐘𝐄𝐆𝐀 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐔𝐏𝐄𝐑",
    "𝐀𝐁𝐄 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐀𝐔𝐊𝐀𝐓 𝐍𝐇𝐈 𝐇𝐄𝐓𝐎 𝐀𝐏𝐍𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑 𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀",
    "𝐊𝐈𝐃𝐙 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐓𝐄𝐑𝐑 𝐋𝐈𝐘𝐄 𝐁𝐇𝐀𝐈 𝐃𝐄𝐃𝐈𝐘𝐀",
    "𝐉𝐔𝐍𝐆𝐋𝐄 𝐌𝐄 𝐍𝐀𝐂𝐇𝐓𝐀 𝐇𝐄 𝐌𝐎𝐑𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐃𝐄𝐊𝐊𝐄 𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 🤣🤣💦💋",
    "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐌𝐄 𝐑𝐄𝐇𝐓𝐀 𝐇𝐄 𝐒𝐀𝐍𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐎𝐑 𝐁𝐀𝐍𝐀 𝐃𝐈𝐀 𝐑𝐀𝐍𝐃 🤤🤣",
    "𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐌𝐔𝐉𝐇𝐊𝐎 𝐏𝐀𝐏𝐀 𝐊𝐘𝐎𝐔𝐍𝐊𝐈 𝐌𝐄𝐍𝐄 𝐁𝐀𝐍𝐀𝐃𝐈𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐏𝐑𝐄𝐆𝐍𝐄𝐍𝐓 🤣🤣",
    "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐒𝐔𝐀𝐑 𝐊𝐀 𝐋𝐎𝐔𝐃𝐀 𝐎𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐎𝐃𝐀",
    "𝐂𝐇𝐀𝐋 𝐂𝐇𝐀𝐋 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐂𝐇𝐈𝐘𝐀 𝐃𝐈𝐊𝐀",
    "𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐈𝐀 𝐍𝐀𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄",
    "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐇𝐄 𝐁𝐀𝐃𝐈 𝐒𝐄𝐗𝐘 𝐔𝐒𝐊𝐎 𝐏𝐈𝐋𝐀𝐊𝐄 𝐂𝐇𝐎𝐎𝐃𝐄𝐍𝐆𝐄 𝐏𝐄𝐏𝐒𝐈",
    "𝟐 𝐑𝐔𝐏𝐀𝐘 𝐊𝐈 𝐏𝐄𝐏𝐒𝐈 𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐒𝐀𝐁𝐒𝐄 𝐒𝐄𝐗𝐘 💋💦",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐄𝐄𝐌𝐒 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦🤣",
    "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐔𝐓𝐇𝐊𝐄 𝐅𝐀𝐑𝐀𝐑 𝐇𝐎𝐉𝐀𝐕𝐔𝐍𝐆𝐀 𝐇𝐔𝐈 𝐇𝐔𝐈 𝐇𝐔𝐈",
    "𝐒𝐏𝐄𝐄𝐃 𝐋𝐀𝐀𝐀 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💋💦🤣",
    "𝐀𝐑𝐄 𝐑𝐄 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐊𝐘𝐎𝐔𝐍 𝐒𝐏𝐄𝐄𝐃 𝐏𝐀𝐊𝐀𝐃 𝐍𝐀 𝐏𝐀𝐀𝐀 𝐑𝐀𝐇𝐀 𝐀𝐏𝐍𝐄 𝐁𝐀𝐀𝐏 𝐊𝐀 𝐇𝐀𝐇𝐀𝐇🤣🤣",
    "𝐒𝐔𝐍 𝐒𝐔𝐍 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐉𝐇𝐀𝐍𝐓𝐎 𝐊𝐄 𝐒𝐎𝐔𝐃𝐀𝐆𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐍𝐔𝐃𝐄𝐒 𝐁𝐇𝐄𝐉",
    "𝐀𝐁𝐄 𝐒𝐔𝐍 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐅𝐀𝐀𝐃 𝐃𝐔𝐍𝐆𝐀",
    "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐊𝐇𝐔𝐋𝐄 𝐁𝐀𝐉𝐀𝐑 𝐌𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 🤣🤣💋",
    "Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..",
    "तेरी छोटी बहन साली कुतिया की चिकनी चिकनी बिना बाल वाली चूत के चिथड़े उड़ा डालूंगा अपने 9 इंच लंबे लंड से , समझा बेटीचोद साले बहन के लौड़े** \n\nतेरा बाप हूं मैं मादरचोद साले gandu , तू मेरी नाजायज औलाद है , जा जाके पूछ अपनी मम्मी साली रंडी से \n\nतेरी अप्पी बता रही थी कि तू बहुत बड़ा मादर चोद है, तूने ही अपनी अम्मी को चोद कर अपनी अप्पी पैदा की, और तू बहुत बड़ा गांडू भी है, कितने रेट है तेरे गाड़ मरवाने के ??\nतेरी मां की चूत को पिकाचू और ग्लेडिएटर्स हमेशा पेलते हैं।\nऔर ये भी बता कि गाड़ मरवाता है, कंडोम लगा के या बिना कण्डोम के ? तेल लेकर तू आएगा या मैं ही जापानी तेल लेकर आउ ?",
    "Teri ammy ke sath mai role play karunga🤣🤣🤣🤣🤣🤣usko malik ki wife banaunga aur khud driver banke pelunga usko!",
    "TERI MAA KI GAAAAND ME DANDAA DAAL KE DANDDA TODD DUNGAA MADARCHOD BAAP HU TERA BEHEN KE LUNDDD",
    "Phool murjhate achhe nahi lagte aap land khujate acche nahi lagte yehi umar hai chodne ki yaaro aap bathroom mein hilaate acche nahi lagte.",
    "Teri behn ko bolunga ki mere liye paani lao aur jb wo paani lene ke liye jhukegi tbi peeche se utha ke pel dunga",
    "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
    "Teri maa ki gaand mein abhi bhar bhar ke gaali deta hun madarchod bhosdike ruk teri maa ka bhosda randi ka pilla madarchod chus le mera loda bhosdike",
    "Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.",
    "Hey mere bete kaise ho beta tum\nUss raat jab maine teri maa choda tha jiske 9 mahine baad tum paida hue bhot maza aaya tha mujhe aur teri maa ko bhi!!",
    "Teri maa ki gaand mein abhi bhar bhar ke gaali deta hun madarchod bhosdike ruk teri maa ka bhosda randi ka pilla madarchod chus le mera loda bhosdike",
    "TERIIIIIIII MAAAAAAAAAA KI CHUTTTTT MEEEEEEEEE GHODEEEE KA LUNDDDDDDD MADARCHODDDDDDD GASTI KE BAXHEEEEE",
    "TERI MAA KA MARS PE KOTHA KHULWAAUNGA 🔥😂",
    "RANDI KE PILLE",
    "TERIIIII MAAA KO BHEJJJ",
    "TERAA BAAAAP HU",
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA",
    "Teri maa KO SARAK PE LETAA DUNGA",
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA",
    "Teri maa KI CHUT MÉ KAALI MITCH",
    "TERI MAA SASTI RANDI HAI",
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD",
    "TERI MAAA RANDI HAI",
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD",
    "TERI MAA KAAA BHOSDAA",
    "TERI MAA KI CHUT ME LAPTOP",
    "Teri maa RANDI HAI",
    "TERI MAA KO BISTAR PE LETAAKE CHODUNGA",
    "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD",
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA",
    "TERI MAA KE GAND ME DETOL DAAL DUNGA",
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD",
    "TERI MAA KO SARAK PE LETAAA DUNGAAA",
    "TERI MAA KAA BHOSDA",
    "MERAAA LUND PAKAD LE MADARCHOD",
    "CHUP TERI MAA AKAA BHOSDAA",
    "TERIII MAA CHUF GEYII KYAAA LAWDEEE",
    "G4ND😈 M3 TERI ᏞᎾhᎬ🥒🥒  KI ᏒᎾᎠ D4LDUNGA😸😸bᎥᏞᏞᎥ 😺 bᎪᏁᎪ  K3 CH0DUNG4💦💦👅👅 T3R ᎪmmᎽ  K0👻👻ᏆᎬᏃᎪb😍😍  ᎠᎪᎪᏞ  ᎠuᏁᎶᎪ T3R1👄B3HN K3😜😜😜 B00R 👙👙MEM4D3RCH0D🙈🙈JH4NT3🖕 ᏁᎾᏟhᏞuᏁᎶᎪ🥳🥳  ᏆᎬᎬ1 bᎬhᏁ  K1🍌🍌SU4R K1 😈ᏁᎪsᎪᏞ Ꮮ0ᎳᎠu 🙈T3R1 ᎪmmᎽ😺😺😺  K0 F4NS1 LAGA DUNG4😹😹💦💦 G44ND 💣ME TER1 AC1D🍆🍆 D44LDUNG4🍒ThᎪᏁᎠᎬ 😹 ᏢᎪᎪᏁᎥ SE 👙ᏁᎬhᏞᎪ K3 CH0DUNG4 🥳🥳TER1 CHHOT1💦💦 B3HN KO😹TATT1💩💩 KRDUNG4 TER1  Ꮆf  KE😺😺 muh  ᏢᎬ 👅👅😈",
    "MADARCHOODOO.••>___βħΔG βΣτΔ βħΔG τΣRΔΔΔ βΔPPP ΔΥΔΔ___<•••🔥ΔΨUSH HΣRΣ🔥RυKKKK RυKK βΣτΔΔ βHΔGGG KΔHΔ RΔHΔΔ HΔII ΔβHI τΟ τΣRI мΔΔ ζHυδΣGII RυKK☜☜☜мΔτLΔββ βΔβΥ мΔRVΔJΣΣΣ мΔПΣGIII👅👅👅👅>>>>◑︿◐JHΔПτ βHΔRR KI ΔυKΔτ  ПΔHI τΣRI ΔυR βΔPPP ςΣ LΔδΣGΔΔΔ◑︿◐<<<<<τΣRI βΣHΣП KI GΔПδ мΣ LΟHΣ KΔ RΟδδ δΔL δυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀▄τΣRI мΔΔ KI GΔПδδ мΣ βΣΔR KI βΟττLΣ δΔL KΣ FΟδδ δυПGΔ🍾🍾🍾________βHΔGGG δΔRLIПG βHΔGGG___GΔПδδ βΔζζHΔ KΣΣ βHΔGGGG____βΔP ΔΥΔ τΣRΔ 😎ΔΨUSH HΣRΣ😎>>>>>◑︿◐JHΔПτ βHΔRR KI ΔυKΔτ  ПΔHI τΣRI ΔυR βΔPPP ςΣ LΔδΣGΔΔΔ◑︿◐<<<<<τΣRI βΣHΣП KI GΔПδ мΣ LΟHΣ KΔ RΟδδ δΔL δυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀▄ΨΩUR ҒΔTHΣR #Pika_Pika_Pikachuuu HΣRΣ😎😎",
    "MADARCHODD😁-):-P:-\:'(:3:'(:'((^-)(^-):3:3:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/ BHEN KE LODE APNE BAAP KO🤥🤥 B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)B-)(^o^)(^o^)GAALI DEGA RANDI WALE 🤒🤒🤒(^o^)(^o^)(^o^)(^o^)(^o^)APNI MA SE PHUCH KI TERI MAAA NE MERI MUTH KAISE MARI THI SALE BHOT BAD TARIKE SE TERI MAA KI GHAND MARI  THI😂😂😂😂 -/:-/:-/:-/:-/:-/:-/:-/:-/:-/:B-)B-)B-)B-)B-)B-)B-)TERI MAA KO LOCAL CONDOM SE CHODA 🌎🌎🌎🌎🌎🌎HA TO GHAND KE ANDAR CONDOM BLAST HOGYA OR BBHADWE TU LODA PAKAD KE BHAR AAGYA BHOSDIKE MADARCHODB-):-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/:-/ CHALL ABB NIKKL BBHAADWEE😒😒",
    "Uss raat bada Maza aaya Jab glคdiatør͢͢͢𝓼 Teri maa ke upar aur teri maa glคdiatør͢͢͢𝓼 ke neeche\n\nOh yeah!! Oh yeah!!",
    "Teri Maa ki chut mein diya Gladiators ne moot!!",
    "Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain… ",
    "MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩",
    "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫",
    "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣",
    "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA",
    "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT",
    "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙",
    "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍",
    "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍",
    "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE",
    "TERI VAHEEN DHANDHE VAALI 😋😛",
    "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI",
    "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚",
    "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱",
    "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩",
    "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈",
    "TERA PEHLA BAAP HU MADARCHOD ",
    "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹",
    "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ",
    "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ",
    "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭",
    "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬",
    "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 ",
    "TERI MAA KI CHUT MEI BATTERY LAGA KE POWERBANK BANA DUNGA 🔋 🔥🤩",
    "TERI MAA KI CHUT MEI C++ STRING ENCRYPTION LAGA DUNGA BAHTI HUYI CHUT RUK JAYEGIIII😈🔥😍",
    "TERI MAA KE GAAND MEI JHAADU DAL KE MOR 🦚 BANA DUNGAA 🤩🥵😱",
    "TERI CHUT KI CHUT MEI SHOULDERING KAR DUNGAA HILATE HUYE BHI DARD HOGAAA😱🤮👺",
    "TERI MAA KO REDI PE BAITHAL KE USSE USKI CHUT BILWAUNGAA 💰 😵🤩",
    "BHOSDIKE TERI MAA KI CHUT MEI 4 HOLE HAI UNME MSEAL LAGA BAHUT BAHETI HAI BHOFDIKE👊🤮🤢🤢",
    "TERI BAHEN KI CHUT MEI BARGAD KA PED UGA DUNGAA CORONA MEI SAB OXYGEN LEKAR JAYENGE🤢🤩🥳",
    "TERI MAA KI CHUT MEI SUDO LAGA KE BIGSPAM LAGA KE 9999 FUCK LAGAA DU 🤩🥳🔥",
    "TERI VAHEN KE BHOSDIKE MEI BESAN KE LADDU BHAR DUNGA🤩🥳🔥😈",
    "TERI MAA KI CHUT KHOD KE USME CYLINDER ⛽️ FIT KARKE USMEE DAL MAKHANI BANAUNGAAA🤩👊🔥",
    "TERI MAA KI CHUT MEI SHEESHA DAL DUNGAAA AUR CHAURAHE PE TAANG DUNGA BHOSDIKE😈😱🤩",
    "TERI MAA KI CHUT MEI CREDIT CARD DAL KE AGE SE 500 KE KAARE KAARE NOTE NIKALUNGAA BHOSDIKE💰💰🤩",
    "TERI MAA KE SATH SUAR KA SEX KARWA DUNGAA EK SATH 6-6 BACHE DEGI💰🔥😱",
    "TERI BAHEN KI CHUT MEI APPLE KA 18W WALA CHARGER 🔥🤩",
    "TERI BAHEN KI GAAND MEI ONEPLUS KA WRAP CHARGER 30W HIGH POWER 💥😂😎",
    "TERI BAHEN KI CHUT KO AMAZON SE ORDER KARUNGA 10 rs MEI AUR FLIPKART PE 20 RS MEI BECH DUNGA🤮👿😈🤖",
    "TERI MAA KI BADI BHUND ME ZOMATO DAL KE SUBWAY KA BFF VEG SUB COMBO [15cm , 16 inches ] ORDER COD KRVAUNGA OR TERI MAA JAB DILIVERY DENE AYEGI TAB USPE JAADU KRUNGA OR FIR 9 MONTH BAAD VO EK OR FREE DILIVERY DEGI🙀👍🥳🔥",
    "TERI BHEN KI CHUT KAALI🙁🤣💥",
    "TERI MAA KI CHUT ME CHANGES COMMIT KRUGA FIR TERI BHEEN KI CHUT AUTOMATICALLY UPDATE HOJAAYEGI🤖🙏🤔",
    "TERI MAUSI KE BHOSDE MEI INDIAN RAILWAY 🚂💥😂",
    "TU TERI BAHEN TERA KHANDAN SAB BAHEN KE LAWDE RANDI HAI RANDI 🤢✅🔥",
    "TERI BAHEN KI CHUT MEI IONIC BOND BANA KE VIRGINITY LOOSE KARWA DUNGA USKI 📚 😎🤩",
    "TERI RANDI MAA SE PUCHNA BAAP KA NAAM BAHEN KE LODEEEEE 🤩🥳😳",
    "TU AUR TERI MAA DONO KI BHOSDE MEI METRO CHALWA DUNGA MADARXHOD 🚇🤩😱🥶",
    "TERI MAA KO ITNA CHODUNGA TERA BAAP BHI USKO PAHCHANANE SE MANA KAR DEGA😂👿🤩",
    "TERI BAHEN KE BHOSDE MEI HAIR DRYER CHALA DUNGAA💥🔥🔥",
    "TERI MAA KI CHUT MEI TELEGRAM KI SARI RANDIYON KA RANDI KHANA KHOL DUNGAA👿🤮😎",
    "TERI MAA KI CHUT ALEXA DAL KEE DJ BAJAUNGAAA 🎶 ⬆️🤩💥",
    "TERI MAA KE BHOSDE MEI GITHUB DAL KE APNA BOT HOST KARUNGAA 🤩👊👤😍",
    "TERI BAHEN KA VPS BANA KE 24*7 BASH CHUDAI COMMAND DE DUNGAA 🤩💥🔥🔥",
    "TERI MUMMY KI CHUT MEI TERE LAND KO DAL KE KAAT DUNGA MADARCHOD 🔪😂🔥",
    "SUN TERI MAA KA BHOSDA AUR TERI BAHEN KA BHI BHOSDA 👿😎👊",
    "TUJHE DEKH KE TERI RANDI BAHEN PE TARAS ATA HAI MUJHE BAHEN KE LODEEEE 👿💥🤩🔥",
    "SUN MADARCHOD JYADA NA UCHAL MAA CHOD DENGE EK MIN MEI ✅🤣🔥🤩",
    "APNI AMMA SE PUCHNA USKO US KAALI RAAT MEI KAUN CHODNEE AYA THAAA! TERE IS PAPA KA NAAM LEGI 😂👿😳",
    "TOHAR BAHIN CHODU BBAHEN KE LAWDE USME MITTI DAL KE CEMENT SE BHAR DU 🏠🤢🤩💥",
    "TUJHE AB TAK NAHI SMJH AYA KI MAI HI HU TUJHE PAIDA KARNE WALA BHOSDIKEE APNI MAA SE PUCH RANDI KE BACHEEEE 🤩👊👤😍",
    "TERI MAA KE BHOSDE MEI SPOTIFY DAL KE LOFI BAJAUNGA DIN BHAR 😍🎶🎶💥",
    "TERI MAA KA NAYA RANDI KHANA KHOLUNGA CHINTA MAT KAR 👊🤣🤣😳",
    "TERA BAAP HU BHOSDIKE TERI MAA KO RANDI KHANE PE CHUDWA KE US PAISE KI DAARU PEETA HU 🍷🤩🔥",
    "TERI BAHEN KI CHUT MEI APNA BADA SA LODA GHUSSA DUNGAA KALLAAP KE MAR JAYEGI 🤩😳😳🔥",
    "TOHAR MUMMY KI CHUT MEI PURI KI PURI KINGFISHER KI BOTTLE DAL KE TOD DUNGA ANDER HI 😱😂🤩",
    "TERI MAA KO ITNA CHODUNGA KI SAPNE MEI BHI MERI CHUDAI YAAD KAREGI RANDI 🥳😍👊💥",
    "TERI MUMMY AUR BAHEN KO DAUDA DAUDA NE CHODUNGA UNKE NO BOLNE PE BHI LAND GHUSA DUNGA ANDER TAK 😎😎🤣🔥",
    "TERI MUMMY KI CHUT KO ONLINE OLX PE BECHUNGA AUR PAISE SE TERI BAHEN KA KOTHA KHOL DUNGA 😎🤩😝😍",
    "TERI MAA KE BHOSDA ITNA CHODUNGA KI TU CAH KE BHI WO MAST CHUDAI SE DUR NHI JA PAYEGAA 😏😏🤩😍",
    "SUN BE RANDI KI AULAAD TU APNI BAHEN SE SEEKH KUCH KAISE GAAND MARWATE HAI😏🤬🔥💥",
    "TERI MAA KA YAAR HU MEI AUR TERI BAHEN KA PYAAR HU MEI AJA MERA LAND CHOOS LE 🤩🤣💥",
]

chutiya = []
glad = [1623434995]

TOXIC ="𒆜𓆩𝐓σχιc✘𝐁σу𓆪𒆜"
BOY =f"tg://user?id={1623434995}" 





@tbot.on(events.NewMessage(incoming=True))
async def _(event):
  if event.sender.id in chutiya:
    await event.reply(random.choice(replies))



@run_async
@sudo_plus
@typing_action
def replycurse(update: Update, context: CallbackContext) -> str:
	message = update.effective_message
	user = update.effective_user
	chat = update.effective_chat
	bot, args = context.bot, context.args
	user_id = extract_user(message, args)
	user_member = bot.getChat(user_id)
	rt = ""
	reply = check_user_id(user_id, bot)
	if reply:
		message.reply_text(reply)
		return ""
	if user_id in glad:
		message.reply_text("I can't betray my Piro Owner")
		return ""
	if user_id in DEV_USERS:
		message.reply_text("This guy is a dev user!!")
		return ""
	if user_id in SUDO_USERS:
		message.reply_text("This guy is a Sudo user!!")
		return ""
	chutiya.append(user_id)
	update.effective_message.reply_text(
		rt
		+ "\nSuccessfully Started reply and curse on {} !!".format(
			user_member.first_name
		)
	)




@sudo_plus
@typing_action
@gladiator(pattern="^/curse(?: |$)(.*)")
async def gladiators(event):
	if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
		Pika = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
		xd = await event.get_reply_message()
		if len(Pika) == 2:
			message = str(Pika[1])
			print(message)
			msg = await event.client.get_entity(message)
			usid = msg.id
			name = msg.first_name
			mention = f"[{name}](tg://user?id={usid})"
			if usid in glad:
				await event.reply("I can't betray my Piro Owner")
				return ""
			if usid in DEV_USERS:
				await event.reply("This guy is a dev user!!")
				return ""
			if usid in SUDO_USERS:
				await event.reply("This guy is a Sudo user!!")
				return
			rng = int(Pika[0])
			for i in range(rng):
				verse = random.choice(curses)
				text_message = f"{mention} {verse}"
				await event.client.send_message(event.chat, text_message)
				await asyncio.sleep(2)
		elif event.reply_to_msg_id:
			msg = await event.get_reply_message()
			stupid = await event.client.get_entity(msg.sender_id)
			usid = stupid.id
			name = stupid.first_name
			mention = f"[{name}](tg://user?id={usid})"
			if usid in glad:
				await event.reply("I can't betray my Piro Owner [{TOXIC}]({BOY})")
				return
			if usid in DEV_USERS:
				await event.reply("This guy is a dev user!!")
				return
			if usid in SUDO_USERS:
				await event.reply("This guy is a Sudo user!!")
				return
			rng = int(Pika[0])
			for i in range(rng):
				verse = random.choice(raid)
				text_message = f"{mention} {verse}"
				await event.client.send_message(event.chat, text_message)
				await asyncio.sleep(2)




@sudo_plus
@typing_action
@gladiator(pattern="^/ucurse(?: |$)(.*)")
async def gladiators(event):
	if event.sender_id in SUDO_USERS or event.sender_id in DEV_USERS:
		xd = await event.get_reply_message()
		Pika = ("".join(event.text.split(maxsplit=1)[1:])).split(" ")
		if len(Pika) == 1:
			message = Pika[0]
			a = 0
			print(message)
			msg = await event.client.get_entity(message)
			usid = msg.id
			name = msg.first_name
			mention = f"[{name}](tg://user?id={usid})"
			if usid in glad:
				await event.reply("I can't betray my Piro Owner")
				return ""
			if usid in DEV_USERS:
				await event.reply("This guy is a dev user!!")
				return ""
			if usid in SUDO_USERS:
				await event.reply("This guy is a Sudo user!!")
				return
			while a != "x":
				verse = random.choice(curses)
				text_message = f"{mention} {verse}"
				await event.client.send_message(event.chat, text_message)
				await asyncio.sleep(2)
		elif event.reply_to_msg_id:
			msg = await event.get_reply_message()
			a = 0
			stupid = await event.client.get_entity(msg.sender_id)
			usid = stupid.id
			name = stupid.first_name
			mention = f"[{name}](tg://user?id={usid})"
			if usid in glad:
				await event.reply("I can't betray @TeamGladiators's crew!!")
				return
			if usid in DEV_USERS:
				await event.reply("This guy is a dev user!!")
				return
			if usid in SUDO_USERS:
				await event.reply("This guy is a Sudo user!!")
				return
			while a != "x":
				verse = random.choice(raid)
				text_message = f"{mention} {verse}"
				await event.client.send_message(event.chat, text_message)
				await asyncio.sleep(2)




@run_async
@sudo_plus
def dreplycurse(update: Update, context: CallbackContext) -> str:
	message = update.effective_message
	user = update.effective_user
	chat = update.effective_chat
	bot, args = context.bot, context.args
	user_id = extract_user(message, args)
	user_member = bot.getChat(user_id)
	rt = ""
	reply = check_user_id(user_id, bot)
	if reply:
		message.reply_text(reply)
		return ""
	if user_id not in chutiya:
		message.reply_text("Never started reply and curse on this user!!")
		return ""
	chutiya.remove(user_id)
	update.effective_message.reply_text(
		rt
		+ "\nSuccessfully stopped reply and curse on {} !!".format(
			user_member.first_name
		)
	)


    



CURSE_HANDLER = CommandHandler(("replycurse"), replycurse)
DCURSE_HANDLER = CommandHandler(("dreplycurse"), dreplycurse)

dispatcher.add_handler(CURSE_HANDLER)
dispatcher.add_handler(DCURSE_HANDLER)

__mod_name__ = "curse"
__handlers__ = [
    CURSE_HANDLER,
    DCURSE_HANDLER,
    
]
