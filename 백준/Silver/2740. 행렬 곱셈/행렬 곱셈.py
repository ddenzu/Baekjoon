import sys
a,b=map(int, sys.stdin.readline().split())
A=[]
for _ in range(a):
    A.append(list(map(int, sys.stdin.readline().split())))
c,d=map(int, sys.stdin.readline().split())
B=[]
for _ in range(c):
    B.append(list(map(int, sys.stdin.readline().split())))

C = [[0 for _ in range(d)] for _ in range(a)]
for i in range(a):
    for j in range(d):
        for k in range(c):
            C[i][j]+=A[i][k]*B[k][j]
for i in C:
    p = ' '.join(str(j) for j in i)
    print(p)