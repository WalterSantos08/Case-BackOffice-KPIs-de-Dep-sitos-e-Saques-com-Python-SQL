# 📊 Projeto Prático em Dados com Python, SQL, Git e GitHub

Este projeto foi desenvolvido como um **projeto prático de portfólio** com foco em **análise de dados**, utilizando **Python**, **SQL (SQLite)** e versionamento com **Git/GitHub**.

O objetivo é simular um cenário real de **BackOffice**, analisando transações de **depósitos e saques**, seus status e métricas operacionais (aprovação, tempo de processamento, rejeições, etc.).

---

## 🎯 Objetivo do Projeto

Construir um pipeline completo de dados, desde a geração do dataset até análises finais, respondendo perguntas como:

- Qual o volume total de **depósitos** e **saques**?
- Qual a **taxa de aprovação** das transações?
- Qual o **tempo médio** de processamento?
- Quais os principais **motivos de rejeição** (principalmente em saques)?
- Como os valores se comportam ao longo do tempo?

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **SQLite (SQL)**
- **Matplotlib**
- **Git / GitHub**

---

## 📁 Estrutura do Projeto

projeto-dados-python-sql/
│
├── data/
│ ├── raw/ # dados brutos (CSV)
│ └── processed/ # banco SQLite final
│
├── sql/
│ ├── create_tables.sql # criação de tabelas e índices
│ └── queries.sql # consultas SQL para análise
│
├── src/
│ ├── gerar_dados.py # gera o dataset em CSV
│ ├── carregar_sqlite.py # carrega CSV no banco SQLite
│ └── analise.py # KPIs + gráficos + outputs
│
├── outputs/
│ ├── kpis_resumo.csv # KPIs gerais
│ ├── kpis_por_tipo.csv # KPIs por tipo (deposit/withdraw)
│ └── graficos/ # gráficos gerados automaticamente
│
├── notebooks/ # espaço para análises em notebook (opcional)
├── requirements.txt
└── README.md

yaml
Copiar código

---

## 📌 Como Rodar o Projeto

### 1) Instalar dependências

```bash
pip install pandas matplotlib
Se você quiser, pode criar um requirements.txt também.

2) Gerar o dataset (CSV)
bash
Copiar código
python src/gerar_dados.py
Isso irá criar:

📄 data/raw/transactions_raw.csv

3) Criar e popular o banco SQLite
bash
Copiar código
python src/carregar_sqlite.py
Isso irá criar:

🗄️ data/processed/backoffice.db

4) Rodar análise e gerar relatórios
bash
Copiar código
python src/analise.py
Isso irá gerar automaticamente:

📄 outputs/kpis_resumo.csv
📄 outputs/kpis_por_tipo.csv
📊 outputs/graficos/*.png

🗄️ Consultas SQL (SQL/SQLite)
O arquivo sql/queries.sql contém consultas úteis como:

Total depositado vs total sacado

Taxa de aprovação por tipo

Série temporal por dia

Tempo médio de processamento

Top motivos de rejeição em saques

Você pode executar as queries usando ferramentas como:

DB Browser for SQLite

extensão SQLite no VSCode

terminal com sqlite3 (se tiver instalado)

📈 KPIs Gerados
Exemplos de métricas calculadas:

Total de transações

Valor total movimentado

Taxa de aprovação (%)

Tempo médio de processamento (min)

P95 do tempo de processamento

Top motivos de rejeição

📊 Gráficos Gerados
Após rodar src/analise.py, os gráficos são salvos em:

📁 outputs/graficos/

Incluindo:

Total por dia (deposit x withdraw)

Taxa de aprovação por tipo

Top 10 motivos de rejeição (withdraw)

🚀 Próximos Passos (Evoluções do Projeto)
Melhorias possíveis para versão 2.0:

Criar um dashboard no Power BI

Criar um modelo de previsão de rejeição (Machine Learning)

Criar uma API para consulta dos dados (FastAPI ou Spring Boot)

Adicionar testes automatizados (pytest)

Automatizar pipeline (ETL) com agendamento

👤 Autor
Walter Santos
Projeto desenvolvido para estudo e portfólio em Dados / Análise / BackOffice.

Copiar código
