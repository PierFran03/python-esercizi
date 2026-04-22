import sqlite3

conn = sqlite3.connect("scuola.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cognome TEXT,
        voto INTEGER
    )
""")

conn.commit()
print("Database creato con successo!")

cursor.execute("INSERT INTO studenti (nome, cognome, voto) VALUES (?, ?, ?)", ("Mario", "Rossi", 95))
cursor.execute("INSERT INTO studenti (nome, cognome, voto) VALUES (?, ?, ?)", ("Anna", "Bianchi", 88))
cursor.execute("INSERT INTO studenti (nome, cognome, voto) VALUES (?, ?, ?)", ("Luca", "Verdi", 72))

conn.commit()
conn.close()

print("Studenti inseriti!")