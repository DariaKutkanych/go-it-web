import sqlite3


def create_db():

    with open("education.sql") as file:
        sql = file.read()

    with sqlite3.connect("education.db") as con:
            cur = con.cursor() 
            cur.executescript(sql)


if __name__=="__main__":

    create_db()
