from ..telegram_config import fetch_app_data, directory

async def target_username_handler(client, username):
    # Convert and handle all types of username and chat id to target chat 
    if ('-' in username or '+' in username) and (username[1].isdigit() == True):
        target_chat = await client.get_entity(int(username))
    else:
        target_chat = await client.get_entity(username)
    return target_chat

def session_retriever(TelegramClient, unique_name):
    # Get the session data to use TelegramClient
    if fetch_app_data(unique_name) == None:
        quit()
    else:
        api_id, api_hash, _ = fetch_app_data(unique_name)
    client_name = (directory + unique_name + '.session')
    client = TelegramClient(client_name, api_id, api_hash)
    return client