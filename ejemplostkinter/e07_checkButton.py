#ejemplo de interfaz basada en check Button
#es una opccion que agrupa los elementos de VFo

from tkinter import Tk,Label,Message,Button,Checkbutton,IntVar

class ventana:

    def __init__(self):
        self.ventana=Tk()
        Label(self.ventana,text="Selecciona que quieres en tu pizza",fg="red",font="Arial 20 bold").pack()
        #--------declarando IntVar para guardar estado--------
        self.v1=IntVar()
        self.v2=IntVar()
        self.v3=IntVar()
        #----------declarando objetos Checkbutton-------------
        self.op1=Checkbutton(self.ventana,text="aceituna",font="Arial 20",variable=self.v1)
        self.op2=Checkbutton(self.ventana,text="mozzarella",font="Arial 20",variable=self.v2)
        self.op3=Checkbutton(self.ventana,text="pepperoni",font="Arial 20",variable=self.v3)
        #--------colocando los objetos Checkbutton -----------
        self.op1.pack()
        self.op2.pack()
        self.op3.pack()
        #-------- declarando boton y label de respuesta ------
        self.boton=Button(self.ventana,text="Receta pizza",fg="blue",bg="yellow",font="Arial 20 bold",command=self.accion)
        self.mensaje=Message(self.ventana,text="receta :)",fg="white",bg="green",font="Arial 25 italic",width=300) 
        #-------------colocando boton y message --------------
        self.boton.pack()
        self.mensaje.pack()
        #--------------- lanzando aplicacion -----------------
        self.ventana.mainloop()

    def accion(self):
        #---------------------------------------------------
        # Nota: cada widget se relaciona a una variable
        #       en este caso cada widget se conecta a una 
        #       variable: self.v1    self.v2    self.v3
        #       widget:   self.op1   self.op2   self.op3
        #---------------------------------------------------
        if self.v1.get()==1 and self.v2.get()==1 and self.v3.get()==1:
            self.mensaje.config(text="Una pizza con todo vaya que tiene buen gusto :D")
        elif self.v1.get()==0 and self.v2.get()==0 and self.v3.get()==0:
            self.mensaje.config(text="Una pizza con nada :/ estas seguro?")
        else:
            texto="Tu pizza tiene: "
            if self.v1.get()==1:
                texto=texto+"\n - aceituna"
            if self.v2.get()==1:
                texto=texto+"\n - mozzarella"
            if self.v3.get()==1:
                texto=texto+"\n - pepperoni"
            texto=texto+"\nDisfuta :D"    
            self.mensaje.config(text=texto)

#=============================================================
# Creando objeto 
#=============================================================
a=ventana()
