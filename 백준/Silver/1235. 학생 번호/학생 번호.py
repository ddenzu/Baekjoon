import sys
N=int(sys.stdin.readline())
m=[]
for _ in range(N):
    m.append(sys.stdin.readline().rstrip())
a=-1
while True:
    ans = set()
    for i in m:
        ans.add(i[a:])
    if len(ans) == N:
        break
    a-=1
print(-a)