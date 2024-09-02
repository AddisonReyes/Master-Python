"""
    Proyecto Python y MySQL
        - Abrir asistente
        - Login o registro
        - Si elegimos registro, creara un usuario en la base de datos
        - Si elegimos login, identificara al usuarion y peguntara por los datos
        - Crear nota, mostrar notas, borrarlas
"""


from users import actions


def main():
    act = actions.Actions()

    print("""
Acciones disponibles:
    - registro
    - login
    """)

    action: str = input("¿Que quieres hacer? ")
    
    match action:
        case 'registro':
            act.register()
        
        case 'login':
            act.login()

        case _:
            pass


if __name__ == '__main__':
    main()