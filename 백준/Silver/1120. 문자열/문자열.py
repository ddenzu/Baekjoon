import sys
a,b = sys.stdin.readline().rstrip().split()
ans = []
for i in range(len(b)-len(a) + 1):
    cnt=0
    B = list(b[i:i+len(a)])
    A = list(a)
    for i in range(len(B)):
        if A[i] == B[i]:
            cnt+=1
    ans.append(cnt)
print(len(a)-max(ans))