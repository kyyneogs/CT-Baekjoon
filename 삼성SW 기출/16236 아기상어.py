import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sharkSize = 2
sharkEat = 0
sharkLoc = [-1, -1]
timeCount = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sharkLoc = [i, j]
            arr[i][j] = 0

def bfs(x, y):
    que, fishList = deque(), []
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    que.append((x,y))

    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if not visited[nx][ny] and (arr[nx][ny] <= sharkSize):
                visited[nx][ny] = visited[x][y]+1
                que.append((nx,ny))
                if arr[nx][ny] and arr[nx][ny] < sharkSize:
                    fishList.append((visited[nx][ny]-1, nx, ny))

    fishList.sort(key = lambda x:(x[0],x[1], x[2]))
    return fishList

while True:
    fishList = bfs(sharkLoc[0], sharkLoc[1])
    if not fishList:
        break

    time, sx, sy = fishList[0]
    sharkEat += 1
    if sharkEat == sharkSize:
        sharkSize += 1
        sharkEat = 0
    sharkLoc = [sx, sy]
    timeCount += time
    arr[sx][sy] = 0

print(timeCount)