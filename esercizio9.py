class Rubrica:
    def __init__(self, nome, cognome, numero):
        self.nome = nome
        self.cognome = cognome
        self.numero = numero

    def mostra(self):
        return f"{self.nome}, {self.cognome}, {self.numero}"
    

def crea_contatto():
    nome = input("Inserisci il nome del contatto: ")
    cognome = input("Inserisci il cognome del contatto: ")
    numero = (input("Inserisci il numero del contatto: "))

    contatto = Rubrica(nome, cognome, numero)

    with open ("rubrica.txt", "a") as f:
        f.write(f"{contatto.nome}, {contatto.cognome}, {contatto.numero}\n")


def cerca_contatto():
    cognome_cerca = input("Inserisci il cognome da voler cerca: ")

    try:
        with open("rubrica.txt", "r") as f:
            for riga in f:
                valori = riga.strip().split(",")
                contatto = Rubrica(valori[0], valori[1], valori[2])

                if contatto.cognome == cognome_cerca:
                    print(contatto.mostra())

    except FileNotFoundError:
        print("Nessun contatto trovato!")


def visualizza_contatti():
    try:
        with open("rubrica.txt", "r") as f:
            for riga in f:
                valori = riga.strip().split(",")
                contatto = Rubrica(valori[0], valori[1], valori[2])
                print(contatto.mostra())

    except FileNotFoundError:
        print("Nessun contatto trovato!")


while True:
    print("1 - Aggiungi un contatto")
    print("2 - Cerca un contatto")
    print("3 - Visualizza contatti")
    print("4 - Esci")

    scelta = input("Cosa vuoi fare?")

    if scelta == "1":
        crea_contatto()
    
    elif scelta == "2":
        cerca_contatto()

    elif scelta == "3":
        visualizza_contatti()

    else:
        break


