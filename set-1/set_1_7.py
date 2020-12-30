import base64
from Crypto.Cipher import AES

if __name__ == "__main__":
    base64_string = open('set_1_7.txt').read()
    aes_string = base64.b64decode(base64_string)

    key_string = 'YELLOW SUBMARINE'
    key_bytes = key_string.encode('utf-8')
    cipher_text = AES.new(key_bytes, AES.MODE_ECB)
    decrypted_bytes = cipher_text.decrypt(aes_string)
    decrypted_string = decrypted_bytes.decode('utf-8')
    print(decrypted_string)