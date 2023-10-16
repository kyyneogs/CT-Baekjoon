from copy import deepcopy

N = 4
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
fishMap =[[[] for _ in range(N)] for _ in range(N)]
fishSet = [[] for _ in range(N**2+1)]

for row in range(N):
    line = list(map(int, input().split()))
    for col in range(0,2*N,2):
        fishMap[row][col//2] = [line[col], line[col+1]-1]

for tx in range(N):
    for ty in range(N):
        idx, _ = fishMap[tx][ty]
        fishSet[idx] = [tx, ty]

def move(fishMap, fishSet):
    for idx in range(1,N**2+1):
        if not fishSet[idx]:
            continue
        x, y = fishSet[idx]
        drc = fishMap[x][y][1]
        for d in range(8):
            n_drc = (drc + d)%8
            nx = x + dx[n_drc]
            ny = y + dy[n_drc]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if [nx, ny] == shark:
                continue
            
            fishSet[idx] = [nx, ny]
            fishMap[x][y][1] = n_drc
            if fishMap[nx][ny]:
                fishSet[fishMap[nx][ny][0]] = [x, y]
                fishMap[x][y], fishMap[nx][ny] = fishMap[nx][ny], fishMap[x][y]
            else:
                fishMap[x][y], fishMap[nx][ny] = [], fishMap[x][y]
            break
        else:
            continue

def eatFish(fishMap, fishSet, sharkInfo, point):
    global maxi
    maxi = max(maxi, point)
    cFishMap = fishMap
    cFishSet = fishSet
    move(cFishMap, cFishSet)

    x, y, drc = sharkInfo
    nx, ny = x, y
    for _ in range(3):
        nx, ny = nx+dx[drc], ny+dy[drc]
        if 0<=nx<N and 0<=ny<N and cFishMap[nx][ny]:
            idx, f_drc = cFishMap[nx][ny]
            cFishMap[nx][ny] = []
            cFishSet[idx] = []
            draw(cFishMap)
            eatFish(deepcopy(cFishMap), deepcopy(cFishSet), [nx, ny, f_drc], point+idx)
            cFishMap[nx][ny] = [idx, f_drc]
            cFishSet[idx] = [nx, ny]

def draw(fishMap):
    print('')
    for i in fishMap:
        print(*i)

maxi = 0
shark = [0, 0]
point, sharkDir = fishMap[0][0]
fishSet[fishMap[0][0][0]] = []
fishMap[0][0] = []
eatFish(fishMap, fishSet, [0,0,sharkDir], point)
print(maxi)
