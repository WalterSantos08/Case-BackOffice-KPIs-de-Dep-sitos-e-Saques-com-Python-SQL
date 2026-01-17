from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    raw_csv = base_dir / "data" / "raw" / "transactions_raw.csv"
    db_path = base_dir / "data" / "processed" / "backoffice.db"
    sql_path = base_dir / "sql" / "create_tables.sql"

    if not raw_csv.exists():
        raise FileNotFoundError(f"CSV nao encontrado: {raw_csv}")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(raw_csv)

    with sqlite3.connect(db_path) as conn:
        # cria tabelas
        create_sql = sql_path.read_text(encoding="utf-8")
        conn.executescript(create_sql)

        # carrega dados
        df.to_sql("transactions", conn, if_exists="append", index=False)

        # checagem
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM transactions;")
        total = cur.fetchone()[0]

    print(f"[OK] SQLite criado e populado: {db_path}")
    print(f"[OK] Linhas inseridas: {total}")


if __name__ == "__main__":
    main()
