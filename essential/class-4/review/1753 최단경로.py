import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])

INF = int(10e9)

def djikstra(start):
    distance = [INF]*(V+1)
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while(que):
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for nodes in graph[now]:
            v, w = nodes
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(que, (cost, v))
    return distance

distance = djikstra(start)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])