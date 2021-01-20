import findspark
findspark.init()

import pyspark

from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()

spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()

# RDD Creation
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)

print(rdd.count())
print(rdd.max())
print(rdd.min())
print(rdd.first()) 
print(rdd.collect()) 