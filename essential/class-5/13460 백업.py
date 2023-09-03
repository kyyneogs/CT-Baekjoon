import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
table = [input().rstrip() for _ in range(N)] 
visited = [[0 for _ in range(M)] for _ in range(N)]

for x, i in enumerate(table):
    for y, j in enumerate(i):
        if j=='R': R = (x,y)
        elif j=='B': B = (x,y)
        elif j=='O': O = (x,y)

def tilt(dx, dy, x, y):
    nx, ny = x+dx, y+dy
    while(table[nx][ny] != '#'):
        visited[nx][ny] = visited[x][y] + 1
        nx, ny = nx+dx, ny+dy
    return nx-dx, ny-dy

def BFS(start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que = deque()
    visited[start[0]][start[1]] = 1
    que.append(start)
    while(que):
        x, y = que.popleft()
        for i in range(4):
            if not visited[x+dx[i]][y+dy[i]]:
                cx, cy = tilt(dx[i], dy[i], x, y)
            if cx!=x or cy!= y:
                que.append((cx,cy))

BFS(R)

for i in visited:
    print(*i)