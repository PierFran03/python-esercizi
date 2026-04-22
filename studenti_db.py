import sqlite3

conn = sqlite3.connect("scuola.db")
cursor = conn.cursor()

def visualizza_studenti():
    cursor.execute("SELECT * FROM studenti")
    studenti = cursor.fetchall()

    for studente in studenti:
        print(f"ID: {studente[0]} | Nome: {studente[1]} {studente[2]} | Voto: {studente[3]}")

def aggiungi_studente():
    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    voto = int(input("Inserisci il voto dello studente: "))

    cursor.execute("INSERT INTO studenti (nome, cognome, voto) VALUES (?, ?, ?)", (nome, cognome, voto))

    conn.commit()
    print("Studente aggiunto!")

def cerca_studente():
    cerca_cognome = input("Inserisci il cognome dello studente che vuoi cercare: ")

    cursor.execute("SELECT * FROM studenti WHERE cognome = ?", (cerca_cognome,))

    studenti = cursor.fetchall()

    for studente in studenti:
        print(f"ID: {studente[0]} | Nome: {studente[1]} {studente[2]} | Voto: {studente[3]}")

def elimina_studente():
    visualizza_studenti()
    id_elimina = int(input("Inserisci l'ID dello studente che vuoi eliminare: "))

    cursor.execute("DELETE FROM studenti WHERE cognome = ?", (id_elimina,))
    conn.commit()
    print("Studente eliminato!")


while True:
    print("1 - Visualizza studenti")
    print("2 - Aggiungi studente")
    print("3 - Cerca studente")
    print("4 - Elimina studente")
    print("5 - Esci")

    scelta = input("Cosa vuoi fare?")

    if scelta == "1":
        visualizza_studenti()

    elif scelta == "2":
        aggiungi_studente()

    elif scelta == "3":
        cerca_studente()

    elif scelta == "4":
        elimina_studente()

    else:
        break

    

