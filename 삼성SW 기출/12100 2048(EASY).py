import sys, copy
input = sys.stdin.readline

def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1,N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp

                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1

                else:
                    pointer += 1
                    board[i][pointer] = tmp
    return board

def right(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp

                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1

                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

def up(board):
    for i in range(N):
        pointer = 0
        for j in range(1,N):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0

                if board[pointer][i] == 0:
                    board[pointer][i] = tmp
                
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer += 1

                else:
                    pointer += 1
                    board[pointer][i] = tmp
    return board

def down(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0

                if board[pointer][i] == 0:
                    board[pointer][i] = tmp
                
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer -= 1
                
                else:
                    pointer -= 1
                    board[pointer][i] = tmp
    return board

def bktrack(layer, arr):
    global ans
    if layer == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i==0:
            bktrack(layer+1, left(copy_arr))
        elif i==1:
            bktrack(layer+1, right(copy_arr))
        elif i==2:
            bktrack(layer+1, up(copy_arr))
        else:
            bktrack(layer+1, down(copy_arr))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

bktrack(0, arr)
print(ans)