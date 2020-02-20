
def takeinput():
    fileName = input()
    with open(fileName,"r") as f:
        totalSildes = int(f.readline())
        sildes = list()
        for i in range(totalSildes):
            temp = f.readline().split(" ")
            sildes.append([temp[0],int(temp[1])])
        
        return sildes,fileName



    #     sliceOfPizza = int(line1[0])
    #     TotalTypesOfPizza = int(line1[1].strip())

    #     typesOfPizza = list(f.readline().strip().split(" "))
    #     typesOfPizza = [int(i) for i in typesOfPizza]
    
    # return typesOfPizza,TotalTypesOfPizza,sliceOfPizza

def saveinfile(sildeShow,filename):
    with open(filename+".out","w") as f:
        print(str(len(sildeShow))+"\n")
        for i in sildeShow:
            if type(i) is list:
                print(*i)
                # print(str(i))
            else:
                print(str(i))
                # print(*i)
                # print(' '.join([str(j) for j in i]))
            # print(i)

       
    
        f.write(str(len(sildeShow))+"\n")
        for i in sildeShow:
            if type(i) is list:
                # print("list")
                f.write(' '.join([str(j) for j in i]))
                f.write("\n")
            else:
                
                f.write(str(i)+"\n")
                 

def makeSildeShow(sildes):
    # print(sildes)
    sildeShow = list()
    temp = list()
    tempCount = 0 
    for i in range(len(sildes)):
        if sildes[i][0] == "H":
            sildeShow.append(i)
        elif sildes[i][0] == "V":
            temp.append(i)
            tempCount+=1
        
        if tempCount == 2:
            sildeShow.append(temp)
            temp = list()
            tempCount = 0

    return sildeShow
    


if __name__ == "__main__":
    sildes,fileName = takeinput()
    sildeShow = makeSildeShow(sildes)
    fileName = fileName[:-4]
    saveinfile(sildeShow,fileName)
