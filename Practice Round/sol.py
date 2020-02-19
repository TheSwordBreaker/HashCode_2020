import sys
result = []
def isSum(index=0,setSum=0):
    global types,result,sliceOfPizza
    
    # print(set,n,sliceOfPizza,index,setSum,result)
    
    if(setSum == sliceOfPizza  ):
        a = str(len(result))+"\n"
        
        f = open("answer.out","w")
        f.write(a)
        f.write(' '.join([str(i) for i in result]))

        # print("it works")
        return True
    if(setSum > sliceOfPizza):
        result.pop()
        return False
    if(sliceOfPizza != setSum and index >= TotalTypesOfPizza):
        result.pop()
        return False
    result.append(index)
    types +=1
    print(types,result,index,setSum+typesOfPizza[index])
    return isSum(index+1,setSum+typesOfPizza[index])  or isSum(index+1,setSum)




#input
types = 0
sys.setrecursionlimit(2000001000)
fileName = input()
with open(fileName,"r") as f:
    line1 = f.readline().split(" ")
    sliceOfPizza = int(line1[0])
    TotalTypesOfPizza = int(line1[1].strip())
    
    
    typesOfPizza = list(f.readline().strip().split(" "))
    typesOfPizza = tuple(int(i) for i in typesOfPizza)

#output
for i in range(sliceOfPizza,1,-1):
    if(isSum(index=0,setSum=0)):
        break
