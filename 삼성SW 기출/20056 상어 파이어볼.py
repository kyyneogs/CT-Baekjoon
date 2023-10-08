N, M, K = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    board[x-1][y-1] = [m, s, d]
board[0][0] = []
print(board)