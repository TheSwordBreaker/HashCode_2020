import numpy as np


def SubsetSum(array, n, check):
    sol = []
    sum = 0
    for i in reversed(range(len(array))):
        if sum + array[i] < check:
            sum += array[i]
            sol.append(i)

    
    print(len(sol))
    print(*sol)
    return sol












def takeinput():
    fileName = input("Enter the File:")
    with open(fileName,"r") as f:
        line1 = f.readline().split(" ")
        sliceOfPizza = int(line1[0])
        TotalTypesOfPizza = int(line1[1].strip())

        typesOfPizza = list(f.readline().strip().split(" "))
        typesOfPizza = [int(i) for i in typesOfPizza]
    
    return typesOfPizza,TotalTypesOfPizza,sliceOfPizza

def saveinfile(result):
    with open("answer"+str(len(result)) +".out","w") as f:
        f.write(str(len(result))+"\n")
        f.write(' '.join([str(i) for i in result]))

array, n, check = takeinput()
result = SubsetSum(array, n, check)
saveinfile(result)