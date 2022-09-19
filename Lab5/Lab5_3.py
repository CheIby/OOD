class node:
    def __init__(self,data,next = None ):
        self.data=data
        self.next=next
        self.pre=None
    
def createList(l=[]):
    head=None
    tail=None

    if len(l)==1:
        a=node(int(l[0]))
        head=a
        tail=a
    else:
        a=node(int(l.pop(0)))
        head=a
        tail=a
        for i in l:
            t=node(int(i))
            tail.next = t
            t.pre = tail
            tail = t

    return head

def printList(H):
    while H!=None:
        print(H.data,end=' ')
        H=H.next
    print()

def mergeOrderesList(p,q):
    lst1=p
    lst2=q
    head=None
    if lst1.data < lst2.data:
        head=node(lst1.data)
        lst1=lst1.next
    else:
        head=node(lst2.data)
        lst2=lst2.next
    tail=head
    while lst1!=None and lst2!=None:
        if lst1.data < lst2.data:
            a=node(lst1.data)
            tail.next = a
            a.pre=tail
            tail = a
            lst1=lst1.next
        else:
            a=node(lst2.data)
            tail.next = a
            a.pre=tail
            tail = a
            lst2=lst2.next
    while lst1 !=None:
        a=node(lst1.data)
        tail.next = a
        a.pre=tail
        tail = a
        lst1=lst1.next
    while lst2!=None:
        a=node(lst2.data)
        tail.next = a
        a.pre=tail
        tail = a
        lst2=lst2.next
    return head

inp = input("Enter 2 Lists : ").split(" ")
L1=[item for item in inp[0].split(',')]
L2=[item for item in inp[1].split(',')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)