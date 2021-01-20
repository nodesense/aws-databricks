

import boto3
import botocore

bucket_name = "<<bucket-name>>"
key = 'demo.txt'
file_name = 'demo.txt'

#bucket_name = "akshayadatabricksdemo11234"
#file= "student.json"
#key = "student.json"

s3 = boto3.resource('s3')

try:
    s3.Bucket(bucket_name).download_file(key, file)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
