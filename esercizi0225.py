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


testo = "Ciao 8! Come va?"
quantiCarNum(testo)

