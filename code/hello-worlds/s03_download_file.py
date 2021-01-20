#s03_download_file.py
import boto3
import botocore

bucket_name = "gks3bucket1"
key = 'student.json'
target_file_name = 'local_student.json'
 
s3 = boto3.resource('s3')

s3.Bucket(bucket_name).download_file(key, target_file_name)
