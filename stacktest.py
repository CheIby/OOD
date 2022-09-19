class Stack:
    def __init__(self):
        self.lst=[]
    
    def push(self,n):
        self.lst.append(n)
    
    def pop(self):
        return self.lst.pop()
    
    def peek(self):
        return self.lst[-1]
    
    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return self.size()==0

S = Stack()
inp = int(input())
while inp>0:
    temp=inp%2
    S.push(temp)
    inp=inp//2
while not S.isEmpty():
    print(S.pop() ,end='')