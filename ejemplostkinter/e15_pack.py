#en este ejemplo veremos como se usa la opcion pack
#si bien la hemos utilizado casi todo el tiempo sin argumentos
#es uno de las opciones que hemos utilizado para colocar
#widgets y otro tipo de elementos 
#para este caso dejaremos de usar clases para manipular objs
#en tkinter

from tkinter import Tk,Label,Frame,Button
from tkinter import YES
import tkinter as tk

#Frame es un contendor que se encargara de ilustrar 
#como podemos usar la funcion pack

padre=Tk() #creando un objeto padre para contenerlos a todos

#NOTA,. Se han creado 3 widgets tipo Label veremos como se
#    comportan de acuerdo a los atributos de la funcion pack

def quitarEtiquetas():
    Eti1.pack_forget()
    Eti2.pack_forget()
    Eti3.pack_forget()
    Etiqueta.config(text="")
    Contenedor.config(width=300,height=300,bg="lightblue",relief="raised")
#----creando funcion para variar pack
def mensaje(texto):
    Etiqueta.config(text=texto)
#--------------------------------------    
contador=0
def accion():
    quitarEtiquetas()
    global contador
    contador=contador+1
    #------------------------------
    if contador==1:
        # ejemplo 1 pack()
        # sin argumentos solo amontona
        Eti1.pack()
        Eti2.pack()
        Eti3.pack()
        mensaje("widget.pack()")
    elif contador==2:
        # ejemplo 2 pack fill rellena a su contenedor
        # recuerde que el contenedor es de 500x500
        Eti1.pack(fill=tk.X)
        Eti2.pack()
        Eti3.pack(fill=tk.X)
        mensaje("widget.pack(fill=tk.X)")
    elif contador==3:
        # ejemplo 3 pack fill Y que se ajusta al contenedor
        Eti1.pack(fill=tk.Y)
        Eti2.pack()
        Eti3.pack(fill=tk.Y)
        mensaje("widget.pack(fill=tk.Y)")
    elif contador==4:
        # ejemplo 4 colocando padding
        Eti1.pack(fill=tk.X,padx=30,pady=45)
        Eti2.pack(fill=tk.X)
        Eti3.pack(fill=tk.X)
    elif contador==5:
        # ejemplo 5 colocando ipadding
        Eti1.pack(fill=tk.X,ipadx=30,ipady=45)
        Eti2.pack(fill=tk.X)
        Eti3.pack(fill=tk.X)
        mensaje("pack(ipadx=xx, ipady=yy)")
    elif contador==6:
        # ejemplo 6 colocando side left
        Eti1.pack(fill=tk.X,side=tk.LEFT)
        Eti2.pack(fill=tk.X,side=tk.LEFT)
        Eti3.pack(fill=tk.X)
        mensaje("pack(side=tk.LEFT)")
    elif contador==7:
        # ejemplo 7 colocando side left side rigth 
        Eti1.pack(fill=tk.X,side=tk.LEFT)
        Eti2.pack(fill=tk.X,side=tk.RIGHT)
        Eti3.pack(fill=tk.X)
        mensaje("pack(side=tk.LEFT tk.RIGHT)")
    else:
        contador=0
        mensaje("")


#creando un contenedor para almacenar los elementos de prueba
Contenedor=Frame(padre)
#creando un boton que modicara el comportamiento del 
Boton=Button(padre,text="CambiarTipoPack",fg="Blue",font="Arial 20",command=accion)
#--creando elementos Etiqueta-------------
Eti1=Label(Contenedor,text="1111111",fg="red",bg="yellow",font="Arial 20")
Eti2=Label(Contenedor,text="222",fg="yellow",bg="blue",font="Arial 20")
Eti3=Label(Contenedor,text="33333333333333333",fg="white",bg="red",font="Arial 20")
#----creando elemento para informar el estado
Etiqueta=Label(padre,font="Arial 20 bold",bg="white")
#--- colocando elementos
Boton.pack()
Etiqueta.pack()
Contenedor.pack()
#-----lanzando ventana
quitarEtiquetas()
padre.mainloop()
