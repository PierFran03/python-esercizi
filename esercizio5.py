rubrica = {}

while True:

    print("1 - Aggiungi Contatto")
    print("2 - Cerca contatto")
    print("3 - Visualizza tutti")
    print("4 - Esci")

    scelta = input("Cosa vuoi fare? ")

    if scelta == "1":
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        numero = input("Numero: ")
        rubrica[f"{nome} {cognome}"] = numero
        print(f"Il contatto {nome} {cognome} {numero} è stato salvato correttamente!!")

    elif scelta == "2":
        nome = input("Nome: ")
        cognome = input("Cognome: ")

        if f"{nome} {cognome}" in rubrica:
            print(f"{nome} {cognome} {rubrica[f'{nome} {cognome}']}")
        else:
            print("Contatto non trovato!")
        
    elif scelta == "3":
        
        if len(rubrica) == 0:
            print("La rubrica è vuota!")

        else:

            for contatto, numero in rubrica.items():
                print(f"{contatto}: {numero}")

    elif scelta == "4":
        break