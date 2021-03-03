class Prestito:

    def __init__(self, cliente, articolo, dataInizioPrestito):
        self.cliente = cliente
        self.articolo = articolo
        self.dataInizioPrestito = dataInizioPrestito
    
    def durataPrestito(self):
        durata = self.articolo.durataPrestito() + self.cliente.bonusGiorniPrestito()
        return durata