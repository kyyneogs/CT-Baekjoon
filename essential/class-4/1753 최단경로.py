import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])

distance = [INF] * (V+1)
def djikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while(q):
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
djikstra(K)
for i in range(1, V+1):
    if distance[i] == INF: print('INF')
    else: print(distance[i])