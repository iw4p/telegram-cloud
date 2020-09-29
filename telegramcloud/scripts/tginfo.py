from telethon import TelegramClient, events, utils
from ..utils.utils import session_retriever
from ..utils.args import (
    tginfo_args
)
args = tginfo_args()


# Get session name from CLI
unique_name = args.name

client = session_retriever(TelegramClient, unique_name)

async def main():

    async with client:
        messages = await client.get_messages(args.username, limit=2)
        print("messages no: ",(messages))

def cli():
    with client:
        client.loop.run_until_complete(main())


