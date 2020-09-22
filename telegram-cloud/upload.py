from telethon import TelegramClient, events, utils

import argparse
from telegram_config import fetch_app_data

parser = argparse.ArgumentParser()

# Read arguments from the command line
parser.add_argument("--name", "-n", help="That unique name you've set at the first", required=True)
parser.add_argument("--path", "-p", help="Path of the file/files you want to upload")
parser.add_argument("--username", "-u", help="Set target username for sending file/files to her/him")
parser.add_argument("--file_id", "-f", help="Give me file_id and I'll send you the file")

args = parser.parse_args()

# Get session name from CLI
unique_name = args.name

# Get the session data to use TelegramClient
api_id, api_hash, name = fetch_app_data(unique_name)
client = TelegramClient(name, api_id, api_hash)

async def main():

    # Get username target 
    username = args.username

    # Convert and handle all types of username and chat id to target chat 
    if ('-' in username or '+' in username) and (username[1].isdigit() == True):
        target_chat = await client.get_entity(int(username))
    else:
        target_chat = await client.get_entity(username)

    # Send file to specific target_chat and retrieve the file_id
    if args.path and username and not args.file_id:
        message = await client.send_file(target_chat, file=args.path)
        await client.edit_message(target_chat, message.id, message.file.id)
        print(message.file.id)

    # Retrieve and download a file from its file_id from specific target_chat
    if args.file_id and args.path and username:
        breaker = False 
        async for message in client.iter_messages(entity=username, search=args.file_id):
            if breaker == False:
                await client.download_media(message, args.path)
                breaker = True
        

with client:
    client.loop.run_until_complete(main())
