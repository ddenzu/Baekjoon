import sys
N = []
for i in range(3):
    N.append(sys.stdin.readline().rstrip())
ans=[]
last=0
for j in range(len(N)):
    if j == 0:
        if N[j]=="black":
            ans.append(0)
        elif N[j]=="brown":
            ans.append(1)
        elif N[j]=="red":
            ans.append(2)    
        elif N[j]=="orange":
            ans.append(3)
        elif N[j]=="yellow":
            ans.append(4)
        elif N[j]=="green":
            ans.append(5)
        elif N[j]=="blue":
            ans.append(6)
        elif N[j]=="violet":
            ans.append(7)
        elif N[j]=="grey":
            ans.append(8)
        elif N[j]=="white":
            ans.append(9)
    elif j == 1:
        if N[j]=="black":
            ans.append(0)
        elif N[j]=="brown":
            ans.append(1)
        elif N[j]=="red":
            ans.append(2)    
        elif N[j]=="orange":
            ans.append(3)
        elif N[j]=="yellow":
            ans.append(4)
        elif N[j]=="green":
            ans.append(5)
        elif N[j]=="blue":
            ans.append(6)
        elif N[j]=="violet":
            ans.append(7)
        elif N[j]=="grey":
            ans.append(8)
        elif N[j]=="white":
            ans.append(9)
    else:
        if N[j]=="black":
            last=1
        elif N[j]=="brown":
            last=10
        elif N[j]=="red":
            last=100   
        elif N[j]=="orange":
            last=1000
        elif N[j]=="yellow":
            last=10000
        elif N[j]=="green":
            last=100000
        elif N[j]=="blue":
            last=1000000
        elif N[j]=="violet":
            last=10000000
        elif N[j]=="grey":
            last=100000000
        elif N[j]=="white":
            last=1000000000
print(int(''.join(str(s) for s in ans))*last)