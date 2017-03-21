def key(number) :
    return int(number * 10 / 4 + 11 * max(number, 4))


def caesar_cipher(text, key) :
    result = ''
    for character in text :
        x = ord(character)
        result += chr((x + key) % 256)
    return result

text = "Hello, World!"
print(text, caesar_cipher(text, key(3)))