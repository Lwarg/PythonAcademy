class Lampadina:

    def __init__(self, vita):
        self.stato = "spento"
        self.vita = vita

    def stato(self):
        return self.stato
    
    def click(self):
        if self.vita > 0:
            self.vita -= 1
            if self.vita == 0:
                self.stato = "rotta"
            else: 
                self.stato = "acceso" if self.stato == "spento" else "spento"
        else:
            self.stato = "rotta"
            
            





