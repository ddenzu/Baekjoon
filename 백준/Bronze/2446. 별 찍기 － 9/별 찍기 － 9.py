import sys
n = int(sys.stdin.readline())
num = (2*n)-1
for i in range(1,(2*n),2):
    if (2*n)-i == 1: # 역방향
        k=n-1
        for j in range(1,(2*n),2):
            if j ==0:
                break
            print(" "*(k),end="")
            print(j*"*")
            k-=1
    else:
        print(" "*(i//2),end="")
        print(((2*n)-i)*"*")