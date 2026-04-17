from datetime import date

nome = input("Inserisci il tuo nome: ")
anno_di_nascita = input("Anno di nascita: ")
anno_di_nascita = int(anno_di_nascita)

anno_corrente = date.today().year

eta = anno_corrente - anno_di_nascita

print(f"Ciao {nome}, hai {eta} anni")
