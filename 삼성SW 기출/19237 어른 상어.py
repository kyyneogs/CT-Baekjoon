N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

shark = [[0,0] for _ in range(M)]
directions = list(map(int, input().split()))

priorities = []
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

smell = [[[0,0]]* N for _ in range(N)]

def spread():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if board[i][j]!= 0:
                smell[i][j] = [board[i][j], K]

def move(cnt):
    simul_board = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                direct = directions[board[x][y]-1]
                found = False
                for index in priorities[board[x][y]-1][direct-1]:
                    nx = x + dx[index - 1]
                    ny = y + dy[index - 1]

                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue

                    if smell[nx][ny][1] == 0:
                        directions[board[x][y]-1] = index

                        if simul_board[nx][ny] == 0:
                            simul_board[nx][ny] = board[x][y]
                        else:
                            simul_board[nx][nx] = min(simul_board[nx][ny], board[x][y])
                            cnt -= 1
                        
                        found = True
                        break
                
                if found:
                    continue

                for index in priorities[board[x][y]-1][direct-1]:
                    nx = x + dx[index - 1]
                    ny = y + dy[index - 1]
                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue

                    if smell[nx][ny][0] == board[x][y]:
                        directions[board[x][y]-1] = index
                        simul_board[nx][nx] = board[x][y]
                        break
    return simul_board, cnt

result = 0
cnt = M

while(True):
    spread()
    simul_board, cnt = move(cnt)
    board = simul_board
    result += 1

    if not cnt:
        print(result)
        break

    if result >= 1000:
        print(-1)
        break