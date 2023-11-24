import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def BFS(x=0, y=0):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited[x][y] = 1
    que = deque([[x, y]])

    while que:
        x, y = que.popleft()
        if x==N-1 and y==M-1:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny])

BFS()
print(visited[N-1][M-1])