import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]

que = deque()

def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2: return [i, j]

def BFS(start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que.append(start)
    visited[start[0]][start[1]] = 1

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if not arr[nx][ny]: continue
            if visited[nx][ny]: continue

            visited[nx][ny] = 1
            distance[nx][ny] = distance[x][y]+1
            que.append([nx, ny])

BFS(find_start())

for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            distance[i][j] = -1

for i in distance:
    print(*i)