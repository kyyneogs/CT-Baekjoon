import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bctrk(x, y, cnt):
    global maxi
    if maxi < cnt:
        maxi = cnt    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and not arr[nx][ny] in stack:
            stack.add(arr[nx][ny])
            bctrk(nx, ny, cnt+1)
            stack.remove(arr[nx][ny])

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

stack = set(arr[0][0])

maxi = 0

bctrk(0, 0, 1)
print(maxi)