import pyspark
from pyspark.sql import SparkSession

ss = SparkSession.builder.master("local[2]").appName("app").getOrCreate()

data = [('stallman', 1953, 'programmer'), ('newton', 1643, 'physics'), ('frink', 1965, 'professor')]

dataDF = ss.createDataFrame