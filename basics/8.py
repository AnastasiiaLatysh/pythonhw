import random

def game(A, B) :
    '''Try to guess a random number from the range [A, B]'''
    random_number = random.randint(A, B)
    print(random_number)

    userWon = False
    while not userWon :
        num = int(input('Guess the number :'))

        while not num :
            num = int(input('Guess the number :'))

        if random_number == num :
            print("Congratulations!")
            userWon = True
        else:
            print("Try again...")




first = int(input('Enter range : \nfrom = '))
last = int(input('to = '))

game(first, last)