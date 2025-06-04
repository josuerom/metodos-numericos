import sqlite3

def connect():
    return sqlite3.connect("database/metodos.db")

def save_result(method, input_data, result, explanation):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metodo TEXT,
            entrada TEXT,
            resultado TEXT,
            explicacion TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("INSERT INTO historial (metodo, entrada, resultado, explicacion) VALUES (?, ?, ?, ?)",
                   (method, str(input_data), str(result), str(explanation)))
    conn.commit()
    conn.close()