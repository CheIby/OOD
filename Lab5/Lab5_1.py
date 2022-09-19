class node:
    def __init__(self,data,next=None):
        self.data=data
        if next == None:
            self.next=None
        else:
            self.next=next

class linkList:
    def __init__(self):
        self.head=None

    def __str__(self):
        s=''
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:s+=' <- '
        return s

    def append(self,data):
        p=node(data)
        if self.head==None:
            self.head=p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=p


print(" *** Locomotive ***")
inp = input("Enter Input : ").split(" ")
a=linkList()
for i in inp:
    a.append(i)
print("Before : " + a.__str__())
t=a.head
while t.data!="0":
    a.append(t.data)
    a.head = a.head.next
    t=t.next
    
print("After : " +a.__str__())

