import configparser, os

path = os.path.expanduser('~/.local/share/telegram-cloud-Config.ini')
config = configparser.ConfigParser()

def get_app_data():

    print("First of all you need an Telegram account and then you have to generate api_id and api_hash, to get it visit my.telegram.org") 
    api_id = input ("Enter api_id:") 
    api_hash = input("Enter api_hash:") 

    config['APP'] = {}

    data = config['APP']
    config['APP']['api_id'] = api_id
    config['APP']['api_hash'] = api_id
    # data['api_id'] = api_id
    # data['api_hash'] = api_hash

    with open(path, 'w') as configfile:
        config.write(configfile)


def fetch_app_data() -> tuple:

    config.read(path)

    api_id = config['APP']['api_id']
    api_hash = config['APP']['api_hash']

    return (api_id, api_hash)

# get_app_data()

# x = fetch_app_data()
# print(x)