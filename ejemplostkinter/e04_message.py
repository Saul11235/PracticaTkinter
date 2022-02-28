#ejemplo de uso de message en tkinter
#este modulo es parecido al widget label

from tkinter import Tk,Message

#creando objeto padre
ventana=Tk()

#creando objeto mensaje
Message(ventana,text="Hola soy un mensaje, me adapto al contexto, puedes moverme y cambiar mis propiedades").pack()

#indicando un ancho fijo en pixeles con width
Message(ventana,text="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum 
        """,width=200).pack()

#Asignando color de fuente, fondo y tipo de fuente usadas
Message(ventana,text="texto con formato",fg="blue",bg="yellow",font="Arial 20 bold").pack()

#podemos configurar un widget en varias lineas de codigo
Mensaje=Message(ventana,text="Hola nuevo texto")
Mensaje.config(fg="blue",bg="cyan",font="Arial 30 bold")
Mensaje.pack()

#lanzando ventana
ventana.mainloop()

