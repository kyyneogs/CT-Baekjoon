from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

mini = int(10e9)
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1: houses.append((i,j))
        elif board[i][j] == 2: chickens.append((i,j))

for chicken_list in combinations(chickens, M):
    tmp = 0
    for nx, ny in houses:
        t_mini = int(10e9)
        for cx, cy in chicken_list:
            t_mini = min(t_mini, abs(cx-nx)+abs(cy-ny))
        tmp += t_mini
    mini = min(mini, tmp)
print(mini)