import math
a = math.factorial(int(input()))
a = list(map(int,str(a)))
m=0
for i in a[::-1]:
    if i==0:
        m+=1
    elif i !=0:
        break
print(m)