import sqlite3
import sqlite3 as sq

from typing import Union

DB_NAME = 'braintrainer.db'
DB_USER_TABLE_NAME = 'users'


def make_db():
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f""" CREATE TABLE IF NOT EXISTS {DB_USER_TABLE_NAME} (
        name TEXT NOT NULL UNIQUE ,
        score INTEGER DEFAULT 0
        )""")

def search_in_db(name: str) -> Union[list, False]:
    try:
        with sq.connect(DB_NAME) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM {DB_USER_TABLE_NAME} WHERE name = "{name}"')
            rows = cursor.fetchall()
            return rows if rows else False
    except sqlite3.Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

def add_user(name: str, score: int = 0) -> Union[dict, bool]:
    rows = search_in_db(name)
    if not rows:
        try:
            with sq.connect(DB_NAME) as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO {DB_USER_TABLE_NAME} VALUES ("{name}", {score})')
        except sq.Error as e:
            print(f'Database error: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')
        else:
            print('Player added successfully!')
            cur.close()
            return {'name': name, 'score': score}
    else:
        print('Such a player already exists')
        return False

def load_user(name: str) -> Union[dict, bool]:
    rows = search_in_db(name)
    if rows:
        result = [dict(row) for row in rows]
        print(result[0])
        return result[0]
    else:
        print('Такого игрока не существует')
        return False
