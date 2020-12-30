import base64
from Crypto.Cipher import AES
from set_2_9 import pad_string

def manage_cipher_blocks(key_string, ciphertext):
    keysize = len(key_string)
    cipher_blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
    return cipher_blocks

def generate_plaintext(cipher_block, previous_block, key_bytes):
    cipher_text = AES.new(key_bytes, AES.MODE_ECB)
    padded_block = pad_string(cipher_block, len(key_bytes), '\x22')
    intermediate_bytes = cipher_text.decrypt(padded_block)
    previous_bytes = previous_block.encode('utf-8')
    plain_bytes = bytes([byte_a ^ byte_b for byte_a, byte_b in zip(previous_bytes, intermediate_bytes)])
    plaintext = plain_bytes.decode('utf-8', errors='ignore')
    return(plaintext)

def decrypt_cipher(cipher, iv, key):
    cipher_blocks = manage_cipher_blocks(key, cipher)
    key_bytes = key.encode('utf-8')
    plaintext = ''
    for index, block in enumerate(cipher_blocks):
        if index == 0:
            plain_block = generate_plaintext(block,iv,key_bytes)
        else:
            plain_block = generate_plaintext(block,cipher_blocks[index-1],key_bytes)
        plaintext += plain_block
    return(plaintext)
    

if __name__ == "__main__":
    base64_string = open('set_2_10.txt').read()
    ciphertext = base64.b64decode(base64_string).decode('utf-8', errors='ignore')
    key_string = "YELLOW SUBMARINE"
    iv = ''
    for byte in key_string:
        iv += '\x00'
    plaintext = decrypt_cipher(ciphertext, iv, key_string)
    # print(plaintext)
