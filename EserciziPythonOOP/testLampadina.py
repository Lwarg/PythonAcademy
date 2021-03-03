import Lampadina as Lamp

vite = 5
ikea = Lamp.Lampadina(vite)

for i in range(vite+3):
    ikea.click()
    print("click",i,", stato:",ikea.stato,", vita rimanente:", ikea.vita)