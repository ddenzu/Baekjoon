N = input()
N = list(N)
F = int(input())
N[-2] = str(0)
N[-1] = str(0)
n = int("".join(N))
m = int(n)
i=0
while n<m+99:
    if n/F == n//F:
        break
    n+=1
n = list(map(int, str(n)))
print(n[-2],end="")
print(n[-1])