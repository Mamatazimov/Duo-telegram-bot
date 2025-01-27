import sqlite3



def add_anime_name(anime_name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO animes_table(name) VALUES (?)", (anime_name,))
    conn.commit()
    conn.close()

def add_anime_video(video_id,series_id,anime_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO videos(file_id,series_id,anime_id) VALUES (?,?,?)", (video_id,series_id,anime_id))
    conn.commit()
    conn.close()

def delete_anime(anime_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM animes_table WHERE id = ?",(anime_id))
    cursor.execute("DELETE FROM videos WHERE anime_id = ?",(anime_id))

    conn.commit()
    conn.close()

def delete_anime_seria(anime_id,series_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM videos WHERE anime_id = ? AND series_id = ?",(anime_id,series_id))

    conn.commit()
    conn.close()

def get_anime_id(anime_name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM animes_table WHERE name = ?",(anime_name,))
    anime_id = cursor.fetchone()
    conn.close()
    return anime_id

def get_all_anime_names():
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name,id FROM animes_table")
    anime_names = cursor.fetchall()
    conn.close()
    anime_list ={}
    for i,id in anime_names:
        anime_list[i]=id
    return anime_list

def searching_anime(name):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    name = name.lower()
    name = f"%{name}%"
    cursor.execute("SELECT * FROM animes_table WHERE name LIKE ?",(name,))
    anime_names = cursor.fetchall()
    conn.close()
    result = anime_names
    return result

def get_anime_series(anime_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT file_id,series_id FROM videos WHERE anime_id = ?",(anime_id,))
    series = cursor.fetchall()
    conn.close()
    return series

def get_anime_name(anime_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM animes_table WHERE id = ?",(anime_id,))
    name = cursor.fetchone()
    conn.close()
    return name

def get_anime_series_id():
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT anime_id,series_id FROM videos")
    file_id = cursor.fetchall()
    conn.close()
    return file_id

def get_anime_seria(anime_id,seria_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("SELECT file_id FROM videos WHERE anime_id = ? AND series_id = ?",(anime_id,seria_id))
    video = cursor.fetchone()
    conn.close()
    return video

def add_category(anime_id,category):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE animes_table SET category = ? WHERE id = ?",(category,anime_id))
    conn.commit()
    conn.close()

def rem_category(anime_id):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE animes_table SET category = NULL WHERE id = ?",(anime_id,))
    conn.commit()
    conn.close()


