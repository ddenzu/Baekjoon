import sys
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
a.sort(key=lambda x:x[1]) 
a.sort(key=lambda x:x[0])
for j in range(n):
    print(a[j][0], end=' ')
    print(a[j][1])