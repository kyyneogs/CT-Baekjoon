import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
# 입력 종료

INF = int(10e9)

def djikstra(start):
    distance = [INF]*(N+1)
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

back = djikstra(X)
maxi = 0
for i in range(1,N+1):
    go = djikstra(i)
    maxi = max(maxi, back[i]+go[X])

print(maxi)