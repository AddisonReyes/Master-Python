from tkinter import *


def main() -> None:
    ventana = Tk()

    ventana.title("Marcos | Master en Python")
    # ventana.geometry("700x400")
    ventana.resizable(0, 0)

    w: float = 250
    h: float = 250

    marco_padre0 = Frame(ventana, width=w, height=h)
    marco_padre0.config(bg="white")
    marco_padre0.pack(side=TOP, fill=X, expand=True)

    marco = Frame(marco_padre0, width=w, height=h)
    marco.config(bg="red", bd=12, relief="raised")
    marco.pack(side=LEFT, anchor=NW)
    marco.pack_propagate(False)

    texto = Label(marco, text="Primer marco")
    texto.config(
        bg="red",
        fg="white",
        font=("Arial", 20),
        anchor=CENTER,
        height=2,
        width=10,
        border=3,
        relief=RAISED,
    )
    texto.pack(
        side=BOTTOM,
        anchor=CENTER,
        fill=X,
        expand=YES,
    )

    marco = Frame(marco_padre0, width=w, height=h)
    marco.config(bg="green", bd=12, relief="raised")
    marco.pack(side=RIGHT, anchor=NE)

    marco_padre1 = Frame(ventana, width=w, height=h)
    marco_padre1.config(bg="white")
    marco_padre1.pack(side=BOTTOM, fill=X, expand=True)

    marco = Frame(marco_padre1, width=w, height=h)
    marco.config(bg="blue", bd=12, relief="raised")
    marco.pack(side=LEFT, anchor=SW)

    marco = Frame(marco_padre1, width=w, height=h)
    marco.config(bg="yellow", bd=12, relief="raised")
    marco.pack(side=RIGHT, anchor=SE)

    ventana.mainloop()


if __name__ == "__main__":
    main()
