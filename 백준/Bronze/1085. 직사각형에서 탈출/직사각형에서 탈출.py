import sys
a,b,c,d = map(int, sys.stdin.readline().split())
ans=[]
ans.append(a-0)
ans.append(b-0)
ans.append(c-a)
ans.append(d-b)
print(min(ans))