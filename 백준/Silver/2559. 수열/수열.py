import sys
a,b = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
A = []
summ = sum(N[:b])
A.append(summ)
for i in range(a-b):
    A.append(A[i]-N[i]+N[i+b])
print(max(A))