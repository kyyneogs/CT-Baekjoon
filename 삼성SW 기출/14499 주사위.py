N, M, x, y, K = map(int, input().split())

arr = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0]*6

def turn(direction):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c

    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d

    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

for _ in range(N):
    arr.append(list(map(int, input().split())))

command = list(map(int, input().split()))

nx, ny = x, y
for i in command:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx<0 or nx>=N or ny<0 or ny>=M:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    turn(i)

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0
    print(dice[0])