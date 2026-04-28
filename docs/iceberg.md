# 🧊 Apache Iceberg

## O que é?

O **Apache Iceberg** é um formato de tabela aberto criado pelo Netflix para trabalhar com grandes volumes de dados analíticos. Diferente de formatos tradicionais, o Iceberg rastreia **arquivos individuais** em vez de pastas, tornando as operações muito mais eficientes.

## Principais características

| Recurso | Descrição |
|---------|-----------|
| ✅ Transações ACID | Leituras e escritas isoladas e consistentes |
| 📸 Snapshots | Cada operação gera um snapshot rastreável |
| ⏱️ Time Travel | Consulta dados em qualquer ponto no tempo |
| 🔄 Schema Evolution | Adiciona/remove colunas sem reescrever dados |
| 🗂️ Partition Evolution | Muda particionamento sem migrar dados |

## Como usamos no projeto

### Configuração
```python
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

## Operações CRUD

### 📥 INSERT — Salvando dados no Iceberg
```python
df_sul = filter_southern_region(df_vendas.join(df_clientes, "id_cliente"))
df_sul.write.format("iceberg").mode("overwrite").saveAsTable("local.vendas_sul")
```

**Resultado:**

| id_cliente | id_venda | valor | status | estado |
|-----------|---------|-------|--------|--------|
| 101 | 1 | 250.5 | concluido | SC |
| 102 | 2 | 120.0 | concluido | RS |
| 101 | 4 | 50.0 | concluido | SC |
| 104 | 5 | 1500.0 | concluido | PR |

### ✏️ UPDATE — Atualizando status de uma venda
```python
spark.sql("UPDATE local.vendas_sul SET status = 'devolvido' WHERE id_venda = 5")
```

**Resultado:** Venda 5 teve status alterado para `devolvido` ✅

### 🗑️ DELETE — Removendo uma venda
```python
spark.sql("DELETE FROM local.vendas_sul WHERE id_venda = 2")
```

**Resultado:** Venda 2 (Laura Silveira, RS) removida da tabela ✅

## Delta Lake vs Apache Iceberg

| Critério | Delta Lake | Apache Iceberg |
|---------|-----------|----------------|
| Criado por | Databricks | Netflix |
| Maturidade | Alta | Alta |
| Multi-engine | Limitado | Excelente |
| Time Travel | ✅ | ✅ |
| ACID | ✅ | ✅ |
| Ideal para | Databricks/Spark | Multi-engine |
