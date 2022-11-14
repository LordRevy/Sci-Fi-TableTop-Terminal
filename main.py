from login_screen import Login
from users import User
from main_screen import Main

BACKGROUND = "dimgray"
ACCENT_COLOR = "black"
TEXT_COLOR = "white"
COLOR_THEME = (BACKGROUND, ACCENT_COLOR, TEXT_COLOR)
RESTRICTIONS = [
    "UNCLASSIFIED", "RESTRICTED", "CLASSIFIED", "SECRET", "FORBIDDEN"
]

#-----------------------------------------------------LOGGING IN
user_info = Login(COLOR_THEME)
user = User(user_info.user)


def run_program():
    Main(user, RESTRICTIONS, COLOR_THEME)


while True: #--------TO BE REPLACED WITH A QUIT BUTTON EVENTUALLY
    run_program()
