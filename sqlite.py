import sqlite3

def main() -> None:
    conexion = sqlite3.connect('pruebas.db')
    cursor = conexion.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255),
        description text,
        precio int(255)
    )""")
    conexion.commit()

    # clear_table(cursor)
    # conexion.commit()

    # insert_value(cursor)
    # conexion.commit()

    products_list = [
        ("Ordenador portatil", "Buen PC", 700),
        ("Telefono Movil", "Buen Telefono", 140),
        ("Placa base", "Buena placa", 80),
        ("Tablet", "Buena tablet", 300),
    ]

    # for product in products_list:
    #     insert_value(cursor, product[0], product[1], product[2])

    # cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", products_list)
    # conexion.commit()

    cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")
    conexion.commit()

    # cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
    cursor.execute("SELECT * FROM productos;")

    productos = cursor.fetchall()

    for producto in productos:
        print(f"ID: {producto[0]}")
        print(f"Titulo: {producto[1]}")
        print(f"Nombre: {producto[2]}")
        print(f"Descripcion: {producto[3]}\n")
    

    cursor.execute("SELECT titulo FROM productos;")
    productos = cursor.fetchone()
    print(productos)

    conexion.close()

def insert_value(cursor, title, description, price, id="null"):
    query: str = f"INSERT INTO productos VALUES ({id}, '{title}', '{description}', {price})"
    cursor.execute(query)

def clear_table(cursor):
    cursor.execute("DELETE FROM productos")


if __name__ == '__main__':
    main()