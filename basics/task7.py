import numpy as np



def diaginal_reverse(arr):
    a = np.array(arr)
    for i in range (0, a.shape[0]):
        for j in range(i, a.shape[1]):
            if (i != j):
                temp = a[i,j]
                a[i, j] = a [j, i]
                a[j,i] = temp
    return a

