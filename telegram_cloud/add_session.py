from telethon import TelegramClient
from .telegram_config import get_app_data, directory
from shutil import move

api_id, api_hash, unique_name = get_app_data()
client = TelegramClient(unique_name, api_id, api_hash)

async def main():
    await client.send_message('me', 'Hello from ' + unique_name)


def cli():
    with client:
        client.loop.run_until_complete(main())
        move(unique_name + '.session', directory)