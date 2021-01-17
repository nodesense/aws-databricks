import boto3

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def create_Folder(bucket,folder_name):

    s3.put_object(Bucket=bucket, Key=(folder_name+'/'))


    all_objects = s3.list_objects(Bucket=bucket)
    for object in all_objects['Contents']:
        print(object['Key'])


create_Folder("<<bucket-name>>","test_directory8")
