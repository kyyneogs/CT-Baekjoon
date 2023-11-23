T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    board[0][0] = 1
    x, y, d = 0, 0, 0

    while board[x][y] < N**2:
        nx = x + dx[d]
        ny = y + dy[d]
        if (0<=nx<N) and (0<=ny<N) and not board[nx][ny]:
            board[nx][ny] = board[x][y]+1
            x, y = nx, ny
        else:
            d = (d+1)%4

    print(f'#{tc}')
    for i in board:
        print(' '.join(map(str, i)))