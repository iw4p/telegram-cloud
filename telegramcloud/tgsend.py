import os
from shutil import move
from pathlib import Path
from telethon import (
    TelegramClient,
    events,
    utils
)
from .telegram_config import (
    fetch_app_data,
    directory
)
from .utils.args import (
    tgsend_args
)
from .utils.utils import (
    target_username_handler,
    session_retriever
)


args = tgsend_args()

# Get session name from CLI
unique_name = args.name
#username = args.username

client = session_retriever(TelegramClient, unique_name)


async def main():
    await client.send_message('me', 'tgsend first message')


def cli():
    with client:
        client.loop.run_until_complete(main())
