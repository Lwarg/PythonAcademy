def leggiFile():
    fin = open('Settimana 1\Martedi\words.txt')
    print(fin.readline())
    print(fin.readline())
    fin.close()

def palindromo(parola):
    for i in range(len(parola)):
        if parola[i]!=parola[-1-i]:
            return False
    return True

# leggiFile()
# C:/Users/splin/Documents/Academy Python/Settimana 1/Martedi/words.txt

def stampaLunghezza():
    lunghezza = 20
    fin = open('Settimana 1\Martedi\words.txt')
    for line in fin:
        riga = fin.readline()
        if len(riga) > lunghezza:
            print(riga)


def stampaPalindrome():
    fin = open('Settimana 1\Martedi\words.txt')
    for riga in fin:
        parola = riga.strip()
        if palindromo(parola):
            print(parola)


def presenza(parola):
    fin = open('Settimana 1\Martedi\words.txt')
    for riga in fin:
        if riga.strip() == parola:
            return True
    return False

def creaFile(nome):
    path = 'Settimana 1\Martedi\\' + nome
    fout = open(path, 'w')
    line = "Ciao\n"
    fout.write(line)

def ordineLunghezza(a, b):
    i = 0
    # Prendiamo le misure della parola più corta
    if len(a) <= len(b):
        maxi = len(a) -1 
        stampa = (a, b)
    else:
        maxi = len(b)-1
        stampa = (b, a)

    return stampa

def ordineAlfabetico(a, b):
    i = 0
    # Prendiamo le misure della parola più corta
    if len(a) <= len(b):
        maxi = len(a) -1 
        stampa = (a, b)
    else:
        maxi = len(b)-1
        stampa = (b, a)

    # Iteriamo fino alla lunghezza della parola più corta
    while i < maxi:
        if a[i] < b[i]:
            return a,b
        elif a[i] == b[i]:
            i += 1
        else:
            return b,a
    
    # Se le parole hanno le stesse lettere ritorna prima la più corta
    return stampa

#def riscrivereDisordinato(oldfile, newfile):
#    import random 
#
#    fin = open(oldfile, 'r')  # apro file in lettura
#    listin = fin.read().split()  # crea una lista corrispondente al file letto
#
#    fout = open(newfile, 'w+') # apre nuovo file in scrittura
#    
#    iterazioni = len(listin)
#    for i in range(iterazioni):
#        seed = random.randint(0, len(listin)) # prendo l'indice in modo random
#        parola = listin[seed] #+ "\n" # aggiungo l'andare a capo
#        fout.write(parola) # scrivo la parola corrispondente
#        print("Numero iniziale di parole: ", iterazioni)
#        print("Seed attuale: ", seed)
#        print("Parola da scrivere: ", parola)
#        print("Lunghezza lista pre pop: ", len(listin))
#        listin.pop(seed) # rimuovo la parola dalla mia lista in modo da non 
#        print("Lunghezza lista post pop: ", len(listin))
#    return
#
#def riscrivereDisordinato1(oldfile, newfile):
#    import random 
#
#    fin = open(oldfile, 'r')  # apro file in lettura
#    listin = fin.read().split()  # crea una lista corrispondente al file letto
#
#    fout = open(newfile, 'w+') # apre nuovo file in scrittura
#    
#    # Rimescolo la lista
#    for i in range(len(listin)):
#        j = random.randint(0, len(listin)) # prendo un secondo indice a caso
#        listin[i], listin[j] = listin[j], listin[i] # scambio di posto due elementi della stringa
#    
#    for i in range(len(listin)):
#        fout.write(listin[i] + "\n") # scrivo la parola 
#    return

def riscrivereDisordinato(oldfile, newfile):
    import random 

    fin = open(oldfile, 'r')  # apro file in lettura
    listin = fin.read().split()  # crea una lista corrispondente al file letto

    fout = open(newfile, 'w+') # apre nuovo file in scrittura
    
    # Rimescolo la lista
    random.shuffle(listin)
    for i in listin:
        fout.write(i + "\n") # scrivo la parola 
    return


def prendiElementi(lista):
    import random
    newList = lista.copy()
    check = input("Scrivi qualcosa per un nuovo elemento")
    while check != ' ' and len(lista)>0:
        if len(lista) > 1:
            i = random.randint(0, len(lista)-1) # scelgo l'indice
            print(i)
            print(lista[i])
            lista.pop(i)
            print(lista)
            check = input("Scrivi qualcosa per un nuovo elemento")
        else:
            print(lista[0])
            print(lista)
            lista = newList.copy()


def azzeraDizionario(diz):
    import random
    chiavi = list(diz.keys()) #  lista delle chiavi per il sorteggio
    original = diz.copy()
    check = input("Scrivi qualcosa per estrarre di nuovo")
    while check != ' ' and len(chiavi)>0:
        i = random.randint(0, len(chiavi)-1) # scelgo l'indice
        if diz[chiavi[i]] > 0:
            diz[chiavi[i]] -= 1
            print(chiavi[i], "ha perso un punto")
            print(diz)
            if diz[chiavi[i]] == 0: # elimina la chiave dalla lista di sorteggio se il suo valore nel dizionario è azzerato
                print(chiavi[i], "è morto")
                chiavi.pop(i)
        if len(chiavi)==0: # chiavi non ha più elementi quando tutti i valori sono stati azzerati
            print("GAME OVER")
            diz = original.copy()
            chiavi = list(diz.keys())
            print("NEW GAME?")
        check = input("Scrivi qualcosa per estrarre di nuovo")


diz = {"tizio": 5, "caio": 5, "sempronio": 5, "toto":5} 
azzeraDizionario(diz)
