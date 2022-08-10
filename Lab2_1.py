import math

class translator:
    def deciToRoman(self, num):
        deci=""
        roman=[]
        while num!=0:
            while num>=1000 and math.floor(num/1000)>=1:
                roman.append("M")
                num-=1000
            while num>=900 and math.floor(num/900)>=1:
                roman.append("CM")
                num-=900
            while num>=500 and math.floor(num/500)>=1:
                roman.append("D")
                num-=500
            while num>=400 and math.floor(num/400)>=1:
                roman.append("CD")
                num-=400
            while num>=100 and math.floor(num/100)>=1:
                roman.append("C")
                num-=100
            while num>=90 and math.floor(num/90)>=1:
                roman.append("XC")
                num-=90
            while num>=50 and math.floor(num/50)>=1:
                roman.append("L")
                num-=50
            while num>=40 and math.floor(num/40)>=1:
                roman.append("XL")
                num-=40
            while num>=10 and math.floor(num/10)>=1:
                roman.append("X")
                num-=10
            while num>=9 and math.floor(num/9)>=1:
                roman.append("IX")
                num-=9
            while num>=5 and math.floor(num/5)>=1:
                roman.append("V")
                num-=5
            while num>=4 and math.floor(num/4)>=1:
                roman.append("IV")
                num-=4
            while num>=1 and math.floor(num/1)>=1:
                roman.append("I")
                num-=1
        return  ''.join(roman)
        

    def romanToDeci(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(s)):
            if i>0 and roman[s[i]] > roman[s[i-1]]:
                num += roman[s[i]]-2*roman[s[i-1]]
            else:
                num+=roman[s[i]]
        return num


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))