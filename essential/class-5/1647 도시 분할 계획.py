import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key = lambda x:x[2])
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    if u<v:
        parent[v] = u
    else:
        parent[u] = v

cnt, result, maxi = 0,0,0
for i in range(M):
    if cnt >= N:
        break
    u, v, w = graph[i]
    up, vp = find_parent(u), find_parent(v)
    if up!=vp:
        union_parent(up, vp)
        cnt += 1
        result += w
        maxi = w if w>maxi else maxi

print(result - maxi)