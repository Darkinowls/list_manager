import os

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_KEY = os.getenv('BOT_KEY')


app = Client("Abobus", api_id=API_ID, api_hash=API_HASH,
             bot_token=BOT_KEY)

