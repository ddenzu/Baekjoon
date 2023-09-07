import sys
A,B = map(int,sys.stdin.readline().split())
def gcd(a,b): # 최대공약수
    while b != 0:
        c = a%b
        if c == 0:
            return b
        a,b=b,c
print(int((A*B) / gcd(A,B)))