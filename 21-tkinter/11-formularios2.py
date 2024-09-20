from tkinter import *

ventana = Tk()

ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20),
)
encabezado.pack(
    anchor=N,
    fill=X,
    expand=YES,
    side=TOP,
)

# Checkbox button
Label(ventana, text="A que te dedicas?").pack()

# Radio buttons


# Dropdown menu


ventana.mainloop()
