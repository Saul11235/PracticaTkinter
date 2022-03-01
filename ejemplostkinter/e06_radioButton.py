#ejemplo de uso de radio button, estamos usando tmbn otra clase
#estos son como botones seleccionables haremos algo parecido a
#una lista desplegable
#
#Nota.-en tkinter tabien existen variables que guardan los  
#      estados de los widgets
#  las variables de tkinter son
#  variable textvariable  onvalue offvalue 
#  dependen de la aplicacion   
#    StringVar IntVar  DoubleVar BooleanVar
#
#--------------------------------------------------------------
# creando clase: "programa"
#--------------------------------------------------------------
from tkinter import Tk,Label,Radiobutton,IntVar

class programa:

    def __init__(self):
        self.ventana=Tk()
        #el estado del radio button se almacena en un IntVar
        self.entero=IntVar()
        #--------------------------------------------
        Label(text="Selecciona tu helado favorito :) ",fg="blue",bg="yellow",font="Arial 20").pack()
                     #--------------------------------------------
        # Nota para guardar los valores
        # variable -- variable para almacenar estado
        #--------------------------------------------
        self.r1=Radiobutton(self.ventana,text="Helado de chocolate",variable=self.entero,font="Arial 24",value=1,command=self.exe)
        #--------------------------------------------
        self.r2=Radiobutton(self.ventana,text="Helado de Maracuya",variable=self.entero,font="Arial 24",value=2,command=self.exe)
         #--------------------------------------------
        self.r3=Radiobutton(self.ventana,text="Helado de Vainilla",variable=self.entero,font="Arial 24",value=3,command=self.exe)
        #--------------------------------------------
        #creando Letrero para respuesta
        self.Letrero=Label(self.ventana,fg="red",text="Me gustan los helados ",font="Arial 40")
        #colocando los objetos Radiobutton-----------
        self.r1.pack()
        self.r2.pack()
        self.r3.pack()
        self.Letrero.pack()
        #Lanza ventana -------------------------------
        self.ventana.mainloop()

    def exe(self):
        #la accion se realiza en funcion del valor que tome 
        #el objeto devolvera su valor con la funcion get
        if self.entero.get()==1:
            self.Letrero.config(text="Te gusta el chocolate")
        elif self.entero.get()==2:
            self.Letrero.config(text="El maracuya es riquisimo")
        else:
            self.Letrero.config(text="La vainilla es buena")

#--------------------------------------------------------------
# creando objeto "prog"
#--------------------------------------------------------------
prog=programa()
    
