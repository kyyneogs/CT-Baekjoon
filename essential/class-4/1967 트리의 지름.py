import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

def DFS(start, sumi):
    for node, weight in graph[start]:
        if not visited[node]:
            visited[node] = sumi + weight
            DFS(node, sumi+weight)

visited = [-1] * (N+1)
visited[1] = 0
DFS(1,0)

indx = visited.index(max(visited))
visited = [-1] * (N+1)
visited[indx] = 0
DFS(indx,0)

print(max(visited))