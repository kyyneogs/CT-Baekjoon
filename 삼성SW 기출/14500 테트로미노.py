N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
maxi = 0

def dfs(x, y, sumi, layer):
    global maxi

    if layer==4:
        maxi = max(maxi, sumi)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, sumi + board[nx][ny], layer+1)
            visited[nx][ny] = 0

def execpt(x,y):
    global maxi
    for i in range(4):
        sumi = board[x][y]
        for j in range(3):
            k = (i+j)%4
            nx = x+dx[k]
            ny = y+dy[k]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                sumi = 0
                break

            sumi += board[nx][ny]
        
        maxi = max(maxi, sumi)

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0

        execpt(i,j)

print(maxi)