import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7962752252:AAFqyYfvMZz_mb-gTf216lXyle8wVFyeHbU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24732393"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ac0d702e4ec6b2d5c232cb5a7e0b7619")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1753958235"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vikasnagar221:Qwerty123@cluster0.xpoc4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "modmicksavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))






# Don't Remove Credit Tg - @Mod_Mick
# Ask Doubt on telegram @Mod_Mick