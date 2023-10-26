import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*10000001
arrSet = set()
for _ in range(N):
    t = int(input())
    arr[t] += 1
    arrSet.add(t)

arrSet = sorted(list(arrSet))
for i in arrSet:
    for _ in range(arr[i]):
        print(i)