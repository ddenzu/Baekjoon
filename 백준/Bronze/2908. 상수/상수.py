a = input().split()
b = a[0]
c = a[1]
b = b[::-1]
c = c[::-1]
if b > c:
    print(b)
elif c > b:
    print(c)