-- 1) Visao geral: total depositado x sacado
SELECT
  type,
  COUNT(*) AS qtd,
  ROUND(SUM(amount), 2) AS total
FROM transactions
GROUP BY type;

-- 2) Taxa de aprovacao por tipo
SELECT
  type,
  ROUND(100.0 * SUM(CASE WHEN status='approved' THEN 1 ELSE 0 END) / COUNT(*), 2) AS approval_rate_pct
FROM transactions
GROUP BY type;

-- 3) Status por dia (serie temporal)
SELECT
  substr(created_at, 1, 10) AS day,
  type,
  status,
  COUNT(*) AS qtd,
  ROUND(SUM(amount), 2) AS total
FROM transactions
GROUP BY day, type, status
ORDER BY day;

-- 4) Tempo medio de processamento (somente approved) por tipo
SELECT
  type,
  ROUND(AVG(processing_time_min), 2) AS avg_time_min
FROM transactions
WHERE status='approved'
GROUP BY type;

-- 5) Top motivos de rejeicao (withdraw)
SELECT
  reject_reason,
  COUNT(*) AS qtd
FROM transactions
WHERE status='denied'
  AND type='withdraw'
GROUP BY reject_reason
ORDER BY qtd DESC
LIMIT 10;

-- 6) Metodos com mais rejeicao (withdraw)
SELECT
  method,
  COUNT(*) AS qtd
FROM transactions
WHERE status='denied'
  AND type='withdraw'
GROUP BY method
ORDER BY qtd DESC;
