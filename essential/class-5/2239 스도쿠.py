import sys
input = sys.stdin.readline

def check_row(row, col, num):
    for i in range(N):
        if col!=i and num==sdoku[row][i]:
            return False
    return True

def check_col(row, col, num):
    for i in range(N):
        if row!=i and num==sdoku[i][col]:
            return False
    return True

def check_cube(row, col, num):
    nrow, ncol = (row//3)*3, (col//3)*3
    for i in range(nrow, nrow+3):
        for j in range(ncol, ncol+3):
            if (row!=i and col!=j) and num==sdoku[i][j]:
                return False
    return True

def DFS(depth=0):
    if depth>=len(zeros):
        for i in sdoku:
            print("".join(map(str, i)))
        exit()
    
    nrow, ncol = zeros[depth]
    for i in range(1,N+1):
        if check_row(nrow, ncol, i) and check_col(nrow, ncol, i) and check_cube(nrow, ncol, i):
            sdoku[nrow][ncol] = i
            DFS(depth+1)
            sdoku[nrow][ncol] = 0

N = 9
sdoku, zeros = [], []
for x in range(N):
    line = list(map(int, input().rstrip()))
    for y,i in enumerate(line):
        if not i:
            zeros.append((x,y))
    sdoku.append(line)

DFS()