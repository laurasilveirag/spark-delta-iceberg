from pyspark.sql import SparkSession
import pyspark.sql.functions as f

def get_raw_data(spark: SparkSession, file_name: str):
    return spark.read.csv(f"../data/raw/{file_name}", header=True, inferSchema=True)

def filter_southern_region(df):
    return df.filter((df.estado.isin("PR", "SC", "RS")) & (df.status == "concluido"))