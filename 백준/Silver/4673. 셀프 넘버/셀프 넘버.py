n = set(range(1, 10001))
s = set()

for i in range(1, 10001):
    for j in str(i):
        i +=int(j)
    s.add(i)

num = sorted(n - s)
for i in num:
    print(i)