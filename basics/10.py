def is_in_list(list, element):
    for i in list:
        if i == element:
            return True
    return False

def char_freq(characters):
    list = []
    for i in characters:
        if not is_in_list(list, i):
            list.append(i)

    freqs = []
    for i in range(len(list)):
        freqs.append(0)
    for curr_char in characters:
        for i in range(len(list)):
            if list[i] == curr_char:
                freqs[i] += 1
                break

    result = {}
    for i in range(len(list)):
       result[list[i]] = round(freqs[i] / len(characters), 3)

    print(result)










my_string = "abbabcbdbabdbdbabababcbcbab"

char_freq(my_string)