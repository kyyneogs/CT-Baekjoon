from copy import deepcopy
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
runner = [[[] for _ in range(N)] for _ in range(N)]
runner_loc = [[] for _ in range(M+1)]
cnt = 0

for i in range(1,M+1):
    tx, ty = map(lambda x:int(x)-1, input().split())
    runner[tx][ty].append(i)
    runner_loc[i] = [tx, ty]
tx, ty = map(lambda x:int(x)-1, input().split())
board[tx][ty] = -1
exiti = [tx, ty]

def move():
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(1,M+1):
        x, y = runner_loc[i]
        if board[x][y] == -1:   # 이미 탈출한 녀석이면 안합니드아..
            continue
        drc = 0
        mini = int(10e9)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            tmp = abs(nx-exiti[0]) + abs(ny-exiti[1])
            if tmp < mini:
                drc = d
                mini = tmp
        nx = x + dx[drc]
        ny = y + dy[drc]
        if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] > 0:
            continue
        cnt += 1
        runner_loc[i] = [nx, ny]
        # runner[nx][ny], runner[x][y] = runner[x][y], []
        runner[nx][ny].extend(runner[x][y])
        runner[x][y] = []

def find_box(s_x, s_y, size):
    flag_runner, flag_exit = False, False
    for x in range(s_x, s_x+size):
        for y in range(s_y, s_y+size):
            # if [x,y] in runner_loc: flag_runner = True
            if runner[x][y] and [x,y] != exiti: flag_runner = True
            if [x,y] == exiti: flag_exit = True
    if flag_runner and flag_exit:
        return True
    return False

def find_mini_box():
    for size in range(2, N+1):
        for s_x in range(N):
            for s_y in range(N):
                f_x, f_y = s_x + size, s_y + size
                if f_x > N or f_y >N:
                    break
                if find_box(s_x, s_y, size):
                    return s_x, s_y, size

def rotation(s_x, s_y, size):
    global exiti
    new_board = [[0]*N for _ in range(N)]
    new_runner = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(s_x, s_x+size):
        for y in range(s_y, s_y+size):
            ox, oy = x - s_x, y - s_y
            nx, ny = oy, size - ox - 1

            new_board[s_x+nx][s_y+ny] = board[x][y] if board[x][y] <= 0 else board[x][y]-1
            new_runner[s_x+nx][s_y+ny] = runner[x][y]

    for x in range(s_x, s_x+size):
        for y in range(s_y, s_y+size):
            board[x][y] = new_board[x][y]
            if board[x][y] == -1: exiti = [x,y]
            runner[x][y] = new_runner[x][y]
            if runner[x][y]:
                for i in runner[x][y]:
                    runner_loc[i] = [x,y]

def check_exit():
    if len(runner[exiti[0]][exiti[1]]) == M:
        return True
    return False

def draw():
    print('')
    for i in board:
        print(*i)
    print('')
    for i in runner:
        print(*i)
    print('')
    print(runner_loc, exiti)

for _ in range(K):
    move()
    check_exit()
    if check_exit():
        break
    a, b, c = find_mini_box()
    rotation(a,b,c)

print(cnt)
print(exiti[0]+1, exiti[1]+1)