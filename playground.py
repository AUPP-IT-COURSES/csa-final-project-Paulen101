import tkinter as tk
from tkinter import ttk, messagebox


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
# create login
class Login:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, username, password):
        if username not in self.users:
            user = User(username, password)
            self.users[username] = user
            return user
        else:
            raise ValueError("Username already exists.")

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            return user
        else:
            raise ValueError("Invalid username or password.")

    def logout(self):
        self.current_user = None

# login GUI
class LoginGUI:
    def __init__(self, login):
        self.login = login
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.root, text="Login", command=self.login_command)
        self.login_button.pack()
        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout_command)
        self.logout_button.pack()
        self.logout_button.pack_forget()

    def login_command(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            self.login.login(username, password)
            messagebox.showinfo("Success", "Login successful!")
            self.login_button.pack_forget()
            self.logout_button.pack()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def logout_command(self):
        self.login.logout()
        messagebox.showinfo("Success", "Logout successful!")
        self.logout_button.pack_forget()
        self.login_button.pack()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    login = Login()
    login_gui = LoginGUI(login)
    login_gui.start()