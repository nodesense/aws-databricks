import findspark
findspark.init()

import pyspark
from pyspark.sql.types import StructType, StringType, IntegerType
#from pyspark.sql.types import *


from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()

spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()

schema = StructType() \
      .add("name",StringType(),True) \
      .add("state",StringType(),True) \
      .add("county_seat",IntegerType(),True)
    

df = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load("file:////C:/spark/data/all_us_counties.csv")

df.printSchema()

df.show()


df.show(100)