from telethon import TelegramClient, events, utils
from ..utils.utils import session_retriever
from ..utils.args import (
    tginfo_args
)
from telethon.tl.types import *

args = tginfo_args()


# Get session name from CLI
unique_name = args.name

client = session_retriever(TelegramClient, unique_name)

async def main():

    async with client:


        messages = await client.get_messages(args.username, filter=InputMessagesFilterEmpty)
        photos = await client.get_messages(args.username, filter=InputMessagesFilterPhotos)
        videos = await client.get_messages(args.username, filter=InputMessagesFilterVideo)
        photos_and_videos = await client.get_messages(args.username, filter=InputMessagesFilterPhotoVideo)
        documents = await client.get_messages(args.username, filter=InputMessagesFilterDocument)
        urls = await client.get_messages(args.username, filter=InputMessagesFilterUrl)
        gifs = await client.get_messages(args.username, filter=InputMessagesFilterGif)
        musics = await client.get_messages(args.username, filter=InputMessagesFilterVoice)
        voices = await client.get_messages(args.username, filter=InputMessagesFilterMusic)
        chat_photos = await client.get_messages(args.username, filter=InputMessagesFilterChatPhotos)
        round_voices = await client.get_messages(args.username, filter=InputMessagesFilterRoundVoice)
        round_videos = await client.get_messages(args.username, filter=InputMessagesFilterRoundVideo)
        geos = await client.get_messages(args.username, filter=InputMessagesFilterGeo)
        contacts = await client.get_messages(args.username, filter=InputMessagesFilterContacts)


        print("All Messages: " + str(messages.total))
        print("All Photos: " + str(photos.total))
        print("All Videos: " + str(videos.total))
        print("All Photos and videos: " + str(photos_and_videos.total))
        print("All Documents: " + str(documents.total))
        print("All Urls: " + str(urls.total))
        print("All Gifs: " + str(gifs.total))
        print("All Musics: " + str(musics.total))
        print("All Voices: " + str(voices.total))
        print("All Chat photos: " + str(chat_photos.total))
        print("All Round voices: " + str(round_voices.total))
        print("All Round videos: " + str(round_videos.total))
        print("All Geo locations: " + str(geos.total))
        print("All Contacts: " + str(contacts.total))
   

def cli():
    with client:
        client.loop.run_until_complete(main())


