import sqlite3 as sql

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

