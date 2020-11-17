import argparse, os
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
    tgcloud_args
)
from .utils.utils import (
    target_username_handler,
    session_retriever
)

args = tgcloud_args()

# Get session name from CLI
unique_name = args.name

# Create client obj
client = session_retriever(TelegramClient, unique_name)


# Printing download progress
def download_callback(current, total):
    print('Downloaded', current, 'out of', total, 'bytes: {:.2%}'.format(current / total))

# Printing upload progress
def upload_callback(current, total):
    print('Uploaded', current, 'out of', total, 'bytes: {:.2%}'.format(current / total))

async def main():

    # Get target username 
    username = args.username

    target_chat = await target_username_handler(client, username)
    # Retrieve and download a file from its name or caption, from specific target_chat
    if args.mode == 'download':
        if args.caption and args.path and username:
            async for message in client.iter_messages(entity=username, search=args.caption):
                try:
                    await client.download_media(message, args.path, progress_callback=download_callback)
                except:
                    pass


    # Upload file to specific target_chat and retrieve the file_id
    elif args.mode == 'upload':

        if args.parse_mode == "text":
            parse_mode = None
        if args.parse_mode == "markdown":
            parse_mode = "md"
        if args.parse_mode == "html":
            parse_mode = "html"

        if args.path and username:
            try:
                message = await client.send_file(entity=target_chat, file=args.path, caption=args.caption, progress_callback=upload_callback, parse_mode=parse_mode)
                print("File id: {}".format(message.file.id))
            except:
                print("Something went wrong, make sure the directory path is valid.")

def cli():
    with client:
        client.loop.run_until_complete(main())


