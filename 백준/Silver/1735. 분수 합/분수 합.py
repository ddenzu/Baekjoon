import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
A = []
B = []
for i in range(0,2):
    A.append(a[i]*b[1])
    B.append(b[i]*a[1])
C = [A[0]+B[0],A[1]]
def GCD(x, y):
    while(y):
        x,y=y,x%y
    return x
c = GCD(A[0]+B[0],A[1])
for i in C:
    print(i//c, end=" ")