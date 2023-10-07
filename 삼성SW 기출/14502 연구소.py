from copy import deepcopy
from collections import deque

def bfs(cnt):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    que = deque(virus_start)
    simul_board = deepcopy(board)

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if not simul_board[nx][ny]:
                simul_board[nx][ny] = 2
                que.append((nx,ny))
                cnt -= 1

    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

virus_start = []
buildable = []
cnt, maxi = 0, 0

for i in range(N):
    for j in range(M):
        if not board[i][j]:
            buildable.append((i,j))
            cnt += 1

        elif board[i][j] == 2:
            virus_start.append((i,j))

for i in range(len(buildable)-2):
    board[buildable[i][0]][buildable[i][1]] = 1

    for j in range(i+1, len(buildable)-1):
        board[buildable[j][0]][buildable[j][1]] = 1

        for k in range(j+1, len(buildable)):
            board[buildable[k][0]][buildable[k][1]] = 1
            maxi = max(maxi, bfs(cnt-3))
            board[buildable[k][0]][buildable[k][1]] = 0

        board[buildable[j][0]][buildable[j][1]] = 0

    board[buildable[i][0]][buildable[i][1]] = 0

print(maxi)