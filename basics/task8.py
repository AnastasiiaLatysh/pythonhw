import random
def game():
    print("First of all, defining the range from which you will be guessing the number \n")
    firstNumber = int(input("Enter first number in range: \n"))
    secondNumber = int(input("Enter second number in range: \n"))
    numberToGues = random.randint(firstNumber, secondNumber)

    isNotGuess = True
    while isNotGuess:
        checkNumber = int(input("Enter number to check: \n"))
        if checkNumber==numberToGues:
            isNotGuess = False
        else:
            print("Try again!")

    print("Congratulation you guess the number!")

game()
