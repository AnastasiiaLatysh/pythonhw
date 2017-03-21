import time
def histogram(list):
    print("```")
    asterik = '*'
    for number in list:
        print(asterik * number)
        time.sleep(1)
    print("```")

list = [4, 9, 7, 19]
histogram(list)