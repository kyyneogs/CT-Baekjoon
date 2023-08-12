import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
print(arr.count(K))