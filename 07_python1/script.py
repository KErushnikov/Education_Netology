from sys import argv
import base64

script, method, text = argv

if method == "crypt":
    text = text.encode('ascii')
    print("Encrypting...")
    text = base64.b64encode(text)
    print(text.decode('ascii'))
elif method == "decrypt":
    text = text.encode('ascii')
    print("Decrypting...")
    text = base64.b64decode(text)
    print(text.decode('ascii'))
else:
    print("Wrong method input")