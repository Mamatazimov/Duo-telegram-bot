import sqlite3

def init_db():
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   user_id INTEGER UNIQUE,
                   referrer_id INTEGER,
                   points INTEGER DEFAULT 0
                   )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos(
                    id INTEGER PRIMARY KEY,
                    file_id TEXT,
                    series_id INTEGER,
                    anime_id INTEGER
                    )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animes_table(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    category TEXT,
                    other_name TEXT
                    )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files(
                    id INTEGER PRIMARY KEY,
                    file_id TEXT,
                    series_id INTEGER,
                    manga_id INTEGER
                    )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS manga_table(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    category TEXT,
                    other_name TEXT
                    )
        """)

    
    conn.commit()
    conn.close()