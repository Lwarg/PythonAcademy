

def charInString(stringa, carattere):
    n = 0
    i = 0
    while i < len(stringa):
        if stringa[i] == carattere:
            n += 1
        i += 1
    return n

def ilPiuGrande(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return

def confronto():
    # 0 non viene confrontato, serve a terminare il programma
    n1 = int(input("Inserire numero "))
    n2 = n1
    while n2 != 0:
        n2 = int(input("Inserire numero "))
        n1 = ilPiuGrande(n1, n2)
    return n1

def isTriangle (a, b, c):
	#stampa "sì" se i tre lati dati in input possono formare un triangolo, "no" altrimenti
    if a+b > c and b+c > a and c+a > b:
        print("sì")
    elif a+b == c or b+c == a or c+a == b:
        print("Triangolo degenere")
    else:
        print("no")
	
def sommatrice():
    # 0  serve a terminare il programma
    n1 = int(input("Inserire numero "))
    n2 = n1
    while n2 != 0:
        n2 = int(input("Inserire numero "))
        n1 = n1+n2
    return n1

def lunghezza():
    stringa = input("Inserire il testo: \n")
    count = 0
    for i in stringa:
        if i != " ":
            count += 1
    return count

def indovinaNumero():
    import random
    target = random.randint(1, 1000)
    flag = True
    while flag:
        guess = int(input("Indovina il numero: "))
        if guess != target:
            check = " è più piccolo" if guess > target else " è più grande"
            print("il numero", check)
        else:
            flag = False
            print("Bravo!")
    return

def limiteSommaPrecedenti():
    # Trova il numero K tale che la somma dei numeri da 0 a K sia minore dell'input N
    flag = True
    while flag:
        N = int(input("Inserire numero: "))
        if N > 0:
            flag = False
    K = 0
    sum = 0
    while sum < N:
        K +=1
        sum = sum + K
    K = K-1
    return K

def printaNumeri(a, b):
    if a>b: # ordine decrescente perchè il primo numero è più grande
        for i in range(a,b,-1):
            print(i)
    else: # ordine decrescente perchè il primo è più piccolo
        for i in range(a,b): 
            print(i)


def compreso(a, b, c):
    if a<=b<=c:
        print("compreso")
    else:
        print("non compreso")

def palindromo():
    parola = input("Inserire testo: ")
    for i in range(len(parola)):
        if parola[i]!=parola[-1-i]:
            print("Non è buono")
            break
    
def istogramma():
    quanti = int(input("Quanti elementi da valutare? "))
    istogramma = "\n"
    for i in range(quanti):
        valore = int(input("Valore elemento: "))
        istogramma = istogramma + valore*"*" +"\n"
    
    print(istogramma)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

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



def mergeDizionario(d1, d2):
    d3 = d2.copy()
    for k1 in d1:
        if k1 in d2:
            d3[k1] = d1[k1]+d2[k1]
        else:
            d3[k1] = d2[k1]
            
    return d3

def mergeList(a1, a2):
    # Inizializza una lista copiando la più lunga tra a1 e a2
    if len(a1) >= len(a2):
        a3 = a1.copy()
        l = len(a2)
    else:
        a3 = a2.copy()
        l = len(a1)
    # Cicla sulla lunghezza più corta aggiungendo i valori
    for i in range(l):
        a3[i] = a1[i]+a2[i]
    return a3   

def printField(sig):
    print(sig[0][0],'|',sig[0][1],'|',sig[0][2])
    print('----------')
    print(sig[1][0],'|',sig[1][1],'|',sig[1][2])
    print('----------')
    print(sig[2][0],'|',sig[2][1],'|',sig[2][2])

def tris():
    import numpy as np
    print('player 1: x, player 2: o')
    occ = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])
    sig = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

    winFlag = False
    while not winFlag:
        # PLAYER 1
        print("Tocca a Player 1")
        flag = True
        while flag:
            # inserimento mossa
            ok = False
            while not ok:
                    rig = int(input("Inserisci riga (da 1 a 3): "))
                    rig -= 1
                    col = int(input("Inserisci colonna (da 1 a 3): "))
                    col -= 1
                    if 0<=rig<=2 and 0<=col<=2:
                        ok = True
                    else:
                        print('Inserisci numeri validi')
            if occ[rig][col] == 0:
                occ[rig][col] = 1
                sig[rig][col] = 'x'
                printField(sig)
                flag = False
            else:
                print("Casella occupata, scegline un'altra...")
            # check vittoria
            win1 = np.array([1, 1, 1])
            if (occ[:,0]==win1).all() or (occ[:,1]==win1).all() or (occ[:,2]==win1).all() or (occ[0,:]==win1).all() or (occ[1,:]==win1).all() or (occ[2,:]==win1).all() or (np.diag(occ)==win1).all() or (np.diag(np.fliplr(occ))==win1).all():
                winFlag = True
                print("Player 1 ha vinto!")

        # PLAYER 2
        if not winFlag:
            print("Tocca a Player 2")
            flag = True
            while flag:
                # inserimento mossa
                ok = False
                while not ok:
                    rig = int(input("Inserisci riga (da 1 a 3): "))
                    rig -= 1
                    col = int(input("Inserisci colonna (da 1 a 3): "))
                    col -= 1
                    if 0<=rig<=2 and 0<=col<=2:
                        ok = True
                    else:
                        print('Inserisci numeri validi')
                if occ[rig][col] == 0:
                    occ[rig][col] = 2
                    sig[rig][col] = 'o'
                    printField(sig)
                    flag = False
                else:
                    print("Casella occupata, scegline un'altra...")
                # check vittoria
                win1 = np.array([2, 2, 2])
                if (occ[:,0]==win1).all() or (occ[:,1]==win1).all() or (occ[:,2]==win1).all() or (occ[0,:]==win1).all() or (occ[1,:]==win1).all() or (occ[2,:]==win1).all() or (np.diag(occ)==win1).all() or (np.diag(np.fliplr(occ))==win1).all():
                    winFlag = True
                    print("Player 2 ha vinto!")
            

