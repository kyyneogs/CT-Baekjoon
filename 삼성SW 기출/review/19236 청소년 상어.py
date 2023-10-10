from copy import deepcopy
N = 4
maxi = 0

fishes = [[[] for _ in range(N)] for _ in range(N)]
fishes_loc = [[]] + [0] * (N*N)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        fishes[i][j] = [line[2*j], line[2*j+1]-1]
        fishes_loc[line[2*j]] = [i,j]

def turn(x, y, fishes, shark):
    d = fishes[x][y][1]
    for i in range(8):
        nx = x+dx[(d+i)%8]
        ny = y+dy[(d+i)%8]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if shark[0]==nx and shark[1]==ny:
            continue
        return i
    return -1

def move(shark, fishes, fishes_loc):
    for i in range(1,17):
        if not fishes_loc[i]:
            continue
        x, y = fishes_loc[i]
        d = fishes[x][y][1]
        d_i = turn(x, y, fishes, shark)
        if d_i < 0:
            continue
        nx, ny = x+dx[(d+d_i)%8], y+dy[(d+d_i)%8]
        if fishes[nx][ny]:
            fishes_loc[fishes[nx][ny][0]], fishes_loc[i] =  fishes_loc[i], fishes_loc[fishes[nx][ny][0]]
            fishes[nx][ny], fishes[x][y] = fishes[x][y], fishes[nx][ny]
        else:
            fishes_loc[i] = [nx, ny]
            fishes[nx][ny], fishes[x][y] = fishes[x][y], []

def shark_catch(cordi, shark, fishes, fishes_loc):
    kx, ky = cordi
    score = 0
    if fishes[kx][ky]:
        score = fishes[kx][ky][0]
        shark[0], shark[1], shark[2] = kx, ky, fishes[kx][ky][1]
        fishes_loc[score] = []
        fishes[kx][ky] = []
    return score

def dfs(shark, fishes, fishes_loc, score):
    global maxi
    maxi = max(maxi, score)
    move(shark, fishes, fishes_loc)

    nx, ny = shark[0], shark[1]
    for i in range(4):
        nx, ny = nx+dx[shark[2]], ny+dy[shark[2]]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        tmp = shark_catch([nx,ny], shark, fishes, fishes_loc)
        if tmp:
            dfs(deepcopy(shark), deepcopy(fishes), deepcopy(fishes_loc), score+tmp)
    return

fishes_loc[fishes[0][0][0]] = []
shark = [0, 0, fishes[0][0][1]]
score = fishes[0][0][0]
fishes[0][0] = []

dfs(shark, fishes, fishes_loc, score)
print(maxi)