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

def encodemsg(q1, q2):
    lstEnd=Queue()
    count=0
    for i in q1.lst:
        if count >= q2.size():
            count=0
        if i.isupper():
            if int(ord(i))+int(q2.lst[count])>90:
                lstEnd.enQueue(chr(ord(i)+int(q2.lst[count])-26))
            else:
                lstEnd.enQueue(chr(ord(i)+int(q2.lst[count])))
        elif i.islower():
            if int(ord(i))+int(q2.lst[count])>122:
                lstEnd.enQueue(chr(ord(i)+int(q2.lst[count])-26))
            else:
                lstEnd.enQueue(chr(ord(i)+int(q2.lst[count])))
        count+=1
    return lstEnd

def decodemsg(q1, q2):
    lstDe=Queue()
    count=0
    for i in q1.lst:
        if count >= q2.size():
            count=0
        if i.isupper():
            if int(ord(i))-int(q2.lst[count])<65:
                lstDe.enQueue(chr(ord(i)-int(q2.lst[count])+26))
            else:
                lstDe.enQueue(chr(ord(i)-int(q2.lst[count])))
        elif i.islower():
            if int(ord(i))-int(q2.lst[count])<97:
                lstDe.enQueue(chr(ord(i)-int(q2.lst[count])+26))
            else:
                lstDe.enQueue(chr(ord(i)-int(q2.lst[count])))
        count+=1
    return lstDe

inp,num = input("Enter String and Code : ").split(',')
q1 = Queue()
q2 = Queue()
inp=inp.replace(" ","")
num=num.replace(" ","")
for i in inp:
    q1.enQueue(i)
for i in num:
    q2.enQueue(i)
endCode=encodemsg(q1,q2)
deCode=decodemsg(endCode,q2)
print("Encode message is :  "+str(endCode.lst))
print("Decode message is :  "+str(deCode.lst))




        