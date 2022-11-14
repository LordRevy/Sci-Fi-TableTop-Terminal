import tkinter as tk
from admin import Admin
import messages
from record_manager import Record_Manager


class Main:

    def __init__(self, user, RESTRICTIONS, COLOR_THEME):
        self.window = tk.Tk()
        self.window.title("Terminal #1078")
        self.colors = COLOR_THEME
        self.window.config(padx=20, pady=20, bg=self.colors[0])
        self.user = user
        self.records = Record_Manager(self.user, RESTRICTIONS)
        self.main_window()

#-----------------------------------------------------RUN ADMIN

    def run_admin(self):
        if self.user.is_admin:
            self.window.destroy()
            Admin(self.user, self.colors)
        else:
            messages.not_admin()


#-----------------------------------------------------MAIN WINDOW

    def main_window(self):
        #-PHOTOS
        mechanicus_image = tk.PhotoImage(file="Images/mechanicus.png")
        mechanicus_image = mechanicus_image.subsample(7, 7)
        aquilla_image = tk.PhotoImage(file="Images/aquilla.png")
        aquilla_image = aquilla_image.subsample(8, 8)
      
        #-CANVAS
        top_canvas = tk.Canvas(width=350,
                               height=75,
                               bg=self.colors[0],
                               highlightthickness=0)
        top_canvas.create_text(180, 37, text="Example Text")
        top_canvas.grid(row=0, column=0, columnspan=3)

        bottom_canvas = tk.Canvas(width=350,
                                  height=75,
                                  bg=self.colors[0],
                                  highlightthickness=0)
        bottom_canvas.create_image(315, 37, image=mechanicus_image)
        bottom_canvas.create_image(60, 37, image=aquilla_image)
        bottom_canvas.grid(row=2, column=0, columnspan=3)

        #-BUTTONS
        view_records_button = tk.Button(text="View Records",
                                        command=self.records.view,
                                        highlightthickness=0,
                                        bg=self.colors[1],
                                        fg=self.colors[2])

        create_record_button = tk.Button(text="Create Record",
                                         command=self.records.create,
                                         highlightthickness=0,
                                         bg=self.colors[1],
                                         fg=self.colors[2])

        record_list_button = tk.Button(text="Record List",
                                       command=self.records.list,
                                       highlightthickness=0,
                                       bg=self.colors[1],
                                       fg=self.colors[2])

        redact_record_button = tk.Button(text="Redact Record",
                                         command=self.records.redact,
                                         highlightthickness=0,
                                         bg=self.colors[1],
                                         fg=self.colors[2])

        admin_button = tk.Button(text="Administratus",
                                 command=self.run_admin,
                                 highlightthickness=0,
                                 bg=self.colors[1],
                                 fg=self.colors[2])

        admin_button.grid(row=0, column=2)
        view_records_button.grid(row=1, column=0)
        create_record_button.grid(row=1, column=1)
        record_list_button.grid(row=1, column=2)
        redact_record_button.grid(row=2, column=1)

        self.window.mainloop()
