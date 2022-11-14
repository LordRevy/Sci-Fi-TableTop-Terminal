import json
import tkinter as tk
import messages


class Admin:

    def __init__(self, user, COLOR_THEME):
        self.window = tk.Tk()
        self.window.title("ADMINISTRATUS RIGHTS GRANTED.")
        self.colors = COLOR_THEME
        self.window.config(padx=20, pady=20, bg=self.colors[0])
        self.user = user
        self.name = tk.Entry(width=20, highlightthickness=0)
        self.admin_window()

#-----------------------------------------------------UPDATE CLEARANCE

    def update_clearance(self, data, updated_user):
        with open("users.json", "w") as file:
            data.update(updated_user)
            json.dump(data, file, indent=4)
            print("\nProcess Complete.")

#-----------------------------------------------------INCREASE CLEARANCE

    def increase_clearance(self):
        name = self.name.get()
        with open("users.json", "r") as file:
            data = json.load(file)
        if name in data:
            updated_user = {
                name: {
                    "Title": data[name]["Title"],
                    "ID Number": data[name]["ID Number"],
                    "Clearance Level": data[name]["Clearance Level"] + 1,
                    "Is Admin": False,
                }
            }
            print(f"\nUser {name} found! Updating clearance...")

            self.update_clearance(data, updated_user)

        else:
            messages.invalid_entry()

#-----------------------------------------------------DECREASE CLEARANCE

    def decrease_clearance(self):
        name = self.name.get()
        with open("users.json", "r") as file:
            data = json.load(file)
            if name in data:
                updated_user = {
                    name: {
                        "Title": data[name]["Title"],
                        "ID Number": data[name]["ID Number"],
                        "Clearance Level": data[name]["Clearance Level"] - 1,
                        "Is Admin": False,
                    }
                }

                print(f"\nUser {name} found! Updating clearance...")

                self.update_clearance(data, updated_user)

            else:
                messages.invalid_entry()

#-----------------------------------------------------EXIT WINDOW

    def exit(self):
        self.window.destroy()

#-----------------------------------------------------ADMIN WINDOW

    def view_users(self):
        with open("users.json", "r") as file:
            data = json.load(file)

        for account in data:
            title = data[account]["Title"]
            print(title, account)


#-----------------------------------------------------ADMIN WINDOW

    def admin_window(self):
        #-BUTTONS
        increase_clearance_button = tk.Button(text="Increase Clearance",
                                              command=self.increase_clearance,
                                              highlightthickness=0,
                                              bg=self.colors[1],
                                              fg=self.colors[2])

        decrease_clearance_button = tk.Button(text="Decrease Clearance",
                                              command=self.decrease_clearance,
                                              highlightthickness=0,
                                              bg=self.colors[1],
                                              fg=self.colors[2])

        exit_button = tk.Button(text="Back To Main Screen",
                                command=self.exit,
                                highlightthickness=0,
                                bg=self.colors[1],
                                fg=self.colors[2])

        view_users_button = tk.Button(text="View all users",
                                      command=self.view_users,
                                      highlightthickness=0,
                                      bg=self.colors[1],
                                      fg=self.colors[2])

        increase_clearance_button.grid(row=0, column=0)
        decrease_clearance_button.grid(row=0, column=2)
        exit_button.grid(row=1, column=2)
        view_users_button.grid(row=1, column=0)

        #-ENTRIES
        self.name.grid(row=0, column=1)

        self.window.mainloop()
