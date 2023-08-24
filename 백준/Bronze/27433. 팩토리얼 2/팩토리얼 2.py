import sys
a = int(sys.stdin.readline())
result=1
if a == 0:
    print(1)
else:
    for i in range(a,0,-1):
        result*=i
    print(result)