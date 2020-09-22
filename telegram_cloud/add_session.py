from telethon import TelegramClient
from .telegram_config import get_app_data

api_id, api_hash, unique_name = get_app_data()
client = TelegramClient(unique_name, api_id, api_hash)

async def main():
    await client.send_message('me', 'Hello from ' + unique_name)

with client:
    client.loop.run_until_complete(main())