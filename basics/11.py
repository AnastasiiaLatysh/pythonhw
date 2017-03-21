def dec_to_bin(number):
    result = ''
    while number != 0:
        result += str((number % 2))
        number = int(number / 2)
    return result


print(dec_to_bin(4))