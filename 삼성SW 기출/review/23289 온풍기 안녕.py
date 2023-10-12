from collections import deque

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [list(map(int, input().split())) for _ in range(W)]

# 0:right, 1:left, 2:up, 3:down
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def init_board():
    t_heaters = []
    t_searchs = []
    t_walls = [[[0]*4 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if 0<board[r][c]<5: t_heaters.append((r,c, board[r][c]-1))
            elif board[r][c]==5: t_searchs.append((r,c))
    for r, c, t in walls:
        r, c = r-1, c-1
        if t==0: # 현재위치의 up, up 위치의 down
            t_walls[r][c][2], t_walls[r-1][c][3] = 1, 1
        else:   # 현재위치의 right, right위치의 left
            t_walls[r][c][0], t_walls[r][c+1][1] = 1, 1
    return t_heaters, t_searchs, t_walls

def check_wall(x, y, drc):
    nx, ny = x + dx[drc], y + dy[drc]
    if walls[x][y][drc] == 1:
        return False
    if nx<0 or nx>=R or ny<0 or ny>=C:
        return False
    return True

def spread(x, y, drc):
    visited = [[0]*C for _ in range(R)]
    que, depth = deque(), 5
    x, y = x + dx[drc], y + dy[drc]
    if x<0 or x>=R or y<0 or y>=C:
        return visited
    hori = [[2, 3], [1,0]]
    visited[x][y] = depth
    que.append((x, y))

    while(que):
        x, y = que.popleft()
        if visited[x][y] == 1: continue
        for i in range(3):
            nx, ny = x, y
            if i<2:
                h_drc = hori[drc//2][i]
                if not check_wall(x, y, h_drc):
                    continue
                nx, ny = x + dx[h_drc], y + dy[h_drc]
            if not check_wall(nx, ny, drc):
                continue
            nx += dx[drc]
            ny += dy[drc]
            if visited[nx][ny]:
                continue
            que.append((nx, ny))
            visited[nx][ny] = visited[x][y] - 1
    return visited

def diffusion():
    new_map = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            for d in range(4):
                if not check_wall(x, y, d):
                    continue
                nx = x + dx[d]
                ny = y + dy[d]
                if board[x][y] > board[nx][ny]:
                    new_map[nx][ny] += (board[x][y] - board[nx][ny]) // 4
                elif board[x][y] < board[nx][ny] :
                    new_map[nx][ny] -= (board[nx][ny] - board[x][y]) // 4
    
    for x in range(R):
        for y in range(C):
            board[x][y] += new_map[x][y]

def edge_diffusion():
    for i in [0, R-1]:
        for j in range(C):
            if board[i][j]:
                board[i][j] -= 1
    for i in range(1,R-1):
        for j in [0, C-1]:
            if board[i][j]:
                board[i][j] -= 1

def copy_board(board1, board2):
    for x in range(R):
        for y in range(C):
            board1[x][y] += board2[x][y]

def check_temp(searchs):
    for x, y in searchs:
        if board[x][y] < K:
            return False
    return True

heaters, searchs, walls = init_board()
board = [[0]*C for _ in range(R)]
for coockies in range(1,102):
    for x, y, drc in heaters:
        new_board = [[0]*C for _ in range(R)]
        new_board = spread(x, y, drc)
        copy_board(board, new_board)
    diffusion()
    edge_diffusion()
    if check_temp(searchs):
        print(coockies)
        exit()
print(coockies)