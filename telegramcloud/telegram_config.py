import configparser, os
from pathlib import Path

home = str(Path.home())
directory = (home + "/.telegram-cloud/")
file_name = "telegram-cloud-config.ini"
path = Path(directory + file_name)
config = configparser.ConfigParser()

def get_app_data():
    print("First of all you need an Telegram account and then you have to generate api_id and api_hash, to get it visit my.telegram.org") 
    api_id = input ("Enter api_id: ") 
    api_hash = input("Enter api_hash: ") 
    unique_name = input("And give me a unique name: ") 

    config[unique_name] = {}

    config[unique_name]['api_id'] = api_id
    config[unique_name]['api_hash'] = api_hash
    config[unique_name]['unique_name'] = unique_name
        
    Path(directory).mkdir(parents=True, exist_ok=True) 
    
    if os.path.isfile(path):
        with open(path, 'a') as configfile:
            config.write(configfile)
    else:
        with open(path, 'w') as configfile:
            config.write(configfile)


    return api_id, api_hash, unique_name


def fetch_app_data(unique_name):
    if (os.path.isfile(path) == False):
        print('Please first type tglogin command to log in your Telegram account')
        return
    else:
        config.read(path)
        if config.has_section(unique_name):
            api_id = config[unique_name]['api_id']
            api_hash = config[unique_name]['api_hash']
            name = config[unique_name]['unique_name']
            return (api_id, api_hash, name)
        else:
            print('Please first type tglogin command to log in your Telegram account')
            return
