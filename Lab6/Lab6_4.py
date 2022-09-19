
def perket(inp,i=0,S=1,B=0):
    if i>=len(inp):
        return
    else:
        a=inp[i]
        a=a.split(' ')
        result = abs((S*int(a[0]))-(B+int(a[1])))
        global ans
        ans=min(ans,result)
        perket(inp,i+1,S*int(a[0]),B+int(a[1]))
        perket(inp,i+1,S,B)
        

inp=input("Enter Input : ").split(",")
ans=999999
perket(inp)
print(ans)