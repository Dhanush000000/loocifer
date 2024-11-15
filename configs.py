# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25038048"))
    API_HASH = getenv("API_HASH", "09e892474901472e030fcdd53fb7384a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7979346594:AAFjYirmIPiMfEfT2WbHKrG53PLX6astM5E")
    SESSION_STRING = getenv("SESSION_STRING", "")
    SUDO = list(map(int, getenv("SUDO", "5798247275 5612704084").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Loocifar123:Loocifar123@cluster0.jkxxq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
