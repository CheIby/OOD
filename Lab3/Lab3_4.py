class Stack:
    def __init__(self):
        self.lst = []
    def push(self, value):
        self.lst.append(value)
    def pop(self):
        return self.lst.pop()
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        if len(self.lst) !=0:
            return False
        else :
            return True

S = Stack()
inp = input('Enter Input : ').split(',')
count=0
for i in inp:
    strSplit=i.split(" ")
    if strSplit[0] == "A":
        S.push(int(strSplit[1]))
    elif strSplit[0] == "B":
        if S.isEmpty():
                print("0")
        else:
            reLst = S.lst
            temp = 0
            for i in reversed(reLst):
                if i>temp:
                    temp=i
                    count+=1
            print(count)
            count=0


        