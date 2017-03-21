def is_in_list(list, element):
    for i in list:
        if i == element:
            return True
    return False


my_string = "abbabcbdbabdbdbabababcbcbab"

list = ['a', 'b', 'c']
print(is_in_list(list, 'v'))