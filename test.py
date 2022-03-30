









'''cosine calck -
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.ml.linalg import Vectors
from itertools import combinations
from numpy import linalg as LA

@F.udf(ArrayType(DoubleType()))
def dot_group(M):
    combs = combinations(M, 2)
    return [
        # or float(i.dot(j) / (LA.norm(i) * LA.norm(j)))
        (i.dot(j) / (LA.norm(i) * LA.norm(j))).tolist()
        for i, j in combs
    ]

dot_group = F.udf(g_dot, ArrayType(DoubleType()))

cdf = spark.createDataFrame(
            [(1.0, Vectors.dense([0.0, 10.0, 0.5])),
             (0.0, Vectors.dense([0.0, 1.0, 0.5])),
             (1.0, Vectors.dense([0.0, 10.0, 0.1])),
             (0.0, Vectors.dense([10.0, 10.0, 0.5])),
             (1.0, Vectors.dense([0.0, 0.0, 0.5])),],
            ["prediction", "features"])

dfs = cdf.groupBy(["prediction"]) \
         .agg(F.collect_list("features").alias("data")) \
         .withColumn("cosines", dot_group("data"))
dfs.show()
'''