import boto3

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

s3.download_file('<<bucket-name>>', 'test_directory2/', 'test.csv')
