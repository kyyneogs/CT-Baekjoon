from collections import deque

N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy = map(int, input().split())
dest= {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    dest[(a-1,b-1)] = (c-1,d-1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, lx=-1, ly=-1):
    if (lx==-1 and ly==-1) and (sx,sy) in dest:
        return sx, sy, 0
    flag = False
    visited = [[0]*N for _ in range(N)]
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = 1
    cand = []
    while(que):
        x, y = que.popleft()
        if flag:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if visited[nx][ny] or board[nx][ny] == 1: continue
            visited[nx][ny] = visited[x][y] + 1

            if (lx==-1 and ly==-1):
                if (nx, ny) in dest:
                    cand.append((nx, ny))
                    flag = True
            else:
                if (nx, ny) == dest.get((sx, sy)):
                    dest.pop((sx, sy))
                    return nx, ny, visited[nx][ny]-1

            que.append((nx, ny))
    if cand:
        cand.sort(key = lambda x: (-board[x[0]][x[1]], -x[1], -x[1]))
        x, y = cand.pop()
        board[x][y] = 0
        return x, y, visited[x][y] -1
    else:
        print(-1)
        exit()

x, y = sx-1, sy-1
while(dest):
    x, y, energy = bfs(x, y)
    F -= energy
    if F < 0: break
    x, y, energy = bfs(x, y, dest[(x,y)][0], dest[(x,y)][1])
    F -= energy
    if F < 0: break
    F += energy*2

if F > -1:
    print(F)
else:
    print(-1)