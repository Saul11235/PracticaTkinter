#funcion entry
from tkinter import Tk,Label,Button,Entry,StringVar,Message

class ventana:

    def __init__(self):
        self.ventana=Tk()
        #---- creando variables para el programa----
        self.Svar1=StringVar()
        self.Svar2=StringVar()
        #--- creando elementos para el programa
        self.Entry1=Entry(self.ventana,font="Arial 15",textvariable=self.Svar1)
        self.Entry2=Entry(self.ventana,font="Arial 15",textvariable=self.Svar2)  
        #--- elementos intercativos
        self.boton=Button(self.ventana,text="Presioname",bg="yellow",font="Arial 20 ",command=self.accion)
        self.EtiquetaRespuesta=Message(self.ventana,font="Arial 20",fg="white",bg="green",width=400)
        #
        #--- colocando todos los elementos 
        Label(self.ventana,text="Ingresa tus datos",fg="red",font="Arial 25 bold").pack()
        Label(self.ventana,text="Nombre:",fg="blue",font="Arial 18").pack()
        self.Entry1.pack()
        Label(self.ventana,text="Apellido:",fg="blue",font="Arial 18").pack()
        self.Entry2.pack()
        self.boton.pack()
        self.EtiquetaRespuesta.pack()
        self.accion()
        #--- lanzar ventana ----------------------
        self.ventana.mainloop()

    def accion(self):
        texto=""
        if self.Svar1.get()=="" and self.Svar2.get()=="":
            texto="escribe tu nombre"
        else:    
            texto="tu nombre es "+self.Svar1.get()+" "+self.Svar2.get()
        self.EtiquetaRespuesta.config(text=texto)

#-------------------------------------------------------------
# creando objeto
#-------------------------------------------------------------
a=ventana()
