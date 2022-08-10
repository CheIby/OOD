import math

def sum(num):
    sum=0
    while num!=0:
        sum=sum+num%10
        num //=10
    return sum

print(" *** Summation of each digit ***")
number = input("Enter a positive number : ")
if len(number)<=30:
    print(f"Summation of each digit =  {sum(int(number))}")
else:
    print("Error")


    