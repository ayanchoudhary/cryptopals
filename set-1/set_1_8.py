import binascii

if __name__ == "__main__":
    hex_strings = open('set_1_8.txt').read().splitlines()
    block_size = 16
    cipher = {'string':'', 'repetitions':0}
    for hex in hex_strings:
        cipher_text = binascii.unhexlify(hex)
        string_blocks = [cipher_text[i:i+block_size] for i in range(0, len(cipher_text), block_size)]
        repetitions = len(string_blocks) - len(set(string_blocks))
        if repetitions > cipher['repetitions']:
            cipher = {'string':hex, 'repetitions':repetitions}
    print(cipher)