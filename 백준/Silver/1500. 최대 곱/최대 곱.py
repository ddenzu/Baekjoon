import sys
s,k = map(int, sys.stdin.readline().split())
ans=[]
an = 1
for i in range(k):
    ans.append(s//k)
for j in range(s%k):
    ans[j] = ans[j] + 1
q = 1
for j in ans:
    q*=j
print(q)