
#(©)CodeXBotz
import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7164877275:AAENVvHUAGnLKnkhVqa3KOJkkCxTvV3POYc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26898723"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6b074d2c9ab42f363d22fa86284f3488")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002001799767"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6358771146"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://vippuniya29:YRjCh78euML5fqFg@vipstudios.kzpq3pu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot1")

"""
delay for message to delete after bot sends them to user. 
default delay is 60 secs you can change it by changing the minutes i mean if u want delay of 2 mins than change 1 to 2 ans so on.
"""
DELAY = "10 * 60"

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hey {mention} Welcome to our Movie and Webseries Provider Bot. Exclusively work for <a href='https://t.me/Vip_studios'>VIP Studios</a> !!\n\nExclusive Content, VIP Experience.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6358771146)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
