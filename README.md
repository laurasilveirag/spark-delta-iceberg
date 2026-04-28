# 🔥 PySpark com Delta Lake e Apache Iceberg

Projeto desenvolvido para a disciplina de **Arquitetura de Dados**, demonstrando o uso do **PySpark** integrado aos formatos de tabela **Delta Lake** e **Apache Iceberg** para processamento e gestão de dados em larga escala.

Para garantir estabilidade e evitar problemas de compatibilidade com o ecossistema Hadoop/Spark, todo o ambiente foi configurado para rodar nativamente em ambiente Unix através do **WSL (Ubuntu)**, gerenciado pelo **[uv](https://github.com/astral-sh/uv)**.

---

## 📦 Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| [Python](https://www.python.org/) | 3.12 | Linguagem base |
| [PySpark](https://spark.apache.org/docs/latest/api/python/) | 3.5.3 | Processamento distribuído |
| [Delta Lake](https://docs.delta.io/latest/index.html) | 3.2.0 | Formato de tabela com transações ACID |
| [Apache Iceberg](https://iceberg.apache.org/) | 1.5.0 | Formato de tabela (open table format) |
| [uv](https://github.com/astral-sh/uv) | latest | Gestor de pacotes e ambientes Python |
| [MkDocs](https://www.mkdocs.org/) | 1.6.x | Geração de documentação web |

---

## 📁 Estrutura do Projeto

```text
spark-delta-iceberg/
├── .gitignore
├── .python-version
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── data/
│   ├── delta/                # Destino dos dados Delta (gerado via código)
│   ├── iceberg/              # Destino dos dados Iceberg (gerado via código)
│   └── raw/                  # Arquivos CSV de entrada (vendas.csv e clientes.csv)
├── docs/
│   ├── delta.md              # Documentação detalhada do Delta Lake
│   ├── iceberg.md            # Documentação detalhada do Apache Iceberg
│   ├── index.md              # Página inicial, Modelo ER e DDLs
│   └── spark.md              # Documentação sobre Apache Spark / PySpark
├── src/
│   ├── commons.py            # Funções compartilhadas (leitura e filtros)
│   ├── run_delta.py          # Script de Produção: Pipeline Delta Lake
│   └── run_iceberg.py        # Script de Produção: Pipeline Apache Iceberg
```

---

## ⚙️ Configuração do Ambiente (Via WSL/Ubuntu)

Para garantir que o Spark encontre o Java e os utilitários de sistema corretos, recomendamos a execução via terminal Linux (WSL).

### 1. Preparar o Ubuntu (WSL)
Abra o terminal do Ubuntu e instale o Java (obrigatório para o Spark):
```bash
sudo apt update && sudo apt install default-jre -y
```

### 2. Instalar o gerenciador uv
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
source $HOME/.local/bin/env
```

### 3. Clonar e sincronizar o projeto
Navegue até a pasta do projeto e crie o ambiente isolado com as dependências corretas:
```bash
git clone [https://github.com/laurasilveirag/spark-delta-iceberg.git](https://github.com/laurasilveirag/spark-delta-iceberg.git)
cd spark-delta-iceberg
uv sync
```

---

## 🚀 Como Executar (Scripts de Produção)

Para simular um ambiente de produção real, as execuções foram consolidadas em scripts Python. 

1. Abra o terminal do Ubuntu integrado ao VS Code.
2. Navegue até a pasta de scripts:
   ```bash
   cd src
   ```
3. **Para rodar o pipeline do Delta Lake:**
   ```bash
   uv run python run_delta.py
   ```
4. **Para rodar o pipeline do Apache Iceberg:**
   ```bash
   uv run python run_iceberg.py
   ```

> **Nota:** Os scripts executarão a extração dos CSVs, o cruzamento de dados, os filtros da região Sul, o salvamento nos respectivos formatos e, em seguida, as validações ACID (UPDATE e DELETE), exibindo o dataframe resultante no terminal.

---

## 📊 Sobre os Dados

Os dados formam um cenário sintético de E-commerce. Consiste em cruzar `vendas.csv` com `clientes.csv`, filtrar as vendas da região Sul do Brasil (PR, SC, RS) e realizar operações CRUD evidenciando as garantias transacionais das arquiteturas Lakehouse. O modelo ER da modelagem e as instruções DDL estão detalhados na nossa documentação web.

---

## 📚 Documentação (MkDocs)

Toda a fundamentação teórica, modelos e explicações exigidas estão publicados em nosso site:
👉 **[https://laurasilveirag.github.io/spark-delta-iceberg](https://laurasilveirag.github.io/spark-delta-iceberg)**

Para testar o site localmente na sua máquina:
```bash
uv run mkdocs serve
```

Para publicar atualizações no GitHub Pages, utilizamos:
```bash
uv run mkdocs gh-deploy
```

---

## 👩‍💻 Autoras
Desenvolvido por **Ana Julia**, **Janaina** e **Laura** — Curso de Engenharia de Dados, SATC.