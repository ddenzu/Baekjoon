import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    arr = [1,1,1,2]
    for i in range(4,n+1):
        j = arr[i-3]+arr[i-2]
        arr.append(j)
    print(arr[-2])