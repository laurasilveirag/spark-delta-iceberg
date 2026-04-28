import os
from pyspark.sql import SparkSession, DataFrame

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/raw")

def get_raw_data(spark: SparkSession, filename: str) -> DataFrame:
    path = os.path.join(DATA_PATH, filename)
    return spark.read.option("header", "true").option("inferSchema", "true").csv(path)

def filter_southern_region(df: DataFrame) -> DataFrame:
    return df.filter(df["estado"].isin(["SC", "RS", "PR"]))
