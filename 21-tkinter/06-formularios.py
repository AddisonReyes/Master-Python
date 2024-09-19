from tkinter import *


class Form:
    def __init__(self, title: str = "", size: str = "", header: str = None) -> None:
        self.header = header
        self.title = title
        self.size = size

    def create_form(self) -> None:
        self.window = Tk()

        self.window.resizable(0, 0)
        self.window.title(self.title)
        if len(self.size) > 1:
            self.window.geometry(self.size)

        self.create_header()

    def run(self) -> None:
        self.window.mainloop()

    def create_header(self, header_label: str = "Formulario con Tkinter") -> None:
        header = Label(self.window, text=header_label)
        header.config(
            fg="white",
            bg="darkgrey",
            font=("Open Sans", 18),
            padx=75,
            pady=10,
        )

        header.grid(
            row=0,
            column=0,
            columnspan=8,
            sticky=W,
        )

    def generate_fields(
        self, data_fields: list[dict], row: int = 1, column: int = 0
    ) -> list:

        for fields in data_fields:
            label = Label(self.window, text=fields["label"])
            label.grid(row=row, column=column, padx=5, pady=5, sticky=W)

            entry = Entry(self.window)
            entry.grid(row=row, column=column + 1, padx=5, pady=5)
            entry.config(justify="left", state="normal")
            row += 1

        return [row, column]

    def create_big_field(self, field: dict, row: int = 1, column: int = 0) -> list:
        label = Label(self.window, text=field["label"])
        label.grid(row=row, column=column, padx=5, pady=5, sticky=N)

        field = Text(self.window)
        field.grid(row=row, column=column + 1, padx=5, pady=5)
        field.config(
            width=30,
            height=5,
            font=("Arial", 12),
            padx=15,
            pady=15,
        )

        row += 1
        return [row, column]

    def create_button(self, field: dict, row: int = 1, column: int = 0) -> list:
        button = Button(self.window, text=field["label"])
        button.grid(row=row, column=column, padx=5, pady=5, sticky=W)
        button.config(
            padx=15,
            pady=15,
            bg="green",
            fg="white",
        )

        row += 1
        return [row, column]

    def create_space(self, row: int = 1, column: int = 0) -> list:
        Label(self.window).grid(row=row, column=column)
        row += 1

        return [row, column]


def main():
    form = Form()
    form.create_form()

    fields: list[dict] = [
        {"label": "Nombre"},
        {"label": "Apellidos"},
    ]

    column: int = 0
    row: int = 1

    row, column = form.generate_fields(data_fields=fields, row=row, column=column)

    big_field: dict = {"label": "Description"}
    row, column = form.create_big_field(field=big_field, row=row, column=column)

    row, column = form.create_space(row=row, column=column)

    button: dict = {"label": "Enviar"}
    row, column = form.create_button(field=button, row=row, column=column)

    form.run()


if __name__ == "__main__":
    main()
