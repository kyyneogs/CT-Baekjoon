import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    DP = [1,1,1,2,2,3,4,5,7,9] + [0] * (N-10)

    for i in range(10, N):
        DP[i] = DP[i-1] + DP[i-5]

    print(DP[N-1])