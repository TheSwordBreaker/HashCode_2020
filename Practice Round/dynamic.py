import numpy as np


def SubsetSum(array, n, check):
    table = np.zeros((n,check+1),dtype=int)

    for i in range(check+1):
        if array[0] <= i:
            table[0][i] = array[0]

    for i in range(1,n):
        for j in range(check+1):
            if array[i] <= j :
                table[i][j] = max(array[i] + table[i-1][j - array[i]] , table[i-1][j])
            else:
                table[i][j] = table[i-1][j]


    #backtrack to get a output
    sol = []

    key = table[n-1][check]
    print(key)
    for i in reversed(range(n)):
        if array[i] <= key and array[i] + table[i-1][key - array[i]] > table[i-1][key]:
            key -= array[i]
            sol.append(i)
    
    if array[0] <= key:
        sol.append(0)
    key = table[n-1][check]

    print(sol,key)













def takeinput():
    fileName = input("Enter the File:")
    with open(fileName,"r") as f:
        line1 = f.readline().split(" ")
        sliceOfPizza = int(line1[0])
        TotalTypesOfPizza = int(line1[1].strip())

        typesOfPizza = list(f.readline().strip().split(" "))
        typesOfPizza = [int(i) for i in typesOfPizza]
    
    return typesOfPizza,TotalTypesOfPizza,sliceOfPizza

array, n, check = takeinput()
SubsetSum(array, n, check)