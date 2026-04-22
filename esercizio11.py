import json

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
    numero = input("Inseriscil il numero del contatto: ")

    contatto = Rubrica(nome, cognome, numero)

    try:
        with open("rubrica.json", "r") as f:
            contatti = json.load(f)

    except FileNotFoundError:
        contatti = []

    contatti.append({"nome": nome, "cognome": cognome, "numero": numero})

    with open("rubrica.json", "w") as f:
        json.dump(contatti, f)

def cerca_contatto():
    
    cognome_cerca = input("Inserisci il cognome del contatto che vuoi cercare: ")

    try:
        with open("rubrica.json", "r") as f:
            contatti = json.load(f)

            for elemento in contatti:
                if elemento["cognome"] == cognome_cerca:
                    contatto = Rubrica(elemento["nome"], elemento["cognome"], elemento["numero"])

                    print(contatto.mostra())

    except FileNotFoundError:
        return("Nessun contatto trovato!")
    

def visualizza_contatti():
    try:
        with open("rubrica.json", "r") as f:
            contatti = json.load(f)

            for elemento in contatti:
                contatto = Rubrica(elemento["nome"], elemento["cognome"], elemento["numero"])

                print(contatto.mostra())

    except FileNotFoundError:
        return("Nessun contatto nella rubrica!")

while True:

    print("1 - Aggiungi Contatto")
    print("2 - Cerca Contatto")
    print("3 - Visualizza Rubrica")
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