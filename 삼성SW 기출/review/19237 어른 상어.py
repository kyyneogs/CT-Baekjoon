N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
shark_list = [[] for _ in range(M)]
priorities = [[] for _ in range(M)]
smells = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

init_dir = list(map(int, input().split()))

for i in range(M): # 방향 우선순위 초기화
    for _ in range(4):
        a, b, c, d = map(int, input().split())
        priorities[i].append([a-1, b-1, c-1, d-1])

for i in range(N): # 샤크 리스트 동기화
    for j in range(N):
        if board[i][j]:
            shark_list[board[i][j]-1] = [i,j, init_dir[board[i][j]-1]-1]

def check(nx, ny):
    if nx<0 or nx >= N or ny<0 or ny>=N: 
        return False
    return True

def move():
    global cnt
    for i in range(M):
        if not shark_list[i]:
            continue
        flag = False
        x, y, d = shark_list[i]
        board[x][y] = 0
        for d_i in priorities[i][d]:
            nx = x+dx[d_i]
            ny = y+dy[d_i]
            if not check(nx, ny) or smells[nx][ny]:
                continue
            if board[nx][ny]:
                shark_list[i] = []
                cnt -= 1
            else:
                board[nx][ny] = i+1
                shark_list[i] = [nx, ny, d_i]
            flag = True
            break

        if not flag:
            for d_i in priorities[i][d]:
                nx = x+dx[d_i]
                ny = y+dy[d_i]
                if not check(nx, ny):
                    continue
                if smells[nx][ny][0] == i+1:
                    board[nx][ny] = i+1
                    shark_list[i] = [nx, ny, d_i]
                    break

def update_smell():
    for i in range(N):
        for j in range(N):
            if smells[i][j]:
                smells[i][j][1] -= 1
                if smells[i][j][1] == 0:
                    smells[i][j] = []
            if board[i][j]:
                smells[i][j] = [board[i][j], K]

cnt = M
for i in range(1000):
    update_smell()
    move()
    if cnt==1:
        print(i+1)
        exit()
print(-1)