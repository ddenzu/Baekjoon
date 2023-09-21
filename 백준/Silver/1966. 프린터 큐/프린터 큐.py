import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())
    B = deque(list(map(int, sys.stdin.readline().split())))
    a_de = deque(list(range(a)))
    cnt = 0
    while B:
        if B[0] == max(B):
            cnt+=1
            B.popleft()
            pop_idx = a_de.popleft()
            if pop_idx == b:
                print(cnt)
        else:
            B.rotate(-1)
            a_de.rotate(-1)