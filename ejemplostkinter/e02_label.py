# analizando las propiedades de las etiquetas en tkinter

import tkinter as tk #importando modulo como tkinter

ventana=tk.Tk() #creando ventana como objeto Padre

#-----------------------------------------------------------
#  CREANDO OBJETOS LABEL
#----------------------------------------------------------
etiquetaLarga=tk.Label(ventana,text="""HOLA SOY UN
        TEXTO DE VARIAS LINEAS
        SOY EN MAYUSCULAS PARA
        PODER NOTARLO""")
#empaquetando
etiquetaLarga.pack()
#--------------------------------------------------------
# NOTA.- Tambien podemos colocar el modulo pack en la misma lin
#--------------------------------------------------------
EtiquetaMismaLinea=tk.Label(ventana,text="mismaLinea").pack()

#  asignando alineacion de texto
#  ojo analizar el metodo pack y las opciones justify
#  pueden ser reemplazados por 
#  tk.LEFT    tk.CENTER   tk.RIGTH
textoEjemplo="derecha "*5+"\n"+"derecha "*8+"\n"+"der"*12
EtiIzq=tk.Label(ventana,text=textoEjemplo,justify="right").pack()

#asignando color de texto
EtiColor=tk.Label(ventana,text="color",fg="blue").pack()

#Cambiando la fuente
EtiFuente=tk.Label(text="Arial",font="Arial 30 bold").pack()

#asignando un fondo de color
EtiFondo=tk.Label(text="fondo",bg="yellow").pack()

#combinando varios
combinacion=tk.Label(text="soy una combinación de tosdo lo que \n que hemos visto",justify=tk.RIGHT,fg="white",bg="red",font="Arial 40 bold").pack()
#----------------------------------------------------------
# Lanzando la ventana
#----------------------------------------------------------
ventana.mainloop()
