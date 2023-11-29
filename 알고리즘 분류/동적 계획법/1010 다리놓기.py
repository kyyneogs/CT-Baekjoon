import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())

    K = M-N

    DP = [[i for i in range(1,K+1)]] + [[0]*K for _ in range(N-1)]
    
    for i in range(1,N):
        for j in range(K):
            DP[i][j] = DP[i-1][j] + DP[i][j-1]

    print(sum(DP[i][-1] for i in range(N))+1 if DP[0] else 1)