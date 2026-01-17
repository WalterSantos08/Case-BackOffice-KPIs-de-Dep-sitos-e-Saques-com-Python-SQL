from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=seconds)


def main() -> None:
    random.seed(42)

    base_dir = Path(__file__).resolve().parents[1]
    out_dir = base_dir / "data" / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)

    n = 5000  # quantidade de transacoes
    start = datetime.now() - timedelta(days=120)
    end = datetime.now()

    tipos = ["deposit", "withdraw"]
    metodos = ["pix", "card", "bank_transfer", "crypto"]
    canais = ["crm", "chat", "email", "app"]
    moedas = ["BRL"]

    motivos_rejeicao = [
        "KYC pendente",
        "Documento ilegivel",
        "Dados divergentes",
        "Suspeita de fraude",
        "Limite excedido",
        "Falha no provedor",
        "Conta bancaria invalida",
    ]

    rows = []
    for i in range(1, n + 1):
        tipo = random.choices(tipos, weights=[0.62, 0.38], k=1)[0]
        dt = random_date(start, end)

        # valores mais realistas
        if tipo == "deposit":
            valor = round(random.triangular(10, 2000, 120), 2)
        else:
            valor = round(random.triangular(20, 5000, 250), 2)

        metodo = random.choices(
            metodos,
            weights=[0.72, 0.18, 0.08, 0.02] if tipo == "deposit" else [0.68, 0.06, 0.23, 0.03],
            k=1
        )[0]

        canal = random.choice(canais)
        user_id = random.randint(1000, 9999)

        # status e tempos
        if tipo == "deposit":
            status = random.choices(["approved", "denied", "pending"], weights=[0.92, 0.05, 0.03], k=1)[0]
            tempo_min = int(random.triangular(1, 45, 5))
        else:
            status = random.choices(["approved", "denied", "pending"], weights=[0.78, 0.10, 0.12], k=1)[0]
            tempo_min = int(random.triangular(5, 1440, 90))  # ate 24h

        motivo = None
        if status == "denied":
            motivo = random.choice(motivos_rejeicao)

        provider = random.choice(["ProviderA", "ProviderB", "ProviderC"])

        rows.append(
            {
                "transaction_id": i,
                "user_id": user_id,
                "created_at": dt.strftime("%Y-%m-%d %H:%M:%S"),
                "type": tipo,
                "status": status,
                "method": metodo,
                "channel": canal,
                "provider": provider,
                "amount": valor,
                "currency": random.choice(moedas),
                "processing_time_min": tempo_min,
                "reject_reason": motivo,
            }
        )

    df = pd.DataFrame(rows)

    # regra simples: se pending, nao tem tempo final confiavel -> deixa, mas pode analisar separado
    out_path = out_dir / "transactions_raw.csv"
    df.to_csv(out_path, index=False, encoding="utf-8")

    print(f"[OK] CSV gerado em: {out_path}")
    print(df.head(5))


if __name__ == "__main__":
    main()
