import sqlite3

conn = sqlite3.connect("scuola.db")
cursor = conn.cursor()

conn.commit()

cursor.execute("SELECT * FROM studenti")
studenti = cursor.fetchall()

for studente in studenti:
    print(f"ID: {studente[0]} | Nome: {studente[1]} {studente[2]} | Voto: {studente[3]}")

conn.close()