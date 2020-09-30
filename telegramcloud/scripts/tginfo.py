from telethon import TelegramClient, events, utils
from ..utils.utils import session_retriever
from ..utils.args import (
    tginfo_args
)
import json

args = tginfo_args()


# Get session name from CLI
unique_name = args.name

client = session_retriever(TelegramClient, unique_name)

async def main():

    async with client:
        dialogs = await client.get_dialogs()
        first = dialogs[1]
        print(first.title)
        # messages = await client.get_messages(args.username, limit=20)
        # for message in messages:
        #     # pdf_name = message.
        #     print(pdf_name)    

def cli():
    with client:
        client.loop.run_until_complete(main())


