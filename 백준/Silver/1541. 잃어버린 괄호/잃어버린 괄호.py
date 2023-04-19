n = input().split('-')
li=[]
for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    li.append(cnt)
ans = li[0]
for k in li[1:]:
    ans-=k
print(ans)