import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "20762333"))
    API_HASH = os.environ.get("API_HASH", "97bb560b7e50f706d2ae6e4bd7caed89")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6862953115:AAF-7MnyallqF65rckSoWY0t3xYqhsPb0IQ")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "664880413")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
