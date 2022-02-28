#ejemplo creando una nueva ventana con tkinter

from tkinter import Tk,Label

#importamos los widgets Tk (ventana) Label (etiqueta)
ventana=Tk()

# Para crear un widget debemos de relacionarlo a un objeto 
# padre, la forma de cada declaracion de widget varia en funcion
# Al tipo de objeto que creemos, en este caso usaremos una 
# Etiqueta

etiqueta=Label(ventana,text="Hola como vamos")

#   hay diferentes formas de colocar objetos. la forma más
#   sencilla es usando la funcion pack

etiqueta.pack() #se coloca en el objeto padre

ventana.mainloop() #lanza la ventana


