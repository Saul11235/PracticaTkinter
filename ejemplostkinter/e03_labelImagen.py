#colocando imagen con Label
from tkinter import Tk,Label,PhotoImage,CENTER

#creando obj ventana
ven=Tk()

#creando objeto tipo imagen
objetoimagen=PhotoImage(file="imagen.png")

#---------------------------------------------
#creando objetos (poner obj padre al incio) 
#---------------------------------------------

Label(ven,text="colocando imagen",font="Arial 20 italic").pack()

eti1=Label(ven,text="Imagen simple",image=objetoimagen).pack()

#Nota.- se pueden ingresar valores adicionales a la funcion pack
#   colocamdo    pack(side="left")
#                pack(side="right")
Label(ven,text="izquierda",fg="blue",font="Arial 30 bold").pack(side="left")
Label(ven,text="derecha",fg="red",font="Arial 30 bold").pack(side="right")

#Nota en caso sea necesario se podra utilizar la funcion composo dentro del widget
Label(text=":) carita",fg="white",bg="black",compound=CENTER).pack()

#---------------------------------------------
# Lanzando ventana
#---------------------------------------------
ven.mainloop()



