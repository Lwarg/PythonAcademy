from Articolo import Articolo 

class Libro (Articolo):
    # Classe figlia della classe Articolo

    def __init__(self, collocazione, titolo, autore, tipo, genere):
        Articolo.__init__(self, collocazione, titolo, autore, tipo)
        self.genere = genere
        