from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = 0
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y, visited):
    que = deque()
    union = []
    que.append((x,y))
    union.append((x,y))

    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
                continue

            if L <= abs(A[nx][ny] - A[x][y]) <= R:
                visited[nx][ny] = 1
                que.append((nx,ny))
                union.append((nx, ny))
    return union

while(True):
    visited = [[0]*N for _ in range(N)]
    flag = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                visited[x][y] = 1
                union = bfs(x,y,visited)
                if len(union) > 1:
                    flag = 1
                    people = sum(A[i][j] for i,j in union) // len(union)
                    for i, j in union:
                        A[i][j] = people
    if not flag:
        break
    result += 1

print(result)