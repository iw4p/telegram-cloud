from telethon import TelegramClient
from .telegram_config import get_app_data, directory
from shutil import move
from pathlib import Path

api_id, api_hash, unique_name = get_app_data()
client = TelegramClient(unique_name, api_id, api_hash)

async def main():
    await client.send_message('me', 'Hello, this text has been sent automatically from telegram-cloud (AKA tgcloud) for making sure you have logged in and session file created successfully. Github.com/iw4p/telegram-cloud')


def cli():
    with client:
        client.loop.run_until_complete(main())
        try:
            move(unique_name + '.session', Path(directory))
        except WindowsError:
            pass