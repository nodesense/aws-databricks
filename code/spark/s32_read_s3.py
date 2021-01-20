
import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"

os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"



import findspark
findspark.init()

import util
import credentials

import pyspark
sc = pyspark.SparkContext('local[*]')


from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()
access_id = credentials.get_access_key()
access_key =  credentials.get_access_secret()

hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
hadoop_conf.set("fs.s3n.awsAccessKeyId", access_id)
hadoop_conf.set("fs.s3n.awsSecretAccessKey", access_key)
hadoop_conf.set("fs.s3n.endpoint", "s3.eu-central-1.amazonaws.com")
 
# hadoop_conf.set("fs.s3a.awsAccessKeyId", access_id)
# hadoop_conf.set("fs.s3a.awsSecretAccessKey", access_key)
# hadoop_conf.set("fs.s3a.endpoint", "s3.eu-central-1.amazonaws.com")
# hadoop_conf.set("com.amazonaws.services.s3a.enableV4", "true")
# hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
 
 
# sc._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
# sc._jsc.hadoopConfiguration().set('fs.s3a.access.key', access_id)
# sc._jsc.hadoopConfiguration().set('fs.s3a.secret.key', access_key)
# sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', "s3.eu-central-1.amazonaws.com")
# sc._jsc.hadoopConfiguration().set('com.amazonaws.services.s3a.enableV4', "true")
 
# sc._jsc.hadoopConfiguration().set('com.amazonaws.services.s3.enableV4', "true")

s3File = sc.textFile("s3n://welcome12345/student.json")

print(s3File.count())
print(s3File.id())