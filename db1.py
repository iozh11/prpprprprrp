# редактирование, добавление удаление
import sqlite3

class Datebase:
    def __init__(self) -> None:
        self.con = sqlite3.connect("tasks.sqlite", check_same_thread=False)  # подключение
        self.cur = self.con.cursor()  # создание курсора для запросов к БД

        sql = """CREATE TABLE IF NOT EXISTS tasks(
                name TEXT,
                date INT,
                ready INT
        )
        """
        self.cur.execute(sql)

        self.con.commit()



    def add_task(self, name, date, ready):
        sql = "INSERT INTO tasks VALUES(?,?,?)"

        self.cur.execute(sql, (name, date, ready))  # запрос

        self.con.commit()  # сохранение изменений



    def select_all_task(self):
        sql = "SELECT * FROM tasks"

        self.cur.execute(sql)  # запрос
        data = self.cur.fetchall()  # записываю все найденные записи
        # print(data)
        return data
    


    def select_ready_task(self):
        sql = "SELECT * FROM tasks WHERE ready = 1"

        self.cur.execute(sql)  # запрос
        data = self.cur.fetchall()  # записываю все найденные записи

        return data
    
    def select_notready_task(self):
        sql = "SELECT * FROM tasks WHERE ready = 0"

        self.cur.execute(sql)  # запрос
        data = self.cur.fetchall()  # записываю все найденные записи

        return data
    
    def select_task(self, name):
        sql = "SELECT * FROM tasks WHERE name=?"

        self.cur.execute(sql, (name,))
        data = self.cur.fetchone()

        return data

# datebase = Datebase()
# datebase()
# datebase.add_task('Покушать', 1111, 0)
# datebase.select_all_task()

