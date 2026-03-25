import sqlite3

def get_connection():
    return sqlite3.connect("test_results.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_name TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()