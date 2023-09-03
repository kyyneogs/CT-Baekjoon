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

def visit(dx, dy, x, y, cnt):
    for i in range(cnt):
        visited[x+dx*i][y+dy*i] = visited[x][y] + 1

def tilt(dx, dy, x, y):
    nx, ny, cnt = x+dx, y+dy, 1
    while(table[nx][ny] != '#'):
        if table[nx][ny] == 'O':
            return nx, ny, cnt
        nx += dx
        ny += dy
        cnt += 1
    return nx-dx, ny-dy, cnt-1

def BFS(R, B):
    (rx, ry), (bx, by) = R, B
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que = deque()
    # visited[rx][ry] = 1
    que.append((rx,ry,bx,by))
    while(que):
        rx, ry, bx, by = que.popleft()
        for i in range(4):
            if not visited[rx+dx[i]][ry+dy[i]]:
                rnx, rny, rcnt = tilt(dx[i], dy[i], rx, ry)
                bnx, bny, bcnt = tilt(dx[i], dy[i], bx, by)
                if table[bnx][bny] != 'O' and table[rnx][rny] == 'O':
                    visit(dx[i], dy[i], rx, ry, rcnt)
                    print(visited[rnx][rny])
                    return
                if rnx==bnx and rny==bny:
                    if rcnt>bcnt:
                        rnx, rny, rcnt = rnx - dx[i], rny - dy[i], rcnt-1
                    else:
                        bnx, bny, bcnt = bnx - dx[i], bny - dy[i], bcnt-1
                visit(dx[i], dy[i], rx, ry, rcnt)
                que.append((rnx, rny, bnx, bny))

BFS(R, B)

for i in visited:
    print(*i)