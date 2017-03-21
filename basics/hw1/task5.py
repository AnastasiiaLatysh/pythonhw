# 5. Define a procedure `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:
#****
#*********
#******
#(usage time.sleep(s) possible for better visualization)

from time import sleep
import sys
def histogram(list):
    asterisk = '*'
    for item in list:
        i = 1
        while (i<=item):
            print(asterisk, end="")
            sys.stdout.flush()
            sleep(0.3)
            i+=1;
        print()


#histogram([4, 9, 7, 10])