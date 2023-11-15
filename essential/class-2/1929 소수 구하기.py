import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [1] * (N+1)
arr[1] = 0

for i in range(2, int(N**0.5)+2):
    if arr[i] == 0:
        continue

    for j in range(i*2, N+1, i):
        arr[j] = 0

for i in range(M,N+1):
    if arr[i]:
        print(i)