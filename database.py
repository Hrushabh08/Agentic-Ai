import sqlite3

def create_connection():
    conn = sqlite3.connect("pharmacy.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dosage TEXT NOT NULL,
        stock INTEGER NOT NULL,
        prescription_required BOOLEAN NOT NULL
    )
    """)

    conn.commit()
    conn.close()
