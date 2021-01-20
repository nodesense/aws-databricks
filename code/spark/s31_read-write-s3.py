import os
os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"
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

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df=spark.read.json("s3n://welcome12345/student.json")

results = df.toJSON().map(lambda j: json.loads(j)).collect()
print(results)
for result in results:
    print(result)
obj = {'first_name': 'kumar', 'last_name': 'rout', 's_id': '12345679'}
results.append(obj)
print(results)
df = spark.read.json(sc.parallelize([results]))
df.write.format('json').save('s3n://welcome12345/studentspark.json')
