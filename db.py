import sqlite3

def create_connection():
    conn = sqlite3.connect('data/database.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        task TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                      )''')
    conn.commit()
    conn.close()

