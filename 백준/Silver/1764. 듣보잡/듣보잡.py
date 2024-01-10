import sys
a,b=map(int, input().split())
A=[]
B=[]
cnt=0
for i in range(a+b):
    if cnt < a:
        A.append(sys.stdin.readline().strip())
    else:
        B.append(sys.stdin.readline().strip())
    cnt+=1
A=set(A)
B=set(B)
print(len(A.intersection(B)))
for i in sorted(A.intersection(B)):
    print(i)