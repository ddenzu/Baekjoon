import sys
from itertools import combinations_with_replacement
a,b = map(int, sys.stdin.readline().split())
A = []
for i in range(a):
    A.append(i+1)
perm = list(combinations_with_replacement(A, b))
for j in perm:
    print(' '.join(map(str,j)))