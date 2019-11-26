#modules
import json
import requests
import os
import sys

#my modules
import textEditor
#variables


class Os:
    def textEditor():
        textEditor.TextEditor.start()

    def jsonEditor():
        pass

    def startPage():
        print('Weclome! ')
        print("Script OS v0.1 alpha")
        print("""
        1)textEditor
        2)jsonEditor""")
        act = input('>>')
        if act == 'textEditor':
            Os.textEditor()
        elif act == 'jsonEditor':
            Os.jsonEditor()


    def parser():
        pass

    def installCustomApp():
        pass

def check_data():
    ifelse = input("Это правильно? y or n")
    if ifelse == 'y':
        Os.startPage()
    elif ifelse == 'n':
        registration()
    else:
        print('command not defined')


def registration():
    print('Weclome to script OS!')
    user_name = str(input('Input your name: '))
    user_pass = str(input('Input your password: '))
    check_data()






if __name__ == "__main__":
    registration()
