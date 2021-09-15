import logging
import os
import sys
import time
import spamwatch
from datetime import datetime
import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient
from os import getenv

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", None)
    BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", None)
    BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", None)
    BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", None)
    BOT_TOKEN6 = os.environ.get("BOT_TOKEN6", None)
    BOT_TOKEN7 = os.environ.get("BOT_TOKEN7", None)
    BOT_TOKEN8 = os.environ.get("BOT_TOKEN8", None)
    BOT_TOKEN9 = os.environ.get("BOT_TOKEN9", None)
    BOT_TOKEN10 = os.environ.get("BOT_TOKEN10", None)
    BOT_TOKEN11 = os.environ.get("BOT_TOKEN11", None)
    BOT_TOKEN12 = os.environ.get("BOT_TOKEN12", None)
    BOT_TOKEN13 = os.environ.get("BOT_TOKEN13", None)
    BOT_TOKEN14 = os.environ.get("BOT_TOKEN14", None)
    BOT_TOKEN15 = os.environ.get("BOT_TOKEN15", None)
    BOT_TOKEN16 = os.environ.get("BOT_TOKEN16", None)
    BOT_TOKEN17 = os.environ.get("BOT_TOKEN17", None)
    BOT_TOKEN18 = os.environ.get("BOT_TOKEN18", None)
    BOT_TOKEN19 = os.environ.get("BOT_TOKEN19", None)
    BOT_TOKEN20 = os.environ.get("BOT_TOKEN20", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    LOGS = os.environ.get("LOGS", None)
    MASTER_NAME = os.environ.get("MASTER_NAME", None)

    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    BOT_ID = int(os.environ.get("BOT_ID", None))
    DB_URI = os.environ.get("DATABASE_URL")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    DONATION_LINK = os.environ.get("DONATION_LINK")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    Start_time = time.time()
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)


else:
    from spambot.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.LOGS
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
    MASTER_NAME = Config.MASTER_NAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")


    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    MONGO_DB_URI = Config.MONGO_DB_URI
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    BOT_ID = Config.BOT_ID
    VIRUS_API_KEY = Config.VIRUS_API_KEY
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL
    AI_API_KEY = Config.AI_API_KEY
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    INFOPIC = Config.INFOPIC
    REDIS_URL = Config.REDIS_URL

SUDO_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)




updater = tg.Updater(BOT_TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("jarv", API_ID, API_HASH)
pbot = Client("jarvpbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
DEV_USERS.append(1623434995)


# Load at end to ensure all prev variables have been set
from spambot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

Toxic = TelegramClient('Toxic', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

Toxic2 = TelegramClient('Toxic2', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

Toxic3 = TelegramClient('Toxic3', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

Toxic4 = TelegramClient('Toxic4', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

Toxic5 = TelegramClient('Toxic5', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

Toxic6 = TelegramClient('Toxic6', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

Toxic7 = TelegramClient('Toxic7', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

Toxic8 = TelegramClient('Toxic8', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

Toxic9 = TelegramClient('Toxic9', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

Toxic10 = TelegramClient('Toxic10', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10)

Toxic11 = TelegramClient('Toxic11', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

Toxic12 = TelegramClient('Toxic12', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

Toxic13 = TelegramClient('Toxic13', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

Toxic14 = TelegramClient('Toxic14', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

Toxic15 = TelegramClient('Toxic15', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

Toxic16 = TelegramClient('Toxic16', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

Toxic17 = TelegramClient('Toxic17', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

Toxic18 = TelegramClient('Toxic18', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

Toxic19 = TelegramClient('Toxic19', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

Toxic20 = TelegramClient('Toxic20', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10) 
