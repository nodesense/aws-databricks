import os
import configparser

config = configparser.ConfigParser()

path = os.path.join(os.path.expanduser('~'), '.aws/credentials')
config.read(path)

print (config.sections()) 

ACCESS_KEY_ID = config.get('default', 'aws_access_key_id')
SECRET_ACCESS_KEY = config.get('default', 'aws_secret_access_key')

print (ACCESS_KEY_ID)
print (SECRET_ACCESS_KEY)

def get_access_key():
    return  ACCESS_KEY_ID

def get_access_secret(): 
    return SECRET_ACCESS_KEY