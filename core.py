import user_data
import os
import json

class Core:
    #ВХОД В СИСТЕМУ
    def singIn():
        act = input('SLM menu>> ')
        if act == 'register':
            os.system('cls')
            user_data.registration()
        elif act == 'singin':
            os.system('cls')
            user_data.singIn()
        elif act == 'help':
            print("""
            """)
            Core.singIn()
    #ГЛАВНАЯ СТРАНИЦА
    def startPage():
        while True:
            #ОТОБРАЖЕНИЕ ПОЛЬЗОВАТЕЛЯ В ОБОЛОЧКЕ
            with open('userdata', 'r') as file:
                global b
                b = json.load(file)
            act = input(b["login"] + '@scriptOS ~]# ')
            #ОСНОВНЫЕ КОМАНДЫ
            if act == 'help':
                print("""
                    all - show all applications
                    show - view catalog
                    clear - clear terminal
                    use - choose application for open file
                    whoami - view user
                    version - view system version""")
            else:
                print('unknown command')





if __name__ == "__main__":
    Core.singIn()
