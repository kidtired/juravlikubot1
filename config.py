import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
admin_id = os.getenv("admin_id")
BOT_URL = os.getenv("BOT_URL")

URL_APPLES = os.getenv("URL_APPLES")
URL_PEAR = os.getenv("URL_PEAR")

print(BOT_TOKEN)