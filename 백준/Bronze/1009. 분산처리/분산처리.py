import sys
n = int(input())
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    a = a%10
    if a == 0:
        print(10)
    elif a in [1,5,6]:
        print(a)
    elif a in [4,9]:
        b = b%2
        if b != 1:
            print((a**2) % 10)
        elif b == 1:
            print(a)
    else:
        b = b%4
        if b == 0:
            print((a**4)%10)
        elif b != 0:
            print((a**b)%10)