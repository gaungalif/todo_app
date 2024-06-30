import hashlib

def hash_password(password):
    """
    Hash the password using SHA-256 algorithm.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def validate_input(input_value):
    """
    Validasi input pengguna untuk memastikan tidak kosong dan tidak hanya berupa spasi.
    """
    if input_value and input_value.strip():
        return True
    return False

def show_message(message, title="Info"):
    """
    Tampilkan pesan menggunakan messagebox Tkinter.
    """
    from tkinter import messagebox
    messagebox.showinfo(title, message)
