a,b=map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
A1 = A-B
B1 = B-A
print(len(A1)+len(B1))