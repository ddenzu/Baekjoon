import sys
n = int(sys.stdin.readline())
ans=[]
ans.append(sys.stdin.readline().rstrip())
for i in range(n-1):
    a = sys.stdin.readline().rstrip()
    if a=='/':
        ans.append('//')
    else:
        ans.append(a)
    b = sys.stdin.readline().rstrip()
    ans.append(b)
ans1 = ''.join(s for s in ans)
print(eval(ans1))