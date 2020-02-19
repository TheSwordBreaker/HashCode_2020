

# A recursive solution for subset sum 
# problem 
  
# Returns true if there is a subset  
# of set[] with sun equal to given sum 
def isSubsetSum(set, n, sum) : 
    
    # Base Cases 
    if (sum == 0) :
        print(set[n],n,sum) 
        return True
    if (n == 0 and sum != 0) : 
        return False
   
    # If last element is greater than 
    # sum, then ignore it 
    if (set[n - 1] > sum) :
        
        return isSubsetSum(set, n - 1, sum); 
    print(n,sum)  
    
    # else, check if sum can be obtained 
    # by any of the following 
    # (a) including the last element 
    # (b) excluding the last element    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 

    
      
      
# Driver program to test above function 


#input
fileName = input("Enter the File:")
with open(fileName,"r") as f:
    line1 = f.readline().split(" ")
     
    sliceOfPizza = int(line1[0])
    TotalTypesOfPizza = int(line1[1].strip())
    
    typesOfPizza = list(f.readline().strip().split(" "))
    typesOfPizza = [int(i) for i in typesOfPizza]

set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set)

answer = () 
result = [i for i in range(1,TotalTypesOfPizza+1)]
print(result)
for i in range(sliceOfPizza,1,-1):
    if ( isSubsetSum(typesOfPizza, TotalTypesOfPizza, i) == True) : 
        print("Found a subset with given sum")
        break
    
       
      
# This code is contributed by Nikita Tiwari. 


