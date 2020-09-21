import configparser, os

path = os.path.expanduser('~/.local/share/telegram-cloud-Config.ini')

print("To use first of all you need an Telegram account and api_id/api_hash, to get it visit my.telegram.org") 
api_id = input ("Enter api_id:") 
api_hash = input("Enter api_hash:") 

config = configparser.ConfigParser()

config['APP'] = {}
data = config['APP']

data['api_id'] = api_id
data['api_hash'] = api_hash

with open(path, 'w') as configfile:
    config.write(configfile)

