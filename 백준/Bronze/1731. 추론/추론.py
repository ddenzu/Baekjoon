import sys
N=int(sys.stdin.readline())
seq = []
for i in range(N):
    seq.append(int(sys.stdin.readline()))
if seq[1] - seq[0] == seq[2] - seq[1]:
    seq.append(seq[-1]+(seq[1] - seq[0]))
else:
    seq.append(seq[-1]*(seq[1]//seq[0]))
print(seq[-1])