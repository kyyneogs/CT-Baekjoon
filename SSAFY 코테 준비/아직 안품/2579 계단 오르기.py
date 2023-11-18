import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

DP = [0]*N
if N==1:
    print(arr[0])
elif N==2:
    print(arr[0]+arr[1])
else:
    DP[0] = arr[0]
    DP[1] = arr[0] + arr[1]

    for i in range(2, N):
        DP[i] = max(DP[i-3] + arr[i-1] + arr[i], DP[i-2] + arr[i])
    print(DP[N-1])