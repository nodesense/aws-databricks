import json
import urllib.parse
import boto3

print('Loading function')


def lambda_handler(event, context):
    try:
        s3 = boto3.resource('s3', aws_access_key_id='<<key_id>>',
                            aws_secret_access_key='<<secret-access-key>>')
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

        print(bucket)

        print(key)
        content_object = s3.Object(bucket, key)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        print(json_content)

        print(event)
        desination_bucket = '<<dest-bucketname>>'
        key = "<<directoryname>>/test.json"
        


        return s3.Bucket(desination_bucket).put_object(Key=key, Body=str(json_content))
    except Exception as e:
        print(e)
        raise e