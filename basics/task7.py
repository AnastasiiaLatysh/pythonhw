def diaginal_reverse(arrOfArr):
    new_arrOfArr= []
    lengs = len(arrOfArr)

    step = 0
    for a in range(lengs):
        new_subArray = []
        for outerArray in arrOfArr:
            new_subArray.append(outerArray[step])
        new_arrOfArr.append(new_subArray)
        step+=1
    return new_arrOfArr

arrOfArr = [[1,2,3],[4,5,6],[6,7,8]]

print("Before reverse: ", arrOfArr )
print("After reverse: ", diaginal_reverse(arrOfArr))