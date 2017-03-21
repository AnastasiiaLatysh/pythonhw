def reverse(iStr):
    new_string = ''
    index = len(iStr)
    while index:
        index -= 1  # index = index - 1
        new_string += iStr[index]  # new_string = new_string + character
    return new_string

iStr = "I am testing"
print("Before reversing: ", iStr)
print("After reversing: ", reverse(iStr))