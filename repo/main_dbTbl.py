import pandas as pd
import pyspark.sql.types
from Crypto.Util import number
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
import numpy as np
from numpy.linalg import norm
import json
from pandas import json_normalize
from pyspark.sql.functions import pandas_udf
# import pyspark.sql.functions as fn

# for rdd to df rdd -
from pyspark.sql.types import StructField, StructType, StringType
from pyspark.sql import Row
from pyspark.sql.functions import get_json_object
import pyspark.sql.functions as funcs
import pyspark.sql.types as types
# cosine calck -
from pyspark.mllib.linalg.distributed import RowMatrix

# - * 2 dbTbl2rdd * -
# - get params for class & school online V
# - get db ex vectors all data - V
# - convert into list (only vectors) > rdd of all vectors V
# - create udf function for cosine calk
# - udf on list of vectors > return min
# - query db with vector param matched - return student det

# here we get params from an input -
# input('what is the class?') #student = 2
# input('what is the school?')
v_school = 'madrid'
v_class = 2
# udf1 - turn vectors nums into list params >
# vc_list_udf = funcs.udf(lambda row: tuple([float(n) for n in list(str(row))]))
# rows = sc.parallelize([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
vc_list_udf = funcs.udf(lambda row: ([float(n) for n in list(str(row))]))

# udf2 - turn vectors nums into list params >
# vc_cosine_calk not valid yet =>
# @funcs.udf((ArrayType(DoubleType()))
#                     def dot_group(M):
#                         combs = combinations(M, 2)
#                         return [(i.dot(j) / (LA.norm(i) * LA.norm(j))).tolist() for i, j in combs]
#
#  # or float(i.dot(j) / (LA.norm(i) * LA.norm(j)))
# dot_group = funcs.udf(g_dot, ArrayType(DoubleType()))
spark = SparkSession \
    .builder \
    .appName("dbTbl2rdd") \
    .getOrCreate()
# do we want use python for reading from db? / only spark? > any latency affect?
# issue with  "vector" field need to convert items to list?/or only in db?
dbTbl1 = spark.read.csv(r"stu_vc_ex.csv", header=True, inferSchema=True)
dbTbl_det = dbTbl1

# process for vectors db to list rdd-
dbTbl2 = dbTbl1.drop('id', 'clas', 'school', 'student')\
         .where(dbTbl1.school == v_school)\
         .where(dbTbl1.clas == v_class)
#                                                \
#                                            .orderBy(id, ascending=True)
dbTbl3 = dbTbl2.withColumn('vector', vc_list_udf(dbTbl2.vector)).rdd\
        .map(lambda x: x)\
        .collect()
#        .orderBy(id, ascending=True)

for row in dbTbl3:
    print((row[0]))

mat = RowMatrix(dbTbl3)
exact = mat.columnSimilarities()
approx = mat.columnSimilarities(0.05)

dbTbl4 = exact.entries.collect()

for row in dbTbl4:
    print(row)

    # print(row[0] + "," +str(row[1]))

# rows = sc.parallelize([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
#
# # Convert to RowMatrix
# mat = RowMatrix(rows)
#
# # Calculate exact and approximate similarities
# exact = mat.columnSimilarities()
# approx = mat.columnSimilarities(0.05)
#
# # Output
# exact.entries.collect()


# here we will use udf to calck cosin for each row in db
# here we will write the query for cosine match with json
# here we will query the db with vector most matching


# process for all db det rdd-
# here we will query db table with vectors input param matched
# here we will return student voice details






# tests -
# # valid option 1  - for reading db csv
# schema = StructType() \
#       .add("vector",pyspark.sql.types.StringType(),True)
#
# dbTbl1 = spark.read.csv(r"stu_vc_ex.csv",
#                          header=True, inferSchema=True, schema=schema)

# def conver_vc_str(number):
#     return str(number)
#
# conver_vc_str_udf = funcs.udf(conver_vc_str, types.DoubleType())
#
# transformed_df = dbTbl1.withColumn(
#     'vector', conver_vc_str_udf('vector')
# )
# transformed_df.show()

# # creating spark session - not sure if needed, check for configuration with group >
# # .config("spark.some.config.option", "some-value") \ # optional
# spark = SparkSession \
#     .builder \
#     .appName("json2rrd") \
#     .getOrCreate()
#
# # - * 1 json2rdd * -
# # - get json with vector values
# # - convert into list > rdd
#
# vc = "vector"
# sc = SparkContext.getOrCreate()
# data_txt = '{ "p1":"test3", "p2":"test2", "vector":"410256"}'
# data_vc = [int(i) for i in list(json.loads(data_txt)[vc])]
# rdd_vc = sc.parallelize(data_vc)
# print(rdd_vc.collect())
# # >>> do we want to give name to rdd? y/n  # rdd_vc.setName("vc").name()
# # >>> do we want to turn into df rdd? y/n
# # >>> how do we give names to field? y/n











