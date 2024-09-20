from tkinter import *
from tkinter import messagebox as MessageBox


class Calculadora:
    def __init__(self, title: str = "Ejercicio completo con Tkinter") -> None:
        self.ventana = Tk()
        self.ventana.title(title)
        # ventana.geometry("400x400")
        self.ventana.config(
            bd=26,
        )

    def crear_calculadora(self) -> None:
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()

        self.marco = Frame(self.ventana, width=300, height=200)
        self.marco.config(
            padx=15,
            pady=15,
            bd=5,
            relief=RAISED,
        )
        self.marco.pack(
            side=TOP,
            anchor=CENTER,
        )
        self.marco.pack_propagate(False)

        self.crear_campos()
        self.crear_botones()

        self.ventana.mainloop()

    def crear_campos(self) -> None:
        Label(self.marco, text="Primer numero: ").pack()
        Entry(self.marco, textvariable=self.numero1, justify="center").pack()

        Label(self.marco, text="Segundo numero: ").pack()
        Entry(self.marco, textvariable=self.numero2, justify="center").pack()

        Label(self.marco, text="").pack()

    def crear_botones(self) -> None:
        self.boton_sumar = Button(
            self.marco,
            text="Sumar",
            command=lambda: self.calculate(operation="sumar"),
        )
        self.boton_sumar.pack(side=LEFT, fill=X, expand=YES)

        self.boton_restar = Button(
            self.marco,
            text="Restar",
            command=lambda: self.calculate(operation="restar"),
        )
        self.boton_restar.pack(side=LEFT, fill=X, expand=YES)

        self.boton_multiplicar = Button(
            self.marco,
            text="Multiplicar",
            command=lambda: self.calculate(operation="multiplicar"),
        )
        self.boton_multiplicar.pack(side=LEFT, fill=X, expand=YES)

        self.boton_dividir = Button(
            self.marco,
            text="Dividir",
            command=lambda: self.calculate(operation="dividir"),
        )
        self.boton_dividir.pack(side=LEFT, fill=X, expand=YES)

    def calculate(self, operation: str) -> None:
        try:
            n1: float = float(self.numero1.get())
            n2: float = float(self.numero2.get())
        except:
            MessageBox.showerror("Error", "Introduce bien los datos")

        match (operation):
            case "sumar":
                self.resultado.set(n1 + n2)
            case "restar":
                self.resultado.set(n1 - n2)
            case "multiplicar":
                self.resultado.set(n1 * n2)
            case "dividir":
                self.resultado.set(n1 / n2)

        self.mostrar_resultado()

    def mostrar_resultado(self) -> None:
        MessageBox.showinfo(
            "Resultado", f"El resultado de la operacion es: {self.resultado.get()}"
        )

        self.numero1.set("")
        self.numero2.set("")


def main():
    Calculadora = Calculadora()
    Calculadora.crear_calculadora()


if __name__ == "__main__":
    main()
