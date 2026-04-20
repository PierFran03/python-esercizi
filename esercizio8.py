class Studente:
    def __init__ (self, nome, cognome, eta, voto):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.voto = voto

    def presentati(self):
        return f"Salve io sono {self.nome} {self.cognome} e ho {self.eta} anni"
    
    def promosso(self):
        if self.voto > 66:
            print("Promosso")
        else:
            print("Non idoneo per la laurea")
        

studente1 = Studente("Pierpaolo", "Franchini", 23, 99)
print(studente1.presentati())
studente1.promosso()

studente2 = Studente("Cosimo", "Franchini", 25, 110)
print(studente2.presentati())
studente2.promosso()

studente3 = Studente("Simone", "Patrono", 23, 40)
print(studente3.presentati())
studente3.promosso()