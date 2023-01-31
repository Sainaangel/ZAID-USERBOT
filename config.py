import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6296490")) #optional
API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "844126468").split()))
OWNER_ID = int(getenv("OWNER_ID", "5467311248"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5609161013:AAHhzn3nULekbZADhjPBbLqDmwfu-dupzps")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/7e5b79d224638c0d1a38f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "⏤͟͞ ＦＬムＳＨ三[🇮🇳]")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001647004968")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 HALDER = getenv("HALDER", "!")
STRING_SESSION1 = getenv("STRING_SESSION1", "BABrY7BN9dbJQ748w_gU7jgarI3LD82o2sI6OlILL6uiL4wiP_ix5IiwbrkxPKiiwt1Ef3yFunNDwOvjV9t9eKZagtmIfDEYxUutM_CrqebpnbmJSlvJ1P7s2V5AoVQg2tWw3NyVNKVhAskGMUZwTBRo0jTvlJdIe7RW1MQ3rk-P4udB6ok-t3GQvrd9fv06NuNQYC-BlrBF1CgqtWvrZm8sEFRcROFU5VA3H18GgTFl5WcBgNo2Ro3DcnkiDS2Pfj5GiHS8bvwqktRad5PqnphscV5G_fGBSWMYBnJH9w4Ix_4eR6kg7XjcWhDhi6aeFw1dOUslyLEzd34nz2CKKivBAAAAAUXgjJAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
