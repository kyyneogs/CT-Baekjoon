from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
board = []
board.append(deque(list(map(int, input().split()))))

def push_one():
    mini = min(board[0])
    for i in range(N):
        if board[0][i] == mini: board[0][i] += 1

def line_to_spiral():
    if len(board[-1]) == N:
        tmp = board[0].popleft()
        board.append(deque([tmp]))
        return True
    len_pop = len(board[-1])
    new_pop = [[] for _ in range(len_pop)]
    if len(board[0]) - len(board[-1]) < len(board): # 대가리가 몸통보다 큰 경우
        return False
    for i in range(len_pop-1, -1, -1):
        tmp = []
        for j in range(len(board)):
            pop = board[j].popleft()
            tmp.append(pop)
        new_pop[i] = tmp
    while(len(board) > 1): board.pop()
    for k in range(len_pop): board.append(deque(new_pop[k]))
    return True

def distribute():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    table = [[0]*len(board[0]) for _ in range(len(board))]

    for x in range(len(board)):
        for y in range(len(board[x])):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[nx]):
                    continue
                if board[nx][ny] > board[x][y]:
                    tmp = (board[nx][ny] - board[x][y]) // 5
                    table[nx][ny] -= tmp
                else:
                    tmp = (board[x][y] - board[nx][ny]) // 5
                    table[nx][ny] += tmp
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] += table[x][y]

def spiral_square_to_line():
    new_line = []
    cycle = len(board[0])
    for _ in range(cycle):
        tmp = []
        for j in range(len(board)):
            if board[j]:
                tmp.append(board[j].popleft())
        new_line.extend(tmp)
    while(board): board.pop() # board 지움.
    board.append(deque(new_line))

def line_to_square():
    T = len(board[0])
    new_line = []
    for i in range(len(board)-1, -1, -1):
        tmp = []
        for _ in range(T//2):
            tmp.append(board[i].popleft())
        new_line.append(tmp[-1::-1])
    for line in new_line:
        board.append(deque(line))

mini = int(10e9)
cnt = 0
while(mini > K):
    cnt += 1
    push_one()
    while(True):
        if not line_to_spiral():
            break
    distribute()
    spiral_square_to_line()
    line_to_square()
    line_to_square()
    distribute()
    spiral_square_to_line()
    mini = max(board[0]) - min(board[0])
print(cnt)