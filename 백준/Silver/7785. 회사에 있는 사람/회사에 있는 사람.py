import sys
T = int(sys.stdin.readline())
dic = {}
for i in range(T):
    Name,State = sys.stdin.readline().split()
    dic.update({Name: State})
result = []
for key,value in dic.items():
    if value == 'enter':
        result.append(key)
result.sort(reverse=True)
for j in result:
    print(j)