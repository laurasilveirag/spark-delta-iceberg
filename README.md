# 🔥 PySpark com Delta Lake e Apache Iceberg

Projeto desenvolvido para a disciplina de **Arquitetura de Dados**, demonstrando o uso do **PySpark** integrado aos formatos de tabela **Delta Lake** e **Apache Iceberg** para processamento e gestão de dados em larga escala.

O ambiente foi configurado com o gestor de pacotes **[uv](https://github.com/astral-sh/uv)**, garantindo reprodutibilidade, performance e isolamento de dependências.

---

## 📦 Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|---|---|---|
| [Python](https://www.python.org/) | 3.13 | Linguagem base |
| [PySpark](https://spark.apache.org/docs/latest/api/python/) | 3.5.3 | Processamento distribuído |
| [Delta Lake](https://docs.delta.io/latest/index.html) | 3.2.0 | Formato de tabela com transações ACID |
| [Apache Iceberg](https://iceberg.apache.org/) | 1.10.0 | Formato de tabela (open table format) |
| [uv](https://github.com/astral-sh/uv) | latest | Gestor de pacotes e ambientes Python |
| [JupyterLab](https://jupyter.org/) | 4.x | Ambiente interativo de notebooks |
| [MkDocs](https://www.mkdocs.org/) | 1.6.x | Geração de documentação web |

---

## 📁 Estrutura do Projeto

```text
spark-delta-iceberg/
├── data/
│   ├── raw/                  # Ficheiros CSV de entrada (vendas.csv e clientes.csv)
│   ├── delta/                # Dados gravados em formato Delta Lake
│   └── iceberg/              # Dados gravados em formato Iceberg
├── docs/
│   ├── assets/               # Imagens e recursos estáticos (ex: diagramas)
│   ├── index.md              # Página inicial do MkDocs
│   ├── delta.md              # Documentação detalhada do Delta Lake
│   ├── iceberg.md            # Documentação detalhada do Apache Iceberg
│   └── spark.md              # Documentação sobre Apache Spark / PySpark
├── src/
│   ├── __init__.py
│   ├── commons.py            # Funções partilhadas (leitura e filtros) para os notebooks
│   ├── delta-lake.ipynb      # Notebook com demonstração prática (CRUD) no Delta Lake
│   └── apache-iceberg.ipynb  # Notebook com demonstração prática (CRUD) no Apache Iceberg
├── mkdocs.yml                # Configuração do site de documentação
├── pyproject.toml            # Dependências e metadados do projeto (gerido pelo uv)
└── README.md                 # Documentação principal do repositório

---

## ⚙️ Configuração do Ambiente

### Pré-requisitos

- Python 3.13 ou superior
- Java 11 ou superior (necessário para o Spark)
- `uv` instalado globalmente

### 1. Instalar o `uv`

**Linux / macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> Documentação completa: [https://github.com/astral-sh/uv#installation](https://github.com/astral-sh/uv#installation)

### 2. Clonar o repositório

```bash
git clone https://github.com/laurasilveirag/spark-delta-iceberg.git
cd spark-delta-iceberg
```

### 3. Instalar as dependências com `uv`

```bash
uv python install
uv sync --frozen
uv pip install .
```

---

## 🚀 Como Executar

1. Abre a pasta do projeto no VS Code ou inicia o JupyterLab.
2. Navega até à pasta src/ e abre o ficheiro delta-lake.ipynb ou apache-iceberg.ipynb
3. Seleciona o kernel do ambiente virtual criado pelo uv (geralmente nomeado como .venv).
4. Execute as células sequencialmente com **Shift + Enter**

> **Atenção:** Os ficheiros CSV (vendas.csv e clientes.csv) precisam de estar corretamente posicionados na pasta data/raw/ antes da execução dos notebooks.

---

## 📊 Sobre os Dados

Os dados utilizados neste projeto formam um cenário sintético de E-commerce, criado exclusivamente para fins académicos de demonstração de manipulação de dados em arquiteturas Lakehouse. O conjunto é composto por:

vendas.csv: Registos de transações, contendo o ID da venda, ID do cliente, data, valor e status do pedido.

clientes.csv: Cadastro de clientes, contendo o ID, nome e o estado (UF) de residência.

Fluxo de Processamento:
A lógica desenvolvida consiste em extrair estes dados brutos, realizar o cruzamento (Join) entre as vendas e os clientes, e filtrar apenas as vendas concluídas de clientes da região Sul do Brasil (PR, SC, RS). Após a transformação, realizamos operações de CRUD (INSERT, UPDATE e DELETE) evidenciando as garantias transacionais (ACID) dos formatos Delta Lake e Apache Iceberg.

---

## 📚 Documentação

A documentação completa do projeto está disponível via MkDocs em:
👉 **[https://laurasilveirag.github.io/spark-delta-iceberg](https://laurasilveirag.github.io/spark-delta-iceberg)**

Para visualizar localmente:

```bash
uv run mkdocs serve
```

Para publicar no GitHub Pages:

```bash
uv run mkdocs gh-deploy
```

---

## 📖 Referências

- [Documentação PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Delta Lake Docs](https://docs.delta.io/)
- [Apache Iceberg Docs](https://iceberg.apache.org/)
- [uv — Astral](https://github.com/astral-sh/uv)
- [Canal DataWay BR — YouTube](https://www.youtube.com/@DataWayBR)

---

## 👩‍💻 Autoras

Desenvolvido por **Ana Julia**, **Janaina** e **Laura** — Curso de Engenharia de Dados, SATC.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
