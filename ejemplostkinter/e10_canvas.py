#ejemplo de dibujo simple con el modulo canvas
#declararemos una funcion que nos dara colores aleatorios
#para declarar funciones aleatorias 

from tkinter import Tk,Label,Button,Canvas,Frame
from random import randint

#Color aleatorio--------------------------------
def colorRandom():
    lista=["red","yellow","black","cyan","purple","orange","blue","green"]
    aleatorio=randint(0,len(lista)-1)
    return(lista[aleatorio])
#Longitud aleatoria de 0 hasta 400 -------------
def Lrand(): return(randint(0,400))
#devuelve ang rand 0 -360 ---------------------
def Arand(): return(randint(0,360))
#-----------------------------------------------

class ventana:

    def __init__(self):
        #creando ventana y lienzo
        self.ventana=Tk()
        self.Lienzo=Canvas(self.ventana,width=400,height=400)
        self.Lienzo.pack()
        #Nota creamos un contenedor para los botones
        self.contenedor=Frame(self.ventana)
        self.contenedor.pack(side="left")
        #creando botones de accion
        Button(self.contenedor,text="Linea",command=self.linea,font="Arial 16").pack(side="left")
        Button(self.contenedor,text="Rect",command=self.rectangulo,font="Arial 16").pack(side="left")
        Button(self.contenedor,text="Arco",command=self.arco,font="Arial 16").pack(side="left")
        Button(self.contenedor,text="Elipse",command=self.elipse,font="Arial 16").pack(side="left")
        Button(self.contenedor,text="Poligono",command=self.poligono,font="Arial 16").pack(side="left")
        Button(self.contenedor,text="Texto",command=self.texto,font="Arial 16").pack(side="left")
        #lanzando ventana
        self.ventana.mainloop()

    def linea(self):
        #dibuja solamene una linea en el cavas
        self.Lienzo.create_line(Lrand(),Lrand(),Lrand(),Lrand(),fill=colorRandom(),width=3)

    def rectangulo(self):
        #dibuja un rect puede tener outline fill o solo uno
        self.Lienzo.create_rectangle(Lrand(),Lrand(),Lrand(),Lrand(),outline=colorRandom(),fill=colorRandom(),width=4)

    def arco(self):
        #dibuja un arco aleatorio
        #para marcar tipo de dibujo
        #   style=tk.ARC       solo arco
        #   style=tk.PIESLICE  rebanada de pie
        #   style=tk.CHORD     cuerda
        self.Lienzo.create_arc(Lrand(),Lrand(),Lrand(),Lrand(),start=Arand(), extent=Arand())
    
    def elipse(self):
        #dibuja una elipse
        self.Lienzo.create_oval(Lrand(),Lrand(),Lrand(),Lrand())
    def poligono(self):
        #dibuja un poligono
        self.Lienzo.create_polygon(Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),Lrand(),fill=colorRandom())

    def texto(self):
        #colocando texto
        texto=colorRandom()
        self.Lienzo.create_text(Lrand(),Lrand(),text=texto,font="Arial 16",fill=colorRandom())

#-------------------------------------------------------
# creando un objeto
#--------------------------------------------------------
a=ventana()


