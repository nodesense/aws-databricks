import os
import findspark
findspark.init()

import util
import credentials

import pyspark

from pyspark.sql import SparkSession
import configparser
from pyspark.sql.functions import col



spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()


valuesA = [('Pirate',1),('Monkey',2),('Ninja',3),('Spaghetti',4)]
TableA = spark.createDataFrame(valuesA,['name','id'])
 
valuesB = [('Rutabaga',1),('Pirate',2),('Ninja',3),('Darth Vader',4)]
TableB = spark.createDataFrame(valuesB,['name','id'])
 
TableA.show()
TableB.show()

ta = TableA.alias('ta')
tb = TableB.alias('tb')

print("Inner join")
inner_join = ta.join(tb, ta.name == tb.name)
inner_join.show()

print("Left join")

left_join = ta.join(tb, ta.name == tb.name,how='left') # Could also use 'left_outer'
left_join.show()

# Pyspark Left Join and Filter Example
print("Left join")
left_join = ta.join(tb, ta.name == tb.name,how='left') # Could also use 'left_outer'
left_join.filter(col('tb.name').isNull()).show()

print("Right join")
right_join = ta.join(tb, ta.name == tb.name,how='right') # Could also use 'right_outer'
right_join.show()

#Pyspark Full Outer Join Example

full_outer_join = ta.join(tb, ta.name == tb.name,how='full') # Could also use 'full_outer'
full_outer_join.show()

