class Cellulare:

    def __init__(self, carica, numeroChiamate):
        self.carica = carica
        self.numeroChiamate = numeroChiamate

    def ricarica(self, unaRicarica):
        # aumento la carica del cellulare con una ricarica
        self.carica += unaRicarica

    def chiamata(self, minutiDurata):
        # aumenta il numero di chiamate e diminuisce la carica
        self.numeroChiamate += 1
        count = 0
        # chiama finchè non esaurisci il credito o i minuti di chiamata (aggiornamento ogni secondo)
        while self.carica > 0.2/60 and minutiDurata > 0: 
            self.carica -= 0.2/60
            minutiDurata -= 1/60
            count += 1/60
        self.carica = int(self.carica*100)/100
        count = int(count*100)/100
        print("Minuti effettuati: ",count)

    def numero404(self):
        return self.carica

    def getNumeroChiamate(self):
        return self.numeroChiamate

    def azzeraChiamate(self):
        self.numeroChiamate = 0
                
    

