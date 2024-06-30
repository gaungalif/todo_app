from db import create_table
import ui

if __name__ == "__main__":
    # Inisialisasi tabel database
    create_table()
    
    # Tampilkan jendela login
    ui.show_login_window()

