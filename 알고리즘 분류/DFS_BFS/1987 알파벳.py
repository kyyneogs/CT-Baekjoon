import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

R, C = map(int, input().split())

board = [input().rstrip() for _ in range(R)]

def DFS(x, y, cnt, stack):
    global maxi

    if x<0 or x>=R or y<0 or y>=C or board[x][y] in stack:
        maxi = max(maxi, cnt)
        return
    
    _stack = stack + board[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        DFS(nx, ny, cnt+1, _stack)

maxi = 0

DFS(0, 0, 0, '')

print(maxi)