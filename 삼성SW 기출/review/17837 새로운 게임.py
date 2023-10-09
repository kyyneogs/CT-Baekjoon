N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
horse = []

for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)

# left-right-up-down
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def turn(d):
    if d==0 or d==2: return d+1
    else: return d-1

def simulation(horse_num):
    x, y, d = horse[horse_num]
    nx = x + dx[d]
    ny = y + dy[d]

    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
        d = turn(d)
        horse[horse_num][2] = d
        nx = x+dx[d]
        ny = y+dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] == 2:
            return False
    
    horse_stack = []
    for indx, indx_num in enumerate(chess[x][y]):
        if indx_num == horse_num:
            horse_stack.extend(chess[x][y][indx:])
            chess[x][y] = chess[x][y][:indx]
            break
    
    if board[nx][ny] == 1:
        horse_stack = horse_stack[-1::-1]
    
    for i in horse_stack:
        horse[i][0], horse[i][1] = nx, ny
        chess[nx][ny].append(i)
        
    if len(chess[nx][ny]) >= 4:
        return True
    
    return False

for i in range(1000):
    flag = False
    for j in range(K):
        flag += simulation(j)
        if flag:
            print(i+1)
            exit()
print(-1)