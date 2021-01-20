import json

def print_message(name):
    return "Hello From {0}".format(name)
def lambda_handler(event, context):
    obj = json.loads(event['body'])
    print(obj['name'])
    return {

        'statusCode': 200,
        'body': json.dumps(print_message(obj['name']))
    }


#api:  curl -X POST -H 'Content-Type: application/json' -d '{"name": "akshaya"}'  https://<<API-Gateway>>/testApi