import sys
a = int(sys.stdin.readline())
b = 2
if a == 0:
    print(4)
else:
    for i in range(0,a):
        c=b-1
        b=b+c
    print(b*b)