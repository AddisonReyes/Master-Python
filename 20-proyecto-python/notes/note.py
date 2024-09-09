import users.conexion as conexion


database, cursor = conexion.db_conexion()


class Note():

    def __init__(self, user_id: int, title: str = "", description: str = "") -> None:
        self.description: str = description
        self.user_id: int = user_id
        self.title: str = title

    def save(self):
        sql_query: str = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        note: tuple = (self.user_id, self.title, self.description)

        cursor.execute(sql_query, note)
        database.commit()

        return [cursor.rowcount, self]
    
    def lists_notes(self):
        sql_query: str = f"SELECT * FROM notas WHERE usuario_id = {self.user_id}"

        cursor.execute(sql_query)
        result = cursor.fetchall()

        return result
    
    def delete_note(self):
        sql_query: str = f"DELETE FROM notas WHERE usuario_id = {self.user_id } AND titulo LIKE '%{self.title}%'"

        cursor.execute(sql_query)
        database.commit()

        return [cursor.rowcount, self]