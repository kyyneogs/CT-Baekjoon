import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(set(arr))

cord = {}
for i, j in enumerate(arr_sort):
    cord[j] = i

for i in range(n):
    print(cord[arr[i]], end=' ')