from db import db_path
import os
import sqlite3 as sql

conn = sql.connect(db_path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Admins')
c.execute('DROP TABLE IF EXISTS Posts')

