import sqlite3
import sqlite3 as sq

DB_NAME = 'braintrainer.db'
DB_USER_TABLE_NAME = 'users'


def make_db():
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f""" CREATE TABLE IF NOT EXISTS {DB_USER_TABLE_NAME} (
        name TEXT NOT NULL UNIQUE ,
        gender INTEGER NOT NULL ,
        school_class INTEGER NOT NULL ,
        score INTEGER DEFAULT 0
        )""")


def add_user(name: str, gender: int, school_class: int, score: int = 0) -> dict:
    try:
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute(f'INSERT INTO {DB_USER_TABLE_NAME} VALUES ("{name}", {gender}, {school_class}, {score})')
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
            return result[0]


def load_user(name: str) -> dict:
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
                result = [dict(row) for row in rows]
                return result[0]
            else:
                return {}
