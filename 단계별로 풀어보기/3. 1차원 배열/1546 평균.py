import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m, k = max(arr), 0.0
for i in arr: k = k + i/m*100
print(k/N)