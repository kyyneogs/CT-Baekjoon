R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(R):
    if board[i][0] == -1:
        top = i
        bot = i+1
        break

def diffuse():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    simul_board = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if not board[x][y] or board[x][y] == -1:
                continue

            dust = board[x][y] // 5
            tmp = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>=R or ny<0 or ny>=C or board[nx][ny]==-1:
                    continue

                simul_board[nx][ny] += dust
                tmp += dust
            board[x][y] -= tmp
    
    for x in range(R):
        for y in range(C):
            board[x][y] += simul_board[x][y]

def clean_top():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y, d = top, 1, 0
    prev = 0

    while(True):
        nx = x + dx[d%4]
        ny = y + dy[d%4]

        if x==top and y==0:
            break

        if nx<0 or nx>=R or ny<0 or ny>=C:
            d += 1
            continue

        board[x][y], prev = prev, board[x][y]
        x, y = nx, ny

def clean_bot():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = bot, 1, 0
    prev = 0

    while(True):
        nx = x + dx[d%4]
        ny = y + dy[d%4]

        if x==bot and y==0:
            break

        if nx<0 or nx>=R or ny<0 or ny>=C:
            d += 1
            continue

        board[x][y], prev = prev, board[x][y]
        x, y = nx, ny

for _ in range(T):
    diffuse()
    clean_top()
    clean_bot()

print(sum(map(sum, board))+2)