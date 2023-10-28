for _ in range(int(input())):
    a = int(input())
    b = int(input())
    A = [ i for i in range(1, b+1)]

    for i in range(a):
        for j in range(1,b):
            A[j]+= A[j-1]
    print(A[-1])