import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

def BFS():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que = deque()
    que.append((0,0,0))
    visited[0][0][0] = 1
    
    while(que):
        z, x, y = que.popleft()

        if x==N-1 and y==M-1:
            return visited[z][x][y]
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if not visited[z][nx][ny] and arr[nx][ny]=='0':
                visited[z][nx][ny] += visited[z][x][y] + 1
                que.append((z,nx,ny))
            elif arr[nx][ny]=='1' and z==0:
                visited[z+1][nx][ny] += visited[z][x][y] + 1
                que.append((z+1,nx,ny))
    return -1
print(BFS())