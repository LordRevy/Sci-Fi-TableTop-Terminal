from tkinter import messagebox


def not_authorized():
    messagebox.showerror(
        title="NOT AUTHORIZED",
        message="User clearance level is too low for the requested operation.")


def not_admin():
    messagebox.showerror(
        title="NOT AUTHORIZED",
        message=
        "This action is reserved for Authorized Administratus only. Consult Administratus for details."
    )


def file_not_found():
    messagebox.showerror(
        title="Record File Not Found",
        message=
        "This Terminal has experienced data corruption resulting in loss of all files."
    )


def invalid_entry():
    messagebox.showerror(
        title="Invalid Entry",
        message="The information you have entered was not found.")


def invalid_value():
    messagebox.showerror(
        title="Invalid Value",
        message="The information you have entered was the incorrect value-type."
    )


def no_admin():
    messagebox.showerror(
        title="No Admin",
        message="No users can be created until the system has an Admin.")


def ask_if_admin():
    return messagebox.askyesno(
        title="No System Admin",
        message=
        "There are no users loaded on this Terminal and therefor has no Admin. Are you the Admin for this system?"
    )


def redact():
    return messagebox.askyesno(
        title="WARNING: REDACTING FILE",
        message=
        "This process will destroy the record and will make it no longer be accessible. Are you sure?"
    )

def user_created():
    messagebox.showinfo(
        title="New User Status",
        message="Successfully created user.")

def user_found(user, clearance):
  messagebox.showinfo(
        title="User found",
        message=f"loading user {user}.\nClearance Level: {clearance}.")

def show_record(title, message_body, author):
  messagebox.showinfo(
        title=title,
        message=f"      {message_body}\n\n-{author}")