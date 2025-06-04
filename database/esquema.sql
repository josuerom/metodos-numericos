CREATE TABLE IF NOT EXISTS historial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metodo TEXT,
    entrada TEXT,
    resultado TEXT,
    explicacion TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);