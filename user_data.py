from core import Core
import os


def registration():
    act = input('scriptOS registration shell>>')
    if act == 'register':
        global name
        global password
        name = input('Enter new user login>>')
        password = input('Enter new user password>>')
        os.system('clear')
        Core.startPage()
    elif act == 'login':
        pass
    else:
        os.system('clear')
        registration()

def chekUserData():
    pass
