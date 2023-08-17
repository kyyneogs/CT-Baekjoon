import sys
N, M = map(int, sys.stdin.readline().split())
C = list(map(int, sys.stdin.readline().split()))

max = 0
for i in range(0,N-2):  # 중복을 막기 위해, N-2까지 제한
    for j in range(i+1,N-1):  # 중복을 막기 위해, i에서 항상 1 앞서있으며 N-1까지 제한
        for k in range(j+1,N):  # 중복을 막기 위해, j에서 항상 1 앞서있음
            tmp = C[i]+C[j]+C[k]
            if tmp>max and tmp<=M: max=tmp
            if max==M: break
print(max)