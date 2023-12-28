import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()
arr.sort(key = lambda x:(x[0], x[1]))

for i in arr:
    print(*i)