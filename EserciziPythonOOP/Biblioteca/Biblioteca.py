from Cliente import Cliente
from Studente import Studente
from Libro import Libro
from CD import CD
from Prestito import Prestito

class Biblioteca:

    def __init__(self, denominazione, luogo, listaArticoli=[], listaPrestiti=[], listaClienti=[]):
        self.denominazione = denominazione 
        self.luogo = luogo
        self.listaArticoli = listaArticoli
        self.listaPrestiti = listaPrestiti
        self.listaClienti = listaClienti


    def getListaPrestiti(self):
        return self.listaPrestiti
    
    def getListaArticoli(self):
        return self.listaArticoli
    
    def getListaClienti(self):
        return self.listaClienti

    def aggiungiCliente(self, nome, cognome):
        self.listaClienti.append(Cliente(nome, cognome))
        print("Aggiunto nuovo cliente")
    
    def aggiungiStudente(self, nome, cognome, facolta="non specificata"):
        self.listaClienti.append(Studente(nome, cognome, facolta))
        print("Aggiunto nuovo studente")

    def aggiungiArticolo(self, collocazione, titolo, autore, genere, tipo):
        if tipo != "libro" and tipo != "CD":
            print("Tipo non supportato")
        elif tipo == "libro":
            self.listaArticoli.append(Libro(collocazione, titolo, autore, tipo, genere))
            print("Aggiunto nuovo libro")
        else:
            self.listaArticoli.append(CD(collocazione, titolo, autore, tipo, genere))
            print("Aggiunto nuovo CD")

    def cercaCliente(self, nome, cognome):
        for cliente in self.listaClienti:
            if cliente.nome == nome and cliente.cognome == cognome:
                return cliente
        print("Cliente", nome, cognome, "non esiste")
        return 0

    def cercaArticolo(self, titolo, autore):
        for articolo in self.listaArticoli:
            if articolo.titolo == titolo and articolo.autore == autore:
                return articolo
        print("Articolo", titolo, autore, "non esiste")
        return 0

    def registraPrestito(self, titolo, autore, nomeCliente, cognomeCliente, dataPrestito):
        cliente = self.cercaCliente(nomeCliente, cognomeCliente)
        articolo = self.cercaArticolo(titolo, autore)
        if cliente == 0:
            print("Cliente",nomeCliente, cognomeCliente, "non iscritto alla biblioteca")
        elif articolo == 0:
            print("Articolo", titolo, autore, "non trovato")
        else:
            cliente
            self.listaPrestiti.append(Prestito(cliente, articolo, dataPrestito))
            print("Prestito registrato correttmente")


