import sys, heapq
input = sys.stdin.readline

INF = int(10e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def djikstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0
    que = [(0, start)]

    while(que):
        dist, now = heapq.heappop(que)

        if dist > distance[now]:
            continue

        for _node, _dist in graph[now]:
            cost = dist + _dist
            if cost < distance[_node]:
                distance[_node] = cost
                heapq.heappush(que, (cost, _node))
    
    return distance

distance = djikstra(X)
for i in range(1,N+1):
    distance[i] += djikstra(i)[X]

print(max(distance[1:]))