import sqlite3
from sqlite3 import Error
import questionnaire as q


class DataBase:
    def __init__(self, database):
        self.database = database
        try:
            self.database_connect = sqlite3.connect(self.database)
            print(f"Соединение с базой данных {database} установлено")
        except Error:
            print(f"Ошибка {Error} соединения с базой данных")
        self.cursor = self.database_connect.cursor()

    def clear_database(self):
        self.cursor.execute("""
                    DROP TABLE IF EXISTS quiz_question""")

    def create_tests(self):

        create_tests_table_sql = """
                    CREATE TABLE IF NOT EXISTS quiz_question(
                    id INTEGER PRIMARY KEY,
                    number INTEGER,
                    title TEXT,
                    ans1 TEXT,
                    ans2 TEXT,
                    ans3 TEXT,
                    ans4 TEXT,
                    r_ans INTEGER
                    )"""

        self.cursor.execute(create_tests_table_sql)

        counter = 1
        for item in q.questionnaire:
            insert_into_questions = """INSERT or IGNORE INTO quiz_question VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(insert_into_questions, [None, counter, item[0], item[1][0], item[1][1], item[1][2], "none", int(item[2])+1])
            counter += 1

        self.database_connect.commit()

    def get_questions(self):
        self.cursor.execute("""
                    SELECT *
                    FROM quiz_question
                    ORDER BY id""")
        data = self.cursor.fetchall()
        return data


if __name__ == "__main__":
    db = DataBase('test.sqlite3')
    db.clear_database()
    db.create_tests()
    q = db.get_questions()
    for item in q:
        print(item)


