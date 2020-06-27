import sqlite3 as sql
import hashlib
from datetime import datetime

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

def change_username(current_username, password, new_username):
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

def get_specific_post(post_title):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()
    try:
        c.execute("SELECT post_title, post_author, post_date, post_content FROM Posts WHERE post_title='" + post_title + "'")
    except: 
        return False
    # print(c.fetchall())
    # print(len(c.fetchall()))
    try:
        returned = c.fetchall()
        if len(returned) > 0:
            return returned
        else:
            return False
    except:
        conn.close() 
        return False

def change_name(current_name, new_name, password):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    hashed = md5(password)

    try:
        c.execute("SELECT password FROM Admin WHERE name='" + current_name + "'")
        password_rec = c.fetchone()[0]
    except: 
        return False
    
    if hashed != password_rec:
        return False

    try:
        c.execute("UPDATE Admin SET name='" + new_name + "' WHERE name='" + current_name + "'")
        conn.commit()
        conn.close()
    except: 
        return False

    return True

def get_first_admin():
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try:    
        c.execute("Select name From Admin LIMIT 1")
        return c.fetchone()[0]
    except: return False

def get_main_content():
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try:
        c.execute("Select main_content FROM Settings")
        return c.fetchall()[0][0]
    except: return False

def get_profile_things():
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try:
        c.execute("Select * FROM Settings")
        return c.fetchall()[0]
    except: return False

def change_main_content(new_content):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try: 
        c.execute("Select main_content FROM Settings")
        check = c.fetchall()[0][0]
    except: return False

    try:
        c.execute("UPDATE Settings SET main_content='" + new_content + "' WHERE main_content='" + check + "'")
        conn.commit()
        conn.close()
        return True
    except: return False

def change_bio(new_bio):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try: 
        c.execute("Select bio FROM Settings")
        check = c.fetchall()[0][0]
    except: return False

    try:
        c.execute("UPDATE Settings SET bio='" + new_bio + "' WHERE bio='" + check + "'")
        conn.commit()
        conn.close()
        return True
    except: return False

def change_city(new_city):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try: 
        c.execute("Select city FROM Settings")
        check = c.fetchall()[0][0]
    except: return False

    try:
        c.execute("UPDATE Settings SET city='" + new_city + "' WHERE city='" + check + "'")
        conn.commit()
        conn.close()
        return True
    except: return False


def change_country(new_country):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try: 
        c.execute("Select country FROM Settings")
        check = c.fetchall()[0][0]
    except: return False

    try:
        c.execute("UPDATE Settings SET country='" + new_country + "' WHERE country='" + check + "'")
        conn.commit()
        conn.close()
        return True
    except: return False

def get_welcome_message():
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try:
        c.execute("Select welcome_message FROM Settings")
        return c.fetchall()[0][0]
    except: return False

def change_welcome_message(new_message):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try: 
        c.execute("Select welcome_message FROM Settings")
        check = c.fetchall()[0][0]
    except: return False

    try:
        c.execute("UPDATE Settings SET main_content='" + new_message + "' WHERE main_content='" + check + "'")
        conn.commit()
        conn.close()
        return True
    except: return False

def create_new_post(title, content):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    author = get_first_admin()
    date = datetime.now().date()
    
    try:
        c.execute('''INSERT INTO Posts (post_title, post_author, post_date, post_content) VALUES (?,?,?,?)''', (title, author, date, content))
        conn.commit()
        return True
    except: 
        return False

def delete_post(title):
    db_path = 'db_folder/database.db'
    conn = sql.connect(db_path)
    c = conn.cursor()

    try:
        c.execute("DELETE FROM Posts WHERE post_title='" + title + "'")    
        conn.commit()
        return True
    except:
        return False
