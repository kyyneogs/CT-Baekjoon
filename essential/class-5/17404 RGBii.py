import sys
input = sys.stdin.readline
INF = int(10e9)

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*3 for _ in range(2)]

mini = INF
for i in range(3):
    DP[0][i], DP[0][(i+1)%3], DP[0][(i+2)%3] = RGB[0][i], INF, INF
    for j in range(1,N):
        DP[1][0] = min(DP[0][1], DP[0][2]) + RGB[j][0]
        DP[1][1] = min(DP[0][0], DP[0][2]) + RGB[j][1]
        DP[1][2] = min(DP[0][1], DP[0][0]) + RGB[j][2]
        DP[0][0], DP[0][1], DP[0][2] = DP[1][0], DP[1][1], DP[1][2]
    mini = min(mini, DP[1][(i+1)%3], DP[1][(i+2)%3])
print(mini)