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
        pass

    def delete(self, user):
        pass