from flask import g
# import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

uri = 'postgres://ungukuf9o6sbq:pe49dcb2a9fbfde8f38be66632713ee8c5323d58d6d23c910206072f97359a053@ec2-54-159-212-244.compute-1.amazonaws.com:5432/d9jgr7g9240o7k'

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
