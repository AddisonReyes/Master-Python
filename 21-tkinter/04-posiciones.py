from tkinter import *


def main() -> None:
    ventana = Tk()
    # ventana.geometry("700x500")
    ventana.resizable(0, 0)

    texto = Label(ventana, text="Bienvenido a mi programa")
    texto.config(
        font=("Consolas", 30),
        fg="white",
        bg="black",  # "#000000"
        padx=520,
        pady=20,
    )
    texto.pack(side=TOP)

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
    texto.pack(side=TOP, expand=YES, fill=X)

    data: list[list] = [
        ["Basico 1", "green", LEFT],
        ["Basico 2", "red", LEFT],
        ["Basico 3", "pink", LEFT],
    ]

    for d in data:
        texto = Label(ventana, text=d[0])
        texto.config(
            font=("Arial", 12),
            cursor="spider",
            justify=RIGHT,
            # width=400,
            bg=d[1],
            height=3,
            padx=10,
            pady=20,
        )
        texto.pack(side=d[2], expand=YES, fill=X)

    ventana.mainloop()


if __name__ == "__main__":
    main()
