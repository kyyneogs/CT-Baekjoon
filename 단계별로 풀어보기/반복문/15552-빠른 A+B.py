import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N): arr.append(list(map(int, sys.stdin.readline().split(' '))))
for i in arr: print(i[0]+i[1])