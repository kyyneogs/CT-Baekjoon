from collections import deque

N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1,-1,0,0]

sx, sy = map(int, input().split())

listbook = {}
for _ in range(M):
    px, py, kx, ky = map(int, input().split())
    listbook[(px-1, py-1)] = [kx-1, ky-1]
    
def check(x,y):
    if 0<=x<N and 0<=y<N and not board[x][y]: return True
    else: return False

def bfs(cnt, start, dest=0):
    sx, sy = start
    if not dest and (sx, sy) in listbook:
        return sx, sy, 0
    que, visited = deque(), [[-1]*N for _ in range(N)]
    visited[sx][sy] = 0
    que.append([sx,sy])
    stack = []

    while(que and cnt):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not check(nx, ny) or visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            que.append([nx,ny])

            if dest:
                if [nx, ny] == dest:
                    listbook.pop((sx, sy))
                    return nx, ny, visited[nx][ny]
            
            else:
                if (nx, ny) in listbook:
                    cnt -= 1
                    stack.append([nx, ny, visited[nx][ny]])
    stack.sort(key = lambda x : (x[2], x[0], x[1]))
    if stack: return stack[0]
    else:
        print(-1)
        exit()

x, y = sx-1, sy-1

while(M>0):
    x, y, dis = bfs(M, [x, y])
    F -= dis
    if F<0:
        print(-1)
        exit()
    
    x, y, dis = bfs(M, [x, y], listbook[(x,y)])
    F -= dis
    M -= 1
    if F<0:
        print(-1)
        exit()
    F += dis*2

print(F)