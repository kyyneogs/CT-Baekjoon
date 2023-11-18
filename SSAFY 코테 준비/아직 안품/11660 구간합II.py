import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]

for k in range(2):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j] += dp[i-1*k][j-(1-k)]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)


# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = 0
#     for i in range(x1, x2+1):
#         result += dp[i][y2] - dp[i][y1-1]
#     print(result)