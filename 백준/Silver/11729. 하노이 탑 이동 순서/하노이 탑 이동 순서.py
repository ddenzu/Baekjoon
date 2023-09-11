import sys
a = int(sys.stdin.readline())
def hanoi(n,start,end,sup):
    if n == 1:
        print(start,end)
    else:
        # 보조기둥으로 옮기기
        hanoi(n-1,start,sup,end)
        print(start,end)
        # 보조기둥을 시작기둥으로, 시작기둥을 보조기둥으로
        hanoi(n-1,sup,end,start)
print((2**a)-1)
hanoi(a,1,3,2)