def initChessboard(rows, columns):
    board = a = [[' ']*columns]*rows
    return board

def printChessboard(sig):
    for i in range(len(sig)):
        stampa = ' | '
        for j in range(len(sig[i])):
            stampa = stampa+sig[i][j]+" | "
        print(stampa)
        print(' -'+len(sig[i])*4*'-')


def forza4():
    import numpy as np
    sig = [[' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' '],
           [' ',' ',' ',' ', ' ', ' ', ' ', ' ']]
    printChessboard(sig)
    occ = np.zeros([8,8])
    winFlag = False
    while not winFlag:
        # PLAYER 1
        print("Tocca a Player 1")
        flag = True
        while flag:
            # inserimento mossa
            col = int(input("Scegli colonna (da 1 a 8): "))
            col -= 1
            if occ[0][col] == 0:
                for i in range(8):
                    if occ[-i-1][col] == 0:
                        occ[-i-1][col] = 1
                        sig[7-i][col] = 'x'
                        break
                printChessboard(sig)
            else:
                print("Colonna piena, scegline un'altra...")
            flag = False

        # PLAYER 2
        if not winFlag:
            print("Tocca a Player 2")
            flag = True
            while flag:
                # inserimento mossa
                col = int(input("Scegli colonna (da 1 a 8): "))
                col -= 1
                if occ[0][col] == 0:
                    for i in range(8):
                        if occ[-i-1][col] == 0:
                            occ[-i-1][col] = 2
                            sig[7-i][col] = 'o'
                            break
                    printChessboard(sig)
                else:
                    print("Colonna piena, scegline un'altra...")
                flag = False

def vecinmat(vec, mat):
  flag = False
  for i in range(len(mat)):
      for j in range(len(mat[0])):
          if mat[i,j] == vec[0]:
              verticale = mat[i:i+4,j] if i+3 < 8 else np.array([0,0,0,0])
              orizzontale = mat[i,j:j+4] if j+3 < 8 else np.array([0,0,0,0])
              diagonale = np.diag(mat[i:i+4,j:j+4]) if i+3 < 8 and j+3 < 8 else np.array([0,0,0,0])
              diag2 = np.diag(np.fliplr(mat[i:i+4,j-3:j+1])) if i+3 < 8 and j-4 >= 0 else np.array([0,0,0,0])
              if (verticale==vec).all() or (orizzontale==vec).all() or (diagonale==vec).all() or (diag2==vec).all():
                  flag = True
              break
      if flag:
          return True
  return False      

def quantiCarNum(testo):
    digits = "1234567890"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = ",;.:-_!\\|\"£$%&/()='?^*+#@]["
    contaD = 0
    contaL = 0
    contaS = 0
    for i in testo:
        for n in digits:
            if i==n:
                contaD += 1
                break
        for l in letters:
            if i==l:
                contaL +=1
                break
        for s in special:
            if i==s:
                contaS +=1
                break
    print("Ci sono", contaD, "cifre")
    print("Ci sono", contaL,"lettere")
    print(("Ci sono", contaS,"caratteri speciali"))

def chatroom_status(chatroom):
    if len(chatroom)==0:
        print("no one online")
    elif len(chatroom)==1:
        print(chatroom[0],"online")
    elif len(chatroom)==2:
        print(chatroom[0], "and", chatroom[1], "online")
    else:
        print(chatroom[0]+",", chatroom[1], "and other",len(chatroom)-2,"online")

def missing_num(num):
    for i in range(1,11):
        if i not in num:
            return i

def add_indexes(num):
    for i in range(len(num)):
        num[i] = num[i] + i
    return num

def index_of_caps(text):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = list()
    for i in range(len(text)):
        if text[i] in caps:
            out.append(i)
    return out

def name_shuffle(name):
    namein = name.split(' ')
    nameout = namein[1]+' '+namein[0]
    return nameout 

def number_sum(lista):
    sum = 0
    for i in lista:
        if type(i)==int or type(i)==float:
            sum = sum + i
    return sum

def get_indices(lista, element):
    out  = list()
    for i in range(len(lista)):
        if lista[i] == element:
            out.append(i)
    return out

def number_length(num):
    numstr = str(num)
    length = 0
    for i in numstr:
        length += 1
    return length

def combination(*args):
    out = 1
    count0 = get_indices(args, 0)
    if len(count0) == len(args):
        return 0
    else:
        for i in args:
            if i != 0:
                out = out*i
    return out

def factorial(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    elif n<0:
        return "No factorial"
    else:
        return n*factorial(n-1)


def pascal_triangle(val):
    out = list()
    for n in range(val):
        rowlist = list()
        for k in range(n+1):
            rowlist.append(int(factorial(n)/(factorial(k)*factorial(n-k))))            
        out.append(rowlist)
    return out
