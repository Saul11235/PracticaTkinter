#ejecutando funcion place para colocar los elementos con place

from tkinter import Tk,Label

#declarando objeto padre
padre=Tk()

#creando etiquetas
etiqueta1=Label(padre,text="11111111",fg="blue",bg="yellow",font="arial 20 bold")
etiqueta2=Label(padre,text="222222",fg="red",bg="blue",font="arial 25 bold")
etiqueta3=Label(padre,text="333333333",fg="white",bg="black",font="arial 14 bold")

#configurando geometria del objeto padre
padre.geometry("400x400") #DimX+*DimY

#colocando las etiquetas con la funcion place, indicamos 
#
#   +------------------------>  X
#   |                       .
#   |                       .
#   |                       .
#   |                       .
#   |                       .    width
#   V . . . . . . . . . . . +--------------+ 
#                           |              |
#   Y                       |              | height
#                           |              |
#                           +--------------+
#
#colocando los elementos con la funcion place

etiqueta1.place(x=0,y=200,width=200,height=100)
etiqueta2.place(x=210,y=240,width=175,height=130)
etiqueta3.place(x=240,y=0,width=140,height=200)

#lanzando ventana
padre.mainloop()
