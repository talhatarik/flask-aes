import base64
from Cryptodome.Cipher import AES
from datetime import date

#Key 16 digit olmalıdır.
def getKeyGenerator():
    key = str(date.today())+"12345"
    while len(key) < 16:
        key = key +"0"

    return key

def getDecode(encode):
    secret_key = getKeyGenerator().encode("utf-8")
    cipher = AES.new(secret_key,AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(encode))

    return decoded.decode("utf-8")


def getEncode(decode):
    msg_text = decode.rjust(32)
    secret_key = getKeyGenerator().encode("utf-8")
    cipher = AES.new(secret_key,AES.MODE_ECB) 
    encoded = base64.b64encode(cipher.encrypt(msg_text.encode("utf-8")))

    return encoded.decode("utf-8")

