from tkinter import *
import tkinter.messagebox as MessageBox
import os

def validate_registration():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if username == "":
        MessageBox.showinfo("Ошибка", "Введите логин")
    elif password == "":
        MessageBox.showinfo("Ошибка", "Введите пароль")
    elif confirm_password == "":
        MessageBox.showinfo("Ошибка", "Введите подтверждение пароля")
    elif password != confirm_password:
        MessageBox.showinfo("Ошибка", "Пароль и подтверждение пароля не совпадают")
    else:
        save_registration(username, password)

def save_registration(username, password):
    file = open("data.txt", "a")
    file.write(username + "," + password + '\n')
    file.close()

    MessageBox.showinfo("Успех", "Регистрация завершена успешно")


def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "":
        MessageBox.showinfo("Ошибка", "Введите логин")
    elif password == "":
        MessageBox.showinfo("Ошибка", "Введите пароль")
    else:
        check_login(username, password)


def check_login(username, password):
    if not os.path.exists("data.txt"):
        MessageBox.showinfo("Ошибка", "Неверный логин или пароль")
        return

    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    found = False
    for line in lines:
        user, passw = line.strip().split(",")
        if user == username and passw == password:
            found = True
            break

    if found:
        MessageBox.showinfo("Успех", "Вход выполнен успешно")
    else:
        MessageBox.showinfo("Ошибка", "Данные для входа неверны")


def register():
    global entry_username, entry_password, entry_confirm_password

    registration_window = Toplevel(root)
    registration_window.title("Регистрация")


    label_username = Label(registration_window, text="Логин:", font=("Arial", 12))
    label_username.pack()
    entry_username = Entry(registration_window, font=("Arial", 12))
    entry_username.pack()

    label_password = Label(registration_window, text="Пароль:", font=("Arial", 12))
    label_password.pack()
    entry_password = Entry(registration_window, show="*", font=("Arial", 12))
    entry_password.pack()

    label_confirm_password = Label(registration_window, text="Подтверждение пароля:", font=("Arial", 12))
    label_confirm_password.pack()
    entry_confirm_password = Entry(registration_window, show="*", font=("Arial", 12))
    entry_confirm_password.pack()

    button_register = Button(registration_window, text="Зарегистрироваться", command=validate_registration)
    button_register.pack()


def show_password():
    if checkbutton_show_password.get():
        entry_password.config(show="")
        entry_confirm_password.config(show="")
    else:
        entry_password.config(show="*")
        entry_confirm_password.config(show="*")


root = Tk()
root.title("Вход")


label_username = Label(root, text="Логин:", font=("Arial", 12))
label_username.pack()
entry_username = Entry(root, font=("Arial", 12))
entry_username.pack()

label_password = Label(root, text="Пароль:", font=("Arial", 12))
label_password.pack()
entry_password = Entry(root, show="*", font=("Arial", 12))
entry_password.pack()

label_show_password = Label(root, text="Показать пароль:")
label_show_password.pack()
checkbutton_show_password = BooleanVar()
checkbutton = Checkbutton(root, variable=checkbutton_show_password, command=show_password)
checkbutton.pack()

button_login = Button(root, text="Войти", command=validate_login)
button_login.pack()

button_register = Button(root, text="Регистрация", command=register)
button_register.pack()

root.mainloop()