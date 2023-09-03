import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
table = [input().rstrip() for _ in range(N)] 

for x, i in enumerate(table):
    for y, j in enumerate(i):
        if j=='R': rx, ry = x, y
        if j=='B': bx, by = x, y

def tilt(dx, dy, x, y):
    cnt = 0
    while(table[x+dx][y+dy] != '#' and table[x][y] != 'O'):
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def DFS(rx, ry, bx, by):
    que = deque()
    visited = set()
    que.append((rx, ry, bx, by))
    visited.add((rx, ry, bx, by))
    depth = 0
    while que:
        cycle = len(que)
        for _ in range(cycle):
            rx, ry, bx, by = que.popleft()
            if depth > 10:
                print(-1)
                return
            if table[rx][ry] == 'O':
                print(depth)
                return
            for i in range(4):
                rnx, rny, rcnt = tilt(dx[i], dy[i], rx, ry)
                bnx, bny, bcnt = tilt(dx[i], dy[i], bx, by)
                if table[bnx][bny] == 'O':
                    continue
                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx, rny = rnx - dx[i], rny - dy[i]
                    else:
                        bnx, bny = bnx - dx[i], bny - dy[i]
                if (rnx, rny, bnx, bny) not in visited:
                    que.append((rnx, rny, bnx, bny))
                    visited.add((rnx, rny, bnx, bny))
        depth += 1
    print(-1)

DFS(rx, ry, bx, by)