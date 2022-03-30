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
print(v_class)
# # udf1 - turn vectors nums into list params >
# # vc_list_udf = funcs.udf(lambda row: tuple([float(n) for n in list(str(row))]))
# vc_list_udf = funcs.udf(lambda row: ([float(n) for n in list(str(row))]))
#
# spark = SparkSession \
#                     .builder \
#                     .appName("dbTbl2rdd") \
#                     .getOrCreate()
# # do we want use python for reading from db? / only spark? > any latency affect?
# # issue with  "vector" field need to convert items to list?/or only in db?
# dbTbl1 = spark.read.csv(r"stu_vc_ex.csv", header=True, inferSchema=True)
# # dbTbl_det = dbTbl1
#
# dbTbl1.show()
