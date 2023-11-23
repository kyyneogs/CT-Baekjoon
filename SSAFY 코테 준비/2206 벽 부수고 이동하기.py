import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS():
    visited[1][0][0] = 1
    que = deque([(1,0,0)])

    while que:
        w, x, y = que.popleft()
        if x==N-1 and y==M-1:
            return visited[w][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nw = w

            if nx<0 or nx>=N or ny<0 or ny>=M or visited[w][nx][ny]>0:
                continue

            if w==1:
                if board[nx][ny]:
                    nw = 0
                que.append((nw, nx, ny))
                visited[nw][nx][ny] = visited[1][x][y]+1

            elif not board[nx][ny] and not visited[1][nx][ny]:
                que.append((0, nx, ny))
                visited[0][nx][ny] = visited[0][x][y]+1
    return -1

print(BFS())