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

inp,num = input("Enter people and time : ").split(" ")
line1 = Queue()
line2 = Queue()
lst=Queue()
time1=0
time2=0
for i in inp:
    lst.enQueue(i)
for i in range(int(num)):
    if line1.size() == 5 and not lst.isEmpty():
        line2.enQueue(lst.deQueue())
    elif not lst.isEmpty():
        line1.enQueue(lst.deQueue())
    print(str(i+1)+ " " + str(lst.lst)+" "+str(line1.lst)+" "+str(line2.lst))
    if not line1.isEmpty():
        time1+=1
        if time1 == 3 :
            line1.deQueue()
            time1=0
    if not line2.isEmpty():
        time2+=1
        if time2 == 2 :
            line2.deQueue()
            time2=0
    
    
    
    
 