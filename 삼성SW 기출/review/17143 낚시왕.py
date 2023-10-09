R, C, M = map(int, input().split()) # x, y, 상어 수
board = [[[] for _ in range(C)] for _ in range(R)]
shark_map = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(M):
    r, c, s, d, z = map(int, input().split()) # x, y, 스피드, 방향, 크기
    board[r-1][c-1].append([s, d-1, z])
    shark_map.append([r-1,c-1,s,d-1,z])

def move(board):

    simul_board = [[[] for _ in range(C)] for _ in range(R)]
    simul_stack = []

    for i in range(R):
        for j in range(C):
            while board[i][j]:
                simul_stack.append([i,j]+board[i][j].pop())
    
    while(simul_stack):
        x, y, s, d, z = simul_stack.pop()

        distance = s
        while(distance):
            x += dx[d]
            y += dy[d]
            if not 0<=x<R or not 0<=y<C:
                x -= dx[d]
                y -= dy[d]
                if d < 2: d = (d+1)%2
                else: d = (d+1)%2 + 2
                break
            distance -= 1
        
        if distance:
            if d<2: wall = R - 1
            else: wall = C - 1

            location = [[i for i in range(wall)], [i for i in range(wall, 0, -1)]]
            t = 0 if 0<d<3 else 1
            k = (distance // wall + t) % 2

            l = distance % wall

            if d<2:
                x = location[k][l]
                d = (k+1)%2 
            else:
                y = location[k][l]
                d = k+2
        
        simul_board[x][y].append([s,d,z])

    for i in range(R):
        for j in range(C):
            if len(simul_board[i][j]) > 1:
                simul_board[i][j].sort(key = lambda x:-(x[2]))
                while(len(simul_board[i][j])>1):
                    simul_board[i][j].pop()

    return simul_board

def catch(board, col):
    for row in range(R):
        if board[row][col]:
            tmp = board[row][col][0]
            board[row][col].pop()
            return tmp[2]
    return 0

start = -1
result = 0
for _ in range(C):
    start += 1
    result += catch(board, start)
    board = move(board)

print(result)

# print(move(new_map))


# R = 5
# C = 7
# distance = 9
# d = 2
# if d<2: wall = R
# else: wall = C

# k = (distance // wall + d%2) % 2
# l = distance % wall

# location = [[i for i in range(wall)], [i for i in range(wall, 0, -1)]]
# print(location[k][l])