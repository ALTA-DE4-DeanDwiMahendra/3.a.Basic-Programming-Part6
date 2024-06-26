def caesar(offset, input_str):
    result = ""
    for char in input_str:
        if char == " ":
            result += char
        else:
            shifted = (ord(char) - ord('a') + offset) % 26 + ord('a')
            result += chr(shifted)
    return result

if __name__ == '__main__':
    print(caesar(3, "abc"))  # def
    print(caesar(2, "alta"))  # cnvc
    print(caesar(10, "alterraacademy"))  # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz"))  # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz"))  # mnopqrstuvwxyzabcdefghijkl
