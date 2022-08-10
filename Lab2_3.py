
def mod_position(arr,s):
    num=int(s)
    count=1
    output=[]
    for i in range(len(arr)):
        if count%num==0:
            output.append(arr[i])
        count+=1
    return output

print("*** Mod Position ***")
checkStr , pos = input("Enter Input : ").split(',')
print(mod_position(checkStr,pos))
