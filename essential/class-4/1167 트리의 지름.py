import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
for i in range(1,v+1):
    w = list(map(int, input().split()))
    for j in range(1, len(w)-2, 2):
        graph[w[0]].append([w[j], w[j+1]])

def DFS(node=1, sumi=0):
    for tnode, tsumi in graph[node]:
        if not visited[tnode]:
            visited[tnode] = sumi + tsumi
            DFS(tnode, sumi+tsumi)

visited = [0] * (v+1)
visited[1] = 1
DFS()
start = visited.index(max(visited))
visited = [0] * (v+1)
visited[start] = 1
DFS(start)

print(max(visited))