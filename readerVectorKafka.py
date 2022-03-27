'''
Run the  generatorVector

'''


import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from textblob import TextBlob
from pyspark.sql.types import StringType, StructType, IntegerType, FloatType

# conection between  spark and kafka
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 pyspark-shell'

bootstrapServers = "localhost:9092"
topics = "vectors"


spark = SparkSession\
        .builder\
        .appName("ReadVectors")\
        .getOrCreate()

        # ReadStream from kafka
df_kafka = spark\
            .readStream \
            .format("kafka")\
            .option("kafka.bootstrap.servers", bootstrapServers)\
            .option("subscribe", topics)\
            .load()

schema = StructType() \
        .add("id", StringType()) \
        .add("student", StringType()) \
        .add("school",StringType()) \
        .add("class",StringType()) \
        .add("vector",StringType()) 



df_kafka = df_kafka.select(col("value").cast("string"))\
        .select(from_json(col("value"), schema).alias("value"))\
        .select("value.*")

# .option("numRows",2) \
df_kafka \
            .writeStream \
            .format("console") \
            .outputMode("append") \
            .start() \
            .awaitTermination()

