class Calculator:

    def __init__(self):
        self.status = True

    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        if b == 0:
            print("You can't divide by zero!")
            return
        return a/b