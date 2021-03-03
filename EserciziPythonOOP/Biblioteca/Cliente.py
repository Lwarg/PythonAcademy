class Cliente:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def bonusGiorniPrestito(self):
        # Di base un cliente non ha giorni di prestito bonus
        return 0

    def isStudente(self):
        # Di base un cliente non è uno studente
        return False
