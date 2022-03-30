import pandas as pd
from Crypto.Util import number
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
import numpy as np
from numpy.linalg import norm
import json
from pandas import json_normalize

# for rdd to df rdd -
from pyspark.sql.types import StructField, StructType, StringType
from pyspark.sql import Row
from pyspark.sql.functions import get_json_object

# creating spark session - not sure if needed, check for configuration with group >
# .config("spark.some.config.option", "some-value") \ # optional
spark = SparkSession \
    .builder \
    .appName("json2rrd") \
    .getOrCreate()

# - * 1 json2rdd * -
# - get json with vector values
# - convert into list > rdd
vc = "vector"
sc = SparkContext.getOrCreate()
data_txt = '{ "p1":"test3", "p2":"test2", "vector":"410256"}'
data_vc = [int(i) for i in list(json.loads(data_txt)[vc])]
rdd_vc = sc.parallelize(data_vc)
print(rdd_vc.collect())
# >>> do we want to give name to rdd? y/n  # rdd_vc.setName("vc").name()
# >>> do we want to turn into df rdd? y/n
# >>> how do we give names to field? y/n


















# bck -
# def parse(s, rdd_flds):
#     try:
#         d = json.loads(s[0])
#         return [tuple(d.get(field) for field in rdd_flds)]
#     except:
#         return []

# def parse(s, rdd_flds):
#     try:
#         d = json.loads(data_txt)
#         return [tuple(d.get(field) for field in rdd_flds)]
#     except:
#         return []

# # data_df = spark.createDataFrame(data_rdd.flatMap(lambda s: parse(s, rdd_flds)), schema)
# data_df = spark.createDataFrame(data_rdd.flatMap(lambda s: parse(s, rdd_flds)), schema)
