from collections import deque
from copy import deepcopy
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def init_rainbow():
    for i in range(N):
        for j in range(N):
            if board[i][j]==0: rainbow_list.append([i,j])

def reset_rainbow():
    for x, y in rainbow_list:
        visited[x][y] = 0

def gravity():
    for i in range(N):
        pointer = N-1
        for j in range(N-2,-1,-1):
            tmp = board[j][i]
            if tmp == -2:
                continue
            if tmp == -1:
                pointer = j
                continue
            board[j][i] = -2
            if board[pointer][i] == -2:
                board[pointer][i] = tmp
                pointer -= 1
            else:
                pointer -= 1
                board[pointer][i] = tmp

def rotate():
    global board
    new_board = []
    for i in range(N-1, -1, -1):
        line = []
        for j in range(N):
            line.append(board[j][i])
        new_board.append(line)
    board = deepcopy(new_board)

def check(nx, ny, block):
    if nx<0 or nx>=N or ny<0 or ny>=N:
        return False
    
    if visited[nx][ny] or board[nx][ny] < 0:
        return False
    
    return True
 
def bfs(start_block, x, y):
    chain_stack = [[x,y]]
    que = deque()
    visited[x][y] = 1
    cnt, rcnt = 1, 0
    que.append([x,y])
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if not check(nx, ny, start_block):
                continue
            if board[nx][ny] == 0:
                rcnt += 1
                cnt += 1
            elif board[nx][ny] == start_block:
                cnt += 1
            else:
                continue

            visited[nx][ny] = 1
            que.append([nx, ny])
            chain_stack.append([nx, ny])
    return cnt, rcnt, chain_stack

def calculate():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                cnt, rcnt, s = bfs(board[i][j], i, j)
                if len(s) > 1:
                    stack.append([cnt, rcnt, s])
                reset_rainbow()
    if stack:
        stack.sort(key = lambda x : (-x[0], -x[1], -x[2][0][0], -x[2][0][1]))
        cnt, _, s = stack[0]
        for i, j in s:
            board[i][j] = -2
        return cnt
    return 0

score = 0

while(True):
    visited = [[0]*N for _ in range(N)]
    rainbow_list = []
    stack = []
    init_rainbow()
    tmp = calculate()
    if not tmp: 
        break
    score += tmp**2
    gravity()
    rotate()
    gravity()

print(score)


# # stack = [[0,1], [1,2]]
# # stack.sort(key = lambda x: (-len(x), -x[0], -x[1]))
# # print(stack)

# stack = [[2, 0, [[0, 4], [0, 5]]], [2, 0, [[5, 3], [5, 4]]]]
# stack.sort(key = lambda x:(-x[2][0][0]))