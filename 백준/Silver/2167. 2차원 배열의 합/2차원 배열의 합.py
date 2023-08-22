import sys
a,b = map(int, sys.stdin.readline().split())
List=[]
for _ in range(a):
    List.append(list(map(int, input().split())))
sum=[]
for _ in range(a+1):
    sum.append([0]*(b+1))
for i in range(1,a+1):
    for j in range(1,b+1):
        sum[i][j]=List[i-1][j-1]+sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]
c = int(input())
for _ in range(c):
    i,j,x,y = map(int, input().split())
    print(sum[x][y]-sum[i-1][y]-sum[x][j-1]+sum[i-1][j-1])
