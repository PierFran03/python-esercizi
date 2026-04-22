numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati = [n ** 2 for n in numeri]

print(f"{quadrati}")

parole = ["ciao", "python", "casa", "programmazione", "gatto"]

quattro_lettere = [n for n in parole if len(n) > 4]
print(f"{quattro_lettere}")