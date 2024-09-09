import notes.actions as notes
import users.user as model


class Actions():

    def __init__(self) -> None:
        pass

    def register(self) -> None:
        print("\nOk!! Vamos a registrarte en el sistema...")

        name: str = input("Introduce tu nombre: ")
        last_name: str = input("Introduce son tus apellidos: ")
        email: str = input("Introduce tu email: ")
        password: str = input("Introduce tu contraseña: ")

        new_user = model.User(name=name, last_name=last_name, email=email, password=password)
        record = new_user.register()

        if record[0] >= 1:
            print(f"\nPerfecto {record[1].name} te has registrado con el email \'{record[1].email}\'")
        
        else:
            print("\nNo te has registrado correctamente!!!")


    def login(self) -> None:
        print("\nVale!! Identificate en el sistema...")

        try:
            email: str = input("Introduce tu email: ")
            password: str = input("Introduce tu contraseña: ")

            new_user = model.User(name="", last_name="", email=email, password=password)
            login = new_user.identify()

            if email == login[3]:
                print(f"\nBienvenido \n{login[1]}, te has registrado en el sistema el {login[5]}")
                self.nextActions(login)
            
            else:
                print("\nNo te has logueado correctamente!!!")
        
        except Exception as e:
            print(f"\nLogin incorrecto!! Intentalo mas tarde")
            # print(type(e).__name__)
            # print(type(e))
    
    def nextActions(self, login: list):
        print("""
Acciones disponibles:
    - Crear nota (crear)
    - Mostrar tus notas (mostrar)
    - Eliminar nota (eliminar)
    - Salir (salir)
        """)

        action = input("¿Que deseas hacer? ")
        noteActions = notes.Actions()

        match action:
            case 'crear':
                print("\nVamos a crear")
                noteActions.create(user=login)

            case 'mostrar':
                print("\nVamos a mostrar")
                noteActions.view(user=login)

            case 'eliminar':
                print("\nVamos a eliminar")
                noteActions.delete(user=login)

            case 'salir':
                print(f"\nOk {login[1]}, hasta pronto!!!")
                exit()

            case _:
                pass

        # print(f"\n\n{login}\n\n")
        self.nextActions(login)