result = {}
def char_freq(inputString):

    if len(inputString)!=0:
        firstChar = inputString[0]
        result[firstChar]= result.get(firstChar) + 1 if firstChar in result else 1
        char_freq(inputString.replace(firstChar, '', 1))
    return result

print(char_freq("abbabcbdbabdbdbabababcbcbab"))