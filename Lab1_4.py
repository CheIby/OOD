print("*** Fun with Drawing ***")
num = input("Enter input : ")
length = int(num)*4-3
for i in range(length):
    for j in range(length):
        if i==0  or i==length-1 or j==0 or j==length-1:
            print('#',end='')
        elif i%2==0 and j%2==0:
            if j>=i:
                print ('#',end='')
            else:
                print('.',end='')
        else:
            print('.',end='')
        
    print()