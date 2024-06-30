from utils import hash_password, validate_input
from db import create_connection

def register(username, password):
    if not validate_input(username) or not validate_input(password):
        raise ValueError("Username dan password tidak boleh kosong.")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

def login(username, password):
    if not validate_input(username) or not validate_input(password):
        raise ValueError("Username dan password tidak boleh kosong.")
    
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user
