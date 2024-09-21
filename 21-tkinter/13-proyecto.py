"""
Crear programa que tenga:
+ Ventana
+ Tamaño fijo
+ No redimensionable
+ Un menu (Inicio, Añadir, Informacion, Salir)
+ Diferentes pantallas
- Formulario para añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
+ Opcion de sair
"""

from tkinter import *

# Definir Ventana
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Proyecto Tkinter ~ Master en Python")
ventana.resizable(0, 0)


# Definir campos de pantalla (Inicio)
home_label = Label(ventana, text="Inicio")

# Definir campos de pantalla (Añadir)
add_label = Label(ventana, text="Añadir producto")

name_data = StringVar()
add_name_label = Label(ventana, text="Nombre del producto")
add_name_entry = Entry(ventana, textvariable=name_data)

price_data = StringVar()
add_price_label = Label(ventana, text="Precio del producto")
add_price_entry = Entry(ventana, textvariable=price_data)


# Definir campos de pantalla (Informacion)
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Addison Reyes - 2024")


# Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=155,
        pady=20,
    )
    home_label.grid(row=0, column=0)

    # Ocultar pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    add_name_label.grid_remove()
    add_price_label.grid_remove()


def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=60,
        pady=20,
    )
    add_label.grid(row=0, column=0, columnspan=10)

    add_name_label.grid(row=1, column=0)
    add_name_label.config(font=("Arial", 10))
    add_price_label.grid(row=2, column=0)
    add_price_label.config(font=("Arial", 10))

    # Ocultar pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=96,
        pady=20,
    )
    info_label.grid(row=0, column=0)

    data_label.config(font=("Arial", 10))
    data_label.grid(row=1, column=0)

    # Ocultar pantallas
    home_label.grid_remove()
    add_label.grid_remove()

    add_name_label.grid_remove()
    add_price_label.grid_remove()


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
