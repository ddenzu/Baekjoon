n = int(input())
C = []
for _ in range(n):
    a,b=map(int, input().split())
    m = a*b
    if a < b:
        a,b= b,a
    while b>0:
        n = a%b
        a = b
        b = n
    C.append(int(m/a))
for j in C:
    print(j)