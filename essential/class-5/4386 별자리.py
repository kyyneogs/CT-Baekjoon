import sys
import math
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(float, input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]
graph = []

for i in range(N-1):
    for j in range(i+1,N):
        graph.append((((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**0.5, i, j))
graph.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    if u<v:
        parent[v] = u
    else:
        parent[u] = v

cnt, result = 0,0
for w, u, v in graph:
    # if cnt>=N:
    #     break
    up, vp = find_parent(u), find_parent(v)
    if up!=vp:
        union_parent(u, v)
        cnt += 1
        result += w
print(round(result, 2))