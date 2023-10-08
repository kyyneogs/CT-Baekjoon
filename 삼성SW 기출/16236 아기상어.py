from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
size = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x, y = i, j

def bfs(x, y, size):
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    que = deque()
    que.append((x,y))
    visited[x][y] = 1

    temp = []

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
                continue
            if board[nx][ny] <= size:
                que.append((nx,ny))
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if 0< board[nx][ny] < size:
                    temp.append((distance[nx][ny],ny,nx))
    
    return sorted(temp, key = lambda x:(-x[0], -x[1], -x[2]))

result = 0

while(True):
    shark = bfs(x,y,size)
    if not len(shark):
        break

    distance, ky, kx = shark.pop()

    result += distance
    board[x][y], board[kx][ky] = 0,0

    x, y = kx, ky
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)