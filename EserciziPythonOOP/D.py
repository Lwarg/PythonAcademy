class D:

    def __init__(self, gg, mm, aa):
        self.gg = gg
        self.mm = mm
        self.aa = aa
        self.val()

    def val(self):
        mesi31 = [1,3,5,7,8,10,12]
        mesi30 = [4,6,9,11]
        febbraio = 2
        if self.mm > 12:
            print("not valid")
            return False
        elif self.mm in mesi31 and self.gg > 31:
            print("not valid")
            return False
        elif self.mm in mesi30 and self.gg > 30:
            print("not valid")
            return False
        else: # Febbraio
            bisestile = False
            if self.aa%100 == 0 and (self.aa/100)%4!= 0:
                bisestile = True
            elif self.aa%100 != 0 and self.aa%4 == 0:
                bisestile =True
            if bisestile and self.gg > 29:
                print("not valid")
                return False
            elif (not bisestile) and self.gg > 28:
                print("not valid")
                return False
        return True


    def out(self):
        print(self.gg, self.mm, self.aa)
    
    def mod(self, new_gg, new_mm, new_aa):
        self.gg = new_gg
        self.mm = new_mm
        self.aa = new_aa
        self.val()
