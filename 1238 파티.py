import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

def djikstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while(que):
        dist, now = heapq.heappop(que)
        if dist > distance[now]:
            continue

        for _dist, _next in graph[now]:
            cost = _dist + dist
            if cost < distance[_next]:
                distance[_next] = cost
                heapq.heappush(que, (cost, _next))
    return distance

back = djikstra(X)

maxi = 0
for i in range(1, N+1):
    tmp = djikstra(i)[X]
    maxi = max(maxi, tmp+back[i])

print(maxi)