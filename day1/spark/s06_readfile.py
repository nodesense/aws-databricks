import findspark
findspark.init()

import pyspark

import util

from pyspark.sql import SparkSession
import configparser

config = configparser.ConfigParser()

spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()

# txt is rdd
txt = spark.sparkContext.textFile(util.get_data_path('LICENSE.txt'))

print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())

