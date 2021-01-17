import json
import urllib.parse
import boto3

print('Loading function')


def lambda_handler(event, context):

    # Get the object from the event and show its content type
    try:
        s3 = boto3.resource('s3', aws_access_key_id='<<key_id>>',
                          aws_secret_access_key='<<secrect access key>>')
        bucket = '<<bucketname>>'
        key = '<<directory_name>>/student.json'
        content_object = s3.Object(bucket, key)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)

        print(json_content)

        file_name = "<<directory_name>>/output.json"
        #lambda_path = "/tmp/" + file_name

        return s3.Bucket("<<bucketname-output>>").put_object(Key=file_name, Body=str(json_content))
    except Exception as e:
        print(e)
        #print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e



