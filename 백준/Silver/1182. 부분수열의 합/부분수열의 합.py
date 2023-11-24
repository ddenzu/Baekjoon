import sys
from itertools import combinations
a,b = map(int, sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split()))
A=[]
B=[]
summ=0
for i in range(1,len(n)+1):
    per = combinations(n,i)
    for j in list(per):
        if sum(j) == b:
            summ+=1
print(summ)