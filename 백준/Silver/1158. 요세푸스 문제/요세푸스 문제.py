import sys
from collections import deque
N,K = map(int, sys.stdin.readline().split())
soon = []
for i in range(N):
    soon.append(i+1)
soon = deque(soon)
ans=[]
while len(ans)!=N:
    soon.rotate(-(K-1))
    ans.append(soon.popleft())
for i in soon:
    ans.append(i)
print(str(ans).replace('[', '<').replace(']', '>'))