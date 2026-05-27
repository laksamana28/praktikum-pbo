import sqlite3
from konfigurasi import DB_PATH

def setup_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deskripsi TEXT NOT NULL,
        jumlah REAL NOT NULL,
        kategori TEXT,
        tanggal DATE NOT NULL
    )
    """)

    conn.commit()

    conn.close()

    print("Database berhasil dibuat")


if __name__ == "__main__":
    setup_database()