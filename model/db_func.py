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
