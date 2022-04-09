# #TODO implement
# # topic_processedTweets into
# # 1 DONE -  telegram
# # 2 db - tweets history
# '''
# Run the  generatorVector
# '''
#
# import os
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *
# from pyspark.sql.types import StringType, StructType, IntegerType, FloatType

from telebot_message_users import TelebotSender

#
# # connection between  spark and kafka
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 pyspark-shell'
#
# bootstrapServers = "localhost:9092"
# topics = "topic_processedTweets"
#
# spark = SparkSession \
#     .builder \
#     .appName("ReadProcessedTweets") \
#     .getOrCreate()
#
# # ReadStream from kafka
# df_kafka = spark \
#     .readStream \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", bootstrapServers) \
#     .option("subscribe", topics) \
#     .load()
#
# schema = StructType() \
#     .add("id_1", StringType()) \
#     .add("user_1", StringType()) \
#     .add("time_stamp1", StringType()) \
#     .add("content_1", StringType()) \
#     .add("currency_1", StringType())
#
# df_kafka = df_kafka.select(col("value").cast("string")) \
#     .select(from_json(col("value"), schema).alias("value")) \
#     .select("value.*")
#
# # .option("numRows",2) \
# df_kafka \
#     .writeStream \
#     .format("console") \
#     .outputMode("append") \
#     .start() \
#     .awaitTermination()


# find users that listens
# find users that listens to specific Influencer


telebot_sender_inst = TelebotSender()
try:
    test = telebot_sender_inst.telegram_bot_sendtext("Testing Telegram bot")
except Exception as e:
    # TODO implement logging and error handling / retrying
    print(e)
