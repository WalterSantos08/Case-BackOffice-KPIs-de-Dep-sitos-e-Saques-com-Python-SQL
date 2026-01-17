import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    base_dir = Path(__file__).resolve().parents[1]
    db_path = base_dir / "data" / "processed" / "backoffice.db"

    if not db_path.exists():
        print(f"[ERRO] Banco não encontrado: {db_path}")
        return

    # Lê do SQLite
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query("SELECT * FROM transactions;", conn)

    # Conversões
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["processing_time_min"] = pd.to_numeric(df["processing_time_min"], errors="coerce")

    # Cria colunas de data
    df["day"] = df["created_at"].dt.date.astype(str)

    # Pastas de saída
    out_dir = base_dir / "outputs"
    charts_dir = out_dir / "graficos"
    out_dir.mkdir(parents=True, exist_ok=True)
    charts_dir.mkdir(parents=True, exist_ok=True)

    # KPIs gerais
    total_transacoes = len(df)
    total_valor = round(df["amount"].sum(), 2)
    approval_rate = round((df["status"].eq("approved").mean() * 100), 2)

    resumo = pd.DataFrame([{
        "total_transacoes": total_transacoes,
        "total_valor": total_valor,
        "approval_rate_pct": approval_rate,
        "inicio": str(df["created_at"].min()),
        "fim": str(df["created_at"].max())
    }])

    resumo.to_csv(out_dir / "kpis_resumo.csv", index=False, encoding="utf-8")

    # KPIs por tipo
    por_tipo = (
        df.groupby("type")
        .agg(
            qtd=("transaction_id", "count"),
            total=("amount", "sum"),
            approval_rate_pct=("status", lambda s: (s.eq("approved").mean() * 100)),
            avg_time_min=("processing_time_min", "mean"),
        )
        .reset_index()
    )

    por_tipo["total"] = por_tipo["total"].round(2)
    por_tipo["approval_rate_pct"] = por_tipo["approval_rate_pct"].round(2)
    por_tipo["avg_time_min"] = por_tipo["avg_time_min"].round(2)

    por_tipo.to_csv(out_dir / "kpis_por_tipo.csv", index=False, encoding="utf-8")

    # Gráfico 1: Total por dia (deposit x withdraw)
    daily = (
        df.groupby(["day", "type"])["amount"]
        .sum()
        .reset_index()
        .pivot(index="day", columns="type", values="amount")
        .fillna(0)
    )

    plt.figure()
    daily.plot()
    plt.title("Total (BRL) por dia - deposit x withdraw")
    plt.xlabel("Dia")
    plt.ylabel("Total (BRL)")
    plt.tight_layout()
    plt.savefig(charts_dir / "total_por_dia.png", dpi=150)
    plt.close()

    # Gráfico 2: Taxa de aprovação por tipo
    approval_by_type = (
        df.assign(is_approved=df["status"].eq("approved").astype(int))
        .groupby("type")["is_approved"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    plt.figure()
    approval_by_type.plot(kind="bar")
    plt.title("Taxa de aprovação (%) por tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Aprovação (%)")
    plt.tight_layout()
    plt.savefig(charts_dir / "approval_por_tipo.png", dpi=150)
    plt.close()

    # Gráfico 3: Top motivos de rejeição (withdraw)
    top_reject = (
        df[(df["status"] == "denied") & (df["type"] == "withdraw")]
        .groupby("reject_reason")["transaction_id"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    if len(top_reject) > 0:
        plt.figure()
        top_reject.plot(kind="bar")
        plt.title("Top 10 motivos de rejeição (withdraw)")
        plt.xlabel("Motivo")
        plt.ylabel("Qtd")
        plt.tight_layout()
        plt.savefig(charts_dir / "top_rejeicoes_withdraw.png", dpi=150)
        plt.close()

    print("[OK] Análise finalizada com sucesso!")
    print(f"[OK] Resumo salvo em: {out_dir / 'kpis_resumo.csv'}")
    print(f"[OK] KPIs por tipo salvo em: {out_dir / 'kpis_por_tipo.csv'}")
    print(f"[OK] Gráficos salvos em: {charts_dir}")


if __name__ == "__main__":
    main()
