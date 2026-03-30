import sqlite3

conn = sqlite3.connect("network.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src TEXT,
    dst TEXT,
    port INTEGER,
    size INTEGER,
    status TEXT
)
""")

def log_data(src, dst, port, size, status):
    cursor.execute("INSERT INTO logs (src, dst, port, size, status) VALUES (?, ?, ?, ?, ?)",
                   (src, dst, port, size, status))
    conn.commit()

def get_logs():
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 50")
    return cursor.fetchall()
