#ejecutando funcion place para colocar los elementos con place

from tkinter import Tk,Label

padre=Tk()

#creando etiquetas
etiqueta1=Label(padre,text="11111111",fg="blue",bg="yellow",font="arial 20 bold")
etiqueta2=Label(padre,text="222222",fg="red",bg="white",font="arial 25 bold")
etiqueta3=Label(padre,text="333333333",fg="white",bg="black",font="arial 14 bold")

#configurando geometria del objeto padre
padre.geometry("400x500")

#colocando las etiquetas con la funcion place, indicamos 
#
#   +
#   
#
#
#
#
#
#
etiqueta1.place(x=0,y=100,width=200)











#lanzando ventana
padre.mainloop()




