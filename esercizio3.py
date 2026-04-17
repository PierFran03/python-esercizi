numeri = []

for i in range(2):
    numero = int(input(f"inserisci il numero {i+1} di 2:"))
    numeri.append(numero)

print(f"I numeri inseriti sono {numeri}")

operazione = input("Quale operazione vuoi fare? (+, -, *, /): ")

if operazione == "+":
    risultato = sum(numeri)
    
elif operazione == "-":
    risultato = numeri[0] - numeri[1]
    
elif operazione == "*":
    risultato = numeri[0] * numeri[1]

elif operazione == "/":
    if numeri[1] == 0:
        print("Errore, non si può dividere per 0!!")
    else:
        risultato = numeri[0] / numeri[1]

print(f"il risultato è {risultato}")

    
