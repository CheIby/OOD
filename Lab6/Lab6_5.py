def staircase(n,i):
    if n>0:
        if i>n:
            pass
        else:
            print(str("_"*(n-i))+str("#"*(i)))
            return staircase(n,i+1)
    elif n<0:
        if i>-n:
            pass
        else:
            print(str("_"*(i-1))+str("#"*((-n)-(i-1))))
            return staircase(n,i+1)
    else:
        print("Not Draw!")

staircase(int(input("Enter Input : ")),1)
