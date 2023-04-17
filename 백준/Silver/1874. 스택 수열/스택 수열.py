import sys
cnt = 1
ans = True
stack = []
pm = []

N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())
    while cnt <= n:
        stack.append(cnt)
        pm.append('+')
        cnt+=1
    if stack[-1] == n:
        stack.pop()
        pm.append('-')
    else:
        ans = False
if not ans:
    print('NO')
else:
    for i in pm:
        print(i)