N = int(input())
board = [[0]*101 for _ in range(101)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

for i in range(N):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1

    curve = [d]

    for j in range(g):
        for k in range(len(curve)-1,-1,-1):
            curve.append((curve[k]+1)%4)
    
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        board[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1] == 4:
            cnt += 1
print(cnt)