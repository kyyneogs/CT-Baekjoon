from copy import deepcopy
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
runner = [[[] for _ in range(N)] for _ in range(N)]
runner_set = set()
cnt = 0

for i in range(1,M+1):
    tx, ty = map(lambda x:int(x)-1, input().split())
    runner[tx][ty].append(i)
    runner_set.add((tx,ty))
tx, ty = map(lambda x:int(x)-1, input().split())
board[tx][ty] = -1
exiti = [tx, ty]

def move():
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tmp_runner_set = deepcopy(runner_set)
    for x, y in tmp_runner_set:
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
        runner_set.remove((x,y))
        runner_set.add((nx, ny))
        runner[nx][ny], runner[x][y] = runner[x][y], []

def find_box(s_x, s_y, size):
    flag_runner, flag_exit = False, False
    for x in range(s_x, s_x+size):
        for y in range(s_y, s_y+size):
            if (x,y) in runner_set: flag_runner = True
            if [x,y] == exiti: flag_exit = True
    if flag_runner and flag_exit:
        return True
    return False

def find_mini_box():
    for size in range(2, N+1):
        for s_x in range(N):
            for s_y in range(N):
                f_x, f_y = s_x + size, s_y + size
                if f_x >= N or f_y >=N:
                    break
                if find_box(s_x, s_y, size):
                    return s_x, s_y, size

def rotation(s_x, s_y, size):
    global exiti
    new_board = deepcopy(board)
    new_runner = deepcopy(runner)
    for x in range(s_x, s_x+size):
        for y in range(s_y, s_y+size):
            nx, ny = s_x + y, s_x+size - x - 1
            new_board[nx][ny] = board[x][y]
            if new_board[nx][ny] > 0:
                new_board[nx][ny] -= 1
            if new_board[nx][ny] == -1:
                exiti = [nx, ny]
            
            new_runner[nx][ny] = runner[x][y]
            if new_runner[nx][ny]:
                runner_set.remove((x,y))
                runner_set.add((nx, ny))
    return new_board, new_runner

def check_exit():
    global runner_set
    new_runner_set = deepcopy(runner_set)
    for x, y in runner_set:
        if [x,y] == exiti:
            runner[x][y] = []
            new_runner_set.remove((x,y))
    runner_set = new_runner_set

for _ in range(K):
    move()
    check_exit()
    if not runner_set:
        break
    a, b, c = find_mini_box()
    board, runner = rotation(a,b,c)

print(cnt)
print(exiti[0]+1, exiti[1]+1)