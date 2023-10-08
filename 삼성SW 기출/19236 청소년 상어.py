from copy import deepcopy
board = [[] for _ in range(4)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
maxi = 0

for i in range(4):
    line = list(map(int, input().split()))
    tmp = []
    for j in range(4):
        tmp.append([line[j*2], line[j*2+1] - 1])
    board[i] = tmp

def dfs(sx, sy, score, board):
    global maxi
    score += board[sx][sy][0]
    maxi = max(maxi, score)
    board[sx][sy][0] = 0

    for fish in range(1,17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == fish:
                    f_x, f_y = x, y
                    break
        
        if f_x == -1 and f_y == -1:
            continue

        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i)%8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            if not (0<=nx<4 and 0<=ny<4) or (sx==nx and sy==ny):
                continue

            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break
    
    s_d = board[sx][sy][1]
    for i in range(1,5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i

        if (0<=nx<4 and 0<=ny<4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, deepcopy(board))

dfs(0,0,0,board)
print(maxi)