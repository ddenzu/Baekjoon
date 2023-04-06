import sys
import math
n = int(input())
A=[]
for _ in range(n):
    a,b=map(int, sys.stdin.readline().split())
    c = math.factorial(b)//(math.factorial(b-a)*math.factorial(a))
    A.append(c)
for i in A:
    print(i)