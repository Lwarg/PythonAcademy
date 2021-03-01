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


istogramma()

