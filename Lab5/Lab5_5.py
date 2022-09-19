class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    a=Node(LL.pop(0))
    head=a
    tail=a
    while len(LL)!=0:
        t=Node(LL.pop(0))
        tail.next = t
        tail = t
    return head

def printLL(head):
    s=''
    t=head
    while t!=None:
        s+= t.value
        if t.next!=None:
            s+=" "
        t=t.next
    return s

def SIZE(head):
    i=0
    t=head
    while t!=None:
        i+=1
        t=t.next
    return i

def moveNode(head,num):
    t=head
    while num!=0:
        t=t.next
        num-=1
    return t

def splitLL(head,num):
    t=moveNode(head,num-1)
    a = t.next
    t.next = None
    return a

def append(head,node):
    if head==None:
        return node
    t=head
    while t.next!=None:
        t=t.next
    t.next=node
    return head

def bottomUp(head,b,size):
    bot=int((size*b)/100)
    if bot==0 or bot==size:
        return head
    tail=moveNode(head,size-1)
    t=splitLL(head,bot)
    tail.next=head
    return t

def riffle(head,r,size):
    rif = int((r*size)/100)
    second=splitLL(head,rif)
    newHead=None
    while head!=None or second!=None:
        if head!=None:
            t=splitLL(head,1)
            head,t=t,head
            newHead=append(newHead,t)
        if second!=None:
            t=splitLL(second,1)
            second,t=t,second
            newHead=append(newHead,t)
    return newHead

def deRiffle(head,r,size):
    rif = int((r*size)/100)
    first=None
    second=None
    while head!=None:
        if SIZE(first)<rif:
            t=splitLL(head,1)
            head,t=t,head
            first=append(first,t)
        if SIZE(second)<size-rif:
            t=splitLL(head,1)
            head,t=t,head
            second=append(second,t)
    a=moveNode(first,rif-1)
    a.next = second
    return first

def deBottomUp(head,b,size):
    bot=int((size*b)/100)
    bot = size-bot
    if bot==0 or bot==size:
        return head
    tail=moveNode(head,size-1)
    t=splitLL(head,bot)
    tail.next=head
    return t

def scarmble(head, b, r, size):
    t=bottomUp(head,b,size)
    print(f"BottomUp {b:.3f} % : {printLL(t)}")
    t=riffle(t,r,size)
    print(f"Riffle {r:.3f} % : {printLL(t)}")
    t=deRiffle(t,r,size)
    print(f"Deriffle {r:.3f} % : {printLL(t)}")
    t=deBottomUp(t,b,size)
    print(f"Debottomup {b:.3f} % : {printLL(t)}")
    
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)