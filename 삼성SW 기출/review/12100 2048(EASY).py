from copy import deepcopy

# 시작시간 : 13:18 종료시간 : 14: ~~

# 1. 우선 입력을 위한 부분을 설계해야 함.
# N <- 보드 크기.

N = int(input())

# 이후 NxN 사이즈의 보드를 입력받음.

board = [list(map(int, input().split())) for _ in range(N)]
maxi = 0

# 2. 문제 접근 방법 -> '최대' 5번 이동해서 얻을 수 있는 '가장' 큰 값 <= 완전 탐색을 해서 모든 경우의 수를 탐색하라는 의미.
# 완탐 중에서도 재귀를 사용하는 것이 좋다고 판단 ( 최대 재귀의 깊이가 5밖에 안됨. 넓이 우선은 큐를 이용하는데 이해하기 어려울 수 있기 때문.)
# 상, 하, 좌, 우 한번 씩 기우는 경우에 대해서 깊이 우선 탐색을 실시.

def dfs(board, layer=0):
    global maxi
    if layer == 5:
        score = 0
        for i in range(N):
            for j in range(N):
                score = max(score, board[i][j])
        
        maxi = max(score, maxi)
        return
    
    simul_board = deepcopy(board)
    for i in range(4):
        simul_board = deepcopy(board)
        if i==0: left(simul_board)
        elif i==1: right(simul_board)
        elif i==2: up(simul_board)
        else: down(simul_board)
        dfs(simul_board, layer+1)

# 실질적으로 보드를 움직이는 작업을 처리하는 함수.
# 방향과 보드 입력값을 받음.
# 이중 포인터의 개념을 사용. 1 포인터는 항상 초기위치 0이고, 기울이는 위치에 따라서 2 포인터 항상 1에서 시작. (2 포인터는 j)
# 2 포인터가 쭉 돌아보면서 빈 곳이면 그냥 패스, 블록이 존재하는 곳이면 옮기기 작업을 실행.
# 상황1. 1포인터의 위치가 비어있는 상태라면 2포인터의 블록을 1포인터 위치로 옮김. 2포인터 블록 삭제. 1포인터 ++ 를 실행하면 안됨 (2포인터에서 또다른 블록을 끌고 올 수 있음)
# 상황2. 1포인터에 블록이 존재. 2포인터와 동일한 숫자의 블록. 2포인터의 블록을 삭제. 1포인터의 블록을 *2, 1포인터 ++ 를 실행 (더이상 1포인터로 블록이 갈수 없음.)
# 상황3. 1포인터의 블록이 존재. 2포인터와 다른 숫자의 블록, 우선 2포인터의 블록 값을 기억하고 삭제, 이후 1포인터 +1 의 위치에 해당 블록을 옮김. 1포인터 ++ 실행
# (더이상 1포인터로는 블록이 갈 수 없음.)

def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if not board[i][j]:
                continue

            tmp = board[i][j]
            board[i][j] = 0

            if not board[i][pointer]:
                board[i][pointer] = tmp
            
            elif board[i][pointer] == tmp:
                board[i][pointer] *= 2
                pointer += 1
            
            else:
                pointer += 1
                board[i][pointer] = tmp

def right(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if not board[i][j]:
                continue

            tmp = board[i][j]
            board[i][j] = 0

            if not board[i][pointer]:
                board[i][pointer] = tmp
            
            elif board[i][pointer] == tmp:
                board[i][pointer] *= 2
                pointer -= 1
            
            else:
                pointer -= 1
                board[i][pointer] = tmp
                

def up(board):
    for i in range(N):
        pointer = 0
        for j in range(1,N):
            if not board[j][i]:
                continue

            tmp = board[j][i]
            board[j][i] = 0

            if not board[pointer][i]:
                board[pointer][i] = tmp
            
            elif board[pointer][i] == tmp:
                board[pointer][i] *= 2
                pointer += 1
            
            else:
                pointer += 1
                board[pointer][i] = tmp

def down(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if not board[j][i]:
                continue

            tmp = board[j][i]
            board[j][i] = 0

            if not board[pointer][i]:
                board[pointer][i] = tmp

            elif board[pointer][i] == tmp:
                board[pointer][i] *= 2
                pointer -= 1
            
            else:
                pointer -= 1
                board[pointer][i] = tmp

dfs(board)
print(maxi)