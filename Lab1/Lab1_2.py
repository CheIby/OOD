print("*** multiplication or sum ***")
x,y = input("Enter num1 num2 : ").split()
x,y=[int(x),int(y)]
if x*y>1000:
    print(f"The result is {x+y}")
else:
    print(f"The result is {x*y}")