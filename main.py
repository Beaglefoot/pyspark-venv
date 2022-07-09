from pyspark.sql import SparkSession
from venv_cm import venv

spark = (
    SparkSession.builder.appName("Test pyspark with venv context manager")
    .master("spark://spark:7077")
    .getOrCreate()
)

df = spark.createDataFrame(
    [("Joe", "Pass", "Guitar"), ("Louis", "Armstrong", "Trumpet")],
    schema=["first_name", "last_name", "instrument"],
)

with venv("/myvenv/.venv"):
    print("--- venv ----")

    import pandas as pd

    musicians = {
        "first_name": ["John"],
        "last_name": ["Coltrane"],
        "instrument": ["Sax"],
    }

    musicians_pandas_df = pd.DataFrame(musicians)

    musicians_spark_df = spark.createDataFrame(musicians_pandas_df)

    musicians_spark_df.union(df).show()
