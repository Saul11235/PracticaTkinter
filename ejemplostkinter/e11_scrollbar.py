#ejemplo de scrollbarr en una ventana

textoLorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum\n"*50

from tkinter import Tk,Text,Scrollbar,END,LEFT,RIGHT,Y

#creando objetos
ventana=Tk()
scroll=Scrollbar(ventana)
texto=Text(ventana,height=30,width=120)

#ingresando texto
#el valor tk.END indica que el puntero vaya al final
texto.insert(END,textoLorem)

#colocando elemento 
texto.pack(side=LEFT,fill=Y)
scroll.pack(side=RIGHT,fill=Y)
#IMPORTANTE---------------------------------------------
#debemos configurar los dos widgets es decir que debemos
#asociar texto a scroll y asociar scroll a texto
texto.config(yscrollcommand=scroll.set)
scroll.config(command=texto.yview)
#-------------------------------------------------------

#lanzando ventana
ventana.mainloop()



