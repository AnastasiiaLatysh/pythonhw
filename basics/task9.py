def balanceOfBrackets(inputString):
    inputChangebleString = str(inputString)
    closetOpenBraket = str(inputChangebleString).find("]")

    if closetOpenBraket==0:
        return False

    if inputChangebleString=="":
        return True
    elif inputChangebleString[(closetOpenBraket-1)]=="[":
        inputChangebleString = inputChangebleString.replace('[]','',1)
        return balanceOfBrackets(inputChangebleString);
    else:
        return False

result = balanceOfBrackets(input("Enter string of brackets: \n"))

if result :
    print("OK, string is balanced")
else:
    print("NOT OK, string isn't balanced")
