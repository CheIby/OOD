from operator import le


print("*** Fun with countdown ***")
lst=[]
lst = [int(item) for item in input("Enter List : ").split()]
lst.sort()
print(len(lst))