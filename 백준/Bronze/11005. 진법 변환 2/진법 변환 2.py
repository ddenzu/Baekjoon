import sys
a,b=map(int,sys.stdin.readline().split())
Num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=[]
while a != 0:
    c = a%b
    d = a//b
    result.append(Num[c])
    a = d  
for i in result[::-1]:
    print(i,end='')