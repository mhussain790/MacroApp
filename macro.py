import pyautogui
import keyboard
import sys


def read_user_info():
    # Open the file in read mode
    with open('user_info.txt', 'r') as f:
        # Read the lines of the file into a list
        lines = f.readlines()

    # Check if the list has at least two elements (i.e. two lines of text)
    if len(lines) >= 2:
        # Store the first and second lines in variables
        username = lines[0].strip()
        password = lines[1]

        return username, password
    else:
        print('The file does not have at least two lines of text.')


def login():

    # Get username and password from text file
    user_info = read_user_info()
    username = user_info[0]
    password = user_info[1]

    # Move mouse to username field and click in field
    # pyautogui.moveTo(x=username_field_x, y=username_field_y)
    # pyautogui.click()

    pyautogui.typewrite(username)

    # Press TAB key to move to PASSWORD field
    pyautogui.press('tab')

    # Type password
    pyautogui.typewrite(password)

    # Press enter to submit
    pyautogui.press('enter')


def bind_f1():
    # Bind the F1 key to the login method using pyautogui
    keyboard.add_hotkey('`', login)


def end_program():
    # Unhook all hotkeys
    keyboard.unhook_all()

    # End the program
    sys.exit()

# # Bind the end_program function to the Command + Esc keys
# keyboard.add_hotkey('shift', end_program)


# Run MacroApp
keyboard.add_hotkey('`', login)
while True:
    pass
