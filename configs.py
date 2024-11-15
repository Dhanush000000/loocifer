# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "8064569587:7632678174:AAE-ftnSuGwmoh1S1uROFBBLGliOD6UhW3g")
    SESSION_STRING = getenv("SESSION_STRING", "")
    SUDO = list(map(int, getenv("SUDO", "5798247275").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
