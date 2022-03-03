#ejemplo de uso de messagebox
from tkinter import Tk,Label,Button,messagebox

class ventana:

    def __init__(self):
        self.ventana=Tk()
        #------creando objetos y botones que hacen anuncios ---
        Label(self.ventana,text="Selecciona el anuncio").pack()
        Button(self.ventana,text="Informacion",command=self.info).pack()
        Button(self.ventana,text="error",command=self.error).pack()
        Button(self.ventana,text="alerta",command=self.alerta).pack()
        self.ventana.mainloop()
        pass

    def info(self):messagebox.showinfo("Titulo","Contenido")

    def error(self):messagebox.showerror("Titulo","Contenido")

    def alerta(self):messagebox.showwarning("Titulo","Contenido")

#-------------------------------------------------------
#lanzando ventana
v=ventana()
