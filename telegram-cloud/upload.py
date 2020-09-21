from telethon import TelegramClient
from telegram_config import fetch_app_data

api_id, api_hash, name = fetch_app_data()

client = TelegramClient(name, api_id, api_hash)

async def main():
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())