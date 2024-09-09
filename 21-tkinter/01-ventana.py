# Tkinter
# Modulo para crear interfaces graficas de usuario

import os.path
from tkinter import *


class Programa:

    def __init__(
        self,
        title: str = "Aplicacion",
        icon: str = "./img/mushroom.ico",
        icon_alt: str = "./21-tkinter/img/mushroom.ico",
        size: str = "770x470",
        resizable: bool = False,
    ) -> None:

        self.title = title
        self.icon = icon
        self.icon_alt = icon_alt
        self.size = size
        self.resizable = resizable

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        icon_path = os.path.abspath(self.icon)

        if not os.path.isfile(icon_path):
            icon_path = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(icon_path)

        # Mostrar texto en el programa
        text: Label = Label(ventana, text=icon_path)
        text.pack()

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

        # Arrancar y mostrar la ventana hasta que se cierre
        ventana.mainloop()


def main():
    prog = Programa()
    prog.cargar()


if __name__ == "__main__":
    main()
