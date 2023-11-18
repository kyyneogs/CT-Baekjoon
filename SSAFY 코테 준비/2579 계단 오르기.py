import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
dp = [0]*(N+1)

for i in range(1, N+1):
    if i <=2:
        dp[i] = arr[i] + dp[i-1]
    else:
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[N])