from  itertools import combinations
import numpy as np

#input
fileName = input("Enter the File:")
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
       
# FInding the best value
# for i in range(len(SumOfSets)):
#     if(SumOfSets[i] >= AnswerIndex):
#         if(SumOfSets[i] <= sliceOfPizza):
#             AnswerIndex = i
#             if(AnswerIndex == sliceOfPizza):
#                 break
#             print("-----")
#             print(SumOfSets[i] )
#             print("-----")
#             print(*Sets[i])
#             print("####")


# SumOfSets = np.array(SumOfSets)
# for i in range(sliceOfPizza,0,-1):
#     AnswerIndex += np.where(SumOfSets == i)
# # AnswerIndex = np.where(SumOfSets == sliceOfPizza)

#  FInding the best value
d = dict(zip(SumOfSets,Sets))

for i in range(sliceOfPizza,0,-1):
    if(i in d):
        print(i)
        print(d[i])
        break





# for i in range(len(SumOfSets)):
#     if(SumOfSets[i] == sliceOfPizza):
#         AnswerIndex = i
#         break
#     elif(SumOfSets[i] <= sliceOfPizza):
#         # AnswerIndex = i
#         # break
#         pass

# s = SumOfSets.sort(reverse=True)


# print(d)
# # result = filter(lambda x: x % 2 == 0, seq) 
# print(SumOfSets)

# for i in range(len(SumOfSets)):
#     if(SumOfSets[i] == sliceOfPizza):
#         AnswerIndex = i
#         break
#     elif(SumOfSets[i] <= sliceOfPizza):
#         # AnswerIndex = i
#         # break
#         pass


#         print("-----")
#         print(SumOfSets[i] )
#         print("-----")
#         print(*Sets[i])
#         print("####")


# output
# print(AnswerIndex)
# print(SumOfSets[AnswerIndex])
# print(*Sets[AnswerIndex])

# print(AnswerIndex[0][0])

# print(SumOfSets[AnswerIndex[0][0]])
# print(*Sets[AnswerIndex[0][0]])