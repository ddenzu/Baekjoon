import sys
a = int(sys.stdin.readline())
sta = []
for i in range(a):
    b = sys.stdin.readline().rstrip()

    if b == '2':
        if len(sta) == 0:
            print(-1)
        else:
            print(sta.pop())

    elif b == '3':
        print(len(sta))

    elif b == '4':
        if len(sta) == 0:
            print(1)
        else:
            print(0)

    elif b == '5':
        if len(sta) == 0:
            print(-1)
        else:
            print(sta[-1])

    elif len(b) > 2:
        sta.append(int(b[2:]))