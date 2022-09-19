class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        a = Node(item)
        if self.isEmpty():
            self.head = a
            self.tail = a
        else:
            a.previous = self.tail
            self.tail.next = a
            self.tail=a

    def addHead(self, item):
        a=Node(item)
        if self.isEmpty():
            self.head=a
            self.tail=a
        else:
            self.head.previous = a
            a.next=self.head
            self.head=a

    def insert(self, pos, item):
        a=Node(item)
        t=self.head
        if pos <= self.size() and pos > 0:
            i=0
            while i< pos-1:
                t=t.next
                i+=1
            a.previous = t.previous
            a.next = t
            t.previous.next = a
            t.previous = a
        elif pos == 0 or -1*pos > self.size():
            
            if self.size()!=0:
                t.previous = a
                a.next = t
                self.head = a
            else:
                self.head=a
                self.tail=a
        elif pos < 0:
            t=self.tail
            i=1
            while i<-1*pos:
                t=t.previous
                i+=1
            a.previous=t.previous
            t.previous.next = a
            a.next = t
            t.previous = a 
        else:
            a.previous = self.tail
            self.tail.next = a
            self.tail = a

    def search(self, item):
        t=self.head
        while t!=None:
            if t.value==item:
                return "Found"
            t=t.next
        return "Not Found"

    def index(self, item):
        t=self.head
        i=0
        while t!=None:
            if t.value == item:
                return i
            t=t.next
            i+=1
        return -1
        
    def size(self):
        sum=0
        head=self.head
        while head!=None:
            sum+=1
            head=head.next
        return sum

    def pop(self, pos):
        t=self.head
        if pos<0 or pos>=self.size():
            return "Out of Range"
        else:
            i=0
            while i<pos:
                t=t.next
                i+=1
            if self.size()==1:
                self.head=None
                self.previous=None
            elif i==0:
                self.head = t.next
                self.head.previous = None
            elif i==self.size()-1:
                self.tail = t.previous
                self.tail.next = None
            else:
                t.next.previous = t.previous
                t.previous.next = t.next
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
