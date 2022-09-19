class Stack:
    def __init__(self):
        self.lst=[]

    def push(self,i):
        self.lst.append(i)
    def pop(self):         
        self.lst.pop()
    def isEmpty(self):  
        if len(self.lst) == 0:
            return True
        else:
            return False
    def size(self) : 
        return len(self.lst)

def ManageStack(x):
    lst=Stack()
    for i in x:
        strSplit=i.split(" ")
        if strSplit[0] == "A":
            if strSplit[1] not in lst.lst:
                lst.push(int(strSplit[1]))
            print(f"Add = {strSplit[1]}")
        elif strSplit[0] == "P":
            if lst.size() !=0 :
                print(f"Pop = {lst.lst.pop()}")
            else:
                print("-1")
        elif strSplit[0] == "D":
            temp=[]
            if lst.size() !=0:
                for j in lst.lst:
                    if j != int(strSplit[1]):
                        temp.append(j)
                    else:
                        print(f"Delete = {j}")
            else:
                print("-1")
            lst.lst=temp
        elif strSplit[0] == "LD":
            temp=[]
            if lst.size() != 0:
                for j in reversed(lst.lst):
                    if j >= int(strSplit[1]):
                        temp.append(j)
                    else:
                        print(f'Delete = {j} Because {j} is less than {int(strSplit[1])}')
            else:
                print("-1")
            lst.lst=temp
            lst.lst.reverse()
        elif strSplit[0] == "MD":
            temp=[]
            if lst.size() != 0:
                for j in reversed(lst.lst):
                    if j <= int(strSplit[1]):
                        temp.append(j)
                    else:
                        print(f'Delete = {j} Because {j} is more than {int(strSplit[1])}')
            else:
                print("-1")
            lst.lst=temp
            lst.lst.reverse()
    return lst.lst

x=input("Enter Input : ").split(",")

print("Value in Stack = " + str(ManageStack(x)))

