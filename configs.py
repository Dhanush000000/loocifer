# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25038048"))
    API_HASH = getenv("API_HASH", "09e892474901472e030fcdd53fb7384a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7662618595:AAGyMkpqf70ZttUx4D8vgXhXhqCQrmrIfx4")
    SESSION_STRING = getenv("SESSION_STRING", "")
    SUDO = list(map(int, getenv("SUDO", "5798247275").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
