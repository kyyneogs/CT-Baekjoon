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
arr = []
for i in range(N):
    x, y, z = map(int, input().split())
    arr.append((x,y,z,i+1))
graph = []
parent = [i for i in range(N+1)]

for i in range(3):
    arr.sort(key=lambda x:x[i])
    for j in range(1,N):
        dis = min(abs(arr[j-1][0] - arr[j][0]), abs(arr[j-1][1] - arr[j][1]), abs(arr[j-1][2] - arr[j][2]))
        graph.append((arr[j-1][3], arr[j][3], dis))
graph.sort(key = lambda x:x[2])

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