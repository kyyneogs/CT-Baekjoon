from copy import deepcopy
R, C, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1].append((s, d-1, z))

def move():
    simul = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                x, y = i, j 
                s, d, z = board[i][j][0]
                nx = x + dx[d]
                ny = y + dy[d]
                s_t = s
                while s_t>0:
                    nx = x+dx[d]
                    ny = y+dy[d]

                    if nx<0 or nx>=R or ny<0 or ny>=C:
                        if d in [0, 2]:
                            d += 1
                        else:
                            d -= 1
                        continue
                    else:
                        x, y = nx, ny
                        s_t -= 1
                simul[x][y].append([s,d,z])
    
    for i in range(R):
        for j in range(C):
            board[i][j] = simul[i][j]

cnt = 0

for y in range(C):
    for x in range(R):
        if board[x][y]:
            tmp = board[x][y][0]
            cnt += tmp[2]
            board[x][y].remove(tmp)
            break
    
    move()

    for i in range(R):
        for j in range(C):
            if len(board[i][j])>1:
                board[i][j].sort(reverse=True)
                while(len(board[i][j])>1):
                    board[i][j].pop()

print(cnt)