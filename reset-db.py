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

#pass = default_pass
c.execute("INSERT INTO Admin VALUES ('admin_default', 'Linus Torvalds', 'b827ae8d71bf3ab400e3822a16041749')")
conn.commit()
conn.close()