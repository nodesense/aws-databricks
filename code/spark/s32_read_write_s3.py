import os
os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"
import findspark
findspark.init()
from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()
#config.read(os.path.expanduser("~/.aws/credentials"))
access_id = '<<key-id>>' #config.get(aws_profile, "aws_access_key_id")
access_key = '<<key-secret>>' #config.get(aws_profile, "aws_secret_access_key")
sc=spark.sparkContext
hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
hadoop_conf.set("fs.s3n.awsAccessKeyId", access_id)
hadoop_conf.set("fs.s3n.awsSecretAccessKey", access_key)
spark = SparkSession.builder \
.appName("my_app") \
.config('spark.sql.codegen.wholeStage', False) \
.getOrCreate()\

df=spark.read.json("s3://akshayademos3/test_directory3/hello3.json")



df.write.format('json').save('s3://akshayademos3/test_directory3/uploadFromDB2')