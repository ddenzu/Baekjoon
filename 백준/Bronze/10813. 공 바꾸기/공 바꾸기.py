import sys
n,m =map(int,sys.stdin.readline().split())
a=1
list=[]
for _ in range(n):
    list.append(a)
    a+=1
for i in range(m):
    j,k =map(int,sys.stdin.readline().split())
    list[j-1] , list[k-1] = list[k-1] , list[j-1]
print(' '.join(map(str,list)))