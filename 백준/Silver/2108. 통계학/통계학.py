import sys
from collections import Counter
n = int(input())
A=[]
for _ in range(n):
    A.append(int(sys.stdin.readline()))
A.sort()
print(round(sum(A)/n))
print(A[n // 2])
cnt = Counter(A).most_common()
if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(A[-1] - A[0])