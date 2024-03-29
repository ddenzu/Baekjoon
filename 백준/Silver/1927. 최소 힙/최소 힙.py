import sys
from heapq import heappop , heappush
heap = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x)