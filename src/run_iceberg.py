import pyspark
from commons import get_raw_data, filter_southern_region

print("Iniciando o Spark e o Apache Iceberg...")

builder = pyspark.sql.SparkSession.builder.appName("IcebergLab") \
    .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.0") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hadoop") \
    .config("spark.sql.catalog.spark_catalog.warehouse", "../data/iceberg") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "../data/iceberg")

spark = builder.getOrCreate()

print("Spark iniciado! Processando dados...")

df_vendas = get_raw_data(spark, "vendas.csv")
df_clientes = get_raw_data(spark, "clientes.csv")
df_sul = filter_southern_region(df_vendas.join(df_clientes, "id_cliente"))

print("Salvando dados na tabela Iceberg...")
df_sul.write.format("iceberg").mode("overwrite").saveAsTable("local.db.vendas_sul")

print("Lendo tabela e executando CRUD...")
spark.sql("UPDATE local.db.vendas_sul SET valor = valor * 1.10 WHERE id_venda = 1")
spark.sql("DELETE FROM local.db.vendas_sul WHERE id_venda = 3")

print("\n=== RESULTADO FINAL: TABELA ICEBERG SUL ===")
spark.sql("SELECT * FROM local.db.vendas_sul").show()