from  itertools import combinations
import numpy as np

#input
fileName = input()
with open(fileName,"r") as f:
    line1 = f.readline().split(" ")
     
    sliceOfPizza = int(line1[0])
    TotalTypesOfPizza = int(line1[1].strip())
    
    typesOfPizza = list(f.readline().strip().split(" "))
    typesOfPizza = [int(i) for i in typesOfPizza]
    # print(sliceOfPizza,typesOfPizza,TotalTypesOfPizza)
    
   
        
#Declaration

Subsets,Sets,SumOfSets = [],[],[]
AnswerIndex = 0
Answer = []

#create a all subset in tuple using combinations function of itertools module
for i in range(1,TotalTypesOfPizza):
  Subsets.append(list(combinations(typesOfPizza,i)))


# create to list for sets and there sum
for j in Subsets:
    for i in j:
        Sets.append(list(i))
        SumOfSets.append(sum(list(i)))
        # print(Sets,SumOfSets)
       
d = dict(zip(SumOfSets,Sets))

for i in range(sliceOfPizza,0,-1):
    if(i in d):
        
        my = d[i]
        print(len(my))
        print(*my)
        break
#output
with open("answer"+str(len(my)) +".out","w") as f:
    f.write(str(len(my))+"\n")
    f.write(' '.join([str(i) for i in my]))




