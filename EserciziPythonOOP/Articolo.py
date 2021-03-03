class Articolo:

    def __init__(self, collocazione, titolo, autore, tipo):
        # gli input sono tutti di tipo stringa
        self.collocazione = collocazione  # nella biblioteca gli articoli saranno catalogati
        self.titolo = titolo
        self.autore = autore
        self.tipo = tipo # gli articoli sono libri o CD

    def durataPrestito(self, durata=30):
        # La durata di un prestito è di default 30 giorni, ma si potrebbe anche modificare
        durata = int(durata)
        return durata

    