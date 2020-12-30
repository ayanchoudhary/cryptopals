from set_1_3 import main, score_string, sort_func

if __name__ == "__main__":
    hex_strings = open('set_1_4.txt').read().splitlines()
    scored_strings = []
    for hex_string in hex_strings:
        string = main(hex_string)
        score_string(scored_strings, string)
    scored_strings.sort(reverse=True, key=sort_func)
    print(scored_strings[0]['string'])
