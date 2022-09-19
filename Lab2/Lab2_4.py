from operator import le


def sum(inputLst):
    lst=inputLst
    lst = [int(i) for i in lst]
    lst.sort()
    resultList =[]
    if len(lst) <= 2:
        return "Array Input Length Must More Than 2"
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                if lst[i] + lst[j] + lst[k] == 5 and [lst[i],lst[j],lst[k]] not in resultList:
                    resultList.append([lst[i],lst[j],lst[k]])
    return resultList

lst = input("Enter Your List : ").split(" ")
print(sum(lst))
