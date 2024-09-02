import mysql.connector


def view_tables(cursor):
    cursor.execute("SHOW TABLES")
    for t in cursor:
        print(t)


def view_databases(cursor):
    cursor.execute("SHOW DATABASES")
    for db in cursor:
        print(db)


def main():
    database = mysql.connector.connect(
        database="master_python",
        host="localhost",
        user="root",
        passwd="",
    )

    print(database)

    cursor = database.cursor(buffered=True)

    cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id int(10) auto_increment not null,
            marca varchar(40) not null,
            modelo varchar(40) not null,
            precio float(10, 2) not null,
            CONSTRAINT pk_vehiculo PRIMARY KEY(id)
        )
    """)

    # cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
    # database.commit()

    # coches = [
    #     ('Seat', 'Ibiza', 5000),
    #     ('Renault', 'Clio', 15000),
    #     ('Citroen', 'Saxo', 2000),
    #     ('Mercedes', 'Clase C', 35000),
    # ]

    # cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
    # database.commit()

    # DELETE
    cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
    # cursor.execute("DELETE FROM vehiculos")
    database.commit()

    print(cursor.rowcount, "borrados!!")

    # UPDATE
    cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'")
    database.commit()

    print(cursor.rowcount, "actualizados!!")

    # SELECT 
    cursor.execute("SELECT * FROM vehiculos")
    result = cursor.fetchall()

    print("---- TODOS MIS COCHES ----")
    for coche in result:
        print(coche)

    cursor.execute("SELECT * FROM vehiculos")    
    coche = cursor.fetchone()
    print(f"\n---- UN COCHE ----")
    print(coche)


    # view_tables(cursor)
    # view_databases(cursor)

if __name__ == '__main__':
    main()