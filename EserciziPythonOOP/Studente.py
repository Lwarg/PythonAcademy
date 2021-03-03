from Cliente import Cliente

class Studente (Cliente):
    # Classe figlia della classe Cliente

    def __init__(self, nome, cognome, facolta="non specificata"):
        Cliente.__init__(self, nome, cognome)
        self.facolta = facolta # di default può non essere specificata

    def bonusGiorniPrestito(self):
        # gli studenti hanno diritto a 10 giorni bonus per i prestiti
        return 10

    def isStudente(self):
        return True
