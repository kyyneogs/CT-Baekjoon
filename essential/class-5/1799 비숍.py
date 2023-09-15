import sys
input = sys.stdin.readline

def check(x, y, flag):
    dx = x+y
    dy = 0
    k = dx - N + 1

    if k > 0:
        dx -= k
        dy += k
    
    for _ in range(N-abs(k)):
        check_board[dx][dy] = flag
        dx -= 1
        dy += 1

def DFS():
    pass

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check_board = [[True]*N for _ in range(N)]