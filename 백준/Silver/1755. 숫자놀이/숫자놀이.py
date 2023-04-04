import sys
a,b=map(int, sys.stdin.readline().split())
N=[]
N_dic = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 0: "zero"}
N_dic_swap = {v:k for k,v in N_dic.items()}
for i in range(a,b+1):
    if i<10:
        N.append(N_dic[i])
    else:
        i = list(map(int, str(i)))
        N.append(N_dic[i[0]]+" "+N_dic[i[1]])
N.sort()
cnt=0
for j in N:
    if j in N_dic_swap:
        print(N_dic_swap[j],end=" ")
        cnt+=1
    else:
        j = j.split()
        print(N_dic_swap[j[0]],end="")
        print(N_dic_swap[j[1]],end=" ")
        cnt+=1
    if cnt%10 == 0:
        print()