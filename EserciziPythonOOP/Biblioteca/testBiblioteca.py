import Cliente
import Studente
import Libro
import CD
import Biblioteca as B
import Prestito


# creo l'oggetto biblioteca e lo chiamo b
b = B.Biblioteca("Biblioteca Civica di Trieste", "Trieste")

# aggiungo i clienti
b.aggiungiCliente("Giacomo", "Rossi")
b.aggiungiStudente("Mario", "Resistenza")
b.aggiungiCliente("Max", "Brutus")
b.aggiungiCliente("Bruno", "Verdi")

## questo ciclo deve stampare nome e cognome dei clienti
#for cliente in b.getListaClienti():
#    print(cliente.nome, cliente.cognome) 

## interroghiamo l'oggetto biblioteca per cercare un cliente
## e vedere se e` uno studente 
#mb = b.cercaCliente("Max", "Brutus") 
#print(mb.nome)
#print(mb.cognome)
#print(mb.isStudente())
#print(mb.bonusGiorniPrestito())

# aggiungo degli articoli:
b.aggiungiArticolo("CD06", "Pink Floyd", "The Wall", "Rock", "CD")
b.aggiungiArticolo("L205", "Schopenhauer", "Il mondo come volontà", "Filosofia", "libro")
b.aggiungiArticolo("L208", "Freud", "L'interpretazione dei Sogni", "Filosofia", "libro") 

## richiedo la lista degli articoli:
#for i in b.getListaArticoli():
#    print(i.titolo, i.autore, i.genere)

# aggiungo dei prestiti
b.registraPrestito("Pink Floyd", "The Wall", "Giacomo", "Rossi", "12-01-2012")
b.registraPrestito("Schopenhauer", "Il mondo come volontà", "Mario", "Resistenza", "8-12-2012")

# richiedo la lista dei prestiti:
for prestito in b.getListaPrestiti():
    print(prestito.cliente.nome, prestito.cliente.cognome, prestito.dataInizioPrestito, 
    prestito.durataPrestito(), prestito.articolo.titolo, prestito.articolo.autore) 
