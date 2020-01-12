import user_data
import textEditor
import os
import json

#УСТАНОВЛЕННЫЕ ПРИЛОЖЕНИЯ
apps=['Text Editor']
#ВЕРСИЯ ОС
version = '0.2.1'
class Core:
    #ВХОД В СИСТЕМУ
    def signIn():
        os.system('clear')
        act = input('SLM menu>> ')
        if act == 'register':
            os.system('clear')
            user_data.registration()
        elif act == 'signin':
            os.system('clear')
            user_data.signIn()
        elif act == 'help':
            print("""
            """)
            Core.signIn()
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
                    version - view system version
                    exit - end the session""")

            elif act == 'all':
                for i in apps:
                    print('\n'.join(apps))

            elif act == 'show':
                os.system('ls')

            elif act == 'clear':
                os.system('clear')

            elif act == 'whoami':
                print(b["login"])

            elif act == 'version':   # TODO: СДЕЛАТЬ ОБНОВЛЕНИЕ СИСТЕМЫ?
                print(version)

            elif act == 'exit':
                Core.signIn()

            else:
                print('unknown command')





if __name__ == "__main__":
    Core.signIn()
