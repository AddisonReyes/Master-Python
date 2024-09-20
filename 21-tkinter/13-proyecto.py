"""
Crear programa que tenga:
+ Ventana
+ Tamaño fijo
+ No redimensionable
+ Un menu (Inicio, Añadir, Informacion, Salir)
- Diferentes pantallas
- Formulario para añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
+ Opcion de sair
"""

from tkinter import *

# Definir Ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter ~ Master en Python")
ventana.resizable(0, 0)


# Pantallas
def home():
    home_label = Label(ventana, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20,
    )
    home_label.grid(row=0, column=0)


def add():
    add_label = Label(ventana, text="Añadir producto")
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20,
    )
    add_label.grid(row=0, column=0)


def info():
    info_label = Label(ventana, text="Informacion")
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20,
    )
    info_label.grid(row=0, column=0)

    data_label = Label(ventana, text="Creado por Addison Reyes - 2024")
    data_label.config(font=("Arial", 10))
    data_label.grid(row=1, column=0)


# Cargar pantalla de inicio
home()


# Menu Superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

# Cargar Ventana
ventana.mainloop()
