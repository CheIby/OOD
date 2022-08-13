
class TorKham:
    def __init__(self,lst):
        self.lst =lst
    def checkLst(self):
        finalLst =[]
        temp = self.lst[0]
        oldTemp = [] 
        i=0
        for i in range(len(self.lst)):
            temp = self.lst[i]
            if temp[0] == 'P' :
                if len(finalLst) == 0:
                    output = temp.split(' ')
                    finalLst.append(output[1])
                    oldTemp = temp
                    print(f"\'{output[1]}\' -> {finalLst}")
                else:
                    if temp[2].upper() == oldTemp[len(oldTemp)-2].upper() and temp[3].upper() == oldTemp[len(oldTemp)-1].upper():
                        output = temp.split(' ')
                        finalLst.append(output[1])
                        oldTemp = temp
                        print(f"\'{output[1]}\' -> {finalLst}")
            elif temp[0] == 'R' :
                temp=[]
                oldTemp=[]
                finalLst=[]
                print("game restarted")
            elif temp[0] == 'X' :
                print("" ,end='')
            else :
                print(f"\'{temp}\' is Invalid Input !!!")
            i+=1
           
print("*** TorKham HanSaa ***")
lst=[]
lst.extend(input("Enter Input : ").split(','))
lstResult = TorKham(lst)
lstResult.checkLst()
