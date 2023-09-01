# 누적합, 투포인터?

import sys
input = sys.stdin.readline
INF = int(-1e9)

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
maxi = INF

for i in range(1,N+1):
    arr[i] += arr[i-1]

for i in range(0,N+1-K):
    sumi = arr[i+K] - arr[i]
    maxi = sumi if sumi > maxi else maxi

print(maxi)