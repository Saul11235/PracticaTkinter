#ejemplo de uso de radio button, estamos usando tmbn otra clase
#--------------------------------------------------------------
# creando clase: "programa"
#--------------------------------------------------------------
from tkinter import Tk,Label

class programa:

    def __init__(self):
        self.ventana=Tk()
        #--------------------------------------------
        Label(text="ejemplo radioButton").pack()
        #--------------------------------------------
        self.ventana.mainloop()

#--------------------------------------------------------------
# creando objeto "prog"
#--------------------------------------------------------------
prog=programa()
    
