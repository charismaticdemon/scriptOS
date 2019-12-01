import core
import pathlib

class TextEditor:
    def goToOs():
        core.Core.startPage()

    def write():
        while True:
            fileName = input('Enter file name here: ')
            data = input('Enter text here: ')
            my_file = open(fileName, "w")
            my_file.write(data)
            my_file.close()
            act = input('Exit?:(y or n or menu)')
            if act == 'y':
                TextEditor.goToOs()
            elif act == 'n':
                print('')
            elif act == 'menu':
                TextEditor.start()
            else:
                print('command not found')


    def read():
        while True:
            filename = input('Enter text name file >> ')
            file = open(filename, 'r')
            print(file.read())
            file.close()
            vibor2 = input('Exit?: y or n or menu')
            if vibor2 == 'y':
                TextEditor.goToOs()
            elif vibor2 == 'n':
                print('ok')
            elif act == 'menu':
                TextEditor.start()
            else:
                print('Error keymap')

    def start():
        print('Welcome to textEditor v0.2! \n')
        act = input('write or read >> ')
        if act == 'write':
            TextEditor.write()
        elif act == 'read':
            TextEditor.read()
        else:
            print('Command not found')


def access():
    print('access error')


if __name__ == '__main__':
    TextEditor.access()
