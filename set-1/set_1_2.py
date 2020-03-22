def xor_2_strings(string_1, string_2):
    int_a = int(string_1, 16)
    int_b = int(string_2, 16)
    result = int_a ^ int_b
    return result

if __name__ == "__main__":
    import argparse, codecs
    parser = argparse.ArgumentParser()
    parser.add_argument('--str_1', required=True)
    parser.add_argument('--str_2', required=True)
    args = parser.parse_args()
    xor = xor_2_strings(args.str_1, args.str_2)
    hex_xor = hex(xor)
    print('{:x}'.format(xor))
    