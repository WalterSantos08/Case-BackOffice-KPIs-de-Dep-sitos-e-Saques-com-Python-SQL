DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    transaction_id        INTEGER PRIMARY KEY,
    user_id               INTEGER NOT NULL,
    created_at            TEXT NOT NULL,
    type                  TEXT NOT NULL CHECK (type IN ('deposit','withdraw')),
    status                TEXT NOT NULL CHECK (status IN ('approved','denied','pending')),
    method                TEXT NOT NULL,
    channel               TEXT NOT NULL,
    provider              TEXT NOT NULL,
    amount                REAL NOT NULL,
    currency              TEXT NOT NULL,
    processing_time_min   INTEGER NOT NULL,
    reject_reason         TEXT
);

CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_transactions_type ON transactions(type);
CREATE INDEX idx_transactions_status ON transactions(status);
