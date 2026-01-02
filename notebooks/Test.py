from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = (SparkSession.builder
         .appName("WSL-driver")
         .getOrCreate())

df = spark.range(10)
df.show()