import mysql.connector

def db_conexion():
    database = mysql.connector.connect(
        database="master_python",
        host="localhost",
        user="root",
        passwd="",
        port=3306,
    )

    cursor = database.cursor(buffered=True)
    return database, cursor