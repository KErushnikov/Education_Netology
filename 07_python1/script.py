from sys import argv
import base64

def code():
    if int(len(argv)) == 3:
        if argv[1] == "crypt":
            text = argv[2].encode('ascii')
            print("Encrypting...")
            text = base64.b64encode(text)
            print(text.decode('ascii'))
        elif argv[1] == "decrypt":
            text = argv[2].encode('ascii')
            print("Decrypting...")
            text = base64.b64decode(text)
            print(text.decode('ascii'))
        else:
            print("Incorrect method")
            argv[1] = str(input("Type crypt or decrypt: "))
            if argv[1] == "crypt":
                text = argv[2].encode('ascii')
                print("Encrypting...")
                text = base64.b64encode(text)
                print(text.decode('ascii'))
            elif argv[1] == "decrypt":
                text = argv[2].encode('ascii')
                print("Decrypting...")
                text = base64.b64decode(text)
                print(text.decode('ascii'))

    else:
        print("Wrong arguments")
        argv[1] = str(input("Type crypt or decrypt: "))
        argv[2] = str(input("Type message: "))
        if argv[1] == "crypt":
                text = argv[2].encode('ascii')
                print("Encrypting...")
                text = base64.b64encode(text)
                print(text.decode('ascii'))
        elif argv[1] == "decrypt":
            text = argv[2].encode('ascii')
            print("Decrypting...")
            text = base64.b64decode(text)
            print(text.decode('ascii'))

code()

while True:
    try:
        flag = input('Ones again? [Y/N]: ')
        if flag == "Y":
            argv[1] = str(input("Type crypt or decrypt: "))
            argv[2] = str(input("Type message: "))
            code()
        elif flag !="N":
            print('Stupid? Type Y or N!')
        else:
            print("As u wish" "\n"
                  "Quiting..." "\n")
            break
    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        print("Press N in another iteration")