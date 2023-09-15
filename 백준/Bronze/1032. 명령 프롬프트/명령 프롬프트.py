import sys
n = int(sys.stdin.readline())
ans = []
for i in range(n):
    ans.append(list(sys.stdin.readline().rstrip()))
i=0
j=0
c = []
if len(ans) == 1:
    print(''.join(s for s in ans[0]))
else:
    while i<len(ans) and j<len(ans[0]):
        if ans[i][j] == ans[i+1][j]:
            c.append(ans[i][j])
            j+=1
        else:
            c.append('?')
            j+=1

        if j == len(ans[1]):
            if i == n-2:
                print(''.join(s for s in c))
                break
            i+=1
            j=0
            ans[i] = c
            c = []
            continue