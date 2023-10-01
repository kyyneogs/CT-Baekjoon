import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0]*N

if len(arr)<3:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2,N):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])
    print(dp[N-1])