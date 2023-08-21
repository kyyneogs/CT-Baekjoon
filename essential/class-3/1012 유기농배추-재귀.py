import sys
sys.setrecursionlimit(10000)

def search(x, y):
    if x<=-1 or x >=m or y <= -1 or y>=n:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        search(x+1,y)
        search(x, y+1)
        search(x-1, y)
        search(x, y-1)
        return True
    return False

test_case = int(sys.stdin.readline())
for i in range(test_case):
    worm = 0
    m, n, cab = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]
    cab_arr = []
    for j in range(cab):
        x, y = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
        cab_arr.append([x, y])
    
    for k in cab_arr:
        if search(k[0],k[1]) == True:
            worm += 1
    print(worm)