import sqlite3



def register_user(user_id, referrer_id=None):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users(user_id, referrer_id) VALUES (?, ?)", (user_id, referrer_id))
    conn.commit()
    conn.close()

def add_point(user_id, points):
    conn = sqlite3.connect("basa.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, user_id))
    conn.commit()
    conn.close()

