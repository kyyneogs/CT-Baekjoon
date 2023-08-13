import sys
arr = [1,1,2,2,2,8]
N = list(map(int, sys.stdin.readline().split()))
for i,j in enumerate(N): arr[i]=arr[i]-j
print(*arr)