a = int(input())
e = []
p = []
f = 0

for i in range(a):
    b = str(input())
    b = list(map(int, b.split(' ')))
    c = sum(b[1:])
    d = c/b[0]
    e.append(d)
    for j in range(1,len(b)):
        if b[j] > d:
            f+=1
    h = (f/b[0])*100
    l = "{:.3f}".format(h)
    p.append(l)
    f = 0
    c = 0
    d = 0
for j in range(a):
    print(p[j],end='')
    print("%")