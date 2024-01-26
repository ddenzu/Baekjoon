a,b = map(int, input().split())
if b >= 45:
    b -= 45
    print(a, b)
elif b <= 44:
    a = a-1
    c = 45-b
    b = 60-c
    if a <= 0:
        a += 24
        if a == 24:
            a = 0
        print(a, b)
    else:
        print(a, b)