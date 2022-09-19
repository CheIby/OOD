
class Stack:
    def __init__(self):
        self.lst=[]
    
    def __str__(self):
        s=''
        while not self.isEmpty():
            s+=self.lst.pop(0)
        return s

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

inp = input("Enter expresion : ")
stack = Stack()
def check(inp):
    open=["(","{","["]
    close =[")","}","]"]
    for i in inp:
        if i in open:
            stack.push(i)
        elif i in close:
            if stack.isEmpty():
                return(inp + " close paren excess")
            elif close.index(i) == open.index(stack.peek()):
                stack.pop()
            else:
                return(inp + " Unmatch open-close")
        else:
            pass
    if not stack.isEmpty():
        return(inp + " open paren excess   " + str(stack.size()) +" : " + str(stack) )
    else:
        return (inp + " MATCH")


print(check(inp))
print(stack)