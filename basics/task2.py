def sum(mas):
    result = 0
    for element in mas:
        result+=element
    return result

def multiply(mas):
    result = 1
    for element in mas:
        result *= element
    return result

mas = [1,2,3,4,5]
print("Our massive: ", mas)
print("After summing: ", sum(mas))
print("After multiply: ", multiply(mas))
