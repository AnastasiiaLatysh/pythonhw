# 2. Define a function `sum()` and a function `multiply()` that sums and multiplies (respectively) all
# the numbers in a list of numbers. For example, `sum([1, 2, 3, 4])` should return 10, and `multiply([1, 2, 3, 4])` should return 24.

def sum(list):
    result = 0
    for item in list:
        result += item
    return result

print(sum([1, 2, 3, 4]))

def multiply(list):
    result = 1
    for item in list:
        result*=item
    return result

print(multiply([1, 2, 3, 4]))
