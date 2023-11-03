a = int(input())
b = str(input())
b = b.split()
c = list(map(int, b))
d = max(c)
e = 0
for i in range(a):
    c[i] = c[i]/d*100
    e += c[i]
print(e/a)