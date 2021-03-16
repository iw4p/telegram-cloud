import os, sys
from shutil import move
from pathlib import Path
from telethon import (
    TelegramClient,
    events,
    utils
)

from ..utils.args import (
    tgutil_args
)
from ..utils.utils import (
    target_username_handler,
    session_retriever
)


args = tgutil_args()

# Get session name from CLI
unique_name = args.name

client = session_retriever(TelegramClient, unique_name)

async def main():

    # Get target username 
    username = args.username

    target_chat = await target_username_handler(client, username)
    text = " ".join(args.text)

    if len(text) == 0:
        print ("No text specified. Can't delete/change empty text")
        sys.exit (1)

    elif args.mode == 'edit':
        if args.text and username:
            await client.edit_message(username, args.text, args.newtext)

    elif args.mode == 'delete':
        if args.text and username:
            await client.delete_messages(username, args.text)

    # await client.send_message(entity=target_chat, message=message, silent=args.silent, parse_mode=parse_mode)


def cli():
    with client:
        client.loop.run_until_complete(main())
