import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]
starting = []
for i in range(N):
    for k,j in enumerate(input().rstrip()):
        board[i].append(int(j))
        if j=='1':
            starting.append((i,k))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]

def BFS(sx, sy):
    stack = []
    que = deque()
    que.append((sx,sy))
    cnt = 0
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if not board[nx][ny] and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                que.append((nx, ny))
                stack.append((nx, ny))
    for x, y in stack:
        visited[x][y] = cnt

def solution(sx, sy):
    cost = 1
    for i in range(4):
        nx, ny = sx+dx[i], sy+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if visited[nx][ny]:
            cost += visited[nx][ny]
        else:
            BFS(nx, ny)
    board[sx][sy] = cost
    


for x,y in starting:
    solution(x,y)

for j in board:
    print(*j)