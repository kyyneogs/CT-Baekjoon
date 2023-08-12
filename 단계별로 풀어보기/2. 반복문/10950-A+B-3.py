import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    M1, M2 = map(int, sys.stdin.readline().split(' '))
    arr.append(M1+M2)
for i in arr: print(i)