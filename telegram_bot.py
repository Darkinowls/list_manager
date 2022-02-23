import os

from dotenv import load_dotenv
from pyrogram import Client

LIST = 'list'
HI = 'hi'
JSON = 'json'
HEAD = 'head'
SLASH = '/'
BOT_NAME = 'Abobus'
SCROLL_EMOJI = '\U0001F4DC'

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

list_bot = Client(BOT_NAME, api_id=API_ID, api_hash=API_HASH,
                  bot_token=BOT_TOKEN)


def use_bot():
    from bot_methods.general import define_general_methods
    from bot_methods.header import define_header_methods
    from bot_methods.list import define_list_methods
    define_general_methods()
    define_header_methods()
    define_list_methods()


use_bot()
