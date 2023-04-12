from Cryptodome.Cipher import AES
from Cryptodome import Random
import hashlib

plain_text = 'There is no sadder story in the world than the tale of message 404' #Нет повести печальней в этом мире, чем сообщение - 404
key = hashlib.sha256(b'403').digest()

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]
plain_text = pad(plain_text)

iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(plain_text.encode()))
#cipher = AES.new(key, AES.MODE_CBC)
#cipher_text = (cipher.encrypt(plain_text.encode()))
print(f"Ciphered text: {cipher_text}, Key: {key}")

for i in range(100,1000):
    i = str(i)
    i=i.encode('utf-8')
    key = hashlib.sha256(i).digest()
    iv = cipher_text[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
    if plain_text != b'':
        print(f"Plain text: {plain_text}, Key: {i}")
    else:
        continue