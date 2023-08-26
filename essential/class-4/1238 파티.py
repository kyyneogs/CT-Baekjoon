import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    graph[i].append([j, k])

def djikstra(start):
    q = []
    distance = [INF] * (N+1)
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
    return distance

back = djikstra(X)
result = 0

for i in range(1,N+1):  
    go = djikstra(i)[X]
    result = max(result, go+back[i])
print(result)