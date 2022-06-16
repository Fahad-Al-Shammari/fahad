## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDFze1KQCSWEIEVn6vCufZKHwOBOktx3E06vz-PFFDmg8Y_D_zyO0l6VERbHOTw_8CcFQSNMP8rxvBuHf01XDutTLcGMUjTW4bSezbL0wRjDqqJl-898RdMVS-6vCJQ0CfBrMB1Hfok1dalOBHBL76STp9vsrdEeDieX57rJDtDUN0U6UjZbsHSi2tg6-yNZak3jXXAsSp7kJOaT8GKTjBmXZtXAfRhpo0AtrhI7aFytmHxbGt04dM6vF7FV-QpgXbp4L63rKiOW0d3mB7zTwxvGm_3viJbdNaRK-PnrLHi1C1r6CsUnxUI_UIM6D_i0_F3rIVPiYodjYubBaWIYPJIAAAAATFmNKYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5316487719:AAG9YzxM-c0Wb1V10cVKGxVW0ol7Mbyd5wg")
BOT_NAME = getenv("BOT_NAME", "𝐀𝐑𝐀𝐘")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Fahad")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FF7F2")
ALIVE_NAME = getenv("ALIVE_NAME", "Fahad")
BOT_USERNAME = getenv("BOT_USERNAME", "L_RRBOT")
OWNER_ID = getenv("OWNER_ID", "1514640887")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ARAY")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FF7F2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FF7F2")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1514640887").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
