# 답지 보고함...
import sys
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]

if N < 3:
    print(sum(S))
else:
    DP = [0] * N
    DP[0] = S[0]
    DP[1] = S[1] + S[0]
    for i in range(2, N):
        DP[i] = max(DP[i-3]+S[i-1]+S[i], DP[i-2]+S[i])
    print(DP[N-1])