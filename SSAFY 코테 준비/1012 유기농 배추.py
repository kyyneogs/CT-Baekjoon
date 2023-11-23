import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x,y): 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx,ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    arr = []
    cnt = 0

    for _ in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
        arr.append((b, a))

    for x, y in arr:
        if not visited[x][y]:
            visited[x][y] = 1
            cnt += 1
            DFS(x, y)

    print(cnt)