import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students
    VALUES (?, ?, ?)
    """, (name, age, city)
    )
    conn.commit()


if __name__ == '__main__':
    connection = sqlite3.connect('database.db') # DataBase
    create_tables(connection)
    add_student(connection, "Igor", 22, "Bishkek")
    add_student(connection, "Arzybek", 26, "Sokuluk")
    connection.close()