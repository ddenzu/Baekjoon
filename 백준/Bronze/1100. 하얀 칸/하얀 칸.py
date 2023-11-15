import sys
C = []
for i in range(8):
    c = list(sys.stdin.readline().strip())
    C.append(c)
cnt=0
for j in range(8):
    for k in range(8):
        if C[j][k] == "F":
            if (j+k)%2 != 1:
                cnt+=1

print(cnt)