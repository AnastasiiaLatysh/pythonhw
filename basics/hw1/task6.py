#6. Define a function `caesar_cipher` that takes string and `key(number)`, whuch returns encrypted string

def ceaser_cipher(text, key):
    slip = ''
    key_abs = abs(key)
    if (key >= 0):
        for x in range(key_abs).__reversed__():
            slip += text[-x-1]
        return slip + text[:-key]
    elif (key < 0):
        for x in range(key_abs):
            slip += text[x]
        return  text[key_abs :] + slip

print(ceaser_cipher('abcdefghi', -3))
