import sqlite3



def add_manga_name(anime_name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO manga_table(name) VALUES (?)", (anime_name,))
    conn.commit()
    conn.close()

def add_manga_file(file_id,series_id,manga_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO files(file_id,series_id,manga_id) VALUES (?,?,?)", (file_id,series_id,manga_id))
    conn.commit()
    conn.close()

def delete_manga(manga_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM manga_table WHERE id = ?",(manga_id))
    cursor.execute("DELETE FROM files WHERE manga_id = ?",(manga_id))

    conn.commit()
    conn.close()

def delete_manga_seria(manga_id,series_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM files WHERE manga_id = ? AND series_id = ?",(manga_id,series_id))

    conn.commit()
    conn.close()


def get_manga_id(manga_name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM manga_table WHERE name = ?",(manga_name,))
    manga_id = cursor.fetchone()
    conn.close()
    return manga_id

def get_all_manga_names():
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name,id FROM manga_table")
    manga_names = cursor.fetchall()
    conn.close()
    manga_list ={}
    for i,id in manga_names:
        manga_list[i]=id
    return manga_list

def get_manga_name(manga_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM manga_table WHERE id = ?",(manga_id,))
    manga_name = cursor.fetchone()
    conn.close()
    return manga_name

def searching_manga(name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    name = name.lower()
    name = f"%{name}%"
    cursor.execute("SELECT * FROM manga_table WHERE name LIKE ?",(name,))
    manga_names = cursor.fetchall()
    conn.close()
    return manga_names

def get_manga_series_id():
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT manga_id,series_id FROM files")
    manga_series = cursor.fetchall()
    conn.close()
    return manga_series

def get_manga_seria(manga_id,series_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT file_id FROM files WHERE manga_id = ? AND series_id = ?",(manga_id,series_id))
    manga_seria = cursor.fetchone()
    conn.close()
    return manga_seria

def get_manga_series(manga_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT file_id,series_id FROM files WHERE manga_id = ?",(manga_id,))
    manga_series = cursor.fetchall()
    conn.close()
    return manga_series


def add_category(manga_id,category):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE manga_table SET category = ? WHERE id = ?",(category,manga_id))
    conn.commit()
    conn.close()

def rem_category(manga_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE manga_table SET category = NULL WHERE id = ?",(manga_id,))
    conn.commit()
    conn.close()








