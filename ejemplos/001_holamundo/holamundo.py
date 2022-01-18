#ejemplo de holamundo en tkinter

#importa todo el contenido de tkinter, no recomendado
from tkinter import Tk, Label 

ventana=Tk() #creado objeto tipo Tk 

#creado objeto tipo label . etiqueta
#NOTA,. en tkinter se debe indicar primero el objeto padre
letrero=Label(ventana, text="Hola mundo desde tkinter")

letrero.pack() #usando funcion pack para colocar en el padre

#el objeto tk se muestra de modo grafico
ventana.mainloop()
