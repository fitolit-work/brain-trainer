import sqlite3
import sqlite3 as sq

DB_NAME = 'braintrainer.db'
DB_USER_TABLE_NAME = 'users'


def make_db():
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f""" CREATE TABLE IF NOT EXISTS {DB_USER_TABLE_NAME} (
        name TEXT NOT NULL UNIQUE ,
        score INTEGER DEFAULT 0
        )""")

def search_in_db(name: str):
    try:
        with sq.connect(DB_NAME) as con:
            con.row_factory = sqlite3.Row
    except:
        print('Error loading database')
    else:
        try:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM {DB_USER_TABLE_NAME} WHERE name = "{name}"')
        except:
            print('There was an error getting player')
            print('Check your input')
        else:
            rows = cursor.fetchall()
            if rows:
                return rows
            return False

def add_user(name: str, score: int = 0) -> dict:
    rows = search_in_db(name)
    if not rows:
        try:
            with sq.connect(DB_NAME) as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO {DB_USER_TABLE_NAME} VALUES ("{name}", {score})')
        except:
            print('A player registration error occurred')
            print('Check your input')

        else:
            print('Player added successfully!')
            cur.close()
            try:
                con.row_factory = sqlite3.Row
                cursor = con.cursor()
                cursor.execute(f'SELECT * FROM {DB_USER_TABLE_NAME} WHERE name = "{name}"')

            except:
                print('There was an error getting player')
                print('Check your input')
            else:
                rows = cursor.fetchall()
                result = [dict(row) for row in rows]
                print(result)
                print(result[0])
                return result[0]
    else:
        print('Такой игрок уже существует')

def load_user(name: str) -> dict:
    rows = search_in_db(name)
    if rows:
        result = [dict(row) for row in rows]
        print(result[0])
        return result[0]
    else:
        print('Такого игрока не существует')
