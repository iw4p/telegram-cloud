import os, sys
from shutil import move
from pathlib import Path
from telethon import (
    TelegramClient,
    events,
    utils
)

from ..utils.args import (
    tgsend_args
)
from ..utils.utils import (
    target_username_handler,
    session_retriever
)


args = tgsend_args()

# Get session name from CLI
unique_name = args.name
#username = args.username

client = session_retriever(TelegramClient, unique_name)


async def main():

    # Get target username 
    username = args.username

    target_chat = await target_username_handler(client, username)
    message = " ".join(args.message)

    if args.stdin:
        message = sys.stdin.read()
        if len(message) == 0:
            sys.exit(1)

    if len(message) == 0:
        print ("No text specified. Can't send empty message")
        sys.exit (1)

    if args.parse_mode == "text":
        parse_mode = None
    if args.parse_mode == "markdown":
        parse_mode = "md"
    if args.parse_mode == "html":
        parse_mode = "html"

    await client.send_message(entity=target_chat, message=message, silent=args.silent, parse_mode=parse_mode)


def cli():
    with client:
        client.loop.run_until_complete(main())
