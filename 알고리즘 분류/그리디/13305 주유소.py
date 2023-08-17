import sys
N = int(sys.stdin.readline())
mile = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    if city[i-1] < city[i]: city[i] = city[i-1]

sum = 0
for i in range(N-1): sum = sum + mile[i]*city[i]
print(sum)