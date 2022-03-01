#scale en tkinter

from tkinter import Tk,Label,IntVar,Scale,HORIZONTAL

class ventana:

    def __init__(self):
        self.ventana=Tk()
        #lanzando ventana---------------
        Label(self.ventana,text="Multiplicacion usando scale", font="Arial 20",fg="red").pack()
        #Declarando variables para guaradar estado
        self.var1=IntVar()
        self.var2=IntVar()
        #Declarando objetos scale
        self.scale1=Scale(self.ventana,from_=0,to=100,variable=self.var1,command=self.refrescarLabel)
        #para cambiar declarar atributo oritent=HORIZONTAL
        self.scale2=Scale(self.ventana,from_=0,to=100,variable=self.var2,orient=HORIZONTAL,command=self.refrescarLabel)
        #creando etiqueta con los valores
        self.Etiqueta=Label(self.ventana,font="Arial 30 bold",fg="blue",bg="yellow")
        #colocando los elementos
        self.scale1.pack()
        self.scale2.pack()
        self.Etiqueta.pack()
        #lanzando pantalla
        self.refrescarLabel()
        self.ventana.mainloop()

    def refrescarLabel(self,*args): 
        #nota se puso *args para que la lib no tenga excepciones
        valor1=self.var1.get()
        valor2=self.var2.get()
        texto=" "+str(valor1)+" x "+str(valor2)+" = "+str(valor1*valor2)+" "
        self.Etiqueta.config(text=texto)
#-----------------------------------------------------------
#creando objeto ventana
v=ventana()   
