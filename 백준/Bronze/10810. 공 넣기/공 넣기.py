import sys
a,b=map(int,sys.stdin.readline().split())

A=[]
for i in range(a):
    A.append(0)

for i in range(b):
    c,d,f=map(int,sys.stdin.readline().split())
    for j in range(c-1,d):
        A[j]=f

for i in A:
    print(i,end=' ')