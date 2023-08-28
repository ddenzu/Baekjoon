import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())
A = []
A = deque(A)
for i in range(a):
    A.append(i+1)
g = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(b):
    if A.index(g[i]) < len(A) - A.index(g[i]):
        while True:
            if g[i] == A[0]:
                del A[0]
                break
            else:
                A.rotate(-1)
                cnt+=1
    else:
        while True:
            if g[i] == A[0]:
                del A[0]
                break
            else:
                A.rotate(1)
                cnt+=1
print(cnt)