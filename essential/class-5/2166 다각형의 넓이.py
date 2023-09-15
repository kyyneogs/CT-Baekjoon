import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.append(arr[0])

x, y = 0, 0
for i in range(N):
    x += arr[i][0] * arr[i+1][1]
    y += arr[i][1] * arr[i+1][0]

print(round((x+y)/2, 2))