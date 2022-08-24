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
    def peek(self):
        return self.lst[-1]

inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')
checkBox = ["-" , "+" , "*" ,"/"  ,"^","(",")"]
priority ={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':3,
    '^':4
    }
for i in inp:
    if i not in checkBox:
        print(i,end="")
        # print('\n'+i)
    else:
        # print('\n'+i, S.lst, sep = " and ")
        if i=='(':
            S.push(i)
        elif i==')' and not S.isEmpty():
            while S.peek() !='(':
                print(S.pop(), end='')
            S.pop()
        elif S.size() > 0 and priority.get(i) <= priority.get(S.peek()):
            while not S.isEmpty() and S.peek() != '(' and priority.get(i) <= priority.get(S.peek()):
                print(S.pop(), end='')
            S.push(i)
        else:
            S.push(i)
while not S.isEmpty():
    print(S.pop(), end='')
