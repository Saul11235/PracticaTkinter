#ejemplo de uso de dialogos en tkinter
#veremos como se usan algunos dialogos 
from tkinter import Tk,Label,Button
#para mostrar los resultados de los dialogos usaremos messagebox
from tkinter.messagebox import showinfo
#los dialogos que veremos seran filemediadialog colorchooser
from tkinter.colorchooser import askcolor#seleccionador de color
from tkinter.filedialog import askopenfile #selecciona archivo a abrir

class ventana:

    def __init__(self):
        self.ventana=Tk()
        Label(self.ventana,text="Ejemplo de algunos tipos de Dialogos").pack()
        #--creando botones de dialogo--------
        Button(self.ventana,text="Color",command=self.color).pack()
        Button(self.ventana,text="Abrir archivo",command=self.abrir).pack()
        #------------------------------------
        #lanzando ventana
        self.ventana.mainloop()

    def color(self):
        #lee un color y lo muestra con showinfo
        colorLeido=askcolor(color="red",title="Selecciona un color")
        showinfo("Titulo",str(colorLeido)) 

    def abrir(self):
        RutaLeida=askopenfile()
        showinfo("Archivo leido",str(RutaLeida))

#-----------------------------------------
# creando objeto
#-----------------------------------------
v=ventana()
