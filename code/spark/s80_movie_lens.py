#spark ui url http://localhost:4040/jobs/

import os

import findspark
findspark.init()



import pyspark

from pyspark.sql import SparkSession
import configparser
from pyspark.sql.functions import *


config = configparser.ConfigParser()

spark = SparkSession.builder.master("local[1]").appName("SparkLocal").getOrCreate()

RATING_PATH = "C:/Users/Gopalakrishnan/aws-databricks/day1/data/movielens-100k/ratings.csv"
MOVIES_PATH = "C:/Users/Gopalakrishnan/aws-databricks/day1/data/movielens-100k/movies.csv"


ratings = spark.read.option("header", "true").csv(RATING_PATH)
ratings.show(5)
ratings.printSchema()

movies = spark.read.option("header", "true").csv(MOVIES_PATH)
movies.show(5)
movies.printSchema()


most_popular = ratings\
.groupBy("movieId")\
.agg(count("userId"))\
.withColumnRenamed("count(userId)", "num_ratings")\
.sort(desc("num_ratings"))

most_popular.show(10)

most_popular_movies = most_popular.join(movies, most_popular.movieId == movies.movieId)
most_popular_movies.show(20, truncate=False)

top_rated = ratings\
.groupBy("movieId")\
.agg(avg(col("rating")))\
.withColumnRenamed("avg(rating)", "avg_rating")\
.sort(desc("avg_rating"))

top_rated_movies = top_rated.join(movies, top_rated.movieId == movies.movieId)
top_rated_movies.show(10)

top_rated = ratings\
.groupBy("movieId")\
.agg(count("userId"), avg(col("rating")))\
.withColumnRenamed("count(userId)", "num_ratings")\
.withColumnRenamed("avg(rating)", "avg_rating")

top_rated_movies = top_rated.join(movies, top_rated.movieId == movies.movieId).sort(desc("avg_rating"), desc("num_ratings"))
top_rated_movies.show(10)

# Calculate average, minimum, and maximum of num_ratings
top_rated_movies.select([mean('num_ratings'), min('num_ratings'), max('num_ratings')]).show(1)

# median
top_rated_movies.approxQuantile('num_ratings', [0.5], 0)

# first quartile
top_rated_movies.approxQuantile('num_ratings', [0.25], 0)


# third quartile
top_rated_movies.approxQuantile('num_ratings', [0.75], 0)

top_rated_movies.where("num_ratings > 500").show(20, truncate=False)

#Most polarising movies (Marmite movies)¶

ratings_stddev = ratings\
.groupBy("movieId")\
.agg(count("userId").alias("num_ratings"), 
     avg(col("rating")).alias("avg_rating"),
     stddev(col("rating")).alias("std_rating")
    )\
.where("num_ratings > 500")

ratings_stddev.show(5)
marmite_movies = ratings_stddev.join(movies, ratings_stddev.movieId == movies.movieId)

marmite_movies.sort(desc("std_rating")).show(15, truncate=False)


raw_input("press any key to quit")

