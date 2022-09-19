def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)

inp = int(input("Enter Number : "))
print(f"fibo({inp}) = " + str(fibo(inp)))