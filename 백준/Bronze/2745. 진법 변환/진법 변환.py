import sys
a,b=sys.stdin.readline().split()
a=a[::-1]
b=int(b)
Num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt=0
result=0
for i in a:
    result+=Num.index(i)*(b**cnt)
    cnt+=1
print(result)