import sys
num = int(sys.stdin.readline())
q = []
for _ in range(num):
    q.append(list(map(int, input().split())))
for i in range(1,num):
    for j in range(len(q[i])):
        if j==0:
            q[i][j]=q[i][j]+q[i-1][j]
        elif j==len(q[i])-1:
            q[i][j]=q[i][j]+q[i-1][j-1]
        else:
            q[i][j]=q[i][j]+max(q[i-1][j],q[i-1][j-1])
print(max(q[num-1]))