import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]
ans_board = [[] for _ in range(N)]
starting = []
for i in range(N):
    for k,j in enumerate(input().rstrip()):
        board[i].append(int(j))
        ans_board[i].append(int(j))
        if j=='1':
            starting.append((i,k))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0 for _ in range(M)] for _ in range(N)]
group_dict = {}
que = deque()

def BFS(sx, sy, group):
    visited[sx][sy] = group
    que.append((sx,sy))
    cnt = 1
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if not board[nx][ny] and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = group
                que.append((nx, ny))
    group_dict[group] = cnt
    return group + 1

def solution(sx, sy, group):
    cost = 1
    group_stack = set()
    for i in range(4):
        nx, ny = sx+dx[i], sy+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if not visited[nx][ny] and not board[nx][ny]: 
            group = BFS(nx, ny, group)
        if visited[nx][ny] and visited[nx][ny] not in group_stack:
            cost += group_dict[visited[nx][ny]]
            group_stack.add(visited[nx][ny])
            
    ans_board[sx][sy] = cost % 10
    return group

group = 1
for x,y in starting:
    group = solution(x,y, group)

for i in ans_board:
    for j in i:
        print(j, end='')
    print('')