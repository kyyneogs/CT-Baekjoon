import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [i for i in range(N)]

stars = [tuple(map(float, input().split())) for _ in range(N)]
graph = []

for i in range(N-1):
    for j in range(i+1, N):
        graph.append((((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5, i, j))
graph.sort()

result = 0
for w, u, v in graph:
    up, vp = find_parent(u), find_parent(v)
    if up!=vp:
        union_parent(u, v)
        result += w

print(round(result, 2))