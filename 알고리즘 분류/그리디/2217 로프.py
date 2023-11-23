import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
maxi, cnt = 0, N

for i in range(N-1, -1, -1):
    maxi = max(maxi, arr[-1]*cnt)
    arr.pop()
    cnt -= 1

print(maxi)