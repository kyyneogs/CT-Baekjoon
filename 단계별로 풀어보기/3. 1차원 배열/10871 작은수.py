import sys
N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(filter(lambda x: x<X, arr))
print(*arr)