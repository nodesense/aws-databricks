import os

def lambda_handler(event, context):
    text = "Welcome %s" % (event['name'])
    return text

#event :: {'name':'your_name'}