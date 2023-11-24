import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N = int(input())
board = []
arr = set()
for i in range(N):
    line = list(map(int, input().split()))
    for j in set(line):
        arr.add(j)
    board.append(line)
arr.add(0)

def BFS(x, y):
    visited[x][y] = 1
    que = deque([(x, y)])

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx, ny))

maxi = 0
for i in arr:
    visited = [[0]*N for _ in range(N)]
    stack = []
    cnt = 0

    for x in range(N):
        for y in range(N):
            if board[x][y] <= i:
                visited[x][y] = 1
            else:
                stack.append((x, y))

    for x, y in stack:
        if not visited[x][y]:
            BFS(x, y)
            cnt += 1
    
    maxi = max(maxi, cnt)

print(maxi)