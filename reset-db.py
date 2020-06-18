from db import db_path
import os
import sqlite3 as sql

conn = sql.connect(db_path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Admin')
c.execute('DROP TABLE IF EXISTS Posts')
c.execute('DROP TABLE IF EXISTS Settings')

c.execute("""CREATE TABLE "Admin" (
            "username"  TEXT NOT NULL,
            "name" TEXT,
            "password"  TEXT,
            PRIMARY KEY ("username")
            );""")

c.execute("""CREATE TABLE "Posts" (
            "post_title"  TEXT NOT NULL,
            "post_author" TEXT,
            "post_date"  TEXT,
            "post_content"  TEXT,
            PRIMARY KEY ("post_title")
            );""")

c.execute("""CREATE TABLE "Settings" (
            "main_content"  TEXT NOT NULL,
            PRIMARY KEY ("main_content")
            );""")

#pass = default_pass
c.execute("INSERT INTO Admin VALUES ('admin_default', 'Linus Torvalds', 'b827ae8d71bf3ab400e3822a16041749')")
c.execute("INSERT INTO Posts VALUES ('My first Post!', 'Linus Torvalds', '6/15/2020', 'This is my first post, I am so excited to see what I can do with pyBLOG!')")
c.execute("INSERT INTO Posts VALUES ('This is the second post', 'Linus Torvalds', '6/16/2020', 'This is a second post, I am loving pyBLOG so far!')")
c.execute("INSERT INTO Settings VALUES ('Hello and welcome to my pyBLOG!')")

conn.commit()
conn.close()
