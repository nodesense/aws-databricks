import logging
import boto3
from botocore.exceptions import ClientError
s3_resource = boto3.resource('s3')

def delete_all_objects(bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})
    s3_resource.Bucket(bucket_name).delete()

delete_all_objects("<<bucket-name>>")

