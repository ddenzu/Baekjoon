import sys
from math import gcd
a = int(sys.stdin.readline())
list = []
for _ in range(a):
    list.append(sys.stdin.readline())
LI = list
b = len(list)
result = []
for j in range(0, b+1):
    result.append(int(LI[j+1])-int(LI[j]))
    if j == b-2:
        break
p = result[0]
for k in range(1, len(result)):
    p=gcd(p, result[k])
ans=0
for i in result:
    ans+=i//p-1
print(ans)