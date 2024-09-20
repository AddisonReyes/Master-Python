"""
CALCULADORA:
- Dos campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado enuna alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox


def calculate(operation: str) -> None:
    try:
        n1: float = float(numero1.get())
        n2: float = float(numero2.get())
    except:
        MessageBox.showerror("Error", "Introduce bien los datos")

    match (operation):
        case "sumar":
            resultado.set(n1 + n2)
        case "restar":
            resultado.set(n1 - n2)
        case "multiplicar":
            resultado.set(n1 * n2)
        case "dividir":
            resultado.set(n1 / n2)

    mostrar_resultado()


def mostrar_resultado() -> None:
    MessageBox.showinfo(
        "Resultado", f"El resultado de la operacion es: {resultado.get()}"
    )

    numero1.set("")
    numero2.set("")


ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
# ventana.geometry("400x400")
ventana.config(
    bd=26,
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=RAISED,
)
marco.pack(
    side=TOP,
    anchor=CENTER,
)
marco.pack_propagate(False)

Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()


boton_sumar = Button(
    marco,
    text="Sumar",
    command=lambda: calculate(operation="sumar"),
)
boton_sumar.pack(side=LEFT, fill=X, expand=YES)

boton_restar = Button(
    marco,
    text="Restar",
    command=lambda: calculate(operation="restar"),
)
boton_restar.pack(side=LEFT, fill=X, expand=YES)

boton_multiplicar = Button(
    marco,
    text="Multiplicar",
    command=lambda: calculate(operation="multiplicar"),
)
boton_multiplicar.pack(side=LEFT, fill=X, expand=YES)

boton_dividir = Button(
    marco,
    text="Dividir",
    command=lambda: calculate(operation="dividir"),
)
boton_dividir.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()
