import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

A = sorted(A)
for i in L:
    target = i
    start = 0 # index
    end = len(A) -1 # index
    Exist_I = False
    while start <= end:
        mid = (start + end) // 2 # index

        if target == A[mid]:
            Exist_I = True
            print(1)
            break
        elif target > A[mid]:
            start = mid + 1

        else:
            end = mid - 1
    if not Exist_I:
        print(0)