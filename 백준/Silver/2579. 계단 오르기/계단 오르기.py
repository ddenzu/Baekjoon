import sys
num = int(sys.stdin.readline())
q = [0]*301
for j in range(num):
    q[j]=int(sys.stdin.readline())
arr = [0]*301
arr=[q[0],q[0]+q[1],max(q[1]+q[2],q[0]+q[2])]
for i in range(3,num):
    arr.append(max(arr[i-3]+q[i-1]+q[i],arr[i-2]+q[i]))
print(arr[num-1])