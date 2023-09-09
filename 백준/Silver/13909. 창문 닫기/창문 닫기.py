import sys
n = int(sys.stdin.readline())
a = 1
while True:
    b = (a**2)
    if n >= b and n < ((a+1)**2):
        print(a)
        break
    a+=1