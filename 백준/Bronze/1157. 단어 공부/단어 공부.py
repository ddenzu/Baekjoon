s = input().upper()
c = list(set(s))
cnt=[]
for i in c:
    cnt.append(s.count(i))
if cnt.count(max(cnt))>1:
    print("?")
else:
    print(c[cnt.index(max(cnt))])