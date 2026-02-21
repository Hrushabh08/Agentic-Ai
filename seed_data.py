from database import create_connection, create_table

def seed():
    create_table()
    conn = create_connection()
    cursor = conn.cursor()

    medicines = [
        (1, "Amlodipine", "5mg", 100, 1),
        (2, "Paracetamol", "500mg", 200, 0),
        (3, "Metformin", "500mg", 150, 1),
        (4, "Cough Syrup", "100ml", 50, 0),
        (5, "Azithromycin", "250mg", 75, 1),
        (6, "Vitamin C", "500mg", 120, 0),
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO medicines
    (id, name, dosage, stock, prescription_required)
    VALUES (?, ?, ?, ?, ?)
    """, medicines)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
