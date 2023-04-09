import sys
n=int(sys.stdin.readline())
grade = []
for i in range(n):
    grade.append(list(map(int, sys.stdin.readline().split())))
grade.sort(key=lambda grade: -grade[2])
i=0
cnt=[]
ccnt=[]
while True:
    if len(cnt)==3:
        if len(set(cnt))==1:
            del cnt[-1]
            del ccnt[-1]
            continue
        else:
            for j in range(3):
                b = grade[ccnt[j]][:2]
                c = ' '.join(str(s) for s in b)
                print(c)
            break
    cnt.append(grade[i][0])
    ccnt.append(i)
    i+=1