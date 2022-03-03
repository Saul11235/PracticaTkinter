##ejemplo de uso de messagebox y submodulos ask

from tkinter import Tk,Label,Button,messagebox

class ventana:

    def __init__(self):
        self.ventana=Tk()
        #------creando objetos y botones que hacen anuncios -------
        Label(self.ventana,text="Selecciona la pregunta").pack()
        Button(self.ventana,text="SI-NO-CANCEL",command=self.preguntaSINOCANCEL).pack()
        Button(self.ventana,text="SI-NO",command=self.preguntaSINO).pack()
        Button(self.ventana,text="RETRY-CANCEL",command=self.preguntaRETRYCANCEL).pack()
        #Lanzando ventana------------------------------------------
        self.ventana.mainloop()


    def preguntaSINOCANCEL(self):
        respuesta=messagebox.askyesnocancel("titulo","contenido")
        messagebox.showinfo("tu respuesta",str([respuesta]))

    def preguntaSINO(self):
        respuesta=messagebox.askyesno("titulo","contenido")
        messagebox.showinfo("tu respuesta",str([respuesta]))

    def preguntaRETRYCANCEL(self):
        respuesta=messagebox.askretrycancel("titulo","contenido")
        messagebox.showinfo("tu respuesta",str([respuesta]))

#-------------------------------------------------------
# Lanzando ventanas
#-------------------------------------------------------
v=ventana()



