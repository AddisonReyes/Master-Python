import notes.note as model


class Actions():

    def create(self, user):
        print(f"Ok {user[1]}!! Vamos a crear una nueva nota...")

        title: str = input("Introduce el titulo de tu nota: ")
        description: str = input("Introduce el contenido de tu nota: ")

        note = model.Note(user_id=user[0], title=title, description=description)
        record = note.save()

        if record[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {record[1].title}")
        
        else:
            print(f"\nNo se ha guardado la nota, lo siento {user[1]}")

    def view(self, user):
        print(f"Vale {user[1]}!! Aqui tienes tus notas:")

        note = model.Note(user_id=user[0])
        notes = note.lists_notes()

        for note in notes:
            print("\n"+ "*"*20)
            print(f"{note[2]}")
            print(f"{note[3]}")
            print("*"*20)


    def delete(self, user):
        print(f"\nOkey {user[1]}!! Vamos a borrar notas")

        title = input("Introduce el titulo de la nota a borrar: ")
        note = model.Note(user_id=user[0], title=title)

        delete = note.delete_note()
        if delete[0] >= 1:
            print(f"Hemos borrado la nota: {note.title}")
        else:
            print("No se ha borrado la nota, prueba luego...")