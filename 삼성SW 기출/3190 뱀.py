from collections import deque

n = int(input())
k = int(input())

arr = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
for i in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 2

L = int(input())
command = {}
for _ in range(L):
    a, b = input().split()
    command[int(a)] = b

que = deque()
que.append((0,0))
x, y = 0, 0
arr[x][y] = 1
sec = 0

def turn(x, direction):
    if x=='L':
        return (direction-1)%4
    else:
        return (direction+1)%4

while(True):
    sec += 1
    x += dx[direction]
    y += dy[direction]

    if x<0 or x>=n or y<0 or y>=n:
        break

    if arr[x][y] == 2:
        arr[x][y] = 1
        que.append((x,y))
        if sec in command:
            direction = turn(command[sec], direction)
    
    elif arr[x][y] == 0:
        arr[x][y] = 1
        que.append((x,y))
        tx, ty = que.popleft()
        arr[tx][ty] = 0
        if sec in command:
            direction = turn(command[sec], direction)

    else:
        break

print(sec)