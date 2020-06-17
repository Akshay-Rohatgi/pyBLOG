from db import db_path
import os
import sqlite3 as sql

conn = sql.connect(db_path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Admin')
c.execute('DROP TABLE IF EXISTS Posts')

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
c.execute("INSERT INTO Posts VALUES ('default_post', 'Linus Torvalds', '6/15/2020', 'First Post!')")
c.execute("INSERT INTO Posts VALUES ('default_post_2', 'Linus Torvalds', '6/16/2020', 'Second Post!')")
c.execute("INSERT INTO Settings VALUES ('Hello and welcome to my pyBLOG!')")

conn.commit()
conn.close()
