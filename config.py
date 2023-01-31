import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6296490")) #optional
API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "5467311248"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6080251945:AAFPZ-5EA-GpbWG1KuPd0ET2J_ehDzQ1PUs")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001647004968")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBu1WDNirSFt2zhK2dhSC6-p2lYSd_wM4uv1vwgUWEliHrqbLBOdMKI0dEm0ZfuXOFFtCB9R1kQSrZSn1aqNiqG-3pD-vljRbJJ8HSYTIHoA-JP0FLJkBZMrmj4juRid2VUG6yaR7m7P_dxcMgCtzghZgeb_AWS8SleFnXFj-73P8Hnv0a2BfaBd9DsfyzaeXvG-QzQNhZGgl_Aceq3v_9sWhBegg10XmdLtmOwy3Wo4OgaCONDeZExE26Vxi40QlZEm0bFGK_3rbSAmogrNl_Sr8qPQA376HNV4sbL62u2wXBPSpRYL-w4E5W55Oi3IiNYk0JKxJHs62z_ZpHfiS_6QI=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
