def caesar_cipher (text , number):
    if number<0:
        number = number%26 + 26
    word = ''
    for i in text:
        if 'A' <= i <= 'Z':
            i = chr((ord(i)-ord('A')+number)%26 + ord('A'));
        if 'a' <= i <= 'z':
            i = chr((ord(i)-ord('a')+number)%26 + ord('a'));
        word += i
    return word