import sqlite3 as sql

db_path = 'db_folder/database.db'

def check_login(username):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()
    try:
        c.execute("SELECT password FROM Admin WHERE username='" + username + "'")
    except: 
        return False

    try:
        return c.fetchone()[0]
    except:
        return False

def get_all_post_contents():
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()
    try:
        c.execute("SELECT post_title, post_author, post_date, post_content FROM Posts")
    except: 
        return False
    
    try:
        return c.fetchall()
    except: return False
