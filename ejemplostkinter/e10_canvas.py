#ejemplo de dibujo simple con el modulo canvas
#declararemos una funcion que nos dara colores aleatorios
#para declarar funciones aleatorias 

from tkinter import Tk,Label,Button,Canvas
from random import randint

def colorRandom():
    lista=["red","yellow","black","white","cyan","purple","pink","orange"]
    aleatorio=randint(0,len(lista)-1)
    return(lista[aleatorio])

class ventana:

    def __init__(self):
        self.ventana=Tk()
        self.ventana.mainloop()
        pass


#-------------------------------------------------------
# creando un objeto
#--------------------------------------------------------
#a=ventana()

for x in range(34):
    print(colorRandom())

