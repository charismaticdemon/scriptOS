class TextEditor:
    def write():
        data = input()
        file = open('nntd.txt', 'w')
        file.write(data)
        print('success!')

    def read():
        filename = input('Enter text name file >> ')
        file = open(filename, 'r')
        print(file.read())

    def start():
        print('Welcome to textEditor v0.1 alpha! \n')
        act = input('write or read >> ')
        if act == 'write':
            TextEditor.write()
        elif act == 'read':
            TextEditor.read()
        else:
            print('Command not found')

def access():
    print('access_error')

if __name__ == "__main__":
    start()
