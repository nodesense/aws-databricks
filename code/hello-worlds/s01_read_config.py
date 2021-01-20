import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.aws/credentials"))

aws_profile="default" #Section [default]
access_id = config.get(aws_profile, "aws_access_key_id") 
access_key = config.get(aws_profile, "aws_secret_access_key") 

print(access_id)
print(access_key)


configConfig = configparser.ConfigParser()
configConfig.read(os.path.expanduser("~/.aws/config"))

region = configConfig.get(aws_profile, "region")
print(region)