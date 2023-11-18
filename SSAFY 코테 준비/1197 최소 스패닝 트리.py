import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union_parent(a, b):
    a, b = (a, b) if a>b else (b, a)
    parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key = lambda x:x[2])

cnt, weights = 0, 0
for i in range(E):
    if cnt == V:
        break
    u, v, w = graph[i]
    up, vp = find_parent(u), find_parent(v)

    if up!=vp:
        union_parent(up, vp)
        cnt += 1
        weights += w

print(weights)