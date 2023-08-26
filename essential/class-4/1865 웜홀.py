import sys
input = sys.stdin.readline
INF = int(1e9)

def BF():
    distance = [INF] * (N+1)
    for i in range(N):
        for j in range(len(graph)):
            now, nxt, cost = graph[j]
            if distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                if i == N-1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    for i in range(M+W):
        S, E, T = map(int, input().split())
        if i>=M: T = -T
        else: graph.append((E,S,T))
        graph.append((S,E,T))
    
    if BF(): print('YES')
    else: print('NO')