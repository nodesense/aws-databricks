#
# Some constants
#
aws_profile = "default"
aws_region = "eu-central-1"
s3_bucket = "gks3bucket1"

import findspark
findspark.init()
# 
# Reading environment variables from aws credential file 
#
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.aws/credentials"))

access_id = config.get(aws_profile, "aws_access_key_id") 
access_key = config.get(aws_profile, "aws_secret_access_key") 
os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"

import pyspark
sc=pyspark.SparkContext()
sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")

hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("com.amazonaws.services.s3.enableV4", "true")
hadoop_conf.set("fs.s3a.access.key", access_id)
hadoop_conf.set("fs.s3a.secret.key", access_key)

hadoop_conf.set("fs.s3a.connection.maximum", "100000")

hadoop_conf.set("fs.s3a.endpoint", "s3." + aws_region + ".amazonaws.com")

sql=pyspark.sql.SparkSession(sc)
path = s3_bucket + "/student.json"

#dataS3=sql.read.parquet("s3a://" + path)


s3File = sc.textFile("s3a://" + path)


print(s3File.count())
print(s3File.id())
