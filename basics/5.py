def histogram(list) :
    print('~')
    for number in list :
        h = ''
        for i in range(0, number) :
            h += '*'
        print(h)
    print('~')


import random

list = random.sample(range(10), 5)

histogram(list)