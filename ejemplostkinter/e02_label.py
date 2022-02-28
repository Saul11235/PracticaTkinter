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
EtiquetaMismaLinea=tk.Label(ventana,text="**mismLin**").pack()

#asignando alineacion de texto
EtiIzq=tk.Label(ventana,text="izq",justify=tk.RIGHT).pack()





#----------------------------------------------------------
# Lanzando la ventana
#----------------------------------------------------------
ventana.mainloop()
