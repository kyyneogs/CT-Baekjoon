# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())
# graph = [[0,0,0]]+[list(map(int, input().split())) for _ in range(E)]
# graph.sort(key = lambda x:x[2])
# table = [i for i in range(V+1)]

# start = graph[1][0]
# cnt, result = 0, 0

# for i in range(1,E):
#     u, v, w = graph[i]
#     if cnt > V:
#         break
#     if table[v] == start:
#         continue
#     table[v] = start
#     result += w 
# print(result)

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key = lambda x:x[2])
parent = [i for i in range(V+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

cnt, result = 0, 0

for i in range(E):
    u, v, w = graph[i]
    if cnt > V-1:
        break 
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += w
        cnt +=1
print(result)