import sys
n = int(sys.stdin.readline())
i=2
result = []
while True:
    if n==1:
        break
    elif n//i == n/i:
        n=n/i
        result.append(i)
    else:
        i+=1
for i in result:
    print(i)