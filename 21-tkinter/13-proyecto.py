"""
Crear programa que tenga:
+ Ventana
+ Tamaño fijo
+ No redimensionable
+ Un menu (Inicio, Añadir, Informacion, Salir)
+ Diferentes pantallas
+ Formulario para añadir productos
+ Guardar datos temporalmente
+ Mostrar datos listados en la pantalla home
+ Opcion de sair
"""

from tkinter import *
from tkinter import ttk

# Definir Ventana
ventana = Tk()
# ventana.geometry("400x400")
ventana.minsize(400, 400)
ventana.title("Proyecto Tkinter ~ Master en Python")
ventana.resizable(0, 0)

products = []

# Definir campos de pantalla (Inicio)
home_label = Label(ventana, text="Inicio")
products_frame = Frame(ventana, width=250)

products_table = ttk.Treeview(height=12, columns=2)
products_table.heading("#0", text="Producto", anchor=W)
products_table.heading("#1", text="Precio", anchor=W)


# Definir campos de pantalla (Añadir)
add_frame = Frame(ventana)
add_label = Label(ventana, text="Añadir producto")

name_data = StringVar()
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

price_data = StringVar()
add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame, text="")


def add_products():
    products.append(
        [
            name_data.get(),
            price_data.get(),
            add_description_entry.get("1.0", "end-1c"),
        ]
    )

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


boton = Button(add_frame, text="Guardar", command=add_products)

# Definir campos de pantalla (Informacion)
info_label = Label(ventana, text="Informacion")
info_frame = Frame(ventana)

data_label = Label(info_frame, text="Creado por Addison Reyes - 2024")


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

    products_table.grid(row=1, column=0, columnspan=2)
    products_frame.grid(row=1)

    # Listar productos
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")
    #         Label(products_frame, text=product[0]).grid()
    #         Label(products_frame, text=product[1]).grid()
    #         Label(products_frame, text=product[2]).grid()
    #         Label(products_frame, text="----------------").grid()

    # Tabla de productos
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_table.insert("", 0, text=product[0], values=(product[1]))

    # Ocultar pantallas
    add_label.grid_remove()
    info_label.grid_remove()

    info_frame.grid_remove()
    add_frame.grid_remove()


def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=60,
        pady=20,
    )
    add_label.grid(row=0, column=0, columnspan=2)

    add_separator.grid(row=1, column=1)

    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, sticky=W)
    add_name_label.config(font=("Arial", 10))
    add_name_entry.grid(row=1, column=1, sticky=W)
    add_name_entry.config(font=("Arial", 10))

    add_price_label.grid(row=2, column=0, sticky=W)
    add_price_label.config(font=("Arial", 10))
    add_price_entry.grid(row=2, column=1, sticky=W)
    add_price_entry.config(font=("Arial", 10))

    add_description_label.grid(row=3, column=0, sticky=NW)
    add_description_label.config(font=("Arial", 10))
    add_description_entry.grid(row=3, column=1, sticky=W)
    add_description_entry.config(
        width=30,
        height=7,
        font=("Arial", 10),
    )

    add_separator.grid(row=5, column=1)

    boton.config(
        pady=3,
        padx=15,
        bg="black",
        fg="white",
    )
    boton.grid(
        row=6,
        column=1,
        sticky=NW,
    )

    # Ocultar pantallas
    home_label.grid_remove()
    info_label.grid_remove()

    products_frame.grid_remove()
    products_table.grid_remove()
    info_frame.grid_remove()


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=96,
        pady=20,
    )
    info_label.grid(row=0, column=0)

    info_frame.grid(row=1)
    data_label.config(font=("Arial", 10))
    data_label.grid(row=1, column=0)

    # Ocultar pantallas
    home_label.grid_remove()
    add_label.grid_remove()

    products_frame.grid_remove()
    products_table.grid_remove()
    add_frame.grid_remove()


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
