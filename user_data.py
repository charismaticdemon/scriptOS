from core import Core
import os
import json
import time

#РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ
def registration():
    global login
    global password
    login = input('Enter new user login>> ')
    password = input('Enter new user password>> ')

    #СЛОВАРЬ С ДАННЫМИ ПОЛЬЗОВАТЕЛЯ
    userData = {
        'login' : login,
        'password' : password

    }
    #ЗАПИСЬ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ В JSON ФАЙЛ
    try:

        with open('userdata', 'w') as file:
            json.dump(userData, file)
        os.system('cls')
        Core.startPage()
    except FileExistsError:
        print('file exists')

        registration()
    #ВХОД В СУЩЕСТВУЮЩИЙ АККАУНТ
def singIn():
    while True:
        try:
            with open ('userdata', 'r') as file:
                b = json.load(file)
            singLogin = input('Login>> ')
            singPassword = input('Password>> ')
            #ПРОЦЕСС ВХОДА
            if singLogin == b["login"]:
                if singPassword == b["password"]:
                    os.system('cls')
                    Core.startPage()
                else:
                    print('incorrect')
            else:
                print('incorrect')
        except FileNotFoundError:
            print('data not found')
            time.sleep(1.0)
            os.system('cls')
            Core.singIn()
