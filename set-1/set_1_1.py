from binascii import unhexlify, b2a_base64
import argparse

def convert_to_base64(hex_string):
    bytes_array = unhexlify(hex_string)
    base64_string = b2a_base64(bytes_array)
    return base64_string

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hex', required=True)
    args = parser.parse_args()
    base64 = convert_to_base64(hex_string=args.hex).decode('utf-8')
    print(base64)