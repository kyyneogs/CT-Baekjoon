import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x:(x[1], x[0]))
answer = 1
tmp = arr[0][1]
for i in range(1,N):
    if arr[i][0] >= tmp:
        answer += 1
        tmp = arr[i][1]

print(answer)