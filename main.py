import tkinter as tk
import sqlite3


def register():
    register_window = tk.Toplevel(root)
    register_window.title("Регистрация")

    lbl_username = tk.Label(register_window, text="Логин:")
    lbl_username.pack()
    entry_username = tk.Entry(register_window)
    entry_username.pack()

    lbl_password = tk.Label(register_window, text="Пароль:")
    lbl_password.pack()
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack()

    def add_user():
        username = entry_username.get()
        password = entry_password.get()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

        conn.close()
        register_window.destroy()

    btn_register = tk.Button(register_window, text="Зарегистрировать", command=add_user)
    btn_register.pack()


def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    if c.fetchone():
        lbl_result.config(text="Успешная авторизация")
    else:
        lbl_result.config(text="Неверный логин или пароль")

    conn.close()


root = tk.Tk()
root.title("Авторизация")

lbl_username = tk.Label(root, text="Логин:")
lbl_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

lbl_password = tk.Label(root, text="Пароль:")
lbl_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Войти", command=authenticate)
btn_login.pack()

btn_register = tk.Button(root, text="Регистрация", command=register)
btn_register.pack()

lbl_result = tk.Label(root, text="")
lbl_result.pack()

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT,
             password TEXT)''')
conn.commit()
conn.close()

root.mainloop()