import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for l in range(i-1,j):
        arr[l] = k
print(*arr)