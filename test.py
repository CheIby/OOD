def perket(now = 0,S=1,B=0):
    if now >= len(inp):
        return
    ind = inp[now].split()
    ind = [int(i) for i in ind]
    
    isCollectedResult = abs((S*ind[0]) - (B + ind[1]))
    global ans
    ans = min(ans,isCollectedResult)
    perket(now+1,S*ind[0],B + ind[1])
    # print(ind[0], ind[1])
    perket(now+1,S,B)
    # print()    
        
        
    
inp = []    
inp = input('Enter Input : ').split(',')
ans = 9999999
perket()
print(ans)
