
import tkinter as tk
import numpy as np


def restart():
    root.destroy()
    main()

def close():
    root.destroy()

def update_btn_text(id):
    global testo
    global occ
    global root
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8
    global btn9
    global btn_text1
    global btn_text2
    global btn_text3
    global btn_text4
    global btn_text5
    global btn_text6
    global btn_text7
    global btn_text8
    global btn_text9

    player = 1 if testo=='x' else 2
    if id=='1':
        btn_text1.set(testo)
        occ[0][0] = player
        btn1["state"] = "disabled"
    elif id == '2':
        btn_text2.set(testo)
        occ[0][1] = player
        btn2["state"] = "disabled"
    elif id == '3':
        btn_text3.set(testo)
        occ[0][2] = player
        btn3["state"] = "disabled"
    elif id == '4':
        btn_text4.set(testo)
        occ[1][0] = player
        btn4["state"] = "disabled"
    elif id == '5':
        btn_text5.set(testo)
        occ[1][1] = player
        btn5["state"] = "disabled"
    elif id == '6':
        btn_text6.set(testo)
        occ[1][2] = player
        btn6["state"] = "disabled"
    elif id == '7':
        btn_text7.set(testo)
        occ[2][0] = player
        btn7["state"] = "disabled"
    elif id == '8':
        btn_text8.set(testo)
        occ[2][1] = player
        btn8["state"] = "disabled"
    elif id == '9':
        btn_text9.set(testo)
        occ[2][2] = player
        btn9["state"] = "disabled"
    testo = 'x' if testo=='o' else 'o'
    print(occ)
    win1 = np.array([1,1,1])
    win2 = np.array([2,2,2])
    if (occ[:,0]==win1).all() or (occ[:,1]==win1).all() or (occ[:,2]==win1).all() or (occ[0,:]==win1).all() or (occ[1,:]==win1).all() or (occ[2,:]==win1).all() or (np.diag(occ)==win1).all() or (np.diag(np.fliplr(occ))==win1).all():
        winButton = tk.Button(root, text="X ha vinto!", width=10)
        winButton.grid(column=1, row=3)
        winflag = True
    elif (occ[:,0]==win2).all() or (occ[:,1]==win2).all() or (occ[:,2]==win2).all() or (occ[0,:]==win2).all() or (occ[1,:]==win2).all() or (occ[2,:]==win2).all() or (np.diag(occ)==win2).all() or (np.diag(np.fliplr(occ))==win2).all():
        winButton = tk.Button(root, text="O ha vinto!", width=10)
        winButton.grid(column=1, row=3)
        winflag = True
    if not 0 in occ:
        winButton = tk.Button(root, text="Pareggio!", width=10)
        winButton.grid(column=1, row=3)
        winflag = True
    
    if winflag:
        restartbtn = tk.Button(root, text="restart", command=restart, width=4)
        restartbtn.grid(column=2, row=3) 
        closebtn = tk.Button(root, text="close", command=close, width=4)
        closebtn.grid(column=0, row=3) 

def main():
    global testo
    global occ
    global root
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8
    global btn9
    global btn_text1
    global btn_text2
    global btn_text3
    global btn_text4
    global btn_text5
    global btn_text6
    global btn_text7
    global btn_text8
    global btn_text9

    testo = 'x'
    occ = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])

    root = tk.Tk()

    btn_text1 = tk.StringVar()
    btn1 = tk.Button(root, textvariable=btn_text1, command=lambda: update_btn_text('1'), width=6)
    btn_text1.set(" ")
    btn1.grid(column=0, row=0)   

    btn_text1 = tk.StringVar()
    btn1 = tk.Button(root, textvariable=btn_text1, command=lambda: update_btn_text('1'), width=6)
    btn_text1.set(" ")
    btn1.grid(column=0, row=0)

    btn_text2 = tk.StringVar()
    btn2 = tk.Button(root, textvariable=btn_text2, command=lambda: update_btn_text('2'), width=6)
    btn_text2.set(" ")
    btn2.grid(column=1, row=0)

    btn_text3 = tk.StringVar()
    btn3 = tk.Button(root, textvariable=btn_text3, command=lambda: update_btn_text('3'), width=6)
    btn_text3.set(" ")
    btn3.grid(column=2, row=0)

    btn_text4 = tk.StringVar()
    btn4 = tk.Button(root, textvariable=btn_text4, command=lambda: update_btn_text('4'), width=6)
    btn_text4.set(" ")
    btn4.grid(column=0, row=1)

    btn_text5 = tk.StringVar()
    btn5 = tk.Button(root, textvariable=btn_text5, command=lambda: update_btn_text('5'), width=6)
    btn_text5.set(" ")
    btn5.grid(column=1, row=1)

    btn_text6 = tk.StringVar()
    btn6 = tk.Button(root, textvariable=btn_text6, command=lambda: update_btn_text('6'), width=6)
    btn_text6.set(" ")
    btn6.grid(column=2, row=1)

    btn_text7 = tk.StringVar()
    btn7 = tk.Button(root, textvariable=btn_text7, command=lambda: update_btn_text('7'), width=6)
    btn_text7.set(" ")
    btn7.grid(column=0, row=2)

    btn_text8 = tk.StringVar()
    btn8 = tk.Button(root, textvariable=btn_text8, command=lambda: update_btn_text('8'), width=6)
    btn_text8.set(" ")
    btn8.grid(column=1, row=2)

    btn_text9 = tk.StringVar()
    btn9 = tk.Button(root, textvariable=btn_text9, command=lambda: update_btn_text('9'), width=6)
    btn_text9.set(" ")
    btn9.grid(column=2, row=2)
    
    root.mainloop()


main()
