# Apache Iceberg

O **Apache Iceberg** é um formato de tabela de alto desempenho para grandes conjuntos de dados analíticos. Ele foi desenhado para resolver problemas de consistência em ambientes de nuvem.

## Principais Recursos
* **Evolução de Partição:** Permite alterar a forma como os dados são particionados sem reescrever a tabela toda.
* **Snapshots Isolatados:** Leitores e escritores nunca se bloqueiam.
* **Suporte a Catálogos:** Utiliza catálogos (como Hive ou Hadoop) para gerir as tabelas de forma centralizada.

## Operações CRUD no Projeto
O Iceberg exige uma interação direta com o catálogo configurado:

### Escrita Inicial
```python
df_sul.write.format("iceberg").mode("overwrite").saveAsTable("local.db.vendas_sul")
```

### UPDATE (Operação ACID)
```python
spark.sql("UPDATE local.db.vendas_sul SET valor = valor * 1.10 WHERE id_venda = 1")
```

### DELETE
```python
spark.sql("DELETE FROM local.db.vendas_sul WHERE id_venda = 3")
```