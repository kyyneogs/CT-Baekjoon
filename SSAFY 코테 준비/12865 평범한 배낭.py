import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(1, N+1):
    weight, value = arr[i-1]
    for j in range(1, K+1):
        if weight > j:
            dp[j][i] = dp[j][i-1]
        else:
            dp[j][i] = max(dp[j][i-1], value + dp[j-weight][i-1])

print(dp[K][N])