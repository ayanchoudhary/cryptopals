import math
from set_1_3 import main

def edit_distance(str_a, str_b):
    edit_distance = 0
    bytes_a = str_a.encode('utf-8')
    bytes_b = str_b.encode('utf-8')
    xor_bytes = [byte_a ^ byte_b for byte_a, byte_b in zip(bytes_a, bytes_b)]
    for byte in xor_bytes:
        binary = bin(byte)
        for bit in binary:
            if bit == '1':
                edit_distance += 1
    return edit_distance


def find_key_size(string):
    keysize = 40
    normal_keysize = 40
    for key in range(2,40):
        edit_distances = []
        string_blocks = [string[i:i+key] for i in range(0, len(string), key)]
        for index in range(len(string_blocks)-1):
            if index < len(string_blocks)-1 and index % 2 == 0:
                edit_distances.append(edit_distance(string_blocks[index],string_blocks[index+1])/key)
        normalized_keysize = sum(edit_distances)/len(edit_distances)
        if normalized_keysize < normal_keysize:
            keysize = key
            normal_keysize = normalized_keysize
    return keysize

def make_initial_cipher_blocks(string,keysize):
    number_of_blocks = math.ceil(len(string)/keysize)
    initial_blocks = []
    for size in range(number_of_blocks):
        initial_blocks.append(string[size*keysize:(size+1)*keysize])
    return initial_blocks

def transpose_cipher_blocks(initial_blocks,keysize):
    cipher_blocks = []
    for key in range(keysize):
        transpose_string = ''
        for string in initial_blocks:
            if len(string) < key+1:
                continue
            else:
                transpose_string += string[key]
        if len(transpose_string)%2 == 0:
            cipher_blocks.append(transpose_string)
        else:
            transpose_string = '0' + transpose_string
            cipher_blocks.append(transpose_string)
    return cipher_blocks


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--hex', required=True)
    args = parser.parse_args()

    keysize = find_key_size(args.hex)
    print(keysize)
    blocks = make_initial_cipher_blocks(args.hex,keysize)
    cipher_blocks = transpose_cipher_blocks(blocks,keysize)
    key = ''
    for block in cipher_blocks:
        key_byte = main(block)['key']
        key_char = chr(key_byte)
        key += key_char
    print(key)