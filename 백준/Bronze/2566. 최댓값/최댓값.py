b = []
c = []
for i in range(9):
    a = list(map(int, input().split(' ')))
    c.append(max(a))
    b.append(a)
for j in range(9):
    for k in range(9):
        if b[j][k] == max(c):
            print(max(c))
            print(j+1, k+1)
            break