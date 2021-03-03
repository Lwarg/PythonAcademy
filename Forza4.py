import tkinter as tk
import numpy as np

def restart():
    root.destroy()
    main()

def close():
    root.destroy()

def vecinmat(vec, mat):
    # vede se un vettore è contenuto in una matrice
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


def update_text(id):
    global testo
    global occ
    global root
    global btn0
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global textVar
    global textBox

    player = 1 if testo=='x' else 2
    player_colour = "red" if player==1 else "yellow"

    if occ[0][int(id)] == 0: # se la colonna è libera l'elemento corrispondente nella prima riga di occ è 0
        for i in range(8): # cicla lungo la colonna
            if occ[-i-1][int(id)] == 0: # prende la casella libera più in basso
                occ[-i-1][int(id)] = player # segna la casella occupata sulla matrice occ
                
                # disegna il simbolino nella casella
                if id == '0':
                    textBox[63-i*8 - 7].insert(tk.END, testo)
                    textBox[63-i*8 - 7]["fg"] = player_colour
                elif id=='1':
                    textBox[63-i*8 - 6].insert(tk.END, testo)
                    textBox[63-i*8 - 6]["fg"] = player_colour
                elif id == '2':
                    textBox[63-i*8 - 5].insert(tk.END, testo)
                    textBox[63-i*8 - 5]["fg"] = player_colour
                elif id == '3':
                    textBox[63-i*8 - 4].insert(tk.END, testo)
                    textBox[63-i*8 - 4]["fg"] = player_colour
                elif id == '4':
                    textBox[63-i*8 - 3].insert(tk.END, testo)
                    textBox[63-i*8 - 3]["fg"] = player_colour
                elif id == '5':
                    textBox[63-i*8 - 2].insert(tk.END, testo)
                    textBox[63-i*8 - 2]["fg"] = player_colour
                elif id == '6':
                    textBox[63-i*8 - 1].insert(tk.END, testo)
                    textBox[63-i*8 - 1]["fg"] = player_colour
                elif id == '7':
                    textBox[63-i*8 - 0].insert(tk.END, testo)
                    textBox[63-i*8 - 0]["fg"] = player_colour
                
                testo = 'x' if testo=='o' else 'o' # cambia turno
                break # ferma il for dopo aver occupato una casella  
        print(occ)
        # condizioni di vittoria/pareggio
        win1 = np.array([1,1,1,1])
        win2 = np.array([2,2,2,2])
        if vecinmat(win1,occ):
            txt = tk.Text(root, height=4, width=52)
            txt.grid(column=0, row=0, columnspan=8)
            txt.insert(tk.END, "Giocatore 1 ha vinto!")
        elif vecinmat(win2,occ):
            txt = tk.Text(root, height=4, width=52)
            txt.grid(column=0, row=0, columnspan=8)
            txt.insert(tk.END, "Giocatore 2 ha vinto!")
        if not 0 in occ:
            txt = tk.Text(root, height=4, width=52)
            txt.grid(column=0, row=0, columnspan=8)
            txt.insert(tk.END, "Pareggio!")




def main():
    global testo
    global occ
    global root
    global btn0
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global textVar
    global textBox

    testo = 'x' # si alterna con 'o' per caratterizzare il giocatore di turno
    occ = occ = np.zeros([8,8]) # matrice per determinare le caselle libere e occupate

    # finestra
    root = tk.Tk()

    # bottoni close/restart
    restartbtn = tk.Button(root, text="restart", command=restart, width=4)
    restartbtn.grid(column=9, row=1) 
    closebtn = tk.Button(root, text="close", command=close, width=4)
    closebtn.grid(column=9, row=2)

    #  bottoni colonna 
    btn0 = tk.Button(root, command=lambda: update_text('0'), width=6, height=3)
    btn0.grid(column=0, row=0)
    btn1 = tk.Button(root, command=lambda: update_text('1'), width=6, height=3)
    btn1.grid(column=1, row=0)
    btn2 = tk.Button(root, command=lambda: update_text('2'), width=6, height=3)
    btn2.grid(column=2, row=0)
    btn3 = tk.Button(root, command=lambda: update_text('3'), width=6, height=3)
    btn3.grid(column=3, row=0)
    btn4 = tk.Button(root, command=lambda: update_text('4'), width=6, height=3)
    btn4.grid(column=4, row=0)
    btn5 = tk.Button(root, command=lambda: update_text('5'), width=6, height=3)
    btn5.grid(column=5, row=0)
    btn6 = tk.Button(root, command=lambda: update_text('6'), width=6, height=3)
    btn6.grid(column=6, row=0)
    btn7 = tk.Button(root, command=lambda: update_text('7'), width=6, height=3)
    btn7.grid(column=7, row=0)


    # caselle
    textVar = list()
    textBox = list()
    for i in range(1,9):
        for j in range(8):
            textVar.append(tk.StringVar())
            txt = tk.Text(root, height=3, width=6)
            txt["bg"] = "blue"
            textBox.append(txt)
            txt.grid(column=j, row=i)
    
    # lancia finestra
    root.mainloop()


main()
