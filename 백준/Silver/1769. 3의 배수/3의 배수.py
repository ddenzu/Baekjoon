import sys
n = sys.stdin.readline().rstrip()
N = list(map(int, str(n)))
cnt=0
while len(N)!=1:
    N=sum(N)
    cnt+=1
    N = list(map(int, str(N)))
print(cnt)
if N[0]%3==0:
    print('YES')
else:
    print('NO')