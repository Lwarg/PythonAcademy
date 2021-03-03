from Articolo import Articolo 

class CD (Articolo):
    # Classe figlia della classe Articolo

    def __init__(self, collocazione, titolo, autore, tipo, genere):
        Articolo.__init__(self, collocazione, titolo, autore, tipo)
        self.genere = genere

    def durataPrestito(self, durata=7):
        # I CD sono articoli che possono essere prestati per 7 giorni anziché 30
        durata = int(durata)
        return durata