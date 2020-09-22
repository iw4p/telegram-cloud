import configparser, os

path = os.path.expanduser('~/.local/share/telegram-cloud-Config.ini')
config = configparser.ConfigParser()

def get_app_data():

    print("First of all you need an Telegram account and then you have to generate api_id and api_hash, to get it visit my.telegram.org") 
    api_id = input ("Enter api_id:") 
    api_hash = input("Enter api_hash:") 
    unique_name = input("And give me a unique name:") 

    config[unique_name] = {}

    config[unique_name]['api_id'] = api_id
    config[unique_name]['api_hash'] = api_hash
    config[unique_name]['unique_name'] = unique_name

    file_exists = os.path.isfile(path) 

    if file_exists:
        with open(path, 'a') as configfile:
            config.write(configfile)
    else:
        with open(path, 'w') as configfile:
            config.write(configfile)

    return api_id, api_hash, unique_name


def fetch_app_data(unique_name):

    if (os.path.isfile(path) == False):
        get_app_data()
    else:
        config.read(path)

        api_id = config[unique_name]['api_id']
        api_hash = config[unique_name]['api_hash']
        name = config[unique_name]['unique_name']

        return (api_id, api_hash, name)
