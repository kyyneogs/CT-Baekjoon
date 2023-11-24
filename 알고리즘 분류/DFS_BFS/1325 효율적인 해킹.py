import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)

def BFS(x):
    visited = [0]*(N+1)
    visited[x] = 1
    cnt = 0
    que = deque([x])

    while(que):
        
        nodes = que.popleft()

        for node in graph[nodes]:
            if not visited[node]:
                visited[node] = 1
                cnt += 1
                que.append(node)
    
    return cnt

maxi = 0
result = []
for i in range(1,N+1):
    if graph[i]:
        cnt = BFS(i)

        if cnt > maxi:
            maxi = cnt
            result = [i]

        elif cnt == maxi:
            result.append(i)

print(' '.join(map(str, result)))