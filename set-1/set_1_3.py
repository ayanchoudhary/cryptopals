import binascii

def xor_decrypted_string(hex_string):
    bytes_string = bytearray.fromhex(hex_string)
    decrypted_strings = []
    for i in range(256):
        decrypted_xor_string = b''
        for byte in bytes_string:
            xor_char = bytes([byte ^ i])
            decrypted_xor_string += xor_char
        decrypted_strings.append({'string':decrypted_xor_string.decode('utf-8', errors='ignore').strip(), 'key':i})
    return decrypted_strings

def score_string(array,obj):
    score_map = {
        'e': 13,
        't': 12,
        'a': 11,
        'o': 10,
        'i': 9,
        'n': 8,
        's': 7,
        'h': 6,
        'r': 5,
        'd': 4,
        'l': 3,
        'u': 2,
    }
    string_bytes = obj['string'].encode('utf-8')
    score = 0
    for char in score_map:
        for byte in string_bytes:
            if ord(char) ^ byte == 0:
                score += score_map[char]
    array.append({"string":obj['string'], "key":obj['key'], "score":score})

def sort_func(e):
    return e['score']

def main(hex_string):
    decrypted_strings = xor_decrypted_string(hex_string)
    scored_strings = []
    for string in decrypted_strings:
        score_string(scored_strings, string)
    scored_strings.sort(reverse=True, key=sort_func)
    return scored_strings[0]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--hex', required=True)
    args = parser.parse_args()
    decrypted_strings = xor_decrypted_string(args.hex)
    scored_strings = []
    for string in decrypted_strings:
        score_string(scored_strings, string)
    scored_strings.sort(reverse=True, key=sort_func)
    print(scored_strings[0]['string'])
