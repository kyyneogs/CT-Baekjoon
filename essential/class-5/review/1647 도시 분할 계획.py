import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key = lambda x:x[2])
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] !=x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    u, v = (u, v) if u > v else (v, u)
    parent[u] = v

result, maxi = 0, 0
for u, v, w in graph:
    up, vp = find_parent(u), find_parent(v)
    if up!=vp:
        union_parent(up, vp)
        result += w
        maxi = max(maxi, w)

print(result - maxi)