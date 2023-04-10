import sys
n = int(sys.stdin.readline())
book = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a in book:
        book[a]+=1
    else:
        book[a] = 1
max_val = max(book.values())
ans=[]
for key, value in book.items():
    if value == max_val:
        ans.append(key)
ans.sort()
print(ans[0])