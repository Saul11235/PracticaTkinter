# este ejemplo ilustrara la creacion de un boton, tomando en
# cuenta un pequeño programa que mostrara el comportamiento
# del algoritmo utilizaremos una clase llamada "programa" 
# y un objeto llamado prog, este objeto de clase prog contendrá 
# los objetos de la libreria tkinter
# y una logica que le permita una logica simple tarea
# de cambiar los colores de un laberl, usando la funcion config

#------------------------------------------------------------
# DEFINIENDO LA CLASE: programa
#------------------------------------------------------------
from tkinter import Tk,Label,Button

class programa:

    def __init__(self):
        self.ventana=Tk()
        self.Etiqueta=Label(self.ventana)
        self.Boton=Button(self.ventana,text="Presioname")
        #-------------------------------------------
        #configurando y colocando los elementos
        self.Etiqueta.config(font="Arial 50 bold")
        self.Etiqueta.pack()
        self.Boton.config(font="Arial 30 italic")
        self.Boton.pack()
        #-------------------------------------------
        #asignando un comando al widget Button
        self.Boton.config(command=self.accionBoton)
        #-------------------------------------------
        # el marcador logico cambiara entre true y false para
        # cambiar el color de self.Etiqueta
        self.__marcadorLogico=False 
        self.accionBoton()#presiona el boton para colorear label
        self.ventana.mainloop() #lanza la ventana

    def accionBoton(self):
        if self.__marcadorLogico==True:
            self.Etiqueta.config(fg="white",bg="red")
            self.Etiqueta.config(text="Hola, Como estas?")
            self.__marcadorLogico=False
        else:
            self.Etiqueta.config(fg="black",bg="cyan")
            self.Etiqueta.config(text="Hola, yo te saludo")
            self.__marcadorLogico=True

            
#------------------------------------------------------------
# CREANDO EL OBJETO: prog
#------------------------------------------------------------
prog=programa()







