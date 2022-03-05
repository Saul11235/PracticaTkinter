#ejemplo de menu
from tkinter import Tk,Label,Menu
from tkinter.messagebox import showinfo

#creando objeto de ventana
ventana=Tk()

#creando un contenido para que la vista no sea tan triste :)
Label(ventana,text="Hola soy un texto\nSoy contenido\nDe esta ventana",fg="blue",bg="yellow",font="Arial 40").pack(padx=30,pady=30,ipadx=30,ipady=30)

#creando objeto menu
def fun1(): showinfo("fun1","Funcion 1")
def fun2(): showinfo("fun2","Funcion 2")
def fun3(): showinfo("fun3","Funcion 3")
def fun4(): showinfo("fun4","Funcion 4")

#--------------------------------------------------------------
#  disposicion de los elementos, todos objetos 
#   
#   Ventana (tipo Tk)
#      Label.pack(text="conntenido")
#  ===================
#    * BarraMenu (Menu)
#       * Seccion1 (Menu)
#           * Subseccion 11 (Menu)
#               funcion-3 (command)
#           funcion-1  (command)
#           funcion-2  (command)
#       * Seccion2 (Menu)
#           funcion-4 (command)
#
#--------------------------------------------------------------

#creando un objeto Menu
BarraMenu=Menu(ventana)
#configurando barra menu como menu de la ventana
ventana.config(menu=BarraMenu)

#Creando menus dentro de la barra menu
Seccion1=Menu(BarraMenu)
Seccion11=Menu(Seccion1) #subseccion
Seccion2=Menu(BarraMenu)

#Creando nombres de las barras de menu
BarraMenu.add_cascade(label="Seccion 1",menu=Seccion1)
BarraMenu.add_cascade(label="Seccion 2",menu=Seccion2)

#Creando subseccion
Seccion1.add_cascade(label="Subseccion 11",menu=Seccion11)

#Creando comandos
Seccion1.add_command(label= "funcion 1",command=fun1)
Seccion1.add_command(label= "funcion 2",command=fun2)
Seccion11.add_command(label="funcion 3",command=fun3)
Seccion2.add_command(label= "funcion 4",command=fun4)

#lanzando ventana
ventana.mainloop()
