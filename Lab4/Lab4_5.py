class Queue:
    def __init__(self):
        self.lst=[]
    def enQueue(self,num):
        self.lst.append(num)
    def deQueue(self):
        return self.lst.pop(0)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        if len(self.lst)!=0:
            return False
        else:
            return True

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,i):
        self.items.append(i)
    def pop(self):         
        return self.items.pop()
    def isEmpty(self):  
        if len(self.items) == 0:
            return True
        else:
            return False
    def size(self) : 
        return len(self.items)

nor,mir = input("Enter Input (Normal, Mirror) : ").split(" ")
stackMir=Stack()
queueMir=Queue()
stackNor=Stack()
temp=mir[0]

for i in reversed(mir):
    stackMir.push(i)
    if stackMir.size()>2:
        if stackMir.items[-1] == stackMir.items[-2] and stackMir.items[-1] == stackMir.items[-3]:
            queueMir.enQueue(i)
            for j in range(3):
                stackMir.pop()
countMir=queueMir.size()
count=0
fail=0
for i in nor:
    stackNor.push(i)
    if stackNor.size()>2:
        if stackNor.items[-1] == stackNor.items[-2] and stackNor.items[-1] == stackNor.items[-3]:
            if not queueMir.isEmpty():
                temp=stackNor.pop()
                stackNor.push(queueMir.deQueue())
                stackNor.push(temp)
                if stackNor.items[-1] == stackNor.items[-2] and stackNor.items[-1] == stackNor.items[-3]:
                    fail+=1
                    for j in range(3):
                        stackNor.pop()
            else:
                count+=1
                for j in range(3):
                    stackNor.pop()          
print('NORMAL :')
print(stackNor.size())
if stackNor.size()!=0:
    print(''.join(reversed(stackNor.items)))
else:
    print("Empty")
print(f"{count} Explosive(s) ! ! ! (NORMAL)")
if fail!=0:
    print(f"Failed Interrupted {fail} Bomb(s)")
else:
    pass
print("------------MIRROR------------")
print(': RORRIM')
print(stackMir.size())
if stackMir.size()==0:
    print("ytpmE")
else:
    print(''.join(reversed(stackMir.items)))
print(f"(RORRIM) ! ! ! (s)evisolpxE {countMir}")

    