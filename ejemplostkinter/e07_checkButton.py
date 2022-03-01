#ejemplo de interfaz basada en check Button
#es una opccion que agrupa los elementos de VFo

from tkinter import Tk,Label,Button,Checkbutton

class ventana:

    def __init__(self):
        self.ventana=Tk()
        Label(self.ventana,text="Selecciona que quieres en tu pizza",fg="red",font="Arial 20").pack()
        self.op1=Checkbutton(self.ventana,text="aceituna",font="Arial 20")
        self.op1.pack()
        self.ventana.mainloop()


a=ventana()
