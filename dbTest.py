from flask import g
# import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

uri = 'postgres://swfowakoyqaick:515c847a476c6837c04c297188f40fadfa94e2b947e0a9097e21caa3cc2d27e0@ec2-174-129-253-53.compute-1.amazonaws.com:5432/dc1lbk6bk5of1d'

def connect_db():
    conn = psycopg2.connect(uri, cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('admin', ))

    db[1].close()
    db[0].close()
