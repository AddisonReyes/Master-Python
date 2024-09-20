from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(
    bd=70,
)


def sacarAlerta():
    MessageBox.showwarning("Alerta", "Hola!!!")


Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()


def salir(nombre):
    resultado = MessageBox.askquestion(
        "Salir", "Quieres continuar usando la aplicacion?"
    )

    if resultado != "yes":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command=lambda: salir("Addison")).pack()


ventana.mainloop()
