from collections import deque
N, M = map(int, input().split())

board = [input() for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R': rsx, rsy = i, j
        if board[i][j] == 'B': bsx, bsy = i, j

def move(x, y, d):
    cnt, flag = 0, False
    while(board[x+dx[d]][y+dy[d]] != '#'):
        if board[x][y] != 'O':
            flag = True
            break
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt, flag

def check_layer(layer):
    if layer > 10:
        print(-1)
        exit()

def check_rb(rx, ry, bx, by):
    if rx==bx and ry==by:
        return True
    return False

def correction(red_cordi, blu_cordi, d):
    rx, ry, rcnt = red_cordi
    bx, by, bcnt = blu_cordi
    if rcnt > bcnt:
        rx -= dx[d]
        ry -= dy[d]
    else:
        bx -= dx[d]
        by -= dx[d]
    return rx, ry, bx, by

def bfs(red_cordi, blu_cordi):
    rx, ry = red_cordi
    bx, by = blu_cordi
    que = deque()
    visited = set()
    que.append([rx, ry, bx, by])
    visited.add((rx, ry, bx, by))
    layer = 1
    while(que):
        cycle = len(que)
        for _ in range(cycle):
            rx, ry, bx, by = que.popleft()
            check_layer(layer)

            for i in range(4):
                rnx, rny, rcnt, rflag = move(rx, ry, i)
                bnx, bny, bcnt, bflag = move(bx, by, i)

                if bflag==True:
                    continue
                
                if rflag==True:
                    print(layer)
                    return
                
                if check_rb(rnx, rny, bnx, bny):
                    rnx, rny, bnx, bny = correction([rnx, rny, rcnt],[bnx,bny,bcnt],i)
                
                if (rnx, rny, bnx, bny) not in visited:
                    que.append([rnx, rny, bnx, bny, layer+1])
                    visited.add((rnx, rny, bnx, bny))
        layer + 1
    print(-1)

bfs([rsx, rsy], [bsx, bsy])