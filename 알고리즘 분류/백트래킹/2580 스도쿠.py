import sys
input = sys.stdin.readline

def check_row(x, y):
    for i in range(9):
        if arr[x][i] == arr[x][y] and i!=y:
            return False
    return True

def check_col(x, y):
    for i in range(9):
        if arr[i][y] == arr[x][y] and i!=x:
            return False
    return True

def check_cube(x, y):
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3+3):
            if arr[i][j] == arr[x][y] and (i!=x and j!=y):
                return False
    return True

def backtracking(k=0):
    if k >= len(arr_zeros):
        for i in arr:
            print(' '.join(map(str, i)))
        exit()

    for i in range(1, 10):
        x, y = arr_zeros[k]
        arr[x][y] = i
        if check_row(x, y) and check_col(x, y) and check_cube(x, y):
            backtracking(k+1)
        arr[x][y] = 0
            
arr = []
arr_zeros = []

for i in range(9):
    arr.append([])
    for j, k in enumerate(list(map(int, input().split()))):
        if not k: arr_zeros.append((i, j))
        arr[i].append(k)

backtracking()