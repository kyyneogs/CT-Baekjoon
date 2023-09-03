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
    for i in range(0,cnt+1):
        visited[x+dx*i][y+dy*i] = 1

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
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    que = deque()
    que.append((R[0], R[1], B[0], B[1], 1))
    while(que):
        rx, ry, bx, by, depth = que.popleft()
        if depth > 10:
            print(-1)
            return
        for i in range(4):
            if not visited[rx+dx[i]][ry+dy[i]]:
                rnx, rny, rcnt = tilt(dx[i], dy[i], rx, ry)
                bnx, bny, bcnt = tilt(dx[i], dy[i], bx, by)
                if table[bnx][bny] == 'O':
                    continue
                if table[bnx][bny] != 'O' and table[rnx][rny] == 'O':
                    print(depth)
                    return
                
                if rcnt+bcnt>0:
                    if rnx==bnx and rny==bny:
                        if rcnt>bcnt:
                            rnx, rny, rcnt = rnx - dx[i], rny - dy[i], rcnt-1
                        else:
                            bnx, bny, bcnt = bnx - dx[i], bny - dy[i], bcnt-1
                    visit(dx[i], dy[i], rx, ry, rcnt)
                    que.append((rnx, rny, bnx, bny, depth+1))
    print(-1)

BFS(R, B)