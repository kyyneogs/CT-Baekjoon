import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def BFS(x, y):
    cnt = 1
    visited[x][y] = 1
    que = deque([(x, y)])

    while que:
        x, y = que.popleft()
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if board[nx][ny] and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                que.append((nx, ny))
    
    return cnt

cnt = 0
arr = []
for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            arr.append(BFS(i, j))
            cnt += 1

print(cnt)
for i in sorted(arr):
    print(i)