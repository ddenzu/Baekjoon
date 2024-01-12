import sys
n = int(input())
m = []
for i in range(n):
    a = int(sys.stdin.readline())
    m.append(a)
m.sort()
for i in range(n):
    print(m[i])