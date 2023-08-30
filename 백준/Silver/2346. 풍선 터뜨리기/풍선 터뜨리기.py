import sys
from collections import deque
n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().strip().split()))
que = deque(enumerate(k))
result = []
while que:
    p,a=que.popleft()
    result.append(p+1)
    if a>0:
        que.rotate(-(a-1))
    else:
        que.rotate(-a)
print(' '.join(map(str,result)))