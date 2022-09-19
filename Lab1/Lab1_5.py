print("*** Fun with countdown ***")
lst=[]
lst = [int(item) for item in input("Enter List : ").split()]
lstSort=[]
finalLst=[]
i=0
count=0
temp= lst[0]
while i!=len(lst):
    if temp==lst[i]:
        lstSort.append(temp)
        temp-=1
    else :
        temp = lst[i]
        lstSort=[]
        lstSort.append(temp)
        temp-=1
    if temp == 0 :
        finalLst.append(lstSort)
        lstSort=[]
        count+=1
    i+=1
    

resultLst=[]
resultLst.append(count)
resultLst.append(finalLst)
print(resultLst)