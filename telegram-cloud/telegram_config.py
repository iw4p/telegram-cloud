import configparser, os

path = os.path.expanduser('~/.local/share/telegram-cloud-Config.ini')
config = configparser.ConfigParser()

def get_app_data():

    print("First of all you need an Telegram account and then you have to generate api_id and api_hash, to get it visit my.telegram.org") 
    api_id = input ("Enter api_id:") 
    api_hash = input("Enter api_hash:") 
    name = input("And give me a name:") 

    config['APP'] = {}

    config['APP']['api_id'] = api_id
    config['APP']['api_hash'] = api_hash
    config['APP']['name'] = name

    with open(path, 'w') as configfile:
        config.write(configfile)


def fetch_app_data():

    if (os.path.isfile(path) == False):
        get_app_data()
    else:
        config.read(path)

        api_id = config['APP']['api_id']
        api_hash = config['APP']['api_hash']
        name = config['APP']['name']

        return (api_id, api_hash, name)
