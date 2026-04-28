# ⚡ Apache Spark (PySpark)

## O que é?

O **Apache Spark** é um motor de processamento de dados distribuído, projetado para processar grandes volumes de dados de forma rápida e eficiente. Ele é capaz de processar dados em memória, o que o torna muito mais rápido que o Hadoop MapReduce.

O **PySpark** é a interface Python do Apache Spark, permitindo escrever pipelines de dados usando Python.

## Por que usamos?

- Suporte nativo a Delta Lake e Apache Iceberg
- Processamento em memória (muito mais rápido que SQL tradicional)
- Suporte a SQL via `spark.sql()`
- Ampla compatibilidade com formatos de dados (CSV, Parquet, JSON)

## Como configuramos?

### Delta Lake
```python
import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("DeltaLab") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", 
            "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
```

### Apache Iceberg
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IcebergLab") \
    .config("spark.jars.packages", 
            "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.2") \
    .config("spark.sql.extensions", 
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "../data/iceberg") \
    .getOrCreate()
```

## Leitura dos dados

Usamos uma função utilitária em `commons.py` para carregar os CSVs:

```python
def get_raw_data(spark, filename):
    path = os.path.join(DATA_PATH, filename)
    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(path)
```

## Filtro da Região Sul

```python
def filter_southern_region(df):
    return df.filter(df["estado"].isin("SC", "RS", "PR"))
```

## Dados utilizados

### vendas.csv
| id_venda | id_cliente | data_venda | valor | status |
|----------|-----------|------------|-------|--------|
| 1 | 101 | 2023-01-15 | 250.50 | concluido |
| 2 | 102 | 2023-01-16 | 120.00 | concluido |
| 3 | 103 | 2023-01-17 | 340.90 | cancelado |

### clientes.csv
| id_cliente | nome | estado |
|-----------|------|--------|
| 101 | Ana Julia | SC |
| 102 | Laura Silveira | RS |
| 104 | Mateus Souza | PR |
