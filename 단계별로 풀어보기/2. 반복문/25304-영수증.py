import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
S = 0
for _ in range(N):
    M1, M2 = map(int, sys.stdin.readline().split())
    S = S + M1*M2
if X==S: print('Yes')
else: print('No')