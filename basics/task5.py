import time
def histogram(arr):
    for integerVal in arr:
        print('*'*integerVal)
        time.sleep(1)

arr = [4, 9, 7, 11, 1, 5, 12, 3, 5];
print("Our array", arr)
histogram(arr)
