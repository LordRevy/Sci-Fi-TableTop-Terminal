import tkinter as tk
import messages
import json


class Login:

    def __init__(self, COLOR_THEME):
        self.window = tk.Tk()
        self.window.title("PRAISE BE TO THE OMNISIAH.")
        self.colors = COLOR_THEME
        self.window.config(padx=20, pady=20, bg=self.colors[0])
        self.title = tk.Entry(width=20, highlightthickness=0)
        self.name = tk.Entry(width=20, highlightthickness=0)
        self.id_number = tk.Entry(width=12, highlightthickness=0)
        self.login_successful = False
        self.login_window()

#----------------------------------------------------LOGGING IN

    def login_user(self):
        name = self.name.get()
        id_number = self.id_number.get()

        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messages.file_not_found()
        else:
            if name in data and id_number == data[name]["ID Number"]:
                title = data[name]["Title"]
                clearance = data[name]["Clearance Level"]
                is_admin = data[name]["Is Admin"]
                self.login_successful = True
            else:
                messages.invalid_entry()
        finally:
            if self.login_successful:
                self.user = (name, id_number, clearance, title, is_admin)
                messages.user_found(self.user[0], self.user[2])
                self.window.destroy()

#-----------------------------------------------------CREATING USER

    def create_user(self):
        user_ready = False
        title = self.title.get()
        name = self.name.get()
        id_number = self.id_number.get()

        if len(title) > 15:
            title = None

        new_user = {
            name: {
                "Title": title,
                "ID Number": id_number,
                "Clearance Level": 0,
                "Is Admin": False,
            }
        }
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            if messages.ask_if_admin():
                new_user[name]["Clearance Level"] = 10
                new_user[name]["Is Admin"] = True
                data = new_user
                data.update(new_user)
                user_ready = True
            else:
                messages.no_admin()
        else:
            data.update(new_user)
            user_ready = True
        finally:
            if user_ready:
                with open("users.json", "w") as file:
                    json.dump(data, file, indent=4)
                    messages.user_created()


#-----------------------------------------------------LOGIN WINDOW

    def login_window(self):
        #-BUTTONS
        login_button = tk.Button(text="Login",
                                 command=self.login_user,
                                 highlightthickness=0,
                                 bg=self.colors[1],
                                 fg=self.colors[2])

        create_user_button = tk.Button(text="Create",
                                       command=self.create_user,
                                       highlightthickness=0,
                                       bg=self.colors[1],
                                       fg=self.colors[2])

        login_button.grid(row=3, column=1)
        create_user_button.grid(row=4, column=1)

        #-LABELS
        title_label = tk.Label(text="Title (Optional): ", bg=self.colors[0])
        name_label = tk.Label(text="Cogomen Name:", bg=self.colors[0])
        id_number_label = tk.Label(text="ID Number: ", bg=self.colors[0])
        title_label.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        id_number_label.grid(row=2, column=0)

        #-ENTRIES
        self.title.grid(row=0, column=1)
        self.title.insert(0, "Only for creating account")
        self.name.grid(row=1, column=1)
        self.id_number.grid(row=2, column=1)

        self.window.mainloop()

        return self.user
