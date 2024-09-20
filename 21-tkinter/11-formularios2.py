from tkinter import *

ventana = Tk()
ventana.config(
    bd=0.6,
)

# ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20),
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)


# Checkbox button
def mostrarProfesion():
    texto: str = ""

    if web.get():
        texto += "Desarrollo Web"

    if movil.get():
        if web.get():
            texto += " y Desarrollo Movil"
        else:
            texto += "Desarrollo Movil"
    if movil.get() or web.get():
        mostrar.config(
            text=texto,
            bg="green",
            fg="white",
        )
    else:
        mostrar.config(
            text="",
        )


job = Label(ventana, text="A que te dedicas?")
job.config(
    padx=15,
    pady=15,
    font=("Consolas", 10),
)
job.grid(row=1, column=0)

movil = IntVar()
web = IntVar()

Checkbutton(
    ventana,
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion,
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo Movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion,
).grid(row=3, column=0)

mostrar = Label(ventana, text="")
mostrar.grid(row=1, column=1)


# Radio buttons
def marcar():
    marcado.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)

Label(
    ventana,
    text="Cual es tu genero?",
).grid(row=5, column=0)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar,
).grid(row=6, column=0)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar,
).grid(row=7, column=0)
Radiobutton(
    ventana,
    text="No binario",
    value="No binario",
    variable=opcion,
    command=marcar,
).grid(row=8, column=0)
Radiobutton(
    ventana,
    text="Helicotero",
    value="Helicotero",
    variable=opcion,
    command=marcar,
).grid(row=9, column=0)

marcado = Label(ventana)
marcado.grid(row=10, column=0)


# Dropdown menu
opcion_menu = StringVar()
opcion_menu.set("Opcion 1")

Label(
    ventana,
    text="Selecciona una opcion",
).grid(row=5, column=1)

OptionMenu(
    ventana,
    opcion_menu,
    "Opcion 1",
    "Opcion 2",
    "Opcion 3",
).grid(row=6, column=1)

Label(ventana, text="").grid(row=999, column=0)
ventana.mainloop()
