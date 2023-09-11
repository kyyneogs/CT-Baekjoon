import sys
input = sys.stdin.readline

def check(x, y):
    for dx, dy in stack:
        if dx==x or dy==y:
            continue
        if abs(dy-y) == abs(dx-x):
            return False
    return True

def DFS(x, y, result=0):
    if x<0 or x>=N or y<0 or y>=N:
        return result

    if visited[x][y]:
        return result
    
    if arr[x][y]:
        if not check(x, y):
            return result
        result += 1
        stack.append((x,y))
    
    visited[x][y] = 1
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        result = max(result, DFS(nx, ny, result))

    return result

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
maxi = 0

for x in range(N):
    for y in range(N):
        stack = []
        visited = [[0 for _ in range(N)] for _ in range(N)]
        maxi = max(maxi, DFS(x,y))
print(maxi)