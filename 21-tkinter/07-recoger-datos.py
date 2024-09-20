from tkinter import *

window = Tk()
window.geometry("700x700")
window.config(bd=50)

dato = StringVar()
resultado = StringVar()


def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        text_obtained.config(
            bg="green",
            fg="white",
        )


Label(window, text="Mete un texto").pack(anchor=NW)
Entry(window, textvariable=dato).pack(anchor=NW)

Label(window, text="Dato recogido: ").pack(anchor=NW)
text_obtained = Label(window, textvariable=resultado)
text_obtained.pack(anchor=NW)

Button(window, text="Mostrar dato", command=getDato).pack(anchor=NW)

window.mainloop()
