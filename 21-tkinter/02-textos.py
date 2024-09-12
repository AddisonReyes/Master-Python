from tkinter import *


def pruebas(nombre: str, apellidos: str, pais: str) -> str:
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"


def main() -> None:
    ventana = Tk()
    ventana.geometry("700x500")
    ventana.resizable(0, 0)

    texto = Label(ventana, text="Bienvenido a mi programa")
    texto.config(
        font=("Consolas", 30),
        fg="white",
        bg="black",  # "#000000"
        padx=520,
        pady=20,
    )
    texto.pack()

    texto = Label(ventana, text="Master en Python")
    texto.config(
        font=("Arial", 12),
        justify=RIGHT,
        bg="red",
        # width=400,
        height=3,
        padx=10,
        pady=20,
    )
    texto.pack(
        anchor=N,
    )

    texto = Label(ventana, text="Soy Addison Reyes")
    texto.config(
        font=("Arial", 12),
        cursor="spider",
        justify=RIGHT,
        bg="orange",
        # width=400,
        height=3,
        padx=10,
        pady=20,
    )
    texto.pack(
        anchor=SE,
    )

    label = pruebas(
        apellidos="Peralta",
        nombre="Antonio",
        pais="Cuba",
    )
    texto = Label(ventana, text=label)
    texto.config(
        font=("Arial", 12),
        cursor="spider",
        justify=RIGHT,
        # width=400,
        bg="green",
        height=3,
        padx=10,
        pady=20,
    )
    texto.pack(
        anchor=CENTER,
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()
