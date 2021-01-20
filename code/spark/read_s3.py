

import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"

os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"



import findspark
findspark.init()

import util
import credentials

import pyspark

AWS_ACCESS_KEY = credentials.get_access_key()
AWS_SECRET_KEY =  credentials.get_access_secret()

  

 

conf = (
    pyspark.SparkConf()
        .setAppName('test')
        .setMaster('local[*]')
       .set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
.set('fs.s3a.access.key', AWS_ACCESS_KEY)
.set('fs.s3a.secret.key', AWS_SECRET_KEY)
.set("fs.s3a.awsAccessKeyId", AWS_ACCESS_KEY)
.set("fs.s3a.awsSecretAccessKey", AWS_SECRET_KEY)
.set('fs.s3a.endpoint', "s3.eu-central-1.amazonaws.com")
.set('com.amazonaws.services.s3a.enableV4', "true")
.set("fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")

)

sc = pyspark.SparkContext(conf=conf)
     
s3File = sc.textFile("s3a://welcome12345/student.json")

print(s3File.count())
print(s3File.id())