import sqlite3 as sql
import hashlib 

db_path = 'db_folder/database.db'

def md5(text):
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

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
    except:
        conn.close() 
        return False

def change_username(current_username, new_username, password):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    hashed = md5(password)

    try:
        c.execute("SELECT password FROM Admin WHERE username='" + current_username + "'")
        password_rec = c.fetchone()[0]
    except: 
        return False
    
    if hashed != password_rec:
        return False

    try:
        c.execute("UPDATE Admin SET username='" + new_username + "' WHERE username='" + current_username + "'")
        conn.commit()
        conn.close()
    except: 
        return False

    return True

def change_password(current_username, password, new_password):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    hashed = md5(password)

    try:
        c.execute("SELECT password FROM Admin WHERE username='" + current_username + "'")
        password_rec = c.fetchone()[0]
    except: 
        return False
    
    if hashed != password_rec:
        return False

    new_hashed = md5(new_password)

    try:
        c.execute("UPDATE Admin SET password='" + new_hashed + "' WHERE username='" + current_username + "'")
        conn.commit()
        conn.close()
    except: 
        return False

    return True