import boto3

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def list_Folder(bucket):

    all_objects = s3.list_objects(Bucket=bucket)
    for object in all_objects['Contents']:
        print(object['Key'])


list_Folder("<<bucket-name>>")
