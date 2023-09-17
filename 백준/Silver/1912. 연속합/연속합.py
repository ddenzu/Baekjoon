import sys
num = int(sys.stdin.readline())
arr = [*map(int,input().split())]
result=[arr[0]]
for i in range(1,len(arr)):
    result.append(max(result[i-1]+arr[i],arr[i]))
print(max(result))