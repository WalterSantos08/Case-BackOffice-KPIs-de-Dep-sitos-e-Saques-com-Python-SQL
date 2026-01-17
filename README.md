# 📊 Case BackOffice — KPIs de Depósitos e Saques

## 💡 Sobre o Projeto

Este é um **case prático de análise de dados** aplicado ao cenário de BackOffice financeiro, focado em transações de **depósitos** e **saques**. O objetivo principal é demonstrar um pipeline completo de dados — desde a geração e armazenamento até métricas e visualizações — usando **Python**, **SQLite** e **SQL**.

O projeto executa um fluxo de ETL (Extract, Transform, Load), gera **KPIs**, produz **relatórios em CSV** e salva **gráficos** automaticamente para facilitar a interpretação dos dados.

---

## 🧩 Tecnologias

| Tecnologia | Finalidade |
|------------|-------------|
| Python 3 | Linguagem principal |
| pandas | Manipulação de dados |
| SQLite | Banco de dados leve |
| SQL | Consultas estruturadas |
| matplotlib | Visualizações (gráficos) |

---

## 📁 Estrutura do Projeto

```text
Case-BackOffice-KPIs/
│
├── data/
│   ├── raw/                 # dados brutos (CSV)
│   └── processed/           # banco SQLite final
│
├── sql/
│   ├── create_tables.sql    # criação de tabelas e índices
│   └── queries.sql          # consultas SQL para análise
│
├── src/
│   ├── gerar_dados.py       # gera o dataset em CSV
│   ├── carregar_sqlite.py   # carrega CSV no banco SQLite
│   └── analise.py           # KPIs + gráficos + outputs
│
├── outputs/
│   ├── kpis_resumo.csv      # KPIs gerais
│   ├── kpis_por_tipo.csv    # KPIs por tipo (deposit/withdraw)
│   └── graficos/            # gráficos gerados automaticamente
│
├── requirements.txt         # dependências
└── README.md                # documentação
```

---

## 📌 Funcionalidades

### 🛠️ ETL e Preparação de Dados
- Geração de um dataset sintético de transações (`gerar_dados.py`)
- Criação de banco SQLite e carregamento das transações (`carregar_sqlite.py`)
- Estrutura de tabelas com índices

### 📊 Análise Automática
- Cálculo de métricas principais (KPIs)
- Produção de relatórios em CSV
- Geração de gráficos salvos em arquivos

### 📈 Consultas SQL
- Total por tipo (deposit/withdraw)
- Taxa de aprovação por tipo
- Série temporal por dia
- Tempo médio de processamento
- Top motivos de rejeição

---

## 📦 Como Executar

### 1) Instalar Dependências
Instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib
```

---

### 2) Gerar Dataset

```bash
python src/gerar_dados.py
```

O arquivo será salvo em:
📄 `data/raw/transactions_raw.csv`

---

### 3) Criar e Popular Banco

```bash
python src/carregar_sqlite.py
```

Banco criado em:
🗄️ `data/processed/backoffice.db`

---

### 4) Rodar Análise Completa

```bash
python src/analise.py
```

Saídas geradas automaticamente:

📄 `outputs/kpis_resumo.csv`  
📄 `outputs/kpis_por_tipo.csv`  
📊 `outputs/graficos/*.png`

---

## 📊 Resultados Obtidos

### 📈 KPIs

- **Total de transações**
- **Valor total movimentado**
- **Taxa de aprovação (%)**
- **Tempo médio de processamento**
- **Top motivos de rejeição**

Arquivos de KPI:
- `kpis_resumo.csv`
- `kpis_por_tipo.csv`

---

## 📉 Visualizações

As visualizações geradas são gravadas em:

📁 `outputs/graficos/`

Você encontrará:

| Gráfico | Descrição |
|---------|-----------|
| `total_por_dia.png` | Volume por dia (deposit x withdraw) |
| `approval_por_tipo.png` | Taxa de aprovação por tipo |
| `top_rejeicoes_withdraw.png` | Top motivos de rejeição em saques |

> 💡 **Dica:** abra os PNGs no VSCode ou visualizador de imagens para explorar os gráficos.

---

## 🛠️ SQL Queries

O arquivo `sql/queries.sql` contém consultas como:

- Total por tipo
- Taxa de aprovação por tipo
- Série temporal por dia
- Tempo médio de processamento
- Top motivos de rejeição

Você pode executá-las com:
- DB Browser for SQLite
- Extensão SQLite no VSCode
- CLI do sqlite3

---

## 🌟 Próximas Evoluções

Este projeto pode ser estendido com:

- Dashboard interativo (Power BI / Streamlit)
- Previsão de rejeições (Machine Learning)
- API para consulta dos KPIs (FastAPI)
- Testes automatizados (pytest)
- Automatização de ETL programada

---

## 👤 Autor

**Walter Santos**  
📌 GitHub: https://github.com/WalterSantos08

Desenvolvido como projeto de portfólio em análise de dados e engenharia de dados.
