from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

land = [[5]*N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    trees[X-1][Y-1].append(Z)

def SS():
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] <= land[i][j]:
                    land[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len(trees[i][j])):
                        land[i][j] += trees[i][j].pop()//2
                    break

def FW():
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5==0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0<= ny < N:
                            trees[nx][ny].appendleft(1)
            land[i][j] += A[i][j]

for _ in range(K):
    SS()
    FW()

result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])

print(result)