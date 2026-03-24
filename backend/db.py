import sqlite3

def init_db():
    conn = sqlite3.connect("test_history.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_name TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()