from copy import deepcopy

def filler(board, direc, x, y):
    cnt = 0
    for i in direc:
        nx = x
        ny = y
        while(True):
            nx += dx[i]
            ny += dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                break

            if board[nx][ny] == 6:
                break

            if not board[nx][ny]:
                board[nx][ny] = -1
                cnt += 1
    return cnt

def dfs(layer, board, cnt):
    global mini
    if layer == len(cctv):
        mini = min(mini, cnt)
        return
    
    simul_board = deepcopy(board)
    ind, x, y = cctv[layer]
    cntk = cnt
    for i in direc[ind]:
        cnt -= filler(simul_board, i, x, y)
        dfs(layer+1, simul_board, cnt)
        simul_board = deepcopy(board)
        cnt = cntk


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mini = int(10e9)
cnt = 0

direc = [
    [],
    [[0],[1],[2],[3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    [[0,1,2,3]]
]

cctv = []
for i in range(N):
    for j in range(M):
        if board[i][j] and board[i][j]!=6:
            cctv.append((board[i][j], i, j))
        elif not board[i][j]:
            cnt += 1

dfs(0, board, cnt)
print(mini)