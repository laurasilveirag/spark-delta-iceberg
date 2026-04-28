# 🔥 PySpark com Delta Lake e Apache Iceberg

Projeto desenvolvido para a disciplina de **Arquitetura de Dados** da SATC, demonstrando o uso do **PySpark** integrado aos formatos de tabela **Delta Lake** e **Apache Iceberg** para processamento e gestão de dados em larga escala.

O ambiente foi configurado com o gestor de pacotes **[Poetry](https://python-poetry.org/)**, garantindo reprodutibilidade, performance e isolamento de dependências.

---

## 👩‍💻 Autoras

Desenvolvido por **Ana Santinoni**, **Janaína Carlos** e **Laura Silveira** — Curso de Engenharia de Dados, SATC.

---

## 📦 Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| [Python](https://www.python.org/) | 3.12 | Linguagem base |
| [Python](https://www.python.org/) | 3.12 | Linguagem base |
| [PySpark](https://spark.apache.org/docs/latest/api/python/) | 3.5.3 | Processamento distribuído |
| [Delta Lake](https://docs.delta.io/latest/index.html) | 3.2.0 | Formato de tabela com transações ACID |
| [Apache Iceberg](https://iceberg.apache.org/) | 1.4.2 | Formato de tabela open table format |
| [Poetry](https://python-poetry.org/) | 2.3.4 | Gestor de pacotes e ambientes Python |
| [JupyterLab](https://jupyter.org/) | 4.x | Ambiente interativo de notebooks |
| [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | latest | Geração de documentação web |

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
│   ├── raw/                  # Arquivos CSV de entrada (vendas.csv e clientes.csv)
│   ├── delta/                # Dados gravados em formato Delta Lake
│   └── iceberg/              # Dados gravados em formato Iceberg
├── docs/
│   ├── index.md              # Página inicial do MkDocs
│   ├── delta.md              # Documentação detalhada do Delta Lake
│   ├── iceberg.md            # Documentação detalhada do Apache Iceberg
│   ├── index.md              # Página inicial, Modelo ER e DDLs
│   └── spark.md              # Documentação sobre Apache Spark / PySpark
├── src/
│   ├── __init__.py
│   ├── commons.py            # Funções compartilhadas (leitura e filtros)
│   ├── delta-lake.ipynb      # Notebook com demonstração prática (CRUD) no Delta Lake
│   └── apache-iceberg.ipynb  # Notebook com demonstração prática (CRUD) no Apache Iceberg
├── mkdocs.yml                # Configuração do site de documentação
├── pyproject.toml            # Dependências e metadados do projeto (gerido pelo Poetry)
└── README.md                 # Documentação principal do repositório
```

---

## ⚙️ Configuração do Ambiente

### Pré-requisitos

- Python 3.12 ou superior
- Java 17 ou superior (necessário para o Spark)
- Poetry instalado globalmente

### 1. Instalar o Poetry

```bash
pip install poetry
```

> Documentação completa: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)

### 2. Clonar o repositório

```bash
git clone [https://github.com/laurasilveirag/spark-delta-iceberg.git](https://github.com/laurasilveirag/spark-delta-iceberg.git)
cd spark-delta-iceberg
```

### 3. Instalar as dependências com Poetry

```bash
poetry install --no-root
```

---

## 🚀 Como Executar

### Opção 1 — JupyterLab (recomendado para visualização)

```bash
poetry run jupyter lab
```

1. Acesse `http://localhost:8888` no navegador
2. Navegue até a pasta `src/`
3. Abra `delta-lake.ipynb` ou `apache-iceberg.ipynb`
4. Execute as células com **Shift + Enter** ou clique em **Run → Run All Cells**

### Opção 2 — Terminal

```bash
cd src/
poetry run python commons.py
```

> **Atenção:** Os arquivos CSV (`vendas.csv` e `clientes.csv`) precisam estar na pasta `data/raw/` antes da execução dos notebooks.

---

## 📊 Sobre os Dados

Os dados utilizados formam um cenário sintético de **E-commerce**, criado para demonstração de manipulação de dados em arquiteturas Lakehouse.

**vendas.csv** — Registros de transações:

| id_venda | id_cliente | data_venda | valor  | status    |
|----------|-----------|------------|--------|-----------|
| 1        | 101       | 2023-01-15 | 250.50 | concluido |
| 2        | 102       | 2023-01-16 | 120.00 | concluido |
| 3        | 103       | 2023-01-17 | 340.90 | cancelado |
| 4        | 101       | 2023-01-18 | 50.00  | concluido |
| 5        | 104       | 2023-01-19 | 1500.0 | concluido |

**clientes.csv** — Cadastro de clientes:

| id_cliente | nome           | estado |
|-----------|----------------|--------|
| 101       | Ana Julia      | SC     |
| 102       | Laura Silveira | RS     |
| 103       | Carlos Silva   | SP     |
| 104       | Mateus Souza   | PR     |

### Fluxo de Processamento

```
clientes.csv ─┐
               ├──► PySpark ──► Filtro Região Sul ──► Delta Lake
vendas.csv  ──┘                                   └──► Apache Iceberg
```

---

## 🗂️ Notebooks

### delta-lake.ipynb

Demonstra operações CRUD no **Delta Lake**:

- **INSERT** — Salva os dados filtrados no formato Delta
- **UPDATE** — Aumenta o valor da venda 1 em 10%
- **DELETE** — Remove a venda 3 da tabela

### apache-iceberg.ipynb

Demonstra operações CRUD no **Apache Iceberg**:

- **INSERT** — Salva os dados filtrados no formato Iceberg
- **UPDATE** — Altera o status da venda 5 para `devolvido`
- **DELETE** — Remove a venda 2 da tabela

---

## 📚 Documentação

A documentação completa está disponível em:

👉 **[https://laurasilveirag.github.io/spark-delta-iceberg](https://laurasilveirag.github.io/spark-delta-iceberg)**

Para testar o site localmente na sua máquina:
```bash
poetry run mkdocs serve
```

Para publicar atualizações no GitHub Pages, utilizamos:
```bash
poetry run mkdocs gh-deploy
```

---

## 📖 Referências

- [Documentação PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Delta Lake Docs](https://docs.delta.io/)
- [Apache Iceberg Docs](https://iceberg.apache.org/)
- [Poetry Docs](https://python-poetry.org/docs/)
- [Canal DataWay BR — YouTube](https://www.youtube.com/@DataWayBR)

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
