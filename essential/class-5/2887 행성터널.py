import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    if u<v:
        parent[v] = u
    else:
        parent[u] = v

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
graph = []
parent = [i for i in range(N+1)]
for i in range(N-1):
    for j in range(i, N):
        dis = min(abs(arr[i][0]-arr[j][0]), abs(arr[i][1]-arr[j][1]), abs(arr[i][2]-arr[j][2]))
        graph.append((i, j, dis))
graph.sort(key=lambda x:x[2])

cnt, result = 0, 0
for u, v, w in graph:
    if cnt >= N-1:
        break

    up, vp = find_parent(u), find_parent(v)
    if up!=vp:
        union_parent(up, vp)
        cnt += 1
        result += w
print(result)