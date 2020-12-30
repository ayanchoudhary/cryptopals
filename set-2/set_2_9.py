def pad_string(string, pad, value):
    bytes_string = string.encode('utf-8')
    padding = 0
    if pad > len(bytes_string):
        padding = pad - len(bytes_string)
    for byte in range(padding):
        pad = value.encode('utf-8')
        bytes_string += pad
    return(bytes_string.decode('utf-8'))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', required=True)
    parser.add_argument('--len', required=True)
    args = parser.parse_args()

    bytes_string = args.str.encode('utf-8')
    padding = 0
    if int(args.len) > len(bytes_string):
        padding = int(args.len) - len(bytes_string)
    for byte in range(padding):
        pad = '\x04'.encode('utf-8')
        bytes_string += pad
    print(bytes_string)