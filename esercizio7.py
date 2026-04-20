def aggiungi_appunto():
    testo = input("Inserisci il testo che vuoi aggiungere: ")
    with open("file.txt", "a") as f:
        f.write(testo + "\n")

def leggi_appunti():
    try:
        with open("file.txt", "r") as f:
            contenuto = f.read()
            print(f"{contenuto}")

    except FileNotFoundError:
        print("Nessun appunto trovato!")


while True:

    print("1 - Aggiungi Appunti")
    print("2 - Leggi Appunti")
    print("3 - Esci")

    scelta = input("Cosa intendi fare?")

    if scelta == "1":
        aggiungi_appunto()

    elif scelta == "2":
        leggi_appunti()
    
    else:
        break

