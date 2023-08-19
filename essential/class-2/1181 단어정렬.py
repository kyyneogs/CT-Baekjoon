import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

arr = list(set(arr))
arr.sort()
arr.sort(key = lambda x: len(x))

for i in arr:
    print(i)