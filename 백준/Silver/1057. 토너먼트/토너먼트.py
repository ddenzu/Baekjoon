import sys
import math
n,a,b = map(int, sys.stdin.readline().split())
N = []
for i in range(n):
    N.append(i+1)
round = 0
while True:
    if math.ceil(a)==math.ceil(b):
        break
    round+=1
    a,b=math.ceil(a/2),math.ceil(b/2)
print(round)