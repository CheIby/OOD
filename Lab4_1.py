class Queue:
    def __init__(self):
        self.items=[]
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

inp = input("Enter Input : ").split(',')
queue = Queue()
dq = Queue()
for i in inp:
    strSplit = i.split(' ')
    if strSplit[0] == 'E':
        queue.enQueue(int(strSplit[1]))
        print(', ' .join(map(str,queue.items)))
    elif strSplit[0] == 'D':
        if queue.size() >1:
            dq.enQueue(queue.deQueue())
            print(str(dq.items[-1]) + " <- " + str(', ' .join(map(str,queue.items))) )
        elif queue.size() ==1:
            dq.enQueue(queue.deQueue())
            print(str(dq.items[-1]) + " <- Empty")
        elif queue.size()==0:
            print("Empty")
if queue.size() == 0:
    queue.enQueue("Empty")
if dq.size() == 0:
    dq.enQueue("Empty")
print(str(', ' .join(map(str,dq.items))) + " : "+str(', ' .join(map(str,queue.items))))