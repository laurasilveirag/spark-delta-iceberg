# 🛒 Lakehouse de E-commerce

## Contextualização do Projeto
Este projeto demonstra a implementação de uma arquitetura Lakehouse utilizando **Apache Spark**, **Delta Lake** e **Apache Iceberg**. O cenário foca no processamento de vendas de um e-commerce distribuído no Brasil.

## Fluxo de Dados
1. Ingestão de dados brutos (CSV).
2. Tratamento e Cruzamento de dados (Vendas x Clientes).
3. Persistência em tabelas ACID (Delta e Iceberg).
4. Demonstração de operações DML (Insert, Update, Delete).

![Diagrama de Arquitetura](assets/diagrama.png)