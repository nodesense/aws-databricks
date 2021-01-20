#s04_upload_file.py
import logging
import boto3
  
# Upload the file
s3_client = boto3.client('s3')

response = s3_client.upload_file("local_student.json", "gks3bucket1", "local_student.json.bak")
 