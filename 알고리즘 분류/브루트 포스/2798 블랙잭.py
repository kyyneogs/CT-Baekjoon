import sys
N, M = map(int, sys.stdin.readline().split())
C = list(map(int, sys.stdin.readline().split()))

max = 0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            tmp = C[i]+C[j]+C[k]
            if tmp>max and tmp<=M: max=tmp
            if max==M: break
print(max)