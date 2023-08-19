import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    n, m = sys.stdin.readline().split()
    arr.append([i, int(n), m])

arr.sort(key = lambda x: (x[1], x[0]))

for i in arr:
    print(i[1],i[2], sep=' ')