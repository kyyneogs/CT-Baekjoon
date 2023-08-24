import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    for initial in start:
        que.append(initial)

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < N and 0<= ny<M and not arr[nx][ny]:
                if arr[nx][ny]==0:
                    que.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1 

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start = []
for i in range(N):
    for j in range(M):
        if arr[i][j] ==1:
            start.append([i,j])

BFS(start)
find = True

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            find=False
            break

if find:
    print(max(max(arr))-1)
else:
    print('-1')