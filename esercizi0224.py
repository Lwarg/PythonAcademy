
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

        

#forza4()



