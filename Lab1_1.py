print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input ("Enter hh mm ss : ").split()
h,m,s = [int(h),int(m),int(s)]
second = "{:,}".format((h*60*60)+(m*60)+s)
hh,mm,ss = ['','','']
if h<10:
    hh=f'0{h}'
else:
    hh=f'{h}'
if m<10:
    mm=f'0{m}'
else:
    mm=f'{m}'
if s<10:
    ss=f'0{s}'
else:
    ss=f'{s}'

if m>=60 or m<0:
    print(f'mm({m}) is invalid!')
elif s>=60 or s<0:
    print(f'ss({s}) is invalid!')
else:
    print(f'{hh}:{mm}:{ss} = {second} seconds')
