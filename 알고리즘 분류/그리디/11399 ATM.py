import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
for i in arr: 
    sum = sum + i*N
    N = N-1
print(sum)