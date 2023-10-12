from copy import deepcopy

N = 4
M, S = map(int, input().split())
fish_map = [[[] for _ in range(N)] for _ in range(N)]
blood_map = [[0]*N for _ in range(N)]
for _ in range(M):
    x, y, d = map(int, input().split())
    fish_map[x-1][y-1].append(d-1)
shark_loc = list(map(int, input().split()))
shark_loc[0], shark_loc[1] = shark_loc[0]-1, shark_loc[1]-1

def draw():
    print('')
    for i in fish_map:
        print(*i)

def turn(x, y, d, shark_loc):
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    for i in range(8):
        d_i = (d-i)%8
        nx = x + dx[d_i]
        ny = y + dy[d_i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if [nx, ny] == shark_loc or blood_map[nx][ny]:
            continue
        return nx, ny, d_i
    return x, y, -1

def fish_moves(fish_map, shark_loc):
    new_fish_map = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            while fish_map[i][j]:
                direction = fish_map[i][j].pop()
                nx, ny, new_dir= turn(i, j, direction, shark_loc)
                if new_dir<0:
                    new_fish_map[nx][ny].append(direction)
                else:
                    new_fish_map[nx][ny].append(new_dir)
    return new_fish_map

def dfs(loc, visited, score=0, depth=0):
    global maxi, command
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    x, y = loc
    if depth==3:
        if maxi < score:
            maxi = score
            command = deepcopy(visited)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs([nx,ny], visited, score+len(fish_map[nx][ny]), depth+1)
            visited.pop()
        else:
            dfs([nx,ny], visited, score, depth+1)

def shark_moves(sx, sy, blood_map, fish_map):
    global maxi, command
    visited = []
    dfs([sx,sy], visited)
    print(command)
    for nx, ny in command:
        if fish_map[nx][ny]:
            fish_map[nx][ny] = []
            blood_map[nx][ny] = 3
    return nx, ny
    
# def shark_moves(x, y, command, blood_map, fish_map):
#     dx = [-1,0,1,0]
#     dy = [0,-1,0,1]
#     nx , ny = x, y
#     for i in command:
#         nx += dx[i]
#         ny += dy[i]
#         if fish_map[nx][ny]:
#             fish_map[nx][ny] = []
#             blood_map[nx][ny] = 4
#     return nx, ny

def blood_update(blood_map):
    for i in range(N):
        for j in range(N):
            if blood_map[i][j]:
                blood_map[i][j] -= 1

def copy_fishes(org_fish_map, fish_map):
    for i in range(N):
        for j in range(N):
            if org_fish_map[i][j] or fish_map[i][j]:
                fish_map[i][j] += org_fish_map[i][j]

s_x, s_y = shark_loc
for _ in range(S):
    maxi , command = -1, []
    org_fish_map = deepcopy(fish_map)
    fish_map = fish_moves(fish_map, [s_x,s_y])
    s_x, s_y = shark_moves(s_x, s_y, blood_map, fish_map)
    blood_update(blood_map)
    copy_fishes(org_fish_map, fish_map)

score = 0
for i in range(N):
    for j in range(N):
        score += len(fish_map[i][j])

print(score)