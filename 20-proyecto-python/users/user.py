import users.conexion as conexion
import datetime
import hashlib


database, cursor = conexion.db_conexion()


class User():

    def __init__(self, name: str, last_name: str, email: str, password: str) -> None:
        self.last_name: str = last_name
        self.password: str = password
        self.email: str = email
        self.name: str = name

    def register(self) -> list:
        date: datetime.date = datetime.date.today()

        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))

        sql_query: str = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        user: tuple = (self.name, self.last_name, self.email, encryption.hexdigest(), date)

        try:
            cursor.execute(sql_query, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identify(self) -> list:
        encryption = hashlib.sha256()
        encryption.update(self.password.encode('utf8'))
    
        sql_query: str = "SELECT * FROM usuarios WHERE email = %s AND clave = %s"
        user: tuple = (self.email, encryption.hexdigest())

        cursor.execute(sql_query, user)
        result = cursor.fetchone()
        return result