import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
DP = [1]*N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[j]+1, DP[i])

print(max(DP))