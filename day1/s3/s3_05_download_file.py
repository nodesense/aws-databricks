

import boto3
import botocore

bucket = "<<bucket-name>>"
key = 'demo.txt'
file_name = 'demo.txt'
s3 = boto3.resource('s3')

try:
    s3.Bucket(bucket).download_file(key, file_name)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
