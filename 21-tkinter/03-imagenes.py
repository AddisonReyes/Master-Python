import os.path
from tkinter import *

from PIL import Image, ImageTk


def main():
    ventana = Tk()
    # ventana.geometry("960x540")

    Label(ventana, text="Hola, sooy Victor!!").pack(anchor=W)

    img_path = os.path.abspath("./img/fox.jpg")

    if not os.path.isfile(img_path):
        img_path = os.path.abspath("./21-tkinter/img/fox.jpg")

    imagen = Image.open(img_path)
    render = ImageTk.PhotoImage(imagen)

    Label(ventana, image=render).pack(anchor=E)

    ventana.mainloop()


if __name__ == "__main__":
    main()
