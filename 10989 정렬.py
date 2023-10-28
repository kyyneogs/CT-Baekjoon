import sys
input = sys.stdin.readline

N = int(input())
nDict = {}
for _ in range(N):
    t = int(input())
    if t not in nDict:
        nDict[t] = 1
    else:
        nDict[t] += 1

arr = list(nDict.items())
arr.sort()
for i, j in arr:
    for _ in range(j):
        print(i)