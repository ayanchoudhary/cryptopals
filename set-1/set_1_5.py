import binascii

def xor_multiple_key(string, key):
    string_bytes = string.encode('utf-8')
    key_bytes = key.encode('utf-8')
    indice = len(key_bytes)
    xor_bytes = b''
    for index, string_byte in enumerate(string_bytes):
        locator = index % indice
        key = key_bytes[locator]
        xor_char = bytes([string_byte ^ key])
        xor_bytes += xor_char
    hex_bytes = binascii.b2a_hex(xor_bytes)
    hex_string = hex_bytes.decode('utf-8')
    return hex_string


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', required=True)
    parser.add_argument('--key', required=True)
    args = parser.parse_args()
    xor_string = xor_multiple_key(args.str, args.key)
    print(xor_string)