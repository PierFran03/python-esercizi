numeri = []

for i in range(5):
    numero = int(input(f"inserisci il numero {i+1} di 5:"))
    numeri.append(numero)

print(numeri)
    
massimo = max(numeri)
minimo = min(numeri)
media = sum(numeri) / len(numeri)

print(f"il massimo è: {massimo}, il minimo è: {minimo}, la media è: {media}")