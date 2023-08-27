import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N-1):
    tmp = [0] * (i+2)
    for j, k in enumerate(arr[i]):
        l, r = arr[i+1][j] + k, arr[i+1][j+1] + k
        tmp[j] = l if l>tmp[j] else tmp[j]
        tmp[j+1] = r if r>tmp[j+1] else tmp[j+1]
    arr[i+1] = tmp
print(max(arr[N-1]))