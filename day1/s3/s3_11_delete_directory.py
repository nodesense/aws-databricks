import boto3


s3 = boto3.resource("s3")
s3_client = boto3.client("s3")

s3.Object("<<bucket-name>>", "test_directory2/").delete()