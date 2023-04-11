import sys
a = sys.stdin.readline().split()
ans = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        b = (2**(len(a[i])-(j+1)))
        c = int(a[i][j])*b
        ans+=c
ans2 = []
while True:
    ans2.insert(0,ans%2)
    ans = ans//2
    if ans==0:
        break
print(''.join(str(s) for s in ans2))