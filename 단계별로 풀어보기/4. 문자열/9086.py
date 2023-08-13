import sys
N = int(sys.stdin.readline())
for _ in range(N):
    K = sys.stdin.readline().strip()
    print(K[0],K[-1], sep='')