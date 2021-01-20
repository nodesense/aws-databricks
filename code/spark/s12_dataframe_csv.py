import findspark
findspark.init()

import pyspark

from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()

spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()


df = spark.read.csv("file:////C:/spark/data/all_us_states.csv")
df.printSchema()

df.show()
