import random

numero = random.randint(1, 100)
tentativi = 1

tentativo = int(input("Indovina il numero tra 1 e 100: "))

while tentativo != numero:
    if tentativo < numero:
        print(f"Il numero che hai inserito è minore del numero casuale.")
        tentativo = int(input("Riprova: "))
    elif tentativo > numero:
        print("Il numero che hai inserito è maggiore del numero casuale.")
        tentativo = int(input("Riprova: "))
    
    tentativi += 1

print(f"Congratulazioni!! Hai indovinato!!Ci hai messo {tentativi} tentativi ") 