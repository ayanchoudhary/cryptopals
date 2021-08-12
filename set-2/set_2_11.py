from Crypto.Cipher import AES
import argparse, os, math
from random import randint
from set_2_9 import pad_string

def encryption_oracle(string):
    mode = randint(0,1)
    key_bytes = os.urandom(16)
    append = randint(5,10)
    rand_bytes = os.urandom(append).decode('utf-8', errors='ignore')
    encrypting_string = rand_bytes+string+rand_bytes
    padded_string = pad_string(encrypting_string, math.ceil(len(encrypting_string)/len(key_bytes))*16, '\x12')
    if mode == 0:
        mode = 'ECB'
        cipher = AES.new(key_bytes, AES.MODE_ECB)
    else:
        mode = 'CBC'
        iv = os.urandom(16)
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    aes_string = cipher.encrypt(padded_string)
    return {'mode': mode, 'cipher': aes_string.decode('utf-8', errors='ignore')}


def detect_aes(string, block_size):
    cipher = {'string':'', 'repetitions':0}
    string_blocks = [string[i:i+block_size] for i in range(0, len(string), block_size)]
    repetitions = len(string_blocks) - len(set(string_blocks))
    cipher = {'string':string, 'repetitions':repetitions}
    return cipher

def detection_oracle(string):
    for size in range(1,len(string)):
        print(detect_aes(string,size))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', required=True)
    args = parser.parse_args()
    cipher = encryption_oracle(args.str)
    detection_oracle(cipher['cipher'])
    print(cipher)
