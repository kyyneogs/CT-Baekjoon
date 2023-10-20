import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

DP = [0]*N
DP[0] = arr[0]
DP[1] = arr[0] + arr[1]

