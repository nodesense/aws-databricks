import boto3
import pandas as pd

import json
import urllib.parse
def read_json():
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = '<<bucket-name>>'
    key = 'test_directory3/student.json'
    content_object = s3.Object(key, bucket)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print(json_content)

read_json()


