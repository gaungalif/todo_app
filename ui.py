import tkinter as tk
from tkinter import messagebox
import auth
import crud
from utils import validate_input, show_message

current_user_id = None

def show_login_window():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.configure(bg="lightblue")

    tk.Label(login_window, text="Username", bg="lightblue").pack(pady=5)
    username_entry = tk.Entry(login_window, bg="white")
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password", bg="lightblue").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", bg="white")
    password_entry.pack(pady=5)

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        if not validate_input(username) or not validate_input(password):
            show_message("Username dan password tidak boleh kosong.", "Login Failed")
            return

        try:
            user = auth.login(username, password)
            if user:
                global current_user_id
                current_user_id = user[0]
                login_window.destroy()
                show_main_window()
            else:
                show_message("Username atau password salah!", "Login Failed")
        except ValueError as e:
            show_message(str(e), "Login Failed")

    tk.Button(login_window, text="Login", command=handle_login).pack(pady=5)

    tk.Label(login_window, text="Don't have an account? Register below.", bg="lightblue").pack(pady=5)
    tk.Button(login_window, text="Register", command=lambda: show_register_window(login_window)).pack(pady=5)

    login_window.mainloop()

def show_register_window(parent):
    register_window = tk.Toplevel(parent)
    register_window.title("Register")
    register_window.configure(bg="lightblue")

    tk.Label(register_window, text="Username", bg="lightblue").pack(pady=5)
    username_entry = tk.Entry(register_window, bg="white")
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Password", bg="lightblue").pack(pady=5)
    password_entry = tk.Entry(register_window, show="*", bg="white")
    password_entry.pack(pady=5)

    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        if not validate_input(username) or not validate_input(password):
            show_message("Username dan password tidak boleh kosong.", "Register Failed")
            return

        try:
            auth.register(username, password)
            show_message("Akun berhasil dibuat!", "Register Success")
            register_window.destroy()
        except ValueError as e:
            show_message(str(e), "Register Failed")

    tk.Button(register_window, text="Register", command=handle_register).pack(pady=5)

def show_main_window():
    main_window = tk.Tk()
    main_window.title("To-Do List")
    main_window.configure(bg="lightblue")

    tk.Label(main_window, text="Tasks", bg="lightblue").pack(pady=10)

    task_listbox = tk.Listbox(main_window)
    task_listbox.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

    def refresh_task_list():
        task_listbox.delete(0, tk.END)
        tasks = crud.get_tasks(current_user_id)
        for task in tasks:
            task_listbox.insert(tk.END, f"  {task[2]}  ")

    def add_task():
        task = task_entry.get()
        if not validate_input(task):
            show_message("Task tidak boleh kosong.", "Error")
            return

        crud.add_task(current_user_id, task)
        task_entry.delete(0, tk.END)
        refresh_task_list()

    def update_task():
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            new_task = task_entry.get()
            if not validate_input(new_task):
                show_message("Task tidak boleh kosong.", "Error")
                return

            task_id = crud.get_tasks(current_user_id)[selected_task_index[0]][0]
            crud.update_task(task_id, new_task)
            task_entry.delete(0, tk.END)
            refresh_task_list()

    def delete_task():
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_id = crud.get_tasks(current_user_id)[selected_task_index[0]][0]
            crud.delete_task(task_id)
            refresh_task_list()

    task_entry = tk.Entry(main_window, bg="white")
    task_entry.pack(pady=5)

    tk.Button(main_window, text="Add Task", command=add_task).pack(pady=5)
    tk.Button(main_window, text="Update Task", command=update_task).pack(pady=5)
    tk.Button(main_window, text="Delete Task", command=delete_task).pack(pady=5)

    refresh_task_list()

    main_window.mainloop()

# if __name__ == "__main__":
#     from db import create_table
#     create_table()
#     show_login_window()
