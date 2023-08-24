import sys
from collections import deque
input = sys.stdin.readline

que = deque([])
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] ==1:
            que.append([i,j])

def BFS():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx <N and 0<= ny <M and arr[nx][ny]==0:
                que.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1 

BFS()
result = 0
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result-1)


# 이거 마지막 출력부때문에 문제가 있네.
# 한번 마지막 결과 출력하는 부분을 수정해봐야 할 듯 함.

# find = True
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             find=False
#             break
#     if not find: break

# if find:
#     result = max(max(arr))-1
# else:
#     result = -1
# print(result)