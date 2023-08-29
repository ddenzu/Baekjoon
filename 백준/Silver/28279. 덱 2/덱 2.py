import sys
from collections import deque
n=int(sys.stdin.readline())
stk=deque()
for _ in range(n):
    a=list(map(int, sys.stdin.readline().strip().split()))
    if a[0]==1:
        stk.insert(0,a[1])

    elif a[0]==2:
        stk.append(a[1])

    elif a[0]==3:
        if len(stk)==0:
            print(-1)
        else:
            print(stk.popleft())

    elif a[0]==4:
        if len(stk)==0:
            print(-1)
        else:
            print(stk.pop())

    elif a[0]==5:
        print(len(stk))

    elif a[0]==6:
        if len(stk)==0:
            print(1)
        else:
            print(0)

    elif a[0]==7:
        if len(stk)==0:
            print(-1)
        else:
            print(stk[0])

    elif a[0]==8:
        if len(stk)==0:
            print(-1)
        else:
            print(stk[-1])
    