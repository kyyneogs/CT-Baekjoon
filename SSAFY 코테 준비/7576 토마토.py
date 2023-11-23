import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(loc):
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    visited = [[0]*M for _ in range(N)]
    que = deque()
    for x, y in loc:
        visited[x][y] = 1
        que.append((x,y))
    
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if board[nx][ny] == -1 or visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y]+1
            que.append((nx,ny))

    return visited

loc = []
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            loc.append((x,y))

new_board = bfs(loc)

result = 0
for x in range(N):
    for y in range(M):
        if new_board[x][y]==0 and board[x][y]!=-1:
            print(-1)
            exit()
        result = max(result, new_board[x][y]-1)

print(result)