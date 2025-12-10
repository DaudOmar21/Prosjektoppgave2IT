import sqlite3

def init_db():
    conn = sqlite3.connect("kantine.db")
    cur = conn.cursor()
    with open("Scema.sql", "r", encoding="utf-8") as f:
        cur.executescript(f.read())

    products = [
        ("Skolebrød", "Saftig skolebrød med vaniljekrem og kokos.", 25.0, "Bakst", 20, ""),
        ("Vann 0.5L", "Mineralvann", 20.0, "Drikke", 50, ""),
        ("Pølse m/brød", "Rask pølse i brød", 30.0, "Hovedrett", 15, ""),
        ("Salatboks", "Frisk salat med kylling", 55.0, "Sunt", 8, "")
    ]

    cur.executemany(
        "INSERT INTO products (name, description, price, category, stock, image_url) VALUES (?, ?, ?, ?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()
    print("Database opprettet og prøveprodukter lagt inn.")

if __name__ == "__main__":
    init_db()
