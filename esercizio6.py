def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "Il numero inserito è pari"
    else:
        return "Il numero inserito è dispari"

def massimo_tre(a, b, c):
    if a > b and a > c:
        return f"{a} è il numero più grande fra i tre inseriti"
    elif b > a and b > c:
        return f"{b} è il numero più grande fra i tre inseriti"
    else:
        return f"{c} è il numero più grande fra i tre inseriti"

def inverti_stringa(testo):
    return testo[::-1]

numero = int(input("Inserisci un numero: "))
print(pari_o_dispari(numero))

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))

print(massimo_tre(a, b, c))

testo = input("Inserisci la stringa che vuoi invertire: ")
print(inverti_stringa(testo